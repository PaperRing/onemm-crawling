import json

import driver_setting
import page
import search
import store


def crawling(last_page):
    result = {}

    for index in range(1, last_page + 1):
        page.click_page(index)
        store_list = page.load_element()
        store_results = store.get_stores(store_list)
        result.update(store_results)

    return result


def template():
    # 1. 검색
    search.search_by_key("봉천동 카페")
    # 2. 마지막 페이지 가져오기
    last_page = page.get_last_page()
    # 3. 전체 페이지를 돌면서 크롤링
    result = crawling(last_page)
    # 4. 중복제거
    # u_value = set(val for dic in result for val in dic.values())  # 5. 결과 파일 저장
    with open("cafe_흑석동.json", "w", encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))

    driver_setting.driver.close()


if __name__ == '__main__':
    template()
