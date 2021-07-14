import shodan
import time
from os import system
import os

cls = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

menu = '''
[===========================================]
 
 [ C.A.S ]~>
 
 [ Shodan search engine. 
 [ version 1.0        
 [ Created by Cyber-Crypto.Anarchy.Squad
 [ Telegram C.A.S - https://t.me/anarchy_squad
 [ Telegram Hydra crash bots - https://t.me/EvLVHydraNews 
 
 [1] Search IPs.
 [2] Search info.
 [3] Help shodan dorks.
 [4] Exit.

[===========================================]'''

dorksMenu = '''
Dorks shodan, these are well-composed queries to find information.
Dorks:
	[=============================================]
	[ country:   (Example: country:RU
	[ city:      (Example: country:RU city:«Moscow»
	[ os:        (Example: os:«windows 2003»
	[ port:      (Example: port:8080
	[ hostname:  (Example: hostname:shodan
	[ net:       (Example: net:190.73.40.50/24
	[ product:   (Example: product:openssh
	[=============================================]'''

def searchIP():
	try:
		try:
			shodanApiKey = input('\nShodan API key: ')
			api = shodan.Shodan(shodanApiKey)
			dork = input('\nYour dork to search: ')
			results = api.search(dork)  
			IPs = open('resultsIP.txt', 'w')
			ipList = []
			for result in results['matches']:
				IP = result['ip_str']
				if IP not in ipList:
					IPs.write(f'{IP}\n')
					ipList.append(IP)
		except (shodan.APIError)as error:
			print(f'Error: {error}')
	except KeyboardInterrupt:
		print('\nExit...')
	nextCode = input('\nPress key to continue.')

def searchIfo():
	try:
		try:
			shodanApiKey = input('\nShodan API key: ')
			api = shodan.Shodan(shodanApiKey)
			dork = input('\nYour dork to search: ')
			results = api.search(dork)
			info = open('resultsInfo.txt', 'w')
			for result in results['matches']:
				data = (f'''IP: {result['ip_str']}
{result['data']}''')
				info.write(f'{data}\n')
		except (shodan.APIError)as error:
			print(f'Error: {error}')
	except KeyboardInterrupt:
		print('\nExit...')
	nextCode = input('\nPress key to continue.')

while True:
	cls()
	print(menu)
	try:
		select = str(input('\nSelect: ')) 
		if select == '1':
			searchIP()
		elif select == '2':
			searchIfo()
		elif select == '3':
			print(dorksMenu)
			nextCode = input('\nPress key to continue.')
		elif select == '4':
			print('\nGoodby!')
			time.sleep(2)
			exit()
		else:
			print('\nInvalid option.')
			nextCode = input('\nPress key to continue.')
	except KeyboardInterrupt:
		print('\nUse Item 3.')
		time.sleep(3)
