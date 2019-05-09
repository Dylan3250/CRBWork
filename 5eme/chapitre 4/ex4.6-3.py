total_tableau = []

# FONCITON RETOURNE NOMBRE DE NOMBRE PREMIER

tableau = []
nombre = 97
var = 1
for i in range(1, int(nombre/2)):
    if nombre%i == 0:
        var = var + 1

        if(nombre%i != 0):
            while nombre%i == 0:
                var = var + 1


print(var)