import os
from dotenv import load_dotenv

BASE_URL = "https://www.acmicpc.net"

load_dotenv()

boj_id = os.getenv("boj_id")
boj_pwd = os.getenv("boj_pwd")

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
GITHUB_AUTH_URL = os.getenv("GITHUB_AUTH_URL")
GITHUB_TOKEN_URL = os.getenv("GITHUB_TOKEN_URL")
GITHUB_API_URL = os.getenv("GITHUB_API_URL")