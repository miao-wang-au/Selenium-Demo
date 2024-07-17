import time
from datetime import date
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Login:

    def __init__(self, a, b):
        self.username = a
        self.driver = b

        if self.username == "F4F Admin":
            self.driver.find_element(By.NAME, "username").send_keys("f4fadmin@f4f.com")
            self.driver.find_element(By.NAME, "password").send_keys("marDzBHU35wB")
        if self.username == "Customer Service":
            self.driver.find_element(By.NAME, "username").send_keys("customerservice@test.com")
            self.driver.find_element(By.NAME, "password").send_keys("marDzBHU35wB%")
        if self.username == "Hospital Theater":
            self.driver.find_element(By.NAME, "username").send_keys("hospitaltheater@test.com")
            self.driver.find_element(By.NAME, "password").send_keys("marDzBHU35wB%")
        if self.username == "Hospital Stores":
            self.driver.find_element(By.NAME, "username").send_keys("hospitalstores@test.com")
            self.driver.find_element(By.NAME, "password").send_keys("marDzBHU35wB%")
        if self.username == "Sales Rep":
            self.driver.find_element(By.NAME, "username").send_keys("salesrep@test.com")
            self.driver.find_element(By.NAME, "password").send_keys("6B2&XA5hfix^")

# XPATH -> //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -> tagname[attribute='value'] -> //input[type='submit']

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-testid='selectSupplier13']"))
        )
        self.driver.find_element(By.XPATH, "//button[@data-testid='selectSupplier13']").click()

        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]").click()  # The only way that has worked so far

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[@title='Open']"))
        )

        self.driver.find_element(By.XPATH, "//button[@title='Open']").click()

# Click dropdown 'mater Private Hospital'
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]"))
        )
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]").click()


# driver = webdriver.Chrome()
# driver.set_window_position(2000, 0)
# driver.maximize_window()
# driver.get("https://aims-sisk-ui-test.aga.rbxd.ds/login")
#
# Login("Hospital Theater", driver)
# driver.find_element(By.XPATH, "(//button[@title='Account settings'])[1]").click()
# driver.find_element(By.XPATH, "(//li[normalize-space()='Logout'])[1]").click()
#
#
# time.sleep(5)

