from tkinter import *

def submit():
    recup_nombre = nombre.get()
    nombre.destroy()

    i = int(recup_nombre)
    nombre_facto = 1
    while i != 1:
        nombre_facto = i * nombre_facto
        i = i-1

    texte.set("La factorielle de " + str(recup_nombre) + " est " + str(nombre_facto))

    labelle.config(textvariable=texte)

    envoyer.config(text="Quitter", command=fenetre.destroy)


# Définition de base de la fenêtre
fenetre = Tk()

fenetre.title("Factorielle d'un nombre")
fenetre.geometry("400x300")

total_fenetre = Frame(fenetre, bg="lightblue")
titre = Label(total_fenetre, text="Factorielle d'un nombre", bg="black", fg="green")
titre.grid(padx=10, pady=20, ipadx=30, ipady=20, row=0, column=0)

texte = StringVar()
texte.set("Choisissez un nombre, et on s'occupe du reste !")

labelle = Label(total_fenetre, textvariable=texte)
labelle.grid(row=1, column=0, padx=5, pady=5)

nombre = Entry(total_fenetre)
nombre.grid(row=2, column=0)

envoyer = Button(total_fenetre, text="Valider", bg="black", fg="white", command=submit)
envoyer.grid(row=3, column=0, padx=5, pady=20, ipadx=10, ipady=2)

total_fenetre.pack(anchor=CENTER, expand=1, ipadx=10, ipady=10)

fenetre.mainloop()