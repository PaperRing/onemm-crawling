from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('headless')

driver = webdriver.Chrome("/Users/junghee/Project/python/cheeze_project/chromedriver", options=options)
driver.get("https://map.naver.com/v5/")
driver.implicitly_wait(3)
driver.maximize_window()
