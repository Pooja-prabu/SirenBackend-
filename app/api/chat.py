from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def chat_health():
    return {"status": "chat api running"}
