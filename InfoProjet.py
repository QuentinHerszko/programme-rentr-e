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

###Suppression de Projet###

def suppProjet(ListeProjet):
    n = len(ListeProjet)
    selec = Tk()
    selec.title("Supprimer un projet")
    l = LabelFrame(selec,text='Projet total:')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    for i in range(n):
        Checkbutton(l,text="{}, le {}".format(ListeProjet[i].matiere,ListeProjet[i].date),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
    supp = IntVar()
    Button(selec,text="Cancel",fg='red',command=selec.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(selec,text="Supprimer",command=lambda: ActionBouton(selec,supp)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if supp.get() == 1:
        ListeProjetF = []
        for i in range(n):
            if checklist[i].get() == 0:
                ListeProjetF.append(ListeProjet[i])
        return ListeProjetF

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
    k2 = 0
    fenetre = Tk()
    fenetre.title("Informations Projets")
    Label(fenetre,text="---Information sur les Projet---").pack()
    L = ProjetFait(ListeProjet)
    L = ProjetTri(L)
    l = LabelFrame(fenetre,text="Projet à venir:")
    l.pack(padx=[20,10],pady=[0,10])
    fait = LabelFrame(fenetre,text="Projet déjà fait:")
    fait.pack(side=TOP,padx=[20,10],pady=[0,10])
    for i in L:
        if int(i.fait) == 0:
            Label(l,text="{} le {}".format(i.matiere,i.date)).pack(padx=[0,100])
            k1 += 1
        else:
            Label(fait,text="{} le {}".format(i.matiere,i.date)).pack(padx=[0,100])
            k2 += 1
    if k1 == 0:
        Label(l,text="Pas de Projet à venir!").pack()
    if k2 == 0:
        Label(fait,text="Pas encore de Projet fait").pack()
    Ajout = IntVar()
    supp = IntVar()
    Button(fenetre,text="Supprimer un Projet",command=lambda: ActionBouton(fenetre,supp)).pack(side=TOP,pady=[0,10])
    Button(fenetre,text="Quitter", fg='red',command=fenetre.destroy).pack(side=LEFT)
    Button(fenetre,text="Ajouter un Projet",command=lambda: ActionBouton(fenetre,Ajout)).pack(side=RIGHT)
    fenetre.mainloop()
    if Ajout.get() == 1:
        insert = AjoutProjet()
        if not(insert == None):
            L.append(projet(insert[0],insert[1],'0'))
        return [1,L]
    if supp.get() == 1:
        insert = suppProjet(L)
        if not(insert == None):
            L = insert
        return [1,L]
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