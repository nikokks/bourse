import os 

liste = os.listdir('../data')

for element in liste:
	with open('../data/'+element , 'r' ) as f:
		texte = f.read()
	if texte[0] == '{':
		os.remove('../data/'+element)
