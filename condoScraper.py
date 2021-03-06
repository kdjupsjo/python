from httplib import simple_get
from MailHelper import MailInit
from bs4 import BeautifulSoup
import datetime


def WalinFastigheter():
	
	site_url = "http://wahlinfastigheter.se/lediga-objekt/lagenhet/"
	raw_html =  simple_get(site_url)


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
		#MailInit(message)
	else:
		#MailInit("Inga fastigheter ligger ute idag, checked: " + site_url)



def M2Gruppen():
	#äkta
	#raw_html = simple_get("https://www.m2gruppen.se/lediga-bostader/?ort=enk%C3%B6ping&antal_rum=V%C3%A4lj+antal+rum&filtered=1") 
	#test
	raw_html = simple_get("https://www.m2gruppen.se/lediga-bostader/?ort=sommen&antal_rum=V%C3%A4lj+antal+rum&filtered=1")


	html = BeautifulSoup(raw_html, 'html.parser')
	fastigheter	= html.find_all('div', attrs={'class':'box news-grid__item'})

	message = ""; 
	for condo in fastigheter: 
		link = condo.find('a', attrs={'class':'news-grid__link'})
		href = "https://www.m2gruppen.se"
		href += link.get('href')
		title = link.find('h2').contents
		message += str(title) + ": " + href + "\n"

	if(len(message) > 0 ):
		#MailInit(message)
		Report("Lägenheter hos M2Gruppen hittades", fastigheter)
	else:
		Report("Inga Lägenheter ligger ute idag.", fastigheter)	



def Forvaltaren():
	raw_html =  simple_get("https://www.forvaltaren.se/ledigt/lagenhet")


	print(len(raw_html))

	html = BeautifulSoup(raw_html, 'html.parser')

	fastigheter = html.find_all('tr', attrs={'class':'listitem-odd '})
	fastigheter_even = html.find_all('tr', attrs={'class':'listitem-even '})


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

	filename = 'results-{date:%Y-%m-%d}.txt'.format( date=datetime.datetime.now() )
	dataFile = open(filename, 'w')
	dataFile.write(str(data))
	dataFile.close()


WalinFastigheter()
M2Gruppen()

