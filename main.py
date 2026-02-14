from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

bot = webdriver.Chrome(options=chrome_options)
bot.get("http://ozh.github.io/cookieclicker/")

wait = WebDriverWait(bot, 10)

wait.until(ec.presence_of_element_located((By.ID, "langSelect-EN")))
lang_select = bot.find_element(By.CSS_SELECTOR, value="div#langSelect-EN")
lang_select.click()

most_valueable_reward = 0
last_run = time.time()
while True:
    
    if time.time() - last_run >= 300:
        break
    
    wait.until(ec.presence_of_element_located((By.ID, "bigCookie")))
    cookie_button = bot.find_element(By.ID, value="bigCookie")
    cookie_button.click()
    
    if time.time() - last_run >= 5:
        wait.until(ec.presence_of_element_located((By.ID, "product0")))
        rewards = bot.find_elements(By.CSS_SELECTOR, value="div.product.unlocked.enabled")

        most_expensive = None

        for reward in rewards:
            
            reward_price = reward.find_element(By.CSS_SELECTOR, value="span.price").get_attribute("innerText").replace(",", "")
            if int(reward_price) > most_valueable_reward:
                most_valueable_reward = int(reward_price)
                
                most_expensive = reward
                most_expensive.click()
                
                
                print(most_valueable_reward)
        last_run = time.time()
                
    
        
    