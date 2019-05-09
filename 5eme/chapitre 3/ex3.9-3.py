text = input('Veuillez marquer le message que vous voulez coder.')
text = text.lower()
decal = input('Veuillez indiquer un décalage du pattern [optionnel] => Par défaut à 3.')

if not decal:
    decal = 3

def codage(message, limite):
    pattern = ''

    for i in range(int(limite)):
        pattern = pattern + 'abcdefghijklmnopqrstuvwxyz';

    code =  ''

    for i in range (len(message)):
        if message[i] == ' ' or message[i] == "'":
            code = code + message[i]
        else:
            code = code + pattern[pattern.find(message[i])+int(limite)]

    return code


def decodage(message, limite):
    pattern = ''

    for i in range(int(limite)):
        pattern = pattern + 'abcdefghijklmnopqrstuvwxyz';

    code = ''

    for i in range (len(message)):
        if message[i] == ' ' or message[i] == "'":
            code = code + message[i]
        else:
            code = code + pattern[pattern.find(message[i])-int(limite)]

    return code


print('Voici le message coddé : ' + codage(text, decal) + '. Voici le message décoddé du message coddé : ' + decodage(codage(text, decal), decal), end='')