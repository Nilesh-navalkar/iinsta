from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

doc=open('keys.json','r')
keys=json.load(doc)
doc.close()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

browser=webdriver.Chrome(ChromeDriverManager().install())
browser.get(keys['url'])
browser.implicitly_wait(30)


#___________LOGIN__________________
un=browser.find_element(By.CSS_SELECTOR,"[aria-label='Phone number, username, or email']")
un.send_keys(keys['username'])
psw=browser.find_element(By.CSS_SELECTOR,"[aria-label='Password']")
psw.send_keys(keys['password'])

btn=browser.find_element(By.CSS_SELECTOR,"[class='_acan _acap _acas _aj1-']")
browser.execute_script("arguments[0].removeAttribute('disabled')", btn)
btn.click()
browser.implicitly_wait(30)

#___________HANDEL OBSTRUCTION__________________
# try:
#     pass
# except:
#     pass

#___________GET FOLLOWING__________________
nwxt='/'+keys['username']+'/?next=%2F'
nn=browser.find_element(By.CSS_SELECTOR,"[href='{}']".format(nwxt))
nn.click()
time.sleep(3)
nnf=browser.find_element(By.CSS_SELECTOR,"[href='/nil.arts/following/?next=%2F']")
nnf.click()
browser.implicitly_wait(30)
#_aano
# scroll_div=browser.find_element(By.CSS_SELECTOR,"[style='position: relative; display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px;']")
scroll_div=browser.find_element(By.CSS_SELECTOR,"[class='_aano']")
clk_div=browser.find_element(By.CSS_SELECTOR,"[class='_ac78']")
actions = ActionChains(browser)
scrollbar_pos = browser.execute_script("return arguments[0].scrollTop;", scroll_div)
while True:
    actions.move_to_element(clk_div)
    clk_div.click()
    actions.move_to_element(scroll_div)
    time.sleep(5)
    actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
    time.sleep(5)
    new_scrollbar_pos = browser.execute_script("return arguments[0].scrollTop;", scroll_div)
    if new_scrollbar_pos == scrollbar_pos:
        break
    scrollbar_pos = new_scrollbar_pos

following=[]
slc=browser.find_elements(By.CSS_SELECTOR,"[role='button']")
for p in slc:
    s=p.text
    s=s.replace("\n",'///')
    following.append(s[:-10])
try:
    following.remove('')
except:
    pass


# print(set(following))
# print(len(set(following)))

nnf=browser.find_element(By.CSS_SELECTOR,"[aria-label='Close']")
nnf.click()
browser.implicitly_wait(30)


#___________GET FOLLOWERS__________________
nwxt='/'+keys['username']+'/followers/?next=%2F'
nnf=browser.find_element(By.CSS_SELECTOR,"[href='{}']".format(nwxt))
nnf.click()
browser.implicitly_wait(30)

scroll_div=browser.find_element(By.CSS_SELECTOR,"[class='_aano']")
clk_div=browser.find_element(By.CSS_SELECTOR,"[class='_ac78']")
actions = ActionChains(browser)
scrollbar_pos = browser.execute_script("return arguments[0].scrollTop;", scroll_div)
while True:
    actions.move_to_element(clk_div)
    clk_div.click()
    actions.move_to_element(scroll_div)
    time.sleep(5)
    actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
    time.sleep(5)
    new_scrollbar_pos = browser.execute_script("return arguments[0].scrollTop;", scroll_div)
    if new_scrollbar_pos == scrollbar_pos:
        break
    scrollbar_pos = new_scrollbar_pos

followers=[]
slc=browser.find_elements(By.CSS_SELECTOR,"[role='button']")
for p in slc:
    s=p.text
    s=s.replace("\n",'///')
    followers.append(s[:-10])
try:
    followers.remove('')
except:
    pass



nnf=browser.find_element(By.CSS_SELECTOR,"[aria-label='Close']")
nnf.click()
browser.implicitly_wait(30)

browser.quit()

#___________GET DIFF__________________
insights=set(following).difference(set(followers))


#___________GENERATE INSIGHTS__________________
print(insights)
doc=open('insights.txt','w')
for i in list(insights):
    doc.write(str(i))
doc.close()
