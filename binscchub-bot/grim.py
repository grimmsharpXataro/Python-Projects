from selenium import webdriver
import time


url = 'https://binscchub.com/'

browser = webdriver.Chrome()
browser.get(url)

time.sleep(1)

for i in range(300, 399):

	try:

		element=browser.find_element_by_id('post-{}'.format(str(i)))
		element.click()

		bins = browser.find_element_by_class('entry-content')
		bin_content = bins.text 

	except: pass
