# WebScraping

M2.951 - Tipologia i cicle de vida de les dades - Pràctica 1 - WebScraping

## Membres de l'equip

La pràctica ha estat realitzada per **Daniel López**. 

## Fitxers de codi font

Podem trobar els fitxers de codi font a la carpeta **src**:

* **basketscrapper.py**: funció principal per a realitzar el web scraping. Primer de tot es realitza una avaluació inicial del site, revisant el fitxer robots.txt, el sitemap, la grandària del site, la tecnologia emprada i el propietari del lloc. Aquesta informació s’extreu amb l’ajut de la llibreria “Robots.py”, i a més es guarda en un fitxer pdf (en el nostre cas euroleague.pdf) amb l’ajut de la llibreria “Export.py”. La informació recollida ens permet realitzar el web scraping de la web d’estadístiques ajustant els diversos valors recollits, i generant el dataset amb l’ajut de la llibreria “euroleague.py”.
* **robots.py**: llibreria que ens permet realitzar l’avaluació inicial d’un site.
* **export.py**:  llibreria que ens permet generar un fitxer pdf amb la informació que se li passa.
* **euroleague.py**: llibreria que ens permet realitzar el web scraping a la web d’estadístiques de l’eurolliga.

## Documentació

Les respostes a la pràctica, així com la documentació generada pel web scraping la podem trobar a la carpeta **pdf**:

* **daniellopez_prac1.pdf**: document pdf amb les respostes a la pràctica.
* **euroleague.net.pdf**: document pdf amb l'avaluació inicial del site.

## Dataset

Per a la pràctica s'han generat dos datasets corresponents a les dades de les temporades 2017 i 2018 de l'Eurolliga que es troben a la carpeta **csv**:
* **euroleague.net2017.csv**: dades corresponents a la temporada 2017-2018.
* **euroleague.net2018.csv**: dades corresponents a la temporada 2018-2019.

## Requeriments

Per a poder executar el codi font abans esmentat es requereix la instal·lació de les següents llibrerires:
```
pip install requests
pip install lxml
pip install beautifulsoup4
pip install fpdf
```
## Execució

Per a poder executar l'script:
```
python basketscrapper.py <competició> <any>
```
On competició pot ser (**actualment només està definit el mòdul per l'eurolliga**): 
* euroleague
* acb
* nba

I any pot ser: 
* 2000
* 2016
* tots

### Exemples
```
python basketscrapper.py euroleague 2018
python basketscrapper.py euroleague tots
```
