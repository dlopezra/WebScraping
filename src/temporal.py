 #https://github.com/rafoelhonrado/foodPriceScraper
 #https://github.com/tteguayco/Web-scraping
 #https://github.com/search?q=tipologia
 #https://github.com/GViscarretUOC/TipologiaYCicloDeDatos
 #https://github.com/alessalazar89/Tipologia
## Se ha instalado reppy pip install reppy
## S'ha instal·lat e builtwith amb pip install builtwith
## pip install python-whois
## pip install beautifulsoup4
## pip install google
 
 #rrate = rp.request_rate("*")
    #rrate.requests
    #rrate.seconds
    #rp.crawl_delay("*")
    #rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")
    #rp.can_fetch("*", "http://www.musi-cal.com/")

#from urllib import parse
#from urllib import robotparser
#AGENT_NAME = 'PyMOTW'
#URL_BASE = 'https://example.com/'
#parser = robotparser.RobotFileParser()
#parser.set_url(parse.urljoin(URL_BASE, 'robots.txt'))
#parser.read()


#from urllib.request import urlopen
#req = urllib.request.Request("https://www.euroleague.net/robots.txt", headers={'User-Agent' : "Magic Browser"}) 
#with urlopen(req) as stream:
#    print(stream.read().decode("utf-8"))


#def does_url_exist(url):
#    try: 
#        r = requests.head(url)
#        if r.status_code < 400:
#            return True
#        else:
#            return False
#    except requests.exceptions.RequestException as e:
#        print(e)
#        # handle your exception

import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt")
rp.read()
rrate = rp.request_rate("*")
#rrate.requests
#rrate.seconds
rp.crawl_delay("*")
rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")
rp.can_fetch("*", "http://www.musi-cal.com/")



rob=test.robots("/robots.txt");
rob.crawl_delay("*");
rob.can_fetch("*", "https://www.euroleague.net/main/statistics")
#rrate = testrp.request_rate("*")
#print(rrate)
#rrate.requests
#rrate.seconds
#print(testrp.crawl_delay("*"))
#print(testrp.request_rate("*"))
#import urllib.robotparser
#rp = urllib.robotparser.RobotFileParser()
#rp.set_url('https://www.euroleague.net/robots.txt')
#rp.read()
#rrate = rp.request_rate("*")
#rrate.requests
#rrate.seconds
#rp.crawl_delay("*")
#rp.can_fetch("*", "https://www.euroleague.net/main/statistics")

import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='Get Google Count.')
parser.add_argument('word', help='word to count')
args = parser.parse_args()

r = requests.get('http://www.google.com/search',
                 params={'q':'"euroleague.net+"',
                         "tbs":"li:1"}
                )

soup = BeautifulSoup(r.text)
print soup.find('div',{'id':'resultStats'}).text