from tkinter import *
from tkinter.messagebox import showerror
import numpy as np

###Variables générales###

def listMat():
    return ["MA0913","MA0914","SEP0921","SEP0922","MA0934","MA0944","MA0944","CHPS0703","AN0904","MA0953"]

###Chargement des données###

def loadCours():
    Cours = []
    f = open("Fiche/save.txt",'r')
    f.readline()
    while(1):
        ln = f.readline()
        if (ln == ''):
            break
        data = ln.split()
        Cours.append(data)
    f.close()
    return Cours

###Fonction de tri###

def CoursTri(Cours):
    CoursTri = []
    Liste = listMat()
    n = len(Cours)
    for i in Liste:
        chap = []
        for j in range(n):
            if Cours[j][0] == i:
                chap.append([int(Cours[j][1]),j])
        chap = sorted(chap)
        Iter = []
        for j in range(len(chap)):
            Iter.append(chap[j][1])
        for j in Iter:
            CoursTri.append(Cours[j])
    return CoursTri

###Fonction du nombre de chapitre###

def NombreChapitre(Cours):
    Liste = listMat()
    n = len(Cours)
    m = len(Liste)
    NbChp = np.zeros(m)
    k = 0
    for i in Liste:
        for j in range(n):
            if Cours[j][0] == i:
                if int(Cours[j][2]) == 0 and int(Cours[j][3]) == 0:
                    NbChp[k] += 1
        k += 1
    return NbChp

###Fonction d'importance###

def ChpRetard(Cours,NbChp):
    Liste = listMat()
    n = len(Cours)
    k = 0
    l = 0
    imp = np.zeros(n)
    for i in Liste:
        m = 0
        for j in range(n):
            if Cours[j][0] == i:
                if int(Cours[j][2]) == 0 and int(Cours[j][3]) == 0:
                    imp[l] = NbChp[k] - m
                    l += 1
                    m += 1
        k += 1
    imp = imp[0:l]
    return imp 

###Insertion de chapitre###

def verifChp(matiere):
    verifMat = listMat()
    a = 0
    for i in verifMat:
        if i == matiere:
            a = 1
    if a == 0:
        showerror("Matière pas reconnue","La matière: {} n'est pas reconnue. Attention au matière comme SEP0922 ou CHPS0703!".format(matiere))
    return a

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

def CancelChp(selec,annule):
    annule.set(1)
    selec.destroy()

def insertChp():
    while(1):
        selec = Tk()
        l = LabelFrame(selec, text="Entrée du chapitre:")
        l.pack(side=TOP,padx=25,pady=[15,5])
        chap = StringVar()     #Nb du chapitre
        matiere = StringVar()  #Matière (ex:MA0913) 
        fichable = IntVar()    #Fiche à faire ou non? (0:oui ; 1:non)
        annule = IntVar()      #Permet de savoir si on a annulé l'action
        chap.set("Chapitre")
        matiere.set("Matière")
        Entry(l,textvariable=matiere).pack(side=LEFT)
        Entry(l,textvariable=chap).pack(side=LEFT)
        Checkbutton(l,text="Pas de fiche",variable=fichable).pack(side=LEFT)
        Button(selec,text="Annuler",command=lambda: CancelChp(selec,annule),fg="red").pack(side=LEFT,padx=[25,5],pady=5)
        Button(selec,text="Aide",command=helpChp).pack(side=LEFT)
        Button(selec,text="Enregistrer",command=selec.destroy,fg="green").pack(side=RIGHT,padx=25,pady=5)
        selec.mainloop()
        if (annule.get() == 1):
            break
        verif = verifChp(matiere.get())
        if (verif == 1):
            break
    if annule.get() == 0:
        return [matiere.get(),chap.get(),fichable.get()]

###Ajout fiches###

def AjoutFiche(Cours):
    n = len(Cours)
    selec = Tk()
    l = LabelFrame(selec,text='Fiche réalisée:')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    for i in range(n):
        if int(Cours[i][2]) == 0 and int(Cours[i][3]) == 0:
            Checkbutton(l,text="{}, chapitre {}".format(Cours[i][0],Cours[i][1]),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
    valider = IntVar()
    Button(selec,text="Cancel",fg='red',command=selec.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(selec,text="Valider",fg='green',command=lambda: CancelChp(selec,valider)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if valider.get() == 1:
        Id = []
        k = 0
        for i in checklist:
            if i.get() == 1:
                Id.append(k)
            k += 1
        for i in Id:
            Cours[i][3] = '1'
        return Cours

###Suppression de chapitres###

def suppChp(Cours):
    n = len(Cours)
    selec = Tk()
    l = LabelFrame(selec,text='Chapitre total:')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    for i in range(n):
        Checkbutton(l,text="{}, chapitre {}".format(Cours[i][0],Cours[i][1]),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
    supp = IntVar()
    Button(selec,text="Cancel",fg='red',command=selec.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(selec,text="Supprimer",command=lambda: CancelChp(selec,supp)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if supp.get() == 1:
        CoursF = []
        for i in range(n):
            if checklist[i].get() == 0:
                CoursF.append(Cours[i])
        Cours = CoursF
        return Cours

###Main###

if __name__ == "__main__":
    Cours = loadCours()
    while(1):
        k = 0
        n = len(Cours)
        colorCode = {1:"black",2:"orange",3:"red"}
        NbChp = NombreChapitre(Cours)
        fenetre = Tk()
        Label(fenetre,text="---Fiches de révision---").pack()
        l = LabelFrame(fenetre,text="Fiche à faire:")
        l.pack(padx=[20,10],pady=[0,10])
        for i in range(n):
            fiche = Cours[i]
            imp = ChpRetard(Cours,NbChp)
            if (int(fiche[2]) == 0 and int(fiche[3]) == 0):
                if imp[k] > 3:
                    imp[k] = 3
                color = colorCode[imp[k]]
                Label(l,text="{}, chapitre {}".format(fiche[0],fiche[1]),justify=LEFT,fg = color).pack(padx=[0,200])
                k += 1
        if k == 0:
            Label(l,text='Pas de fiche à faire ÷)',fg='green').pack()
        fichef = LabelFrame(fenetre,text="Fiche déjà réalisée:",fg="green")
        fichef.pack(side=TOP,padx=[20,10],pady=[0,10])
        k = 0
        for i in range(n):
            if int(Cours[i][3]) == 1:
                Label(fichef,text="{}, chapitre {}".format(Cours[i][0],Cours[i][1]),justify=LEFT).pack(padx=[0,200])
                k += 1
        if k == 0:
            Label(fichef,text="Pas de fiche encore faite ÷(").pack()
        supp = IntVar()
        Button(fenetre,text="Supprimer un chapitre",command=lambda: CancelChp(fenetre,supp)).pack(side=TOP,pady=[0,10])
        annule = IntVar()
        ajoutchp = IntVar()
        ajoutf = IntVar()
        Button(fenetre,text="Quitter",fg="red",command=lambda: CancelChp(fenetre,annule)).pack(side=LEFT)
        Button(fenetre,text="Ajouter un chapitre",command=lambda: CancelChp(fenetre,ajoutchp)).pack(side=LEFT)
        Button(fenetre,text="Ajouter une fiche",command=lambda: CancelChp(fenetre,ajoutf)).pack(side=RIGHT)
        fenetre.mainloop()
        if annule.get() == 1:
            break
        if ajoutchp.get() == 1:
            insert = insertChp()
            if not(insert == None):
                insert.append(0)
                Cours.append(insert)
                Cours = CoursTri(Cours)
        if ajoutf.get() == 1:
            AjoutFiche(Cours)
        if supp.get() == 1:
            test = suppChp(Cours)
            if not(test == None):
                Cours = test

    #Donnée de la forme [matiere,chap,fichable?,fait?] fichable = 1 non et fait = 1 c'est fait
    #Faire un bouton pour supp un chp
