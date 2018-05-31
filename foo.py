from httplib import simple_get
from MailHelper import MailInit
from bs4 import BeautifulSoup




def WalinFastigheter():
	raw_html =  simple_get("http://wahlinfastigheter.se/lediga-objekt/lagenhet/")


	print(len(raw_html))

	html = BeautifulSoup(raw_html, 'html.parser')

	fastigheter = html.find_all('div', attrs={'class':'fastighet'})

	
	print(fastigheter)

	message = ""
	for fast in fastigheter:
		for a in fast.select('a'):
			title = a.get('title')
			
			if(title != None):
				message += title
				message += '\n'
				message += a.get('href')



	if(len(message) > 0 ):
		FormEmail(message)

	print(message)





def Forvaltaren():
	raw_html =  simple_get("https://www.forvaltaren.se/ledigt/lagenhet")


	print(len(raw_html))

	html = BeautifulSoup(raw_html, 'html.parser')

	fastigheter = html.find_all('tr', attrs={'class':'listitem-odd '})
	

	print(fastigheter)

def IKANO(): 
	
	raw_html =  simple_get("https://ikanobostad.se/hyra-bostad/#residents")


	print(len(raw_html))

	html = BeautifulSoup(raw_html, 'html.parser')
	fastigheter = html.find_all('tr', attrs={'class':'is-linked'})
	
	address = set()

	for fastighet in fastigheter:
		print(fastighet.select('td'))



	print(fastigheter)



IKANO()