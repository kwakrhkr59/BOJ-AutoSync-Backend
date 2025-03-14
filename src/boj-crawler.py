from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.acmicpc.net"

# Selenium WebDriver 설정
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # GUI 없이 실행
driver = webdriver.Chrome(options=options)

def login(boj_id, boj_pwd):
    driver.get(f"{BASE_URL}/signin")
    time.sleep(2)  # 페이지 로드 대기

    id_input = driver.find_element(By.NAME, "login_user_id")
    id_input.send_keys(boj_id)

    pw_input = driver.find_element(By.NAME, "login_password")
    pw_input.send_keys(boj_pwd)
    pw_input.send_keys(Keys.RETURN)

    time.sleep(3)  # 로그인 대기

    if "로그아웃" in driver.page_source:
        print(f"{boj_id} 로그인 성공")
        return True
    else:
        print("로그인 실패")
        driver.quit()
        return False

def get_status(boj_id):
    status_url = f"{BASE_URL}/status?user_id={boj_id}&result_id=4"
    driver.get(status_url)
    time.sleep(3)  # 페이지 로드 대기

    page_source = driver.page_source
    return page_source

def get_info(cols):
    submission_id = cols[0].text.strip()  # 제출 ID
    user_id = cols[1].find("a").text.strip()  # 사용자 아이디
    problem_id = cols[2].find("a").text.strip()  # 문제 번호
    problem_title = cols[2].find("a").get("title", "").strip()  # 문제 제목
    result = cols[3].find("span").text.strip()  # 채점 결과
    memory = cols[4].text.strip() + "KB"  # 메모리 사용량
    time = cols[5].text.strip() + "ms"  # 실행 시간
    language = cols[6].text.strip()  # 사용 언어
    code_length = cols[7].text.strip() + "B"  # 코드 길이

    return {
        "submission_id": submission_id,
        "user_id": user_id,
        "problem_id": problem_id,
        "problem_title": problem_title,
        "result": result,
        "memory": memory,
        "time": time,
        "language": language,
        "code_length": code_length,
    }

def extract_submission(text):
    soup = BeautifulSoup(text, "html.parser")
    submission_list = {}

    for row in soup.select("tr"):
        cols = row.find_all("td")
        if len(cols) == 0:
            continue
        
        info = get_info(cols)
        submission_list[info["problem_id"]] = info
    
    return submission_list

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv

    load_dotenv()

    boj_id = os.getenv("BOJ_ID")
    boj_pwd = os.getenv("BOJ_PWD")

    if login(boj_id, boj_pwd):
        text = get_status(boj_id)
        submission_list = extract_submission(text)

        for pid, info in submission_list.items():
            print(f"{pid}: {info}")
    
    driver.quit()
