import time
from datetime import date

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.set_window_position(2000, 0)
driver.maximize_window()
driver.get("https://aims-sisk-ui-test.aga.rbxd.ds/login")

driver.find_element(By.NAME, "username").send_keys("f4fadmin@f4f.com")
driver.find_element(By.NAME, "password").send_keys("marDzBHU35wB")

# XPATH -> //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -> tagname[attribute='value'] -> //input[type='submit']

driver.find_element(By.XPATH, "//button[@type='submit']").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@data-testid='selectSupplier13']"))
)
driver.find_element(By.XPATH, "//button[@data-testid='selectSupplier13']").click()

WebDriverWait(driver, 5)

driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]").click() # The only way that has worked so far

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@title='Open']"))
)

driver.find_element(By.XPATH, "//button[@title='Open']").click()

# Click dropdown 'mater Private Hospital'
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]"))
)
driver.find_element(By.XPATH, "//*[contains(text(), 'Mater Private Hospital')]").click()

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Stock Levels')]"))
)

driver.find_element(By.XPATH, "//*[contains(text(), 'Stock Levels')]").click()

driver.find_element(By.LINK_TEXT, "Consignment").click()

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[6]/td[4]"))
)

levelofstock = driver.find_element(By.XPATH, "//tbody/tr[6]/td[4]").text

print(levelofstock)

###############################################################################################

driver.find_element(By.XPATH, "//*[contains(text(), 'Home')]").click()

# Click button 'Create Requisition Order'
driver.find_element(By.XPATH, "//*[contains(text(), 'Create Requisition Order')]").click()

# Click Select Cost Center dropdown
WebDriverWait(driver, 5).until(
     EC.presence_of_element_located((By.XPATH, "(//button[@title='Open'])[2]"))
)
driver.find_element(By.XPATH, "(//button[@title='Open'])[2]").click()

driver.find_element(By.XPATH, "//*[contains(text(), 'code3')]").click()

driver.find_element(By.ID, "consignment-invoice").click()

driver.find_element(By.XPATH, "//button[@data-testid='tab-1']").click()

driver.find_element(By.ID, "dropdown-field-id-0-0").send_keys("430003S")

WebDriverWait(driver, 15).until(
     EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '430003S')]"))
)

driver.find_element(By.XPATH, "//*[contains(text(), '430003S')]").click()

driver.find_element(By.ID, "select-id-0-2").click()

driver.find_element(By.XPATH, "//option[@data-testid='options-0-2-1']").click()

driver.find_element(By.CSS_SELECTOR, "#text-field-id-0-4").send_keys("{}".format("{}".format(datetime.now().strftime("%d-%m-%Y-%H%M%S"))))

driver.find_element(By.CSS_SELECTOR, "#submitButton").click()

driver.find_element(By.XPATH, "(//button[@type='button'])[14]").click()

driver.find_element(By.XPATH, "//input[@type='password']").send_keys("1234")

WebDriverWait(driver, 7).until(
     EC.presence_of_element_located((By.CSS_SELECTOR, "svg[data-testid='valid-pin-check']"))
)

driver.find_element(By.XPATH, "(//button[@type='button'])[16]").click()

WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.XPATH, "(//div[@role='alert'])[1]"))
)

requisitioncreated = driver.find_element(By.XPATH, "(//div[@role='alert'])[1]").text

print(requisitioncreated)

###############################################################################

driver.find_element(By.LINK_TEXT, "Requisitions").click()

WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(6) button:nth-child(2)"))
)

driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(6) button:nth-child(2)").click()

WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[44]"))
)

driver.find_element(By.XPATH, "(//button[@type='button'])[44]").click()

WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]"))
)

releasemessage = driver.find_element(By.XPATH, "(//div[@class='MuiSnackbarContent-message'])[1]").text

print(releasemessage)
##################################################################################################
WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Stock Levels')]"))
)

time.sleep(5)

driver.find_element(By.XPATH, "//*[contains(text(), 'Stock Levels')]").click()

driver.find_element(By.LINK_TEXT, "Consignment").click()

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr[6]/td[4]"))
)

levelofstockafter = driver.find_element(By.XPATH, "//tbody/tr[6]/td[4]").text

print(levelofstockafter)

assert "1" in "{}".format(int(levelofstock) - int(levelofstockafter))

print("Success")

#time.sleep(5)



