from selenium import webdriver


URL = 'https://binscchub.com/'
LOGFILE = "log.txt"

browser = webdriver.Firefox()
browser.get(url)

time.sleep(1)

for i in range(300, 399):

	try:

		element=browser.find_element_by_id('post-{}'.format(str(i)))
		element.click()

		bins = browser.find_element_by_class('entry-content')
		bin_content = bins.text 

		# trivial

		try:

			fd = open(LOGFILE, "a").write(bin_content)
			fclose(fd)

		except Exception as E:

			print("|-| An exception occured : " + str(E))

	except: pass


