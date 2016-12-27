# -*- coding: utf8 -*-
import re
import operator
import math
import fileinput
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

def compose(f, g):
    return lambda *args: f(g(*args))

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


def parseValue(chaine):
	try:
		returnString = re.findall("\+\d+|-\d+|\d+",chaine)[0]
	except:
		returnString = chaine
	return returnString

def parseType(chaine):
	if chaine == 'HP':
		return "Health"
	else:
		return chaine

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

			print(contenuSplit.split(' ', 1)[0] +" - type: "+ contenuSplit.split(' ', 1)[1]);

			dic[hero_name][niveau][i+1] = \
			{
				'type': parseType(contenuSplit.split(' ', 1)[1]),
				'valeur': parseValue(contenuSplit.split(' ', 1)[0]),
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

# """
allTypes = [
"Damage",
"Health",
"Mana",
"Intelligence",
"Agility",
"Strength",
"All Stats",
"Magic Resistance",
"Armor",
"Respawn Time",
"Cast Range",
"XP Gain",
"Gold/Min",
"Movement Speed",
"Attack Speed",
"Health Regen",
"Spell Amplification",
"Evasion",
"Mana Regen"
];

def parseType(data, givenType):
	dico={}
	dico['heroes'], dico['data'] = [] , []
	dicoIntermediaire = {}
	maxValue = 0
	for hero in data.keys():
		for level in data[hero].keys():
			for choice in data[hero][level].keys():
				if data[hero][level][choice]['type'] == givenType:
					valeur = data[hero][level][choice]['valeur']
					dicoIntermediaire[hero] = [level, valeur]
					if math.fabs(int(valeur)) >= maxValue:
						maxValue= math.fabs(int(valeur))
	for tupleItem in sorted(dicoIntermediaire.items(), key=compose(operator.itemgetter(1),operator.itemgetter(1))):
		"""
		un tupleItem a la forme suivante:
		('df', ['25', 9])
		"""
		dico['data'].append([int((int(tupleItem[1][0])-10)/5),len(dico['heroes']), int(tupleItem[1][1])])
		dico['heroes'].append(tupleItem[0])
	dicoIntermediaire = {}
	dico['maxValue'] = maxValue
	return dico

def allParsedData(data, allTypes):
	dic = {
		"allTypes": allTypes
	}
	print("Nombre de type de talent : "+str(len(allTypes)))
	for talentType in allTypes:
		dic[talentType]= parseType(data, talentType)
	return dic

with open('data.json') as data_file:    
    data = json.load(data_file)

with open('talent_data/parsed_data.js', 'w') as fp:
    # json.dump(allParsedData(data, allTypes), fp)
    # fp.close()

    # f1 = open('talent_data/parsed_data.json', 'r')
    # fin = f1.read()
    # f1.close()
    # f2 = open('talent_data/parsed_data.js', 'w')
    # f2.write('parsed_data='+fin)
    # f2.close()
    fp.write("parsed_data="+str(allParsedData(data, allTypes)))
    fp.close()


# """