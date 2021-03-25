from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randrange
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login():
    #login
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys("username_here")
    password_input.send_keys("password_here")
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    #search in the bar - keeps us logged in for some reason?
    search_bar = browser.find_element_by_xpath("//input[@placeholder='Search']")
    search_bar.send_keys("aspire_purdue")

    #navigate to post
    browser.get('https://www.instagram.com/p/CM2HmH_lpRa/')
    return browser


def comment(browser, lines):
    line_size = len(lines)
    while True:
        sleep(2)
        comment_bar = browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']")
        comment_bar.click()
        comment_bar = browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']")
        message = lines[randrange(0, line_size)]
        comment_bar.send_keys(message)
        sleep(2)

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        try:
            element = WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Add a comment…']")))
        except:
            break
        sleep(randrange(31, 35))


if __name__ == "__main__":
    lines = []
    with open('path_to_file.txt', 'r', encoding="utf8") as file:
        data = file.read().replace('\n', ' ')
        lines = data.split('.')

    while True:
        browser = login()
        comment(browser, lines)
        browser.close()
        sleep(3)