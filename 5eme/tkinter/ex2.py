from tkinter import *
from random import randint

def submit():
    global nombre1
    global nombre2

    recup_nombre = nombre.get()
    nombre.destroy()
    calcul = nombre1 * nombre2

    if recup_nombre.isdigit():
        recup_nombre = int(recup_nombre)
        if recup_nombre == calcul:
            texte.set("Votre calcul est correct ! " + str(nombre1) + " * " + str(nombre2) + " = " + str(recup_nombre) + ".")
        else:
            texte.set("Votre calcul est faux ! " + str(nombre1) + " * " + str(nombre2) + " = " + str(calcul) + " et non " + str(recup_nombre) + " !")
    else:
        texte.set("Vous n'avez pas rentré de nombre")

    labelle.config(textvariable=texte)
    envoyer.config(text="Quitter", command=fenetre.destroy)


# Définition de base de la fenêtre
fenetre = Tk()

fenetre.title("Programme de Math")
fenetre.geometry("400x300")

total_fenetre = Frame(fenetre, bg="lightblue")
titre = Label(total_fenetre, text="Multiplication aléatoire", bg="black", fg="green")
titre.grid(padx=10, pady=20, ipadx=30, ipady=20, columnspan=2, row=0, column=0)

# Définiton des nombres
nombre1 = randint(2,9)
nombre2 = randint(2,9)

texte = StringVar()
texte.set("Que donne le caclul : " + str(nombre1) + " * " + str(nombre2) + " ?")

labelle = Label(total_fenetre, textvariable=texte)
labelle.grid(row=1, column=0, padx=5)

nombre = Entry(total_fenetre)
nombre.grid(row=1, column=1)

envoyer = Button(total_fenetre, text="Valider", bg="black", fg="white", command=submit)
envoyer.grid(columnspan=2, row=2, column=0, padx=5, pady=20, ipadx=10, ipady=2)

total_fenetre.pack(anchor=CENTER, expand=1, ipadx=10, ipady=10)

fenetre.mainloop()