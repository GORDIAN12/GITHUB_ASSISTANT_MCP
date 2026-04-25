from fastapi import APIRouter, HTTPException
from app.services.github_service import get_pull_request
from app.services.analyzer import analyze_pr

router = APIRouter(prefix="/github", tags=["GitHub"])


@router.get("/")
def github_root():
    return {"message": "GitHub routes ready"}

@router.get("/pr/{owner}/{repo}/{pull_number}")
def read_pr(owner: str, repo: str, pull_number: int):
    try:
        data = get_pull_request(owner, repo, pull_number)

        return {
            "title": data["title"],
            "state": data["state"],
            "author": data["user"]["login"],
            "created_at": data["created_at"],
            "changed_files": data["changed_files"],
            "commits": data["commits"],
            "additions": data["additions"],
            "deletions": data["deletions"],
            "body": data["body"] or "Sin descripción"
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/analyze/{owner}/{repo}/{pull_number}")
def analyze(owner: str, repo: str, pull_number: int):
    try:
        data = get_pull_request(owner, repo, pull_number)
        return analyze_pr(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))