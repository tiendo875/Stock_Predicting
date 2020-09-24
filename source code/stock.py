from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import JavascriptException
import datetime
from dateutil.relativedelta import relativedelta

today = (datetime.datetime.now()).strftime("%d/%m/%Y")
five_year_ago = (datetime.datetime.now() - relativedelta(years=5)).strftime("%d/%m/%Y")


browser = webdriver.Chrome(executable_path="./chromedriver")


browser.get("https://www.hsx.vn/Modules/Listed/Web/Symbols")
sleep(3)


#lay het tat cac cac ma chung khoan vao lst_a
def check_exists_ele():
    try:
        browser.find_element_by_class_name("next-page")
    except NoSuchElementException:
        return False
    return True

def check_doDownload_ele():
    try:
        browser2.execute_script("doDownload(arguments[0]);")
    except NoSuchElementException:
        return False
    return True

lst_a = []
while (check_exists_ele()):
    next_page_ele = browser.find_element_by_class_name("next-page")
    lst_stock_ele = browser.find_elements_by_css_selector("td[aria-describedby = 'symbols-grid_Code']")
    lst_a = lst_a+[x.get_attribute('title') for x in lst_stock_ele]
    next_page_ele.click()
    sleep(3)
browser.close()

for x in lst_a:
    browser2 = webdriver.Chrome(executable_path="./chromedriver")
    browser2.get("https://www.vndirect.com.vn/portal/thong-ke-thi-truong-chung-khoan/lich-su-gia.shtml")

    #fill ma chung khoan, tu ngay, den ngay,
    print(x)
    mck_ele = browser2.find_element_by_id("symbolID")
    mck_ele.send_keys(x)
    from_date = browser2.find_element_by_id("fHistoricalPrice_FromDate")
    from_date.send_keys(five_year_ago)
    sleep(2)
    to_date = browser2.find_element_by_id("fHistoricalPrice_ToDate")
    to_date.send_keys(today)
    sleep(2)
    browser2.find_element_by_class_name("box_taidulieu").click()
    sleep(2)
    browser2.close()