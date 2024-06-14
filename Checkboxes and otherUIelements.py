import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
for i in checkboxes:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()
        break

#radiobutton
radiobuttons = driver.find_elements(By.CSS_SELECTOR, '.radioButton')
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

#hide/show textbox
assert driver.find_element(By.ID, "displayed-text").is_displayed()
#clciking on hide button
driver.find_element(By.ID, "hide-textbox").click()
#assert not fails the test case if the text box is displayed
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
