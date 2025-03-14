import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.acmicpc.net"

session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://www.acmicpc.net/"
}

def login(boj_id, boj_pwd):
    login_url = f"{BASE_URL}/signin"
    payload = {'login_user_id': boj_id,
               'login_password': boj_pwd}
    
    res = session.post(url=login_url, data=payload, headers=headers)
    print("res:", res)
    print("res.status_code:", res.status_code)
    if res.status_code == 200:
        print(boj_id, "로그인 성공")
        return True
    else:
        print(res.status_code, "로그인 실패")
        return False

def getStatus(boj_id):
    status_url = f"{BASE_URL}/status?user_id={boj_id}&result_id=4"
    res = session.get(status_url, headers=headers)
     
    print("res", res)
    print("res.status_code", res.status_code)
    print(res.text)
    if res.status_code == 200:
        print(boj_id, "조회 성공")
        return True
    else:
        print(res.status_code, "조회 실패")
        return False

if __name__ ==  '__main__':
    import os
    from dotenv import load_dotenv
    
    load_dotenv()

    boj_id = os.getenv("BOJ_ID")
    boj_pwd = os.getenv("BOJ_PWD")

    if login(boj_id, boj_pwd):
        getStatus(boj_id)