import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.acmicpc.net"

def login(boj_id, boj_pwd):
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Referer": "https://www.acmicpc.net/"
    }
    
    login_url = f"{BASE_URL}/signin"
    payload = {'login_user_id': boj_id,
               'login_password': boj_pwd}
    
    res = session.post(url=login_url, data=payload, headers=headers)
    print("res:", res)
    print("res.status_code:", res.status_code)

if __name__ ==  '__main__':
    import os
    from dotenv import load_dotenv
    
    load_dotenv()

    boj_id = os.getenv("BOJ_ID")
    boj_pwd = os.getenv("BOJ_PWD")
    
    login(boj_id, boj_pwd)