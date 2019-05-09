from tkinter import *
from random import randint

# Définiton du nombre
nombre = randint(1,1000)

def submit():
    global nombre

    recup_nombre = reponse.get()

    if recup_nombre.isdigit():
        recup_nombre = int(recup_nombre)

        if recup_nombre == nombre:
            texte.set("Félicitations, vous avez trouvé le bon nombre : " + str(nombre) + " !")
        elif recup_nombre < nombre:
            texte.set("Le nombre est supérieur à celui que vous avez indiqué : " + str(recup_nombre) + " ! \nRéessayez ? :")
        else:
            texte.set("Le nombre est inférieur à celui que vous avez indiqué : " + str(recup_nombre) + " ! \nRéessayez ? :")
    else:
        texte.set("Vous n'avez pas rentré de nombre")

    labelle.config(textvariable=texte)
    labelle.grid(columnspan=2)
    if recup_nombre != nombre:
        reponse.grid(row=2, column=0, padx=5, pady=10, ipadx=35, ipady=2,columnspan=2)
        envoyer.config(text="Réessayer", command=submit)
        envoyer.grid(row=3, column=0, padx=25, pady=10, ipadx=20, ipady=2, columnspan=2)
    else:
        envoyer.destroy()

    quitter = Button(total_fenetre, text="Quitter", bg="black", fg="white", command=fenetre.destroy)
    quitter.grid(row=3, column=1, padx=25, pady=10, ipadx=10, ipady=2)

# Définition de base de la fenêtre
fenetre = Tk()

fenetre.title("Jeu du plus-au-moins")
fenetre.geometry("450x300")

total_fenetre = Frame(fenetre, bg="lightblue")
titre = Label(total_fenetre, text="Essayez de trouver le bon nombre", bg="black", fg="green")
titre.grid(padx=10, pady=20, ipadx=30, ipady=20, columnspan=2, row=0, column=0)

texte = StringVar()
texte.set("Essayez de trouver le nombre compris entre 1 et 1000 :")

labelle = Label(total_fenetre, textvariable=texte)
labelle.grid(row=1, column=0, padx=5)

reponse = Entry(total_fenetre)
reponse.grid(row=1, column=1)

envoyer = Button(total_fenetre, text="Valider", bg="black", fg="white", command=submit)
envoyer.grid(columnspan=2, row=2, column=0, padx=5, pady=20, ipadx=10, ipady=2)

total_fenetre.pack(anchor=CENTER, expand=1, ipadx=10, ipady=10)

fenetre.mainloop()