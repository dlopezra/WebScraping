from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
import sys
import os

#Definició de constants de la web de la eurolliga
SITE = "euroleague.net"

class euroleague():
    URL = "https://www.euroleague.net"
    URI_ROBOTS = "/robots.txt"
    SITE = "euroleague.net"
    def __init__(self,delay,season):
        self.urlgame='https://www.euroleague.net/main/results/showgame?gamecode=257&seasoncode=E2017#!boxscore'
        self.estadistiques=""
        self.delay=delay
        self.allseasons=0
        any = datetime.now()
        if (season == "tots"):
            self.season=2000
            self.allseasons=1
        elif (int(season )< 2000 or int(season) > any.year):
            if (any.month >= 1 and any.month<7):
                self.season = any.year - 1
            else:
                self.season = any.year
        else:
            self.season=season
        filepath=SITE + str(self.season) + ".csv"
        self.csv=open(filepath,'w+')
    
    def scrapmatch(self,content):
        statplay=0
        equip=0
        data=""
        camp=""
        ronda=""

        soup = BeautifulSoup(content,'lxml')

        # Web Scraping de la web
        players = soup.find_all("td", class_="PlayerContainer")
        #players2 = soup.find("td", class_="PlayerContainer").next_siblings
        teams = soup.find_all("div",class_="eu-team-stats-teamname")
        coachs = soup.find_all("span",class_="title")
        round = soup.find("div", class_="round-header")
        score = soup.find("div",class_="game-score")
        date = soup.find("div",class_="dates")

        # Recollim la data del partit
        data=date.get_text()
        data=data.splitlines()
        camp=data[4]
        data[1]=data[1].replace(",","")
        data[1]=data[1].replace("CET","")
        data[1]=data[1].replace(" : "," ")
        data=datetime.strptime(data[1], '%B %d %Y %H:%M')
        dades=data.strftime('%B %d %Y %H:%M')+ "," + camp + ","

        # Recollim la ronda del partit
        ronda=round.find_all("span")
        for i in ronda:
            dades=dades + i.get_text() + ","

        # Recollim el resultat del partit
        finalscore = score.find_all("span",class_="score")

        #Recollim les dades dels jugadors del partit
        for player in players:
            jugador=player.get_text()
            if ("Team" in jugador):
                equip=equip+1
            else:
                temp=jugador.split(",")
                jugador=temp[1].lstrip() + " " + temp[0]
                coach=coachs[equip].next_element.next_element.next_element.split(",")
                coach=coach[1].lstrip() + " " + coach[0]
                dadesjug=dades + teams[equip].get_text().rstrip().lstrip() + "," + finalscore[equip].get_text() + "," + coach + "," + jugador + ","
                playerstat = player.next_siblings
                imparell=0
                for stat in playerstat:
                    if (imparell==1):
                        dadesjug= dadesjug + stat.string.rstrip() + ","
                        imparell=0
                    else:
                        imparell=imparell+1
                self.estadistiques= self.estadistiques + "\n" + dadesjug[:-1]
                statplay = statplay + 1
        self.csv.write(self.estadistiques)
        self.estadistiques=""   

    def webscrap(self,season):
        ws=euroleague(self.delay,season)
        cap=ws.capçalera()
        self.csv.write(cap)
        gamecode=1
        urlgame='https://www.euroleague.net/main/results/showgame?gamecode=' + str(gamecode) + '&seasoncode=E' + str(season) + '#!boxscore'
        page = requests.get(urlgame)
        while(page.status_code==200):
            ws.scrapmatch(page.content)
            gamecode = gamecode + 1
            urlgame='https://www.euroleague.net/main/results/showgame?gamecode=' + str(gamecode) + '&seasoncode=E' + str(season) + '#!boxscore'
            time.sleep(self.delay)
            page = requests.get(urlgame)
    
    def capçalera(self):
        cap="Data partit, Camp, Temporada, Ronda, Fase, Equip, Punts, Entrenador, Jugador, Minuts, Punts, Intents2, Intents3, Tirs lliures, Rebots ofensius, Rebots defensius, Rebots totals, Assistencies, Robatoris, Perdues, Bloquejos fets, Bloquejos rebuts, Faltes realitzades,Faltes rebudes, PIR (Performance Index Rating)"
        return cap

    def generarCSV(self):
        ws=euroleague(self.delay,self.season)
        if (self.allseasons == 1):
            any = datetime.now()
            anyproces = int(self.season)
            for x in range(anyproces,any.year):
                ws.webscrap(x)
        else:
            ws.webscrap(self.season)
        self.csv.close()



