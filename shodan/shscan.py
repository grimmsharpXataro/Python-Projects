##################################################
#
#		Shodan database lookup API script (by Gr1mmsh@rm).
#
#		Read the README.md for documentation
#
##################################################

import shodan
import os


# Put your API key here
APIKey = ""


__banner__=  """
 :'######::'##::::'##::'#######::'########:::::'###::::'##::: ##:
 '##... ##: ##:::: ##:'##.... ##: ##.... ##:::'## ##::: ###:: ##:
  ##:::..:: ##:::: ##: ##:::: ##: ##:::: ##::'##:. ##:: ####: ##:
 . ######:: #########: ##:::: ##: ##:::: ##:'##:::. ##: ## ## ##:
 :..... ##: ##.... ##: ##:::: ##: ##:::: ##: #########: ##. ####:
 '##::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##.... ##: ##:. ###:
 . ######:: ##:::: ##:. #######:: ########:: ##:::: ##: ##::. ##:
 .......:::..:::::..:::.......:::........:::..:::::..::..::::..::
 '##::::::::'#######:::'#######::'##:::'##:'##::::'##:'########::
  ##:::::::'##.... ##:'##.... ##: ##::'##:: ##:::: ##: ##.... ##:
  ##::::::: ##:::: ##: ##:::: ##: ##:'##::: ##:::: ##: ##:::: ##:
  ##::::::: ##:::: ##: ##:::: ##: #####:::: ##:::: ##: ########::
  ##::::::: ##:::: ##: ##:::: ##: ##. ##::: ##:::: ##: ##.....:::
  ##::::::: ##:::: ##: ##:::: ##: ##:. ##:: ##:::: ##: ##::::::::
  ########:. #######::. #######:: ##::. ##:. #######:: ##::::::::
 ........:::.......::::.......:::..::::..:::.......:::..:::::::::
    ______________________________________________________________
|  /"""

class ShodanLookup():

	def __init__(self, APIkey):

		try:

			self.apiprocess = shodan.Shodan(APIKey)

		except Exception as E: return E


	def HostLookup(self, host):

		try:

			search = self.apiprocess.host(host)

			print("| |\n| | Infos for host {} (last update : {}): ".format(host, search.get('last_update', 'n/a')))

			print("| |\n|i| \tHost IP : {}\n|i| \tHost Organization : {}\n|i| \tISP : {}\n|i| \tHostname(s) : {}\n|i| \tOperating system : {}\n|i| \tArea code : {}\n|i| \tPostal code : {}\n|i| \tDMA code : {}\n|i| \tDomain(s) : {}\n|i| \tPostal code : {}\n|i| \tCountry code : {}\n|i| \tLocation : {}\n|i| \tCity : {}\n|i| \tTag(s) : {}\n|i| \tTimestamp : {}\n| |"
			.format(search['ip_str'], 
			search.get('org', 'n/a'), 
			search.get('isp', 'n/a'),
			search.get('hostnames', 'n/a'), 
			search.get('os', 'n/a'), 
			search.get('area_code', 'n/a'), 
			search.get('postal_code', 'n/a'),
			search.get('dma_code', 'n/a'), 
			search.get('domains', 'n/a'), 
			search.get('postal_code', 'n/a'), 
			search.get('country_code', 'n/a'),
			search.get('location', 'n/a'), 
			search.get('city', 'n/a'),
			search.get('tags', 'n/a'), 
			search.get('timestamp', 'n/a')))

			input("|i| Press ENTER to continue...")
			print("| |")

			for x in search['data']: print("|+| Port {} open\n| | Port details :\n|  \\_________\n\n{}    _________\n|  /".format(x['port'], x['data']))

		except Exception as E: raise E


	def SearchLookup(self, term):

		try:

			search = self.apiprocess.search(term)

			print("| |\n|i| {} matching hosts for the term '{}' :\n| |".format(search['total'], term))

			for x in search['matches']: print("|i| {}".format(x['ip_str']))

		except Exception as E: raise E


	def ExploitLookup(self, term):

		try:

			exploits = self.apiprocess.Exploits(self.apiprocess)
			search = exploits.search(term)

			print("| |\n| | Matching results for '{}' : \n| |".format(term))

			for x in search['matches']: print("|i| {} ({}), ID : {}\n|i| >> {}\n| |".format(x['source'], x['cve'], x['_id'], x['description']))

		except Exception as E: raise E


	def PrintKeyInfo(self):

		print("| |")

		try:

			info = self.apiprocess.info()
			for x in info: print("|i| {} = {}".format(x, info[x]))

		except Exception as E: raise E




def HelpPage():

	print("| |")
	print("| | List of available commands : \n| |")
	print("|i| ip <host> :                       Search informations for <host>")
	print("|i| search <term / exploit> <term> :  Search term / exploit results for <term>")
	print("|i| keyinfo :                         Print actual key info")
	print("|i| help :                            Display this page")
	print("|i| exit :                            Exit app")
	print("|i| cls :                             Clear terminal")


def ErrorHandler(error): print("| |\n|-| Error raised during process : " + str(error))


def MainProcess():

	try:

		print(__banner__)

		try:

			print("| |\n|*| Verifying API key...")

			process = ShodanLookup(APIKey)

		except Exception as E:
			ErrorHandler(E)
			exit(0)
	
		print("|+| Vaild API key\n| |\n| | Info :")
		process.PrintKeyInfo()

		while True:

			try:

				command = input("| |\n|>| Shodan Lookup > ")

				commanddict = command.split(' ')

				if commanddict[0] == "ip":

					if commanddict[1]:

						process.HostLookup(commanddict[1])

					else: print("|-| Invalid command")

				elif commanddict[0] == "search":

					if commanddict[1] and commanddict[2]:

						if commanddict[1] == "term":

							process.SearchLookup(commanddict[2])

						elif commanddict[1] == "exploit":

							process.ExploitLookup(commanddict[2])

						else: print("|-| Invalid command")

					else: print("|-| Invalid command")

				elif commanddict[0] == "keyinfo":

					process.PrintKeyInfo()

				elif commanddict[0] == "help":

					HelpPage()

				elif commanddict[0] == "exit":
				
					print("| |\n|i| Exiting app...\n| |")
					exit(0)

				elif commanddict[0] == "cls":

					os.system("cls||clear")
					print(__banner__)

				else: print("| |\n|-| Invalid command")

			except Exception as E: ErrorHandler(E)
	
	except KeyboardInterrupt:
		print("\n|i| Exiting app... (Ctrl+C)\n| |")
		exit(0)

MainProcess()
