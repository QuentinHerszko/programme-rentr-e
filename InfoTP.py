import time
from tkinter import *
from tkinter.messagebox import showerror
import os

###Variables générales###

def listMat():
    return ["MA0913","MA0914","SEP0921","SEP0922","MA0934","MA0944","MA0944","CHPS0703","AN0904","MA0953"]

###Action sur les boutons###

def ActionBouton(fenetre,variable):
    variable.set(1)
    fenetre.destroy()

###Chargement des TP###

def loadTP():
    ListeTP = []
    f = open("Save/TP.txt",'r')
    ln = f.readline()
    while(1):
        ln = f.readline()
        if ln == '':
            break
        ListeTP.append(ln.split())
    f.close()
    return ListeTP

###Savegarde des TP###

def saveTP(ListeTP):
    f = open("Save/TP.txt",'w')
    f.write("Matiere date\n")
    for i in ListeTP:
        f.write("{} {} {}\n".format(i[0],i[1],i[2]))
    f.close()

###Ajouter un TP###

def verifAjoutTP(matiere,date):
    verifMat = listMat()
    a = 0
    b = 0
    for i in verifMat:
        if i == matiere:
            a = 1
    if a == 0:
        showerror("Matière pas reconnue","La matière: {} n'est pas reconnue. Attention au matière comme SEP0922 ou CHPS0703!".format(matiere))
    annee = date.split('-')[2]
    if annee == '2022' or annee == '2023':
        b = 1
    if b == 0:
        showerror("Date pas correct","La date n'est pas correct, l'année universitaire ne se déroule pas en {}!".format(annee))
    if a == 1 and b == 1:
        return 1
    else:
        return 0 

def AjoutTP():
    selec = Tk()
    l = LabelFrame(selec, text="Entrée un TP:")
    l.pack(side=TOP,padx=25,pady=[15,5])
    date = StringVar()     #Nb du chapitre
    matiere = StringVar()  #Matière (ex:MA0913)
    enregistrer = IntVar()
    TPTest = IntVar()
    date.set("jj-mm-aaaa")
    matiere.set("Matière")
    Entry(l,textvariable=matiere).pack(side=LEFT)
    Entry(l,textvariable=date).pack(side=LEFT)
    Checkbutton(l,text="TP test",variable=TPTest).pack(side=LEFT)
    Button(selec,text="Annuler",command=selec.destroy,fg="red").pack(side=LEFT,padx=[25,5],pady=5)
    #Button(selec,text="Aide",command=helpChp).pack(side=LEFT)
    Button(selec,text="Enregistrer",command=lambda: ActionBouton(selec,enregistrer),fg="green").pack(side=RIGHT,padx=25,pady=5)
    selec.mainloop()
    if enregistrer.get() == 1:
        verif = 0
        while(verif == 0):
            verif = verifAjoutTP(matiere.get(),date.get())
            if not(verif == 1):
                insert = AjoutTP()
                if insert == None:
                    break
                else:
                    matiere.set(insert[0])
                    date.set(insert[1])
        if verif == 1:
            return [matiere.get(),date.get(),TPTest.get()]

def AjoutRapide():
    ListeMois = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    select = Tk()
    l = LabelFrame(select, text="Ajout rapide:")
    l.pack(side=TOP)
    Ajouter = IntVar()
    Matiere = StringVar()
    Matiere.set("Matiere")
    Jours = StringVar()
    Jours.set("7")
    Entry(l,textvariable=Matiere).pack(side=LEFT)
    Entry(l,textvariable=Jours).pack(side=LEFT)
    Button(select,text="Annuler",command=select.destroy,fg="red").pack(side=LEFT)
    Button(select,text="Ajouter",command=lambda: ActionBouton(select,Ajouter),fg="green").pack(side=RIGHT)
    select.mainloop()
    if Ajouter.get() == 1:
        temps = time.time()
        ajout = 86400 * int(Jours.get())
        dateAjout = time.ctime(ajout+temps)
        dateAjout = dateAjout.split()
        [Jour,Mois,Annee] = [dateAjout[2],ListeMois[dateAjout[1]],dateAjout[4]]
        if int(Jour) < 10:
            Jour = "0"+Jour
        if Mois < 10:
            Mois = "0{}".format(Mois)
        Ajout = "{}-{}-{}".format(Jour,Mois,Annee)
        verif = 0
        while(verif == 0):
            verif = verifAjoutTP(Matiere.get(),Ajout)
            if not(verif == 1):
                insert = AjoutRapide()
                if insert == None:
                    break
                else:
                    Matiere.set(insert[0])
                    Ajout = insert[1]
            if verif == 1:
                return [Matiere.get(),Ajout,0]

