liste = []
for i in range(1,4):
    liste.append(input('Veuillez entrer un nombre n°' + str(i) + ' :'))

if liste == sorted(liste):
    print('Les prénoms sont rangés alphabétiquement !')
else:
    print('Les prénoms ne sont pas rangés alphabétiquement !')