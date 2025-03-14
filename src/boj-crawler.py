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
    
    if res.status_code == 200:
        print(boj_id, "로그인 성공")
        return True
    else:
        print(res.status_code, "로그인 실패")
        return False

def getStatus(boj_id):
    status_url = f"{BASE_URL}/status?user_id={boj_id}&result_id=4"
    res = session.get(status_url, headers=headers)
    
    if res.status_code == 200:
        print(boj_id, "조회 성공")
        return res.text
    else:
        print(res.status_code, "조회 실패")
        return None

def getInfo(cols):
    submission_id = cols[0].text.strip()  # 제출 ID
    user_id = cols[1].find("a").text.strip()  # 유저 아이디
    problem_id = cols[2].find("a").text.strip()  # 문제 번호
    problem_title = cols[2].find("a").get("title", "").strip()  # 문제 제목
    result = cols[3].find("span").text.strip()  # 결과 (맞았습니다!! 등)
    memory = cols[4].text.strip() + "KB"  # 메모리 사용량
    time = cols[5].text.strip() + "ms"  # 실행 시간
    language = cols[6].text.strip()  # 사용 언어
    code_length = cols[7].text.strip() + "B"  # 코드 길이

    return {"submission_id": submission_id,
            "user_id": user_id,
            "problem_id": problem_id,
            "problem_title": problem_title,
            "result": result,
            "memory": memory,
            "time": time,
            "language": language,
            "code_length": code_length,
            }

def extractSubmission(text):
    soup = BeautifulSoup(text, "html.parser")

    submission_list = {}
    for row in soup.select("tr"):
        cols = row.find_all("td")
        if len(cols) == 0: continue
        
        info = getInfo(cols)
        submission_list[info["problem_id"]] = info
    
    return submission_list

if __name__ ==  '__main__':
    import os
    from dotenv import load_dotenv
    
    load_dotenv()

    boj_id = os.getenv("BOJ_ID")
    boj_pwd = os.getenv("BOJ_PWD")

    if login(boj_id, boj_pwd):
        text = getStatus(boj_id)
        extractSubmission(text)