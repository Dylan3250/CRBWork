prenom = input("Quel est votre prénom ?")
nom = input("Quel est votre nom ?")

min_prenom = prenom.lower()
min_nom = nom.lower()
tableau = []

first_prenom = min_prenom[0]
cut_nom = min_nom[:8]

password = first_prenom + cut_nom

print('Le mot de passe du reseau est : ' + password)