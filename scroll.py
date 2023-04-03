from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = "https://infinite-scroll.com/options.html"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)
time.sleep(7)
wait = WebDriverWait(browser, 10)
list_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".scroller")))
time.sleep(2)

actions = ActionChains(browser)
scrollbar_pos = browser.execute_script("return arguments[0].scrollTop;", list_element)
while True:
    actions.move_to_element(list_element)
    list_element.click()
    actions.send_keys(Keys.END).perform()
    time.sleep(4)
    new_scrollbar_pos = browser.execute_script("return arguments[0].scrollTop;", list_element)
    if new_scrollbar_pos == scrollbar_pos:
        break
    scrollbar_pos = new_scrollbar_pos

print("correctly ended")
# time.sleep(300)
    
