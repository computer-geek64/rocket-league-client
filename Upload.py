# Upload.py
# Ashish D'Souza
# September 8th, 2018

from selenium import webdriver
from time import sleep
from Encryption import *
import os


with open(os.environ["USERPROFILE"] + "/Documents/rocket-league-client/settings.txt", "r") as file:
    lines = file.readlines()
    file.close()

encrypted_lines = []
for line in range(len(lines)):
    encrypted_lines.append(encrypt(lines[line].strip(), "Ljezzy00Ljezzy00"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobar")
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("https://github.com/login")
browser.find_element_by_id("login_field").send_keys("rocket-league-bot")
browser.find_element_by_id("password").send_keys("Ljezzy00")
browser.find_element_by_class_name("btn-primary").click()
sleep(1)
browser.get("https://github.com/computer-geek64/rocket-league-bot/delete/master/settings.txt")
browser.find_element_by_id("submit-file").click()
sleep(3)
browser.find_elements_by_class_name("BtnGroup-item")[0].click()
sleep(1)
browser.find_element_by_name("filename").send_keys("settings.txt")
browser.find_element_by_class_name("CodeMirror-code").send_keys("\n".join(encrypted_lines))
browser.find_element_by_id("submit-file").click()
sleep(3)
browser.close()
