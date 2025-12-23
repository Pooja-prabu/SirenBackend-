from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    gateway_status = Column(String, nullable=False)
    bank_status = Column(String, nullable=False)
    refund_status = Column(String, nullable=False)
