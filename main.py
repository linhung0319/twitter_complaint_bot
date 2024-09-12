import os
import random
import math

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from fake_useragent import UserAgent


load_dotenv(".env")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

class InternetSpeedTwitterBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        # 添加'detach'選項以保持瀏覽器開啟
        options.add_experimental_option("detach", True)
        # 添加其他選項，例如禁用自動化提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        #options.add_argument(UserAgent().random)
        self.driver = webdriver.Chrome(options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        URL = "https://www.speedtest.net/"
        self.driver.get(URL)


    def tweet_at_provider(self):
        URL = "https://twitter.com/home"
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 10)

        # Log in to Twitter
        email = wait.until(EC.presence_of_element_located( (By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input') ))
        email.send_keys(TWITTER_EMAIL)
        next_step = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_step.click()
        
        password = wait.until(EC.presence_of_element_located( (By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input') ))
        password.send_keys(TWITTER_PASSWORD)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        log_in.click()

        tweet_compose = wait.until(EC.presence_of_element_located( (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div') ))
        random_number = math.floor(random.random() * 100 + 1)
        tweet_compose.send_keys(f"Hi, today's lucky number is {random_number}!!")
        
        post = wait.until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]') ))
        post.click()

def main():
    bot = InternetSpeedTwitterBot()
    #bot.get_internet_speed()
    bot.tweet_at_provider()

if __name__ == "__main__":
    main()