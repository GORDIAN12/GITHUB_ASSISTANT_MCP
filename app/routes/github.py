from fastapi import APIRouter

router = APIRouter(prefix="/github", tags=["GitHub"])

@router.get("/")
def github_root():
    return {"message": "GitHub routes ready"}