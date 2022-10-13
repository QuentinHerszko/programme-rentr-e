import time
from tkinter import *
from tkinter.messagebox import showerror
import os

class DS:
    def __init__(self,matiere,date,fait):
        self.matiere = matiere
        self.date = date
        self.fait = fait

###Variables générales###

def listMat():
    return ["MA0913","MA0914","SEP0921","SEP0922","MA0934","MA0944","MA0944","CHPS0703","AN0904","MA0953"]

###Action sur les boutons###

def ActionBouton(fenetre,variable):
    variable.set(1)
    fenetre.destroy()

###Chargement des DS###

def loadDS():
    ListeDS = []
    f = open("Save/DS.txt",'r')
    ln = f.readline()
    while(1):
        ln = f.readline()
        if ln == '':
            break
        data = ln.split()
        ListeDS.append(DS(data[0],data[1],data[2]))
    f.close()
    return ListeDS

###Savegarde des DS###

def saveDS(ListeDS):
    f = open("Save/DS.txt",'w')
    f.write("Matiere date fait\n")
    for i in ListeDS:
        f.write("{} {} {}\n".format(i.matiere,i.date,i.fait))
    f.close()

###Regarde si un ds est passé ou non###

def DsFait(ListeDS):
    L = []
    dateJour = time.localtime()
    for i in ListeDS:
        dateDS = time.strptime(i.date,"%d-%m-%Y")
        if dateDS < dateJour and int(i.fait) == 0:
            i.fait = '1'
        L.append(i)
    return L

###Ajouter un DS###

def verifAjoutDS(matiere,date):
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

def AjoutDS():
    selec = Tk()
    selec.title("Ajouter un DS")
    l = LabelFrame(selec, text="Entrée un DS:")
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
            verif = verifAjoutDS(matiere.get(),date.get())
            if not(verif == 1):
                insert = AjoutDS()
                if insert == None:
                    break
                else:
                    matiere.set(insert[0])
                    date.set(insert[1])
        if verif == 1:
            return [matiere.get(),date.get()]

###Suppression de DS###

def suppDS(ListeDS):
    n = len(ListeDS)
    selec = Tk()
    selec.title("Supprimer un DS")
    l = LabelFrame(selec,text='DS total:')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    for i in range(n):
        Checkbutton(l,text="{}, le {}".format(ListeDS[i].matiere,ListeDS[i].date),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
    supp = IntVar()
    Button(selec,text="Cancel",fg='red',command=selec.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(selec,text="Supprimer",command=lambda: ActionBouton(selec,supp)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if supp.get() == 1:
        ListeDSF = []
        for i in range(n):
            if checklist[i].get() == 0:
                ListeDSF.append(ListeDS[i])
        return ListeDSF

###Tri des DS###

def DSTri(ListeDS):
    n = len(ListeDS)
    ListeTriee = []
    date = []
    for i in range(n):
        date.append([time.strptime(ListeDS[i].date,"%d-%m-%Y"),i])
    date = sorted(date)
    Iter = []
    for i in date:
        Iter.append(i[1])
    for i in Iter:
        ListeTriee.append(ListeDS[i])
    return ListeTriee

###Panneau principal###

def FenetreDS(ListeDS):
    k1 = 0
    L = DsFait(ListeDS)
    L = DSTri(L)
    fenetre = Tk()
    frame1 = Frame(fenetre,bg = '#433e3f')
    frame1.pack()
    ftit = Frame(frame1,bg="#1d3557")
    ftit.grid(row=0,sticky='nwes',columnspan=2)
    Label(ftit,text="Informations DS",bg="#1d3557",fg="#f4ebe8",font=('calibri',25,'bold','underline'),pady=20,padx=10).pack()
    Label(frame1,text="Matières",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=1,column=0,sticky="nsew")
    Label(frame1,text="Dates",font=('calibri',15,'bold'),justify=LEFT,padx=0,bg="#c73e1d",fg="#f4ebe8").grid(row=1,column=1,sticky='nswe')
    ligne = 2
    for i in L:
        if int(i.fait) == 0:
            Label(frame1,text="{}".format(i.matiere),bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,column=0,sticky='nswe')
            Label(frame1,text="{}".format(i.date),bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,column=1,sticky='nswe')
            ligne += 1
            k1 += 1
    if k1 == 0:
        Label(frame1,text="Pas de DS à venir!",bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,columnspan=2,sticky='nswe')
        ligne += 1
    fbut = Frame(frame1,bg='#433e3f')
    fbut.grid(row=ligne,columnspan=2,sticky='nswe')
    Ajout = IntVar()
    supp = IntVar()
    Button(fbut,text="Quitter",bg='#d62828',fg="#f4ebe8",highlightbackground='#433e3f',command=fenetre.destroy).pack(side=LEFT,pady=10,padx=5)
    Button(fbut,text="Ajouter",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,Ajout)).pack(side=RIGHT,pady=10,padx=[0,5])
    Button(fbut,text="Supprimer",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,supp)).pack(side=RIGHT,pady=10,padx=[0,5])
    fenetre.mainloop()
    if Ajout.get() == 1:
        insert = AjoutDS()
        if not(insert == None):
            L.append(DS(insert[0],insert[1],'0'))
        return [1,L]
    if supp.get() == 1:
        insert = suppDS(L)
        if not(insert == None):
            L = insert
        return [1,L]
    return [0,L]

def MainFenetreDS():
    ListeDS = loadDS()
    v = [0,ListeDS]
    while(1):
        v = FenetreDS(v[1])
        if v[0] == 0:
            break
    saveDS(v[1])

###Vérification des sauvegardes###

def verifSave():
    if not(os.path.exists("Save")):
        os.mkdir("Save")
        f = open("Save/DS.txt",'w')
        f.close()
    if not(os.path.exists("Save/DS.txt")):
        f = open("Save/DS.txt",'w')
        f.close()

if __name__ == '__main__':
    verifSave()
    MainFenetreDS()

    # time.strptime("date","format"), %Y = annee, %m = mois, %d = jour
    # time.localtime() = date du jour