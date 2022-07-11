# Test case
# ---------
# 1. Open the web browser
# 2. Open url https://admin-demo.nopcommerce.com/
# 3. Enter user email - admin@yourstore.com
# 4. Enter password - admin
# 5. Click login button
# 6. capture the title of home page (actual title)
# 7. Verify the title of the home page (Expected)
# 8. close webbrowser

# 1. Open the web browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser_obj= Service("C:/Users/sakuj/Desktop/Python/Drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
# 2. Open url https://admin-demo.nopcommerce.com/
#driver.get("https://admin-demo.nopcommerce.com/")

driver.get(url="https://www.google.com/")
# # 3. Enter user email - admin@yourstore.com
# # identify the element and pass the value
# driver.find_element("Email").send_keys("admin@yourstore.com")
# driver.find_element("Password").send_keys("admin")
# driver.find_element("button-1 login-button").click()

act_title = driver.title
exp_title = "Google"

# if act_title.find(exp_title) != -1:
#     print("Test case Passed")
# else:
#     print("Test case failed")

assert exp_title in act_title

driver.close()