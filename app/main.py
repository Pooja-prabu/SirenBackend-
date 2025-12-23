from fastapi import FastAPI
from app.core.database import engine, Base
from app.api import orders, chat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SupportX Backend")

app.include_router(orders.router, prefix="/orders")
app.include_router(chat.router, prefix="/chat")
