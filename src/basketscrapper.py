## Definición de llibreries necessàries
from Robots import Checks
from Export import CustomPDF
import whois
import builtwith
import sys

## Definición de constants
USER_AGENT="'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'"
DELAY_PETICIONES = 0
PARAMETRES = 3
## Comprovació de paràmetres
if (sys.argv[0] == "python"):
    PARAMETRES = 4
if len (sys.argv) != PARAMETRES :
    print("Utilització: python basketscrapper.py <competició> <any>")
    print("On competició pot ser: euroleague, acb, nba")
    print("Referent a la competició només tenim desenvolupat el mòdul euroleague")
    print("On any pot ser: 2016,1992.... o tots")
    sys.exit (1)
competicio = sys.argv[PARAMETRES - 2]
anycompeticio=sys.argv[PARAMETRES -1]

## Avaluem el paràmetre introduït per saber quines llibreries carreguem i quines constants 
## definim segons el tipus de competició
if (competicio == "euroleague"):
    from euroleague import *
    URL = "https://www.euroleague.net"
    URI_ROBOTS = "/robots.txt"
    SITE = "euroleague.net"
elif (competicio == "nba"):
    from nba import *
elif (competicio == "acb"):
    from acb import *

## Comprobem si la URL conté el fitxer robots.txt
testRobots = Checks(URL)
existeixRobots= testRobots.existeix_robots(URI_ROBOTS)

if (existeixRobots):

    ## Recuperem el fitxer robots.txt per a comprobar les seves dades
    rob = testRobots.robots(URI_ROBOTS)
    DELAY_PETICIONES = testRobots.existeix_delay(USER_AGENT)
    sitemap = rob.sitemaps

## Avaluem les URL's de la competició especificada que contenen les estadístiques
if (competicio == "euroleague"):
    print("La url d'estadistiques esta permesa?",testRobots.url_permesa("https://www.euroleague.net/main/statistics",USER_AGENT))
    print("La url de resultats esta permesa?",testRobots.url_permesa("https://www.euroleague.net/main/results",USER_AGENT))

## Tamany de la web
tamanyWeb = testRobots.tamany_web(SITE)

## Tecnologia de la web
tecnologiaWeb = builtwith.builtwith(URL)

## Propietari de la web
propietariWeb = whois.whois(URL)

#Web Scraping del domini avaluat
stats=euroleague(DELAY_PETICIONES,anycompeticio)
stats.generarCSV()

## Exportació de dades informatives sobre el domini avaluat
exportPdf=CustomPDF()
exportPdf.informacio_scrap_pdf(SITE + ".pdf",existeixRobots,rob,DELAY_PETICIONES,sitemap,tamanyWeb,tecnologiaWeb,propietariWeb)
