tab1 = []
tab2 = []

for i in range (6):
    tab1.append(int(input("Donnez le nombre " + str(i) + " du tab1")))

for i in range (8):
    tab2.append(int(input("Donnez le nombre " + str(i) + " du tab2")))

tab3 = tab1 + tab2
print(tab3)

# tab3 = []
# for i in range(len(tab1)):
#     tab3.append(tab1[i])

# for i in range(len(tab2)):
#     tab3.append(tab2[i])

# print(tab3)