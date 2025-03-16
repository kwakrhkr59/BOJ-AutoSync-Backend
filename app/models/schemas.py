from pydantic import BaseModel

class BojLoginRequest(BaseModel):
    boj_id: str
    boj_pwd: str