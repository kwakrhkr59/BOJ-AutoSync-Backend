from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.services.selenium_driver import get_driver
from app.core.config import BASE_URL

def login(boj_id: str, boj_pwd: str):
    driver = get_driver()
    driver.get(f"{BASE_URL}/signin")

    try:
        # 최대 10초 동안 로그인 필드가 나타날 때까지 대기
        id_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "login_user_id"))
        )
        id_input.send_keys(boj_id)

        pw_input = driver.find_element(By.NAME, "login_password")
        pw_input.send_keys(boj_pwd)
        pw_input.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "로그아웃"))
        )

        print(f"{boj_id} 로그인 성공")
        return True
    except Exception as e:
        print(f"로그인 실패: {e}")
        driver.quit()
        return False