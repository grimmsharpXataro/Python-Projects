# fetch bins CC hub informations

from selenium import webdriver
import time

URL = 'https://binscchub.com/'
LOGFILE = "log.txt"

browser = webdriver.Firefox()
browser.get(URL)

time.sleep(1)

for i in range(300, 399):

	try:

		print("|*| Trying post-{}".format(str(i)))

		element = browser.find_element_by_id('post-{}'.format(str(i))).click()

		bins = browser.find_element_by_class_name('entry-content')
		bin_content = bins.text 

		# trivial

		try:

			fd = open(LOGFILE, "a")
			fd.write("\n\nnew post data (post-{}) : \n\n".format(str(i)))
			fd.write(bin_content)
			fd.close()

			print("|+| \t-> OK")

		except Exception as E:

			print("|-| An exception occured : " + str(E))

		browser.back()

	except Exception as E: print("|-| Not found ({})".format(str(E)))	

	time.sleep(3)