###Suppression de TP###

def suppTP(ListeTP):
    n = len(ListeTP)
    selec = Tk()
    l = LabelFrame(selec,text='TP total:')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    for i in range(n):
        Checkbutton(l,text="{}, le {}".format(ListeTP[i][0],ListeTP[i][1]),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
    supp = IntVar()
    Button(selec,text="Cancel",fg='red',command=selec.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(selec,text="Rendu!",command=lambda: ActionBouton(selec,supp)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if supp.get() == 1:
        ListeTPF = []
        for i in range(n):
            if checklist[i].get() == 0:
                ListeTPF.append(ListeTP[i])
        return ListeTPF

###Tri des TP###

def TPTri(ListeTP):
    n = len(ListeTP)
    ListeTriee = []
    date = []
    for i in range(n):
        date.append([time.strptime(ListeTP[i][1],"%d-%m-%Y"),i])
    date = sorted(date)
    Iter = []
    for i in date:
        Iter.append(i[1])
    for i in Iter:
        ListeTriee.append(ListeTP[i])
    return ListeTriee

###TPTestFait

def TPTestFait(ListeTP):
    L = []
    dateJour = time.localtime()
    for i in ListeTP:
        if i[2] == 1:
            dateTPT = time.strptime(i[1],"%d-%m-%Y")
            if not(dateTPT < dateJour):
                L.append(i)
        else:
            L.append(i)
    return L

###Panneau principal###

def MainFenetreTP(ListeTP):
    k1 = 0
    k2 = 0
    fenetre = Tk()
    Label(fenetre,text="---Information sur les TP---").pack()
    L = TPTri(ListeTP)
    L = TPTestFait(L)
    l = LabelFrame(fenetre,text="TP à venir:")
    l.pack(padx=[20,10],pady=[0,10])
    fait = LabelFrame(fenetre,text="TP test à venir:")
    fait.pack(side=TOP,padx=[20,10],pady=[0,10])
    for i in L:
        if int(i[2]) == 0:
            Label(l,text="{} le {}".format(i[0],i[1])).pack(padx=[0,100])
            k1 += 1
        else:
            Label(fait,text="{} le {}".format(i[0],i[1])).pack(padx=[0,100])
            k2 += 1
    if k1 == 0:
        Label(l,text="Pas de TP à venir!").pack()
    if k2 == 0:
        Label(fait,text="Pas de TP test à venir!").pack()
    Ajout = IntVar()
    rapide = IntVar()
    supp = IntVar()
    Button(fenetre,text="Rendre un TP",command=lambda: ActionBouton(fenetre,supp)).pack(side=TOP,pady=[0,10])
    Button(fenetre,text="Quitter", fg='red',command=fenetre.destroy).pack(side=LEFT)
    Button(fenetre,text="Ajouter un TP",command=lambda: ActionBouton(fenetre,Ajout)).pack(side=RIGHT)
    Button(fenetre,text="Ajout rapide",command=lambda: ActionBouton(fenetre,rapide)).pack(side=RIGHT)
    fenetre.mainloop()
    if Ajout.get() == 1:
        insert = AjoutTP()
        if not(insert == None):
            L.append(insert)
        L = MainFenetreTP(L)
    if rapide.get() == 1:
        insert = AjoutRapide()
        if not(insert == None):
            L.append(insert)
        L = MainFenetreTP(L)
    if supp.get() == 1:
        insert = suppTP(L)
        if not(insert == None):
            L = insert
        L = MainFenetreTP(L)
    return L

###Vérification des sauvegardes###

def verifSave():
    if not(os.path.exists("Save")):
        os.mkdir("Save")
        f = open("Save/TP.txt",'w')
        f.close()
    if not(os.path.exists("Save/TP.txt")):
        f = open("Save/TP.txt",'w')
        f.close()

if __name__ == '__main__':
    ListeTP = loadTP()
    ListeTP = MainFenetreTP(ListeTP)
    saveTP(ListeTP)

    # time.strptime("date","format"), %Y = annee, %m = mois, %d = jour
    # time.localtime() = date du jour
    # A faire: Ajouter un bouton +1 semaine pour les TP à rendre dans 1 semaine.