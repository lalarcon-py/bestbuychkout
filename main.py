from selenium import webdriver

driver = webdriver.Firefox()

url = 'insert your URL here'

driver.get(url)

driver.maximize_window()
click = driver.find_element_by_xpath('insert XPATH to button here')
click.click()
checkout = driver.find_element_by_xpath('insert checkout element button here')
checkout.click()
