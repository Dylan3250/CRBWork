while True:
    erreur = False
    password = input('Veuillez entrer un mot de passe.')

    if len(password) < 4 or len(password) > 8:
        print('Le mot de passe doit contenir entre 4 et 8 lettres.')
        erreur = True
    else:
        repeat = input('Veuillez confirmer votre mot de passe.')
        if len(password) != len(repeat):
            print('Erreur dans le mot de passe, il y a un problème de caractère en trop ou trop peu : ' + str(len(password) - len(repeat)).replace('-','') + ' signe(s)')
            erreur = True

        if password != repeat:
            print('Les deux mots de passe ne sont pas identiques.')
            erreur = True

        if erreur == False:
            print('Votre mot de passe est valide !')
            break