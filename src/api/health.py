from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok"}