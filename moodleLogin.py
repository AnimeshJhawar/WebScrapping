from selenium import webdriver
from getpass import getpass
import time
username = input("Enter in your username: ")
password = getpass("Enter your password: ")

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")


username_textbox = driver.find_element_by_id("username")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

form = driver.find_element_by_id("login")
formText = form.text.split("\n")
captchaPrompt = formText[3].split(" ")
if captchaPrompt[1] == 'subtract':
    captcha = round(int(captchaPrompt[2])) - round(int(captchaPrompt[4]))
elif captchaPrompt[1] == 'add':
    captcha = round(int(captchaPrompt[2])) + round(int(captchaPrompt[4]))
elif captchaPrompt[2] == 'first':
    captcha = round(int(captchaPrompt[4]))
else:
    captcha = round(int(captchaPrompt[6]))

captcha_box = driver.find_element_by_id("valuepkg3")
captcha_box.send_keys(captcha)
login_button = driver.find_element_by_id("loginbtn")
login_button.submit()

time.sleep(10)