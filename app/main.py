from fastapi import FastAPI
from app.routes.github import router as github_router

app = FastAPI(title="GitHub PR Assistant MCP", version="0.1.0")

app.include_router(github_router)

@app.get("/health")
def health():
    return {"status": "ok", "service": "github-pr-assistant-mcp"}