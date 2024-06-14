
#pause the test for few seconds using Time class
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#shop button at top : a[href = "/angularpractice/shop"] or a[href *=shop]  -->CSS where *=is a regex
#//a[contains(@href,'shop')] -->Xpath
driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
product = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for i in product :
    productName = i.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        i.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait =WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successmsg=driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successmsg