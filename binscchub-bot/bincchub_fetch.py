from selenium import webdriver
import time

URL = "https://binscchub.com/"
DUMPFILE = "dump.txt"
LOGFILE = "log.txt"

CONST_LOGEVENTS = 1
CONST_DUMPDATA = 2

class BinCCBot():

	def __init__(self, logfile, dumpfile):

		self.logfilepath = logfile
		self.dumpfilepath = dumpfile

		try:
			self.browser_process = webdriver.Firefox()
			self.browser_process.get(URL)
		except Exception as E: raise E


	def GrepBinData(self, dump_bool, log_bool, max_found):

		fetch_success = 0
		log_wait_bypass = 0
		fetched_entry_array = []

		try:

			if log_bool == CONST_LOGEVENTS : logfd = open(self.logfilepath, "a")

			for post_iter in range(300, 399):

				log_wait_bypass = 0

				try:

					if log_bool == CONST_LOGEVENTS : logfd.write("[{}] : searching for post-{}\n".format(time.ctime(), post_iter))

					element = self.browser_process.find_element_by_id('post-{}'.format(str(post_iter))).click()
					entry_content = self.browser_process.find_element_by_class_name('entry-content').text
					self.browser_process.back()

					fetch_success += 1
					fetched_entry_array.append(entry_content)
					if log_bool == CONST_LOGEVENTS : logfd.write("[{}] : \tpost-{} found\n".format(time.ctime(), post_iter))

					if dump_bool == CONST_DUMPDATA:

						dumpfd = open(self.dumpfilepath, "a")
						dumpfd.write("\n\nnew entry data (post-{}) : \n\n".format(str(post_iter)))
						dumpfd.write(entry_content)
						dumpfd.close()

					else: pass

				except Exception as E: 
					if log_bool == CONST_LOGEVENTS : logfd.write("[{}] : \terror raised : {}\n".format(time.ctime(), str(E)))
					log_wait_bypass = 1			
				
				if fetch_success >= max_found: break

				if log_wait_bypass == 1: 
					time.sleep(1)
				else: time.sleep(3)

		except Exception as E: raise E

		if log_bool == CONST_LOGEVENTS : logfd.close()
		if dump_bool == CONST_DUMPDATA : dumpfd.close()

		return fetched_entry_array


	def ParseBinData(self, data):

		actual_bin_parsed = ""
		bin_parsed_array = []

		try: 

			for entries in data:

				entry_content_stripped = entries.split('\n')

				for x in entry_content_stripped[1][7:]:

					if(x != 'x'):

						actual_bin_parsed += x

					else: break

				bin_parsed_array.append(actual_bin_parsed)

			return bin_parsed_array

		except Exception as E: raise E


def MainProcess():

	try:

		process = BinCCBot(LOGFILE, DUMPFILE)

		print("|+| App initialized")

		bin_data = process.GrepBinData(CONST_DUMPDATA, CONST_LOGEVENTS, 2)

		print("|+| BIN data fetched")

		bin_data_parsed = process.ParseBinData(bin_data)

		print("|+| BIN data parsed : \n| |")

		for i in bin_data_parsed:

			print("|i| \t{}".format(i))

	except Exception as E: print("|x| Error raised during process : {}".format(str(E)))

MainProcess()
