a = int(input('Veuillez indiquer le premier nombre.'))
b = int(input('Veuillez indiquer le secpnd nombre.'))
c = int(input('Veuillez indiquer le troisième nombre.'))

if a < b < c:
    print("Les nombres sont rangés en ordre croissant : " + str(a) + ", " + str(b) + ", " + str(c))
elif a < c < b:
    print("Les nombres ne sont pas ordonnés de façon croissante : " + str(a) + ", " + str(b) + ", " + str(c) + ", la bonne façon serait " + str(a) + ", " + str(c) + ", " + str(b))
elif b < a < c:
    print("Les nombres ne sont pas ordonnés de façon croissante : " + str(a) + ", " + str(b) + ", " + str(c) + ", la bonne façon serait " + str(b) + ", " + str(a) + ", " + str(c))
elif b < c < a:
    print("Les nombres ne sont pas ordonnés de façon croissante : " + str(a) + ", " + str(b) + ", " + str(c) + ", la bonne façon serait " + str(b) + ", " + str(c) + ", " + str(a))
elif c < a < b:
    print("Les nombres ne sont pas ordonnés de façon croissante : " + str(a) + ", " + str(b) + ", " + str(c) + ", la bonne façon serait " + str(c) + ", " + str(a) + ", " + str(b))
elif c < b < a:
    print("Les nombres ne sont pas ordonnés de façon croissante : " + str(a) + ", " + str(b) + ", " + str(c) + ", la bonne façon serait " + str(c) + ", " + str(b) + ", " + str(a))