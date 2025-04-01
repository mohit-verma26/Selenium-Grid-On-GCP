from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor="http://34.45.225.46:4444/wd/hub",
    options=options
)


driver.get("https://www.google.com")
print("Page Title:", driver.title)


print("Chrome successfully launched!")
print(driver.title)

# Close browser
driver.quit()
