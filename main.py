from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

bot = webdriver.Chrome(options=chrome_options)
bot.get("http://ozh.github.io/cookieclicker/")

# cookies = bot.find_element(By.CSS_SELECTOR, value="div.cc_container--open a")
# cookies.click()

wait = WebDriverWait(bot, 10)

wait.until(ec.presence_of_element_located((By.ID, "langSelect-EN")))
lang_select = bot.find_element(By.CSS_SELECTOR, value="div#langSelect-EN")
lang_select.click()

x = 0
last_run = time.time()
while x < 102:
    
    wait.until(ec.presence_of_element_located((By.ID, "bigCookie")))
    cookie_button = bot.find_element(By.ID, value="bigCookie")
    cookie_button.click()
    x += 1
    
    # if time.time() - last_run >= 5:
        
    