import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from fbdemo.secrets import username, password

LOGIN_URL = 'https://m.facebook.com'
BASE_URL = 'https://www.facebook.com/'


class FacebookScrapper:
    def __init__(self, browser='Chrome'):
        self.email = username
        self.password = password
        if browser == 'Chrome':
            options = Options()
            # options.headless = True
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def login(self):
        email_element = self.driver.find_element_by_id('m_login_email')
        email_element.send_keys(self.email)

        password_element = self.driver.find_element_by_id('m_login_password')
        password_element.send_keys(self.password)

        login_button = self.driver.find_element_by_name('login')
        login_button.click()

        time.sleep(2)

    def scrape_people(self, keyword):
        self.driver.get(LOGIN_URL + '/search/people/?q=' + keyword)
        time.sleep(1)