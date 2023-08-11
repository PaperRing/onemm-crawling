import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import driver_setting


def name():
    return WebDriverWait(driver_setting.driver, 3).until(ec.presence_of_element_located((By.XPATH, '//*[@id="_title"]/span[1]'))).text


def category():
    return WebDriverWait(driver_setting.driver, 3).until(ec.presence_of_element_located((By.XPATH, '//*[@id="_title"]/span[2]'))).text


def facility(detail_list):
    try:
        element = WebDriverWait(detail_list, 3).until(ec.presence_of_element_located((By.XPATH, "//span[@class = 'place_blind' and text() = '편의']")))
        parent = element.find_element(By.XPATH, '..')
        grand = parent.find_element(By.XPATH, '..')
        return grand.find_element(By.CSS_SELECTOR, 'div.vV_z_').text.split(",")
    except:
        return []


def address(detail_list):
    try:
        element = WebDriverWait(detail_list, 3).until(ec.presence_of_element_located((By.XPATH, "//span[@class = 'place_blind' and text() = '주소']")))
        parent = WebDriverWait(element, 3).until(ec.presence_of_element_located((By.XPATH, '..')))
        grand = WebDriverWait(parent, 3).until(ec.presence_of_element_located((By.XPATH, '..')))
        return WebDriverWait(grand, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'span._2yqUQ'))).text
    except:
        return ""


def way(detail_list):
    try:
        element = WebDriverWait(detail_list, 3).until(ec.presence_of_element_located((By.XPATH, "//span[@class = 'place_blind' and text() = '찾아가는길']")))
        parent = WebDriverWait(element, 3).until(ec.presence_of_element_located((By.XPATH, '..')))
        grand = WebDriverWait(parent, 3).until(ec.presence_of_element_located((By.XPATH, '..')))
        try:
            grand.find_element(By.TAG_NAME, 'a').click()
        except:
            pass
        return WebDriverWait(grand, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'span.WoYOw'))).text
    except:
        return ""


def work_day(detail_list):
    try:
        result = {}

        element = detail_list.find_element(By.XPATH, "//span[@class = 'place_blind' and text() = '영업시간']")
        parent = element.find_element(By.XPATH, '..')
        grand = parent.find_element(By.XPATH, '..')
        grand.find_element(By.CSS_SELECTOR, 'div._1h3B_').click()
        time.sleep(2)
        day_list = WebDriverWait(grand, 10).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div._20Y9l > span._20pEw')))

        for li in day_list:
            day = li.find_element(By.CSS_SELECTOR, 'span._1v6gO').text
            hour = li.find_element(By.CSS_SELECTOR, 'div._3uEtO').text
            result[day] = hour

        return result
    except:
        return {}


def tel(detail_list):
    try:
        element = driver_setting.driver.find_element(By.CSS_SELECTOR, 'span._3ZA0S').text

        if len(element) > 13:
            path = detail_list.find_element(By.CSS_SELECTOR, 'li._1M_Iz._3xPmJ > div > a > svg')
            path.click()
            return detail_list.find_element(By.CSS_SELECTOR, 'li._1M_Iz._3xPmJ > div > div > div > span').text

        return element
    except:
        return ""


def homepage(detail_list):
    try:
        element = detail_list.find_element(By.XPATH, "//span[@class = 'place_blind' and text() = '홈페이지']")
        parent = element.find_element(By.XPATH, '..')
        grand = parent.find_element(By.XPATH, '..')

        return grand.find_element(By.CSS_SELECTOR, 'div._14J59 > a').text
    except:
        return ""


def description(detail_list):
    try:
        element = detail_list.find_element(By.XPATH, "//span[@class = 'place_blind' and text() = '설명']")
        parent = element.find_element(By.XPATH, '..')
        grand = parent.find_element(By.XPATH, '..')
        try:
            grand.find_element(By.TAG_NAME, 'a').click()
        except:
            pass
        return grand.find_element(By.CSS_SELECTOR, 'span.WoYOw').text
    except:
        return ""


def menu():
    try:
        result = {}
        WebDriverWait(driver_setting.driver, 3).until(ec.presence_of_element_located((By.XPATH, "//span[@class = 'place_blind' and text() = '메뉴']"))).click()
        menu_list = WebDriverWait(driver_setting.driver, 3).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.place_section_content > ul > li')))
        for i in menu_list:
            menu = i.find_element(By.CSS_SELECTOR, 'div.zUc6j').text
            result[menu] = i.find_element(By.CSS_SELECTOR, 'div._3qFuX').text
        return result
    except:
        return {}
