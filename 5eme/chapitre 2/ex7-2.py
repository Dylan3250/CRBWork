a = int(input('Veuillez saisir le 1er nombre.'))
b = int(input('Veuillez saisir le 2eme nombre.'))
c = int(input('Veuillez saisir le 3eme nombre.'))

if b < a and a > c:
    print(a)
elif a < b and b > c:
    print(b)
elif a < c and c > b:
    print(c)