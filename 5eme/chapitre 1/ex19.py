# Pseudo, Password
logins = [["Dylan", "Bricar"], ["Test", "CRB"]]
connected = False

pseudo = input('Quel est votre pseudo ?')
password = input('Quel est votre password ?')

for x in range(len(logins)):
    if logins[x][0] == pseudo and logins[x][1] == password:
        connected = True

if connected == True:
    print("Vous êtes connecté sous " + pseudo + " avec le password " + password)
else:
    print("Identifiants incorrects")
    account = input("Si vous n'avez pas de compte ? Voulez-vous en créer un ?")

if not account or account.lower != "non":
    new_pseudo = input('Quel est votre nouveau pseudo ?')
    new_password = input('Quel est votre nouveau password ?')

logins.append([new_pseudo, new_password])

print(logins)