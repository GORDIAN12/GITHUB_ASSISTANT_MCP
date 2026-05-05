import requests
from app.config import GITHUB_TOKEN, GITHUB_API_URL

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_pull_request(owner: str, repo: str, pull_number: int):
    url=f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls/{pull_number}"
    response=requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_pull_files(owner: str, repo: str, pull_number: int):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls/{pull_number}/files"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_commit_details(owner: str, repo: str, commit_sha: str):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/commits/{commit_sha}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()  
