from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.order import Order
from app.models.transaction import Transaction
from app.services.razorpay_simulator import process_payment

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
def create_order(user_id: int, amount: int, db: Session = Depends(get_db)):
    # Create order
    order = Order(
        user_id=user_id,
        amount=amount,
        status="created"
    )
    db.add(order)
    db.commit()
    db.refresh(order)

    # Simulate Razorpay payment
    payment = process_payment()

    # Save transaction
    transaction = Transaction(
        order_id=order.id,
        gateway_status=payment["gateway_status"],
        bank_status=payment["bank_status"],
        refund_status="none"
    )

    # Mark order failed if gateway fails
    if payment["gateway_status"] != "success":
        order.status = "failed"

    db.add(transaction)
    db.commit()

    return {
        "order_id": order.id,
        "order_status": order.status,
        "payment": payment
    }
