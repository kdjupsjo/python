from httplib import simple_get
from MailHelper import MailInit
from bs4 import BeautifulSoup
import datetime




def WalinFastigheter():
	raw_html =  simple_get("http://wahlinfastigheter.se/lediga-objekt/lagenhet/")


	print(len(raw_html))

	html = BeautifulSoup(raw_html, 'html.parser')

	fastigheter = html.find_all('div', attrs={'class':'fastighet'})

	
	message = ""
	for fast in fastigheter:
		for a in fast.select('a'):
			title = a.get('title')
			
			if(title != None):
				message += title
				message += '\n'
				message += a.get('href')
			else:
				Report("Inga fastigheter ligger ute idag.", fastigheter)



	if(len(message) > 0 ):
		FormEmail(message)

	print(message)





def Forvaltaren():
	raw_html =  simple_get("https://www.forvaltaren.se/ledigt/lagenhet")


	print(len(raw_html))

	html = BeautifulSoup(raw_html, 'html.parser')

	fastigheter = html.find_all('tr', attrs={'class':'listitem-odd '})
	


def IKANO(): 
	
	raw_html =  simple_get("https://ikanobostad.se/hyra-bostad/#residents")


	print(len(raw_html))

	html = BeautifulSoup(raw_html, 'html.parser')
	fastigheter = html.find_all('tr', attrs={'class':'is-linked'})
	
	address = set()

		


def Report(message, data):
	currentTime = datetime.datetime.now()
	message = str(currentTime) + ': ' + message + '\n'; 
	
	with open('log.txt', 'a') as log:
		log.write(message)
		log.close()

	
	filenametest = 'test-{date:%Y-%m-%d}.txt'.format( date=datetime.datetime.now() )

	fileName = str(currentTime)[-8] + '.txt'
	dataFile = open(filenametest, 'w')
	dataFile.write(str(data))
	dataFile.close()


WalinFastigheter()