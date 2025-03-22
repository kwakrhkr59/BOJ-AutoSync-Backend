from fastapi import APIRouter, HTTPException
from app.services.boj_auth import login
from app.services.html_parser import parse_submission_list, parse_source_code
from app.services.selenium_driver import fetch_url
from app.models.schemas import BojLoginRequest
from app.core.config import BASE_URL

router = APIRouter(prefix="/api/boj", tags=["Boj"])

@router.post("/auth/login")
def boj_login(request: BojLoginRequest):
    if not login(request.username, request.password):
        raise HTTPException(status_code=404, detail="Invalid username or password")
    return {"message": "Login successful"}
    
@router.get("/submissions/{boj_id}")
def get_submission_list(boj_id: str):
    status_url = f"{BASE_URL}/status?user_id={boj_id}&result_id=4"
    html_content = fetch_url(status_url)
    submission_list = parse_submission_list(html_content)

    if not submission_list:
        raise HTTPException(status_code=404, detail="No submission list")
    return submission_list

@router.get("/submissions/code/{submission_id}")
def get_source_code(submission_id: str):
    status_url = f"{BASE_URL}/source/{submission_id}"
    html_content = fetch_url(status_url)
    source_code = parse_source_code(html_content)

    if not source_code:
        raise HTTPException(status_code=404, detail="No source code")
    return source_code