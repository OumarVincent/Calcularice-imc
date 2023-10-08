# -*- coding: utf-8 -*-
"""
Created on Fri May 28 21:04:11 2021

@author: Oumar
"""

from tkinter import messagebox
from tkinter import *
def init() :
    fenetrePrincipale = Tk()
    fenetrePrincipale.title("Inscription")
    l1 = Label(fenetrePrincipale, text = "Nom").grid(row = 0, column = 0)
    l2 = Label(fenetrePrincipale, text = "Prénom").grid(row = 1, column = 0)
    l3 = Label(fenetrePrincipale, text = "Âge").grid(row = 2, column = 0)
    l4 = Label(fenetrePrincipale, text = "Sexe").grid(row = 3, column = 0)
    l5 = Label(fenetrePrincipale, text = "Taille(M)").grid(row = 4, column = 0)
    l6 = Label(fenetrePrincipale, text = "Masse(Kg)").grid(row = 5, column = 0)

    e1_var = StringVar()
    e1 = Entry(fenetrePrincipale, textvariable = e1_var).grid(row = 0, column = 1)


    e2 = Entry(fenetrePrincipale).grid(row = 1, column = 1)

    e3_var = IntVar()
    e3 = Entry(fenetrePrincipale, textvariable = e3_var).grid(row = 2, column = 1)

    e4_var = DoubleVar()
    e4 = Entry(fenetrePrincipale, textvariable = e4_var).grid(row = 4, column = 1)

    e5_var = DoubleVar()
    e5 = Entry(fenetrePrincipale, textvariable = e5_var).grid(row = 5, column = 1)
    
    e6_var = IntVar()
    rb1 = Radiobutton(fenetrePrincipale, text = "Feminin", value = '1').grid(row = 3, column = 1)
    rb2 = Radiobutton(fenetrePrincipale, text = "Masculin", value = '2').grid(row = 3, column = 2)
        
    b = Button(fenetrePrincipale ,text="IMC", command = lambda a=0:CalculIMC(fenetrePrincipale,e4_var.get(),e5_var.get()) ).grid(row = 8, column = 0)
    b2 = Button(fenetrePrincipale ,text="Reset", command =lambda a=0: IMC(fenetrePrincipale)).grid(row = 8, column = 1)
    btn = Button(fenetrePrincipale, text ="Fermer", command =lambda a=0: Quit(fenetrePrincipale)).grid(row = 8, column = 2) 
    fenetrePrincipale.mainloop()


def Quit(fenetrePrincipale) :
    fenetrePrincipale.destroy()

def IMC(fenetrePrincipale):
    fenetrePrincipale.destroy()
    init()
    
def CalculIMC(fenetrePrincipale,taille,masse):
    imc = round(masse/(taille*taille),1)
    messagebox.showinfo("Imc", "Ton imc est : {}".format(imc))

init()