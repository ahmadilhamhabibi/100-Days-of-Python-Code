from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# encyclopedia = driver.find_element_by_link_text("encyclopedia")
# encyclopedia.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


driver.get("https://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element_by_name("fName")
fName.send_keys("Ahmad")
lName = driver.find_element_by_name("lName")
lName.send_keys("Habibi")
email = driver.find_element_by_name("email")
email.send_keys("namaku@emailku.com")
sign_up = driver.find_element_by_xpath('/html/body/form/button')
sign_up.send_keys(Keys.ENTER)

# driver.quit()