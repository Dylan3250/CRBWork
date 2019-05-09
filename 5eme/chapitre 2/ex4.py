first = int(input('Veuillez introduire le premier nombre.'))
second = int(input('Veuillez introduire le second nombre.'))

produit = first * second

if first == 0 or second == 0:
    print('Le produit est nul')
elif first < 0 or second < 0:
    print('Le produit des deux nombres retourne un nombre négatif')
elif first > 0 or second > 0:
    print('Le produit des deux nombres retourne un nombre positif')