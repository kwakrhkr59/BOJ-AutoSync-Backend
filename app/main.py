from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import boj_routers

app = FastAPI()

app.include_router(boj_routers.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)