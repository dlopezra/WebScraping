## Definición de librerias necesarias
from Robots import Checks
from Export import create_pdf
import whois
import builtwith

## Definición de constantes
URL = "https://www.euroleague.net"
URI_ROBOTS = "/robots.txt"
SITE = "euroleague.net"
USER_AGENT="'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'"
DELAY_PETICIONES = 0

## Comprobamos si la URL contiene un fichero robots.txt
testRobots = Checks(URL)
existeixRobots= testRobots.existeix_robots(URI_ROBOTS)

if (existeixRobots):

    ## Recuperamos el fichero robots.txt para comprobar sus datos
    rob = testRobots.robots(URI_ROBOTS)
    DELAY_PETICIONES = testRobots.existeix_delay(USER_AGENT)
    sitemap = rob.sitemaps

print(testRobots.url_permesa("https://www.euroleague.net/main/statistics",USER_AGENT))
## Tamaño de la web
tamanyWeb = testRobots.tamany_web(SITE)
print(tamanyWeb)
## Tecnologia de la web
tecnologiaWeb = builtwith.builtwith(URL)
print(tecnologiaWeb) 
## Propietario de la web
propietariWeb = whois.whois(URL)
print(propietariWeb)

create_pdf("test.pdf")
