from selenium import webdriver
from getpass import getpass

username = input("Enter in your username: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome("C:\\Dev\\WebDrivers\\chromedriver.exe")
driver.get("https://www.facebook.com/")

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("u_0_3")
login_button.submit()
