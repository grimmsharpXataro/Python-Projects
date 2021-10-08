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

		element = browser.find_element_by_id('post-{}'.format(str(i)))
		element.click()

		bins = browser.find_element_by_class_name('entry-content')
		bin_content = bins.text 

		# trivial

		try:

			fd = open(LOGFILE, "a").write(bin_content)
			close(fd)

			print("|+| OK")

		except Exception as E:

			print("|-| An exception occured : " + str(E))

	except Exception as E: print("|-| Not found ({})".format(str(E)))	

	time.sleep(3)




