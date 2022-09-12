from tkinter import *
from tkinter.messagebox import showerror
import numpy as np
from InfoDs import loadDS, DsFait
import time

###Variables générales###

def listMat():
    return ["MA0913","MA0914","SEP0921","SEP0922","MA0934","MA0944","MA0944","CHPS0703","AN0904","MA0953"]

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
        Cours.append(data)
    f.close()
    return Cours

###Sauvegarde des données###

def saveCours(Cours):
    f = open("Save/Fiche.txt",'w')
    f.write("Matiere chp fichable fait\n")
    for i in Cours:
        f.write("{} {} {} {}\n".format(i[0],i[1],i[2],i[3]))
    f.close()

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

###Fonction du prochain DS###

def NextDS():
    ListeDS = loadDS()
    ListeDS = DsFait(ListeDS)
    MatiereDS = None
    a = int(time.localtime()[7])
    for i in ListeDS:
        if i[2] == '0':
            b = int(time.strptime(i[1],"%d-%m-%Y")[7])
            Jours = b - a 
            if Jours <= 7:
                MatiereDS = i[0]
                break
    return MatiereDS

###Fonction d'importance###

def ChpRetard(Cours,NbChp,MatiereDS):
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
                    if MatiereDS == Cours[j][0]:
                        imp[l] += 1
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

def insertChp():
    selec = Tk()
    l = LabelFrame(selec, text="Entrée du chapitre:")
    l.pack(side=TOP,padx=25,pady=[15,5])
    chap = StringVar()     #Nb du chapitre
    matiere = StringVar()  #Matière (ex:MA0913) 
    fichable = IntVar()    #Fiche à faire ou non? (0:oui ; 1:non)
    enregistrer = IntVar()
    chap.set("Chapitre")
    matiere.set("Matière")
    Entry(l,textvariable=matiere).pack(side=LEFT)
    Entry(l,textvariable=chap).pack(side=LEFT)
    Checkbutton(l,text="Pas de fiche",variable=fichable).pack(side=LEFT)
    Button(selec,text="Annuler",command=selec.destroy,fg="red").pack(side=LEFT,padx=[25,5],pady=5)
    Button(selec,text="Aide",command=helpChp).pack(side=LEFT)
    Button(selec,text="Enregistrer",command=lambda: ActionBouton(selec,enregistrer),fg="green").pack(side=RIGHT,padx=25,pady=5)
    selec.mainloop()
    if enregistrer.get() == 1:
        verif = 0
        while(verif == 0):
            verif = verifChp(matiere.get())
            if not(verif == 1):
                insert = insertChp()
                if insert == None:
                    break 
                else:
                    matiere.set(insert[0])
                    chap.set(insert[1])
                    fichable.set(insert[2])
        if verif == 1:
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
    Button(selec,text="Supprimer",command=lambda: ActionBouton(selec,supp)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if supp.get() == 1:
        CoursF = []
        for i in range(n):
            if checklist[i].get() == 0:
                CoursF.append(Cours[i])
        return CoursF

###Fenetre principale###

def MainFenetreFiche(Cours):
    C = Cours
    k = 0
    n = len(C)
    colorCode = {1:"black",2:"orange",3:"red"}
    NbChp = NombreChapitre(C)
    MatiereDS = NextDS()
    fenetre = Tk()
    Label(fenetre,text="---Fiches de révision---").pack()
    l = LabelFrame(fenetre,text="Fiche à faire:")
    l.pack(padx=[20,10],pady=[0,10])
    for i in range(n):
        fiche = C[i]
        imp = ChpRetard(C,NbChp,MatiereDS)
        if (int(fiche[2]) == 0 and int(fiche[3]) == 0):
            if imp[k] > 3:
                imp[k] = 3
            color = colorCode[imp[k]]
            if MatiereDS == fiche[0]:
                Label(l,text="{}, chapitre {} /!\ Attention DS /!\ ".format(fiche[0],fiche[1]),justify='left',fg = color).pack(padx=[0,75])
            else:
                Label(l,text="{}, chapitre {}".format(fiche[0],fiche[1]),justify=LEFT,fg = color).pack(padx=[0,200])
            k += 1
    if k == 0:
        Label(l,text='Pas de fiche à faire ÷)',fg='green').pack()
    fichef = LabelFrame(fenetre,text="Fiche déjà réalisée:",fg="green")
    fichef.pack(side=TOP,padx=[20,10],pady=[0,10])
    k = 0
    for i in range(n):
        if int(C[i][3]) == 1:
            Label(fichef,text="{}, chapitre {}".format(C[i][0],C[i][1]),justify=LEFT).pack(padx=[0,200])
            k += 1
    if k == 0:
        Label(fichef,text="Pas de fiche encore faite ÷(").pack()
    supp = IntVar()
    Button(fenetre,text="Supprimer un chapitre",command=lambda: ActionBouton(fenetre,supp)).pack(side=TOP,pady=[0,10])
    annule = IntVar()
    ajoutchp = IntVar()
    ajoutf = IntVar()
    Button(fenetre,text="Quitter",fg="red",command=fenetre.destroy).pack(side=LEFT)
    Button(fenetre,text="Ajouter un chapitre",command=lambda: ActionBouton(fenetre,ajoutchp)).pack(side=LEFT)
    Button(fenetre,text="Ajouter une fiche",command=lambda: ActionBouton(fenetre,ajoutf)).pack(side=RIGHT)
    fenetre.mainloop()
    if ajoutchp.get() == 1:
        insert = insertChp()
        if not(insert == None):
            insert.append(0)
            C.append(insert)
            C = CoursTri(C)
            C = MainFenetreFiche(C)
    if ajoutf.get() == 1:
        C = AjoutFiche(C)
        C = MainFenetreFiche(C)
    if supp.get() == 1:
        test = suppChp(C)
        if not(test == None):
            C = test
            C = MainFenetreFiche(C)
    return C

###Main###

if __name__ == "__main__":
    Cours = loadCours()
    Cours = MainFenetreFiche(Cours)
    saveCours(Cours)