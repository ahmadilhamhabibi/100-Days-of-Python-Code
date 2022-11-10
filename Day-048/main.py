from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/dp/B096P1T9ST/ref=syn_sd_onsite_desktop_113?ie=UTF8&psc=1&pd_rd_plhdr=t")
# # price = driver.find_element_by_class_name("a-price-whole")
# # print(price.text)

driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)

# submit_bug = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug.text)

# python_book = driver.find_element_by_xpath('//*[@id="container"]/li[3]/ul/li[8]/a')
# print(python_book.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements_by_css_selector(".event-widget li a")
# for name in event_names:
#     print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

# driver.close()
driver.quit()