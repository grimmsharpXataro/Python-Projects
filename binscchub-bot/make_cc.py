from selenium import webdriver
import time
import requests
#from BeautifulSoup import BeautifulSoup
import urllib


URL='file:///home/ataro666/Bureau/aa/CC_Gen/CC_Gen.html'

browser = webdriver.Firefox()
browser.get(URL)

time.sleep(1)




element = browser.find_element_by_id("ccpN")
element.send_keys(547874)
submit = browser.find_element_by_xpath('''//*[@id="gerar"]''')
time.sleep(1)
submit.click
	

#<input type="text" class="form-control" id="ccpN" name="ccp"  value="" placeholder="xxxx xxxx xxxx xxxx" maxlength="19">








