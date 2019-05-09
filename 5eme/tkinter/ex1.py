from tkinter import *

def submit():
    recup_nombre = int(nombre.get())
    nombre.destroy()

    if (recup_nombre):
        carre = recup_nombre*recup_nombre
        texte = "Votre calcul est : " + str(recup_nombre) +" * " + str(recup_nombre) +" = " + str(carre) + "."
    else:
        texte = "Vous n'avez pas donné de nombre."

    libelle.config(text=texte)
    envoyer.config(text="Quitter", command=fenetre.destroy)


fenetre = Tk()

fenetre.title("Programme de Math")
fenetre.geometry("400x300")

total_fenetre = Frame(fenetre, bg="lightblue")

titre = Label(total_fenetre, text="Passer des nombres au carré", bg="black", fg="green")
titre.grid(padx=10, pady=20, ipadx=30, ipady=20, columnspan=2, row=0, column=0)

libelle = Label(total_fenetre, text="Quel est votre nombre ?")
libelle.grid(row=1, column=0, padx=5)

nombre = Entry(total_fenetre)
nombre.grid(row=1, column=1)

envoyer = Button(total_fenetre, text="Valider", bg="black", fg="white", command=submit)
envoyer.grid(columnspan=2, row=2, column=0, padx=5, pady=20, ipadx=10, ipady=2)

total_fenetre.pack(anchor=CENTER, expand=1, ipadx=10, ipady=10)

fenetre.mainloop()