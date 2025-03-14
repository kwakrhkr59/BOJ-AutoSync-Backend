from bs4 import BeautifulSoup

def extract_submission_info(content):
    soup = BeautifulSoup(content, "html.parser")

    code_box = soup.find("textarea", {"class": "codemirror-textarea"})
    source_code = code_box.text.strip() if code_box else "코드 없음"

    table_row = soup.find("tbody").find("tr")
    cols = table_row.find_all("td")

    submission_id = cols[0].text.strip()
    user_id = cols[1].find("a").text.strip()
    problem_id = cols[2].find("a").text.strip()
    problem_title = cols[3].text.strip()
    result = cols[4].text.strip()
    memory = cols[5].text.strip() + "KB"
    time = cols[6].text.strip() + "ms"
    language = cols[7].text.strip()
    code_length = cols[8].text.strip() + "B"
    submission_time = cols[9].find("a").get("title", "").strip()

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
        "submission_time": submission_time,
        "source_code": source_code
    }