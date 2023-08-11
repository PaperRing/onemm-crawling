import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import driver_setting


def search_by_key(key):
    try:
        search = driver_setting.driver.find_element(By.CSS_SELECTOR, "input.input_search")
        search.click()
        search.send_keys(key)
        search.send_keys(Keys.ENTER)
        time.sleep(3)

        driver_setting.driver.switch_to.frame("searchIframe")
        driver_setting.driver.find_element(By.CSS_SELECTOR, "#_pcmap_list_scroll_container").click()
    except Exception:
        print(Exception)
