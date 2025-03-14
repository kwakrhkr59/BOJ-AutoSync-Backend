from selenium import webdriver
import time

driver = None

def get_driver():
    global driver
    if driver is None:
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # GUI 없이 실행        
        # options.add_argument("--disable-gpu")  
        # options.add_argument("--window-size=1920x1080")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(options=options)
    return driver

def fetch_url(url):
    get_driver()
    driver.get(url)
    time.sleep(3)  # 페이지 로드 대기

    page_source = driver.page_source
    return page_source