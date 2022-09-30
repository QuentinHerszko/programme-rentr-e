from tkinter import *
from tkinter.messagebox import showerror
import numpy as np
from InfoDs import loadDS, DsFait
import time
import os

############
###class####
############

class FicheRev:
    def __init__(self,matiere,chapitre,aJour,fait):
        self.matiere = matiere
        self.chapitre = chapitre
        self.aJour = aJour
        self.fait = fait

###############
###Fonctions###
###############

###Variables générales###

def listMat(Cours):
    ListeMat = []
    for i in Cours:
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

###Chargement des données###

def loadCours():
    Cours = []
    f = open("Save/Fiche.txt",'r')
    f.readline()
    while(1):
        ln = f.readline()
        if (ln == ''):
            break
        data = ln.split()
        Cours.append(FicheRev(data[0],data[1],data[2],data[3]))
    f.close()
    return Cours

###Sauvegarde des données###

def saveCours(Cours):
    f = open("Save/Fiche.txt",'w')
    f.write("Matiere chp fait en_cours\n")
    for i in Cours:
        f.write("{} {} {} {}\n".format(i.matiere,i.chapitre,i.aJour,i.fait))
    f.close()

def CoursTri(Cours):
    CoursTri = []
    Liste = listMat(Cours)
    n = len(Cours)
    for i in Liste:
        chap = []
        for j in range(n):
            if Cours[j].matiere == i:
                chap.append([int(Cours[j].chapitre),j])
        chap = sorted(chap)
        Iter = []
        for j in range(len(chap)):
            Iter.append(chap[j][1])
        for j in Iter:
            CoursTri.append(Cours[j])
    return CoursTri

###Fonction du nombre de chapitre###

def NombreChapitre(Cours):
    Liste = listMat(Cours)
    n = len(Cours)
    m = len(Liste)
    NbChp = np.zeros(m)
    k = 0
    for i in Liste:
        for j in range(n):
            if Cours[j].matiere == i:
                if int(Cours[j].aJour) == 0 and int(Cours[j].fait) == 0:
                    NbChp[k] += 1
        k += 1
    return NbChp

def NextDS():
    ListeDS = loadDS()
    ListeDS = DsFait(ListeDS)
    MatiereDS = None
    a = int(time.localtime()[7])
    for i in ListeDS:
        if i.fait == '0':
            b = int(time.strptime(i.date,"%d-%m-%Y")[7])
            Jours = b - a 
            if Jours <= 7:
                MatiereDS = i[0]
                break
    return MatiereDS

def ChpRetard(Cours,NbChp,MatiereDS):
    Liste = listMat(Cours)
    n = len(Cours)
    k = 0
    l = 0
    imp = np.zeros(n)
    for i in Liste:
        m = 0
        for j in range(n):
            if Cours[j].matiere == i:
                if int(Cours[j].aJour) == 0 and int(Cours[j].fait) == 0:
                    imp[l] = NbChp[k] - m
                    if MatiereDS == Cours[j].matiere:
                        imp[l] += 1
                    l += 1
                    m += 1
        k += 1
    imp = imp[0:l]
    return imp 

###Insertion de chapitre###

def helpChp():
    aide = Tk()
    l1 = LabelFrame(aide,text="Matière:")
    l2 = LabelFrame(aide,text="Chapitre:")
    l3 = LabelFrame(aide,text="Pas de fiche:")
    l1.pack(padx=20,pady=5)
    Label(l1,text="L'entrée matière désigne la matière dans la quelle le cours est réalisé.").pack()
    Label(l1,text="Exemple: MA0913").pack()
    l2.pack(padx=20,pady=5)
    Label(l2,text="L'entrée chapitre désigne le numéro du chapitre.").pack(padx=[0,145])
    Label(l2,text="Exemple: 1").pack()
    l3.pack(padx=20,pady=5)
    Label(l3,text="Le bouton 'Pas de fiche' permet de désigné si le chapitre n'as pas \n besoin de fiche. \n Si coché, ce chapitre ne sera pas proposé en fiche de révision.",justify=LEFT).pack(padx=[0,30])
    Button(aide,text='OK',command=aide.destroy).pack(pady=5)

def verifMatiere(matiere):
    a = 0
    mat = matiere.split()
    if len(mat) == 1:
        a = 1
    else:
        showerror("Saisie incorrect","La saisie comporte des espaces, écrire sous la forme: truc_bidule à la place de: truc bidule")
    return a

def insertChp():
    selec = Tk()
    selec.title("Ajouter un chapitre")
    l = LabelFrame(selec, text="Entrée du chapitre:")
    l.pack(side=TOP,padx=25,pady=[15,5])
    chap = StringVar()     #Nb du chapitre
    matiere = StringVar()  #Matière (ex:MA0913)
    enregistrer = IntVar()
    chap.set("Chapitre")
    matiere.set("Matière")
    Entry(l,textvariable=matiere).pack(side=LEFT)
    Entry(l,textvariable=chap).pack(side=LEFT)
    Button(selec,text="Annuler",command=selec.destroy,fg="red").pack(side=LEFT,padx=[25,5],pady=5)
    Button(selec,text="Aide",command=helpChp).pack(side=LEFT)
    Button(selec,text="Enregistrer",command=lambda: ActionBouton(selec,enregistrer),fg="green").pack(side=RIGHT,padx=25,pady=5)
    selec.mainloop()
    if enregistrer.get() == 1:
        verif = verifMatiere(matiere.get())
        if verif == 0:
            insert = insertChp()
            if not(insert == None):
                matiere.set(insert[0])
                chap.set(insert[1])
                verif = 1
        if verif == 1:
            return [matiere.get(),chap.get()]

###Ajout fiches###

