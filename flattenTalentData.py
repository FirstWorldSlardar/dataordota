import operator
import json

with open('data.json') as data_file:    
    data = json.load(data_file)


liste = []
for hero in data.keys():
	heroListe = []
	heroListe.append(hero)
	levelListe = []
	for level in data[hero].keys():
		levelListe.append( (level,data[hero][level]["1"]["string"]+" OR "+data[hero][level]["2"]["string"]) )
	for item in sorted(levelListe, key=operator.itemgetter(0)):
		heroListe.append(item[1])
	liste.append(heroListe)


print(liste)

f = open("talent_data/dataSet.js", "w+")
f.write('var dataSet = ')
f.write(str(liste))
f.close()