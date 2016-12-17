# -*- coding: utf8 -*-
import fileinput
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

""" Recuperation des donnees HTML
html = urlopen("http://www.dota2.com/700/gameplay/#HeroChanges")
data = html.read().decode("utf-8")
print(data)


f = open("data.xml", 'w+')
f.write(data)
f.close()
""" 


""" On les parse dans un fichier JSON
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
"""

with open('data.json') as data_file:    
    data = json.load(data_file)


def parseType(givenType):
	dico = {}
	dico[givenType]={}
	dico[givenType]['heroes'], dico[givenType]['data'] = [] , []
	count =0
	for hero in data.keys():
		for level in data[hero].keys():
			for choice in data[hero][level].keys():
				count = count +1
				print(data[hero][level][choice]['type'])
				if data[hero][level][choice]['type'] == givenType:
					valeur = data[hero][level][choice]['valeur']
					dico[givenType]['data'].append([int((int(level)-10)/5),len(dico[givenType]['heroes']), int(valeur)])
					dico[givenType]['heroes'].append(hero)
	print(count)
	return dico


# def transformJS(file):
# 	for linenum,line in enumerate( fileinput.FileInput(file,inplace=1) ):
# 	   if linenum==0 :
# 	     print("parsed_data =")
# 	     print(line.rstrip())
# 	   else:
# 	     print(line.rstrip())

with open('talent_data/parsed_data.json', 'w') as fp:
    json.dump(parseType("Damage"), fp)
    fp.close()

    f1 = open('talent_data/parsed_data.json', 'r')
    fin = f1.read()
    f1.close()
    f2 = open('talent_data/parsed_data.js', 'w')
    f2.write('parsed_data='+fin)
    f2.close()
