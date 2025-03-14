import os
from dotenv import load_dotenv

BASE_URL = "https://www.acmicpc.net"

load_dotenv()

boj_id = os.getenv("BOJ_ID")
boj_pwd = os.getenv("BOJ_PWD")