from reppy.robots import Robots
from bs4 import BeautifulSoup
import requests
import re

SEARCH_URL="https://www.google.com/search?q="

class Checks():
    
    def __init__(self,chkurl):
        self.url = chkurl
        self.ro = []
        self.tamany = 0 
	
    def existeix_robots(self, path):
        try: 
            r = requests.head(self.url + path)
            if r.status_code < 400:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(e)
            # handle your exception

    def robots(self,path):
        self.ro = Robots.fetch(self.url + path)
        return self.ro
    
    def url_permesa(self,url,agent):
        try:
            return self.ro.allowed(url,agent)
        except requests.exceptions.RequestException as e:
            print(e)

    def existeix_delay(self,agent):
        try:
            return self.ro.agent(agent).delay
        except requests.exceptions.RequestException as e:
            print(e)

    def tamany_web(self,url):
        try:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
            }   
            pagina = requests.get(SEARCH_URL + "site:" + url, headers=headers)
            soup = BeautifulSoup(pagina.content, 'html.parser')
            contador = soup.find(id="resultStats")
            return int(''.join(re.findall(r'\d+', contador.text.split()[1])))
        except requests.exceptions.RequestException as e:
            print(e)