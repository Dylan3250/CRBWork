table = 1

while table <= 10:
    print("-------------------------\nTABLE DE " + str(table) + "\n-------------------------")
    for i in range(11):
        print(str(table) + ' X ' + str(i) + ' = ' + str(table*i))
    table = table+1
