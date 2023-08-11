import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import driver_setting

PAGE_PATH = '//*[@id="app-root"]/div/div/div[2]/a'


def iframe(frame_type):
    driver_setting.driver.switch_to.default_content()
    WebDriverWait(driver_setting.driver, 6).until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, f'//*[@id="{frame_type}"]')))


def get_last_page():
    def get():
        element = driver_setting.driver.find_elements(By.XPATH, PAGE_PATH)
        return int(element[len(element) - 2].text)

    last = get()

    if last == 5:
        click_page(5)
        last = get()
        click_page(2)
        print(last)
        return last

    return last


def click_page(index):
    page_num_element = driver_setting.driver.find_element(By.LINK_TEXT, str(index))
    page_num_element.click()
    time.sleep(3)


def load_element():
    # 한번 클릭해줘야함!! 지우지 말기
    driver_setting.driver.find_element(By.CSS_SELECTOR, "#_pcmap_list_scroll_container").click()
    # 로딩된 데이터 개수 확인
    lis = driver_setting.driver.find_elements(By.CSS_SELECTOR, "li")
    before_len = len(lis)

    while True:
        # 맨 아래로 스크롤 내린다.
        scroll = driver_setting.driver.find_element(By.CSS_SELECTOR, "body")
        scroll.send_keys(Keys.END)
        # 스크롤 사이 페이지 로딩 시간
        time.sleep(2)
        # 스크롤 후 로딩된 데이터 개수 확인
        lis = driver_setting.driver.find_elements(By.CSS_SELECTOR, "li")
        after_len = len(lis)
        # 데이터 기다리는 시간을 0으로 만들어 줌
        driver_setting.driver.implicitly_wait(0)

        # 로딩된 데이터 개수가 같다면 반복 멈춤
        print(before_len)
        print(after_len)

        if before_len == after_len:
            break
        before_len = after_len

    return lis
