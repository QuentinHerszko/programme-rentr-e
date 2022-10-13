import time
from tkinter import *
from tkinter.messagebox import showerror
import os

class TP:
    def __init__(self,matiere,date,test):
        self.matiere = matiere
        self.date = date
        self.test = test

###Variables générales###

#def listMat():
    #return ["MA0913","MA0914","SEP0921","SEP0922","MA0934","MA0944","MA0944","CHPS0703","AN0904","MA0953"]

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
        data = ln.split()
        ListeTP.append(TP(data[0],data[1],data[2]))
    f.close()
    return ListeTP

###Savegarde des TP###

def saveTP(ListeTP):
    f = open("Save/TP.txt",'w')
    f.write("Matiere date\n")
    for i in ListeTP:
        f.write("{} {} {}\n".format(i.matiere,i.date,i.test))
    f.close()

###Ajouter un TP###

def verifAjoutTP(matiere,date):
    b = 0
    a = 0
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
    if a == 1 and b ==1:
        return 1
    else:
        return 0

def AjoutTP():
    selec = Tk()
    selec.title("Ajouter un TP")
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
    select.title("Ajout rapide")
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

###Tri des TP###

def TPTri(ListeTP):
    n = len(ListeTP)
    ListeTriee = []
    date = []
    for i in range(n):
        date.append([time.strptime(ListeTP[i].date,"%d-%m-%Y"),i])
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
        if i.test == 1:
            dateTPT = time.strptime(i.date,"%d-%m-%Y")
            if not(dateTPT < dateJour):
                L.append(i)
        else:
            L.append(i)
    return L

###Panneau principal###

def FenetreTP(ListeTP):
    k1 = 0
    k2 = 0
    L = TPTri(ListeTP)
    L = TPTestFait(L)
    n = len(L)
    fenetre = Tk()
    fenetre.title("Informations TP")
    frame1 = Frame(fenetre,bg = '#433e3f')
    frame1.pack()
    ftit = Frame(frame1,bg="#1d3557")
    ftit.grid(row=0,sticky='nwes',columnspan=2)
    Label(ftit,text="Informations sur les TP",bg="#1d3557",fg="#f4ebe8",font=('calibri',25,'bold','underline'),pady=20,padx=10).pack()
    Label(frame1,text="Matières",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=1,column=0,sticky="nsew")
    Label(frame1,text="rendu",font=('calibri',15,'bold'),justify=LEFT,padx=0,bg="#c73e1d",fg="#f4ebe8").grid(row=1,column=1,sticky='nswe')
    checklist = [IntVar() for x in range(n)]
    indice = 0
    ligne = 2
    for i in L:
        if int(i.test) == 0:
            Label(frame1,text="{} pour le {}".format(i.matiere,i.date),bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,column=0,sticky='nswe')
            Checkbutton(frame1,bg="#f4ebe8",highlightbackground='#f4ebe8',variable=checklist[indice]).grid(row=ligne,column=1,sticky='nswe')
            k1 += 1
            ligne += 1
        indice += 1
    if k1 == 0:
        Label(frame1,text="Pas de Tp à faire!",bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,columnspan=2,sticky='nswe')
        ligne += 1
    Label(frame1,text="TP test à venir",bg="#1d3557",fg="#f4ebe8",font=('calibri',20,'bold','underline'),pady=5).grid(row=ligne,sticky='nsew',columnspan=2)
    Label(frame1,text="Matières",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=ligne+1,column=0,sticky="nsew")
    Label(frame1,text=" ",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=ligne+1,column=1,sticky="nsew")
    ligne = ligne + 2
    for i in L:
        if int(i.test) == 1:
            Label(frame1,text="{} pour le {}".format(i.matiere,i.date),bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,column=0,sticky='nswe')
            Label(frame1,text=" ",bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,column=1,sticky='nswe')
            k2 += 1
            ligne += 1
    if k2 == 0:
        Label(frame1,text="Pas de TP test à venir!",bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,columnspan=2,sticky='nswe')
        ligne += 1
    fbut = Frame(frame1,bg='#433e3f')
    fbut.grid(row=ligne,columnspan=2,sticky='nswe')
    Ajout = IntVar()
    rapide = IntVar()
    Actualiser = IntVar()
    Button(fbut,text="Quitter",bg='#d62828',fg="#f4ebe8",highlightbackground='#433e3f',command=fenetre.destroy).pack(side=LEFT,pady=10,padx=5)
    Button(fbut,text="Actualiser",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,Actualiser)).pack(side=RIGHT,pady=10,padx=[0,5])
    Button(fbut,text="Ajout rapide",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,rapide)).pack(side=RIGHT,pady=10,padx=[0,5])
    Button(fbut,text="Ajouter",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,Ajout)).pack(side=RIGHT,pady=10,padx=[0,5])
    fenetre.mainloop()
    if Ajout.get() == 1:
        insert = AjoutTP()
        if not(insert == None):
            L.append(TP(insert[0],insert[1],insert[2]))
        return [1,L]
    if rapide.get() == 1:
        insert = AjoutRapide()
        if not(insert == None):
            L.append(TP(insert[0],insert[1],insert[2]))
        return [1,L]
    if Actualiser.get() == 1:
        newL = []
        for i in range(n):
            if int(checklist[i].get()) == 0:
                newL.append(L[i])
        return [1,newL]
    return [0,L]

def MainFenetreTP():
    ListeTP = loadTP()
    v = [0,ListeTP]
    while(1):
        v = FenetreTP(v[1])
        if v[0] == 0:
            break
    saveTP(v[1])

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
    MainFenetreTP()

    # time.strptime("date","format"), %Y = annee, %m = mois, %d = jour
    # time.localtime() = date du jour
    # A faire: Ajouter un bouton +1 semaine pour les TP à rendre dans 1 semaine.