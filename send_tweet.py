from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
class SendTweet:
    def __init__(self,down,up):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://twitter.com/login")
        time.sleep(3)

        login_butt=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email=input("Type your mail: ")
        login_butt.send_keys(email)
        time.sleep(0.5)
        login_butt.send_keys(Keys.ENTER)
        time.sleep(5)
        passw = input("Type your pass: ")
        try:
            type_pass=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            type_pass.send_keys(passw)
            type_pass.send_keys(Keys.ENTER)
        except NoSuchElementException:
            nickname=input("Enter your nickname: @")
            nickname="@"+nickname
            type_nickname=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            type_nickname.send_keys(nickname)
            time.sleep(0.5)
            type_nickname.send_keys(Keys.ENTER)
            time.sleep(2)
            type_pass = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            type_pass.send_keys(passw)
            type_pass.send_keys(Keys.ENTER)
        time.sleep(5)
        message=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        message.send_keys(f"Hey @COMPANY_NAME my download speed is: {down} and upload speed is: {up} which is less than what I am paying for!")
        post_button=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
        post_button.click()
        time.sleep(2)
        driver.quit()