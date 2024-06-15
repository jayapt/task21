from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class LoginAutomation:

   def __init__(self, url, username, password):
       self.url = url
       self.username = username
       self.password = password
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.sleep(5)

   @staticmethod
   def sleep(seconds):
       sleep(seconds)

   def inputBox(self, value, key):
       self.driver.find_element(By.ID, value).send_keys(key)
       self.sleep(5)

   def submitBtn(self):
       self.driver.find_element(By.ID, "login-button").click()
       self.sleep(10)

   def get_cookies(self): # function to enter the contents of the entire page
       return self.driver.get_cookies()

   def print_cookies(self, cookies): # function to print cookies
       for cookie in cookies:
           print('cookies before login',cookie) # display the cookies before login

   def quit(self): # function to quit once the task is completed
       self.driver.quit()

   def login(self):  # function to login with credentials.
       self.boot()
       cookies_before_login = self.get_cookies()
       self.print_cookies(cookies_before_login)
       self.inputBox("user-name", self.username)
       self.inputBox("password", self.password)
       self.submitBtn()
       cookies_after_login = self.get_cookies()
       self.print_cookies(cookies_after_login)
       return cookies_after_login  # Return cookies after login

url = "https://www.saucedemo.com/"
username = "standard_user"    # login username key
password = "secret_sauce"     # password key

obj = LoginAutomation(url, username, password)
cookies_after_login = obj.login()  # Perform login and get cookies
print("Cookies after login:", cookies_after_login)

obj.quit()  # Quit the driver