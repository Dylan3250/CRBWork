import time

start_time = time.time()

def is_premier(nombre):

    for i in range(2, int(nombre/2)):
        if nombre%i == 0:
            return True


print(str(is_premier(77777777771188111111111111111111111111111111111888211)) + ' executé en ' + str(time.time() - start_time) + ' seconde(s)', end='\n')