def AjoutFiche(Cours):
    n = len(Cours)
    selec = Tk()
    l = LabelFrame(selec,text='Fiche réalisée:')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    if n == 0:
        Label(selec,text="Pas de fiches à rendre").pack()
    for i in range(n):
        if int(Cours[i].aJour) == 0 and int(Cours[i].fait) == 0:
            Checkbutton(l,text="{}, chapitre {}".format(Cours[i].matiere,Cours[i].chapitre),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
    valider = IntVar()
    Button(selec,text="Cancel",fg='red',command=selec.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(selec,text="Valider",fg='green',command=lambda: ActionBouton(selec,valider)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if valider.get() == 1:
        Id = []
        k = 0
        for i in checklist:
            if i.get() == 1:
                Id.append(k)
            k += 1
        for i in Id:
            Cours[i].fait = '1'
    return Cours

def suppChp(Cours):
    n = len(Cours)
    selec = Tk()
    selec.title("Supprimer un chapitre")
    l = LabelFrame(selec,text='Chapitre total:')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    for i in range(n):
        Checkbutton(l,text="{}, chapitre {}".format(Cours[i].matiere,Cours[i].chapitre),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
    supp = IntVar()
    Button(selec,text="Cancel",fg='red',command=selec.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(selec,text="Supprimer",command=lambda: ActionBouton(selec,supp)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if supp.get() == 1:
        CoursF = []
        for i in range(n):
            if checklist[i].get() == 0:
                CoursF.append(Cours[i])
        return CoursF

###Fenetre principale###

def FenetreFiche(cours):
    C = cours
    n = len(C)
    colorCode = {1:"black",2:"orange",3:"red"}
    NbChp = NombreChapitre(C)
    MatiereDS = NextDS()
    fenetre = Tk()
    fenetre.title("Informations fiches de révision")
    Label(fenetre,text="---Fiches de révision---").pack()
    l = LabelFrame(fenetre,text="Fiche à faire:")
    l2 = LabelFrame(fenetre,text="Fiche à jour:")
    l3 = LabelFrame(fenetre,text="Fiche faite:")
    l.pack(padx=[20,10],pady=[0,10])
    l2.pack(padx=[20,10],pady=[0,10])
    l3.pack(padx=[20,10],pady=[0,10])
    Label(l2,text='Matière').grid(row=0,column=0,padx=[0,10])
    Label(l2,text='Reprendre').grid(row=0,column=1,padx=[0,135])
    k = 0
    j1 = 1
    j2 = 1
    imp = ChpRetard(C,NbChp,MatiereDS)
    if not(len(imp) == 0):
        Label(l,text='Matière').grid(row=0,column=0)
        Label(l,text='     A jour     ').grid(row=0,column=1)
        Label(l,text='     Finie     ').grid(row=0,column=2)
    else:
        Label(l,text='Pas de fiche à faire ÷)',fg='green').pack()
    checklist = [[IntVar(), IntVar()] for x in range(n)]
    indices = []
    indices2 = []
    for i in C:
        if (int(i.aJour) == 0 and int(i.fait) == 0):
            if imp[j1-1] > 3:
                imp[j1-1] = 3
            color = colorCode[imp[j1-1]]
            indices.append(k)
            if MatiereDS == i.matiere:
                Label(l,text="{}, chapitre {} /!\ Attention DS /!\ ".format(i.matiere,i.chapitre),justify='left',fg = color).grid(row=j1,column=0)
            else:
                Label(l,text="{}, chapitre {}".format(i.matiere,i.chapitre),justify=LEFT,fg = color).grid(row=j1,column=0)
            Checkbutton(l,variable=checklist[k][0]).grid(row=j1,column=1)
            Checkbutton(l,variable=checklist[k][1]).grid(row=j1,column=2)
            j1+=1
        elif int(i.aJour) == 1:
            indices2.append(k)
            Label(l2,text='{}, chapitre {}'.format(i.matiere,i.chapitre),justify=LEFT).grid(row=j2,column=0)
            Checkbutton(l2,variable=checklist[k][0]).grid(row=j2,column=1,padx=[0,135])
            j2 += 1
        else:
            Label(l3,text='{}, chapitre {}'.format(i.matiere,i.chapitre),justify=LEFT).pack(padx=[0,175])
        k += 1
    supp = IntVar()
    Button(fenetre,text="Supprimer un chapitre",command=lambda: ActionBouton(fenetre,supp)).pack(side=TOP,pady=[0,10])
    actualiser = IntVar()
    ajoutf = IntVar()
    Button(fenetre,text="Quitter",fg="red",command=fenetre.destroy).pack(side=LEFT)
    Button(fenetre,text="Actualiser",command=lambda: ActionBouton(fenetre,actualiser)).pack(side=RIGHT)
    Button(fenetre,text="Ajouter une fiche",command=lambda: ActionBouton(fenetre,ajoutf)).pack(side=RIGHT)
    fenetre.mainloop()
    if actualiser.get() == 1:
        for i in indices:
            if checklist[i][0].get() == 1:
                C[i].aJour = '1'
            elif checklist[i][1].get() == 1:
                C[i].fait = '1'
        for i in indices2:
            if checklist[i][0].get() == 1:
                C[i].aJour = '0'
        return [1,C]
    if ajoutf.get() == 1:
        insert = insertChp()
        if not(insert == None):
            ajout = FicheRev(insert[0],insert[1],'0','0')
            C.append(ajout)
            C = CoursTri(C)
        return [1,C]
    if supp.get() == 1:
        test = suppChp(C)
        if not(test == None):
            C = test
        return [1,C]
    return [0,C]

def MainFenetreFiche():
    Cours = loadCours()
    v = [0,Cours]
    while(1):
        v = FenetreFiche(v[1])
        if v[0] == 0:
            break
    saveCours(v[1])

###Vérification des sauvegardes###

def verifSave():
    if not(os.path.exists("Save")):
        os.mkdir("Save")
        f = open("Save/Fiche.txt",'w')
        f.close()
    if not(os.path.exists("Save/Fiche.txt")):
        f = open("Save/Fiche.txt",'w')
        f.close()

##########
###Main###
##########

if __name__ == "__main__":
    verifSave()
    MainFenetreFiche()