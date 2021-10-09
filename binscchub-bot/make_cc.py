from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import requests
#from BeautifulSoup import BeautifulSoup
import urllib


URL='file:///home/XXXX/Bureau/aa/CC_Gen/CC_Gen.html'

browser = webdriver.Firefox()
browser.get(URL)

time.sleep(1)


#BIN_un = open(LOGFILE, "r")
#for line in BIN_un:
BIN = 55478
CCV2 =547
MONTH = 6
YEAR = 2030
YEAR=format(str(YEAR))
MONTH=format(str(MONTH))
element = browser.find_element_by_id("ccpN")
element.send_keys(BIN)

amount = browser.find_element_by_name("ccghm")
time.sleep(0.5)
amount.send_keys(10)

ccv2= browser.find_element_by_id('eccv')
ccv2.clear()
ccv2.send_keys(CCV2)

year= browser.find_element_by_name('eyear')
#year.click()
select=Select(browser.find_element_by_name('eyear'))
select.select_by_visible_text(YEAR)

time.sleep(0.5)

month= browser.find_element_by_name('emeses')
#month.click()
select=Select(browser.find_element_by_name('emeses'))
select.select_by_visible_text(MONTH)

submit = browser.find_element_by_xpath('''//*[@id="gerar"]''')
time.sleep(1)
submit.click()












