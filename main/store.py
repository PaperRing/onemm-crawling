import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import driver_setting
from page import iframe
from store_element import facility, address, way, work_day, tel, homepage, description, menu, category, name


# 가게상세보기 클릭
def get_detail(store):
    time.sleep(3)
    detail_link = WebDriverWait(store, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, "span.place_bluelink.TYaxT")))
    detail_link.click()
    time.sleep(2)
    iframe("entryIframe")
    return WebDriverWait(driver_setting.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.place_section > div.PIbes')))


def get_stores(store_list):
    result = {}

    for store in store_list:
        store_result = {}

        detail_list = get_detail(store)

        facility_list = facility(detail_list)
        if " 반려동물 동반" not in facility_list:
            iframe("searchIframe")
            continue

        title = name()
        store_result['facility'] = facility_list
        store_result['category'] = category()
        store_result['address'] = address(detail_list)
        store_result['way'] = way(detail_list)
        store_result['work_day'] = work_day(detail_list)
        store_result['tel'] = tel(detail_list)
        store_result['homepage'] = homepage(detail_list)
        store_result['description'] = description(detail_list)
        store_result['menu'] = menu()

        result[title] = store_result

        iframe("searchIframe")

        print(title)

    return result

# 낙성대동 카페 검색 시, 3페이지로 넘어갈때 할리스 서울대사거리 지점 거리뷰가 선택됨
