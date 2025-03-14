from bs4 import BeautifulSoup

def parse_submission_row(columns):
    submission_id = columns[0].text.strip()  # 제출 ID
    user_id = columns[1].find("a").text.strip()  # 사용자 아이디
    problem_id = columns[2].find("a").text.strip()  # 문제 번호
    problem_title = columns[2].find("a").get("title", "").strip()  # 문제 제목
    result = columns[3].find("span").text.strip()  # 채점 결과
    memory = columns[4].text.strip() + "KB"  # 메모리 사용량
    time = columns[5].text.strip() + "ms"  # 실행 시간
    language = columns[6].text.strip()  # 사용 언어
    code_length = columns[7].text.strip() + "B"  # 코드 길이

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

def parse_submission_list(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    submission_list = {}

    for row in soup.select("tr"):
        cols = row.find_all("td")
        if len(cols) == 0:
            continue
        
        info = parse_submission_row(cols)
        submission_list[info["problem_id"]] = info
    
    return submission_list

def parse_source_code(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    code_box = soup.find("textarea", {"class": "codemirror-textarea"})
    source_code = code_box.text.strip() if code_box else "코드 없음"

    return source_code