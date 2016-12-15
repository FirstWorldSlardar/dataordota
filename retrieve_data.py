# -*- coding: utf8 -*-
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

""" Recuperation des donnees 
html = urlopen("http://www.dota2.com/700/gameplay/#HeroChanges")
data = html.read().decode("utf-8")
print(data)


f = open("data.xml", 'w+')
f.write(data)
f.close()
"""

soup = BeautifulSoup(open("data.xml"), "lxml").find(id="HeroChanges")

dic = {}

count = 1
for element in soup.find_all('figure'):
	hero_name = element.find('h1').text.split(":")[0]
	# on récupère le nom du héro contenu dans le titre (qui est séparé du reste par ":"
	# systématiquement)

	dic[hero_name] = {}
	for li in element.ol.find_all('li'):
		niveau = li.text[6:].split(':')[0] 
		# niveau du héro avec changement (10/15/20/25)
		contenu = li.text[10:]

		print(hero_name)
		print(contenu)
		dic[hero_name][niveau] = {}
		for i in range(2):
			try:
				contenuSplit = contenu.split(' OR ')[i]
			except:
				contenuSplit = contenu.split(' OR')[i]

			dic[hero_name][niveau][i+1] = \
			{
				'type':contenuSplit.split(' ', 1)[1] ,
				'valeur':contenuSplit.split(' ', 1)[0],
				'string': contenuSplit
			}
		# on ajoute les deux possibilités pour chaque niveau
	
	count +=1
	print(count)

print(count)
# enregistrement en json
with open('data.json', 'w') as fp:
    json.dump(dic, fp)
# A prendre en compte plus tard :

# HP et Health est la même chose
