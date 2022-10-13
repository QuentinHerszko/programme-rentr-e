import time
from tkinter import *
from tkinter.messagebox import showerror
import os

class projet:
    def __init__(self,matiere,date,fait):
        self.matiere = matiere
        self.date = date
        self.fait = fait

###Variables générales###

def listMat(ListeProjet):
    ListeMat = []
    for i in ListeProjet:
        matiere = i.matiere
        v = 0
        for j in ListeMat:
            if j == matiere:
                v = 1
        if v == 0:
            ListeMat.append(matiere)
    return ListeMat

###Action sur les boutons###

def ActionBouton(fenetre,variable):
    variable.set(1)
    fenetre.destroy()

###Chargement des Projet###

def loadProjet():
    ListeProjet = []
    f = open("Save/Projet.txt",'r')
    ln = f.readline()
    while(1):
        ln = f.readline()
        if ln == '':
            break
        data = ln.split()
        ListeProjet.append(projet(data[0],data[1],data[2]))
    f.close()
    return ListeProjet

###Savegarde des Projet###

def saveProjet(ListeProjet):
    f = open("Save/Projet.txt",'w')
    f.write("Matiere date\n")
    for i in ListeProjet:
        f.write("{} {} {}\n".format(i.matiere,i.date,i.fait))
    f.close()

###Regarde si un Projet est passé ou non###

def ProjetFait(ListeProjet):
    L = []
    dateJour = time.localtime()
    for i in ListeProjet:
        dateProjet = time.strptime(i.date,"%d-%m-%Y")
        if dateProjet < dateJour and int(i.fait) == 0:
            i.fait = 1
        L.append(i)
    return L

###Ajouter un Projet###

def verifAjoutProjet(matiere,date):
    a = 0
    b = 0
    mat = matiere.split()
    if len(mat) == 1:
        a = 1
    else:
        showerror("Saisie incorrect","La saisie comporte des espaces, écrire sous la forme: truc_bidule à la place de: truc bidule")
    annee = date.split('-')[2]
    if annee == '2022' or annee == '2023':
        b = 1
    if b == 0:
        showerror("Date pas correct","La date n'est pas correct, l'année universitaire ne se déroule pas en {}!".format(annee))
    if a == 1 and b == 1:
        return 1
    else:
        return 0 

def AjoutProjet():
    selec = Tk()
    selec.title("Ajouter un projet")
    l = LabelFrame(selec, text="Entrée un Projet:")
    l.pack(side=TOP,padx=25,pady=[15,5])
    date = StringVar()     #Nb du chapitre
    matiere = StringVar()  #Matière (ex:MA0913)
    enregistrer = IntVar()
    date.set("jj-mm-aaaa")
    matiere.set("Matière")
    Entry(l,textvariable=matiere).pack(side=LEFT)
    Entry(l,textvariable=date).pack(side=LEFT)
    Button(selec,text="Annuler",command=selec.destroy,fg="red").pack(side=LEFT,padx=[25,5],pady=5)
    #Button(selec,text="Aide",command=helpChp).pack(side=LEFT)
    Button(selec,text="Enregistrer",command=lambda: ActionBouton(selec,enregistrer),fg="green").pack(side=RIGHT,padx=25,pady=5)
    selec.mainloop()
    if enregistrer.get() == 1:
        verif = 0
        while(verif == 0):
            verif = verifAjoutProjet(matiere.get(),date.get())
            if not(verif == 1):
                insert = AjoutProjet()
                if insert == None:
                    break
                else:
                    matiere.set(insert[0])
                    date.set(insert[1])
        if verif == 1:
            return [matiere.get(),date.get()]

###Tri des Projet###

def ProjetTri(ListeProjet):
    n = len(ListeProjet)
    ListeTriee = []
    date = []
    for i in range(n):
        date.append([time.strptime(ListeProjet[i].date,"%d-%m-%Y"),i])
    date = sorted(date)
    Iter = []
    for i in date:
        Iter.append(i[1])
    for i in Iter:
        ListeTriee.append(ListeProjet[i])
    return ListeTriee

###Panneau principal###

def FenetreProjet(ListeProjet):
    k1 = 0
    L = ProjetFait(ListeProjet)
    L = ProjetTri(L)
    n = len(L)
    fenetre = Tk()
    fenetre.title("Informations Projets")
    frame1 = Frame(fenetre,bg = '#433e3f')
    frame1.pack()
    ftit = Frame(frame1,bg="#1d3557")
    ftit.grid(row=0,sticky='nwes',columnspan=2)
    Label(ftit,text="Informations projet",bg="#1d3557",fg="#f4ebe8",font=('calibri',25,'bold','underline'),pady=20,padx=10).pack()
    Label(frame1,text="Matières",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=1,column=0,sticky="nsew")
    Label(frame1,text="rendu",font=('calibri',15,'bold'),justify=LEFT,padx=0,bg="#c73e1d",fg="#f4ebe8").grid(row=1,column=1,sticky='nswe')
    ligne = 2
    checklist = [IntVar() for x in range(n)]
    for i in L:
        Label(frame1,text="{} pour le {}".format(i.matiere,i.date),bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,column=0,sticky='nswe')
        Checkbutton(frame1,bg="#f4ebe8",highlightbackground='#f4ebe8',variable=checklist[k1]).grid(row=ligne,column=1,sticky='nswe')
        ligne += 1
        k1 += 1
    if k1 == 0:
        Label(frame1,text="Pas de Projet à venir!",bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,columnspan=2,sticky='nswe')
        ligne += 1
    fbut = Frame(frame1,bg='#433e3f')
    fbut.grid(row=ligne,columnspan=2,sticky='nswe')
    Ajout = IntVar()
    Actualiser = IntVar()
    Button(fbut,text="Quitter",bg='#d62828',fg="#f4ebe8",highlightbackground='#433e3f',command=fenetre.destroy).pack(side=LEFT,pady=10,padx=5)
    Button(fbut,text="Actualiser",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,Actualiser)).pack(side=RIGHT,pady=10,padx=[0,5])
    Button(fbut,text="Ajouter",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,Ajout)).pack(side=RIGHT,pady=10,padx=[0,5])
    fenetre.mainloop()
    if Ajout.get() == 1:
        insert = AjoutProjet()
        if not(insert == None):
            L.append(projet(insert[0],insert[1],'0'))
        return [1,L]
    if Actualiser.get() == 1:
        newL = []
        for i in range(n):
            if checklist[i].get() == 0:
                newL.append(L[i])
        return [1,newL]
    return [0,L]

def MainFenetreProjet():
    ListeProjet = loadProjet()
    v = [0,ListeProjet]
    while(1):
        v = FenetreProjet(v[1])
        if v[0] == 0:
            break
    saveProjet(v[1])

###Vérification des sauvegardes###

def verifSave():
    if not(os.path.exists("Save")):
        os.mkdir("Save")
        f = open("Save/Projet.txt",'w')
        f.close()
    if not(os.path.exists("Save/Projet.txt")):
        f = open("Save/Projet.txt",'w')
        f.close()

if __name__ == '__main__':
    MainFenetreProjet()

    # time.strptime("date","format"), %Y = annee, %m = mois, %d = jour
    # time.localtime() = date du jour