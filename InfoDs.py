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

###Chargement des DS###

def loadDS():
    ListeDS = []
    f = open("Save/DS.txt",'r')
    ln = f.readline()
    while(1):
        ln = f.readline()
        if ln == '':
            break
        ListeDS.append(ln.split())
    f.close()
    return ListeDS

###Savegarde des DS###

def saveDS(ListeDS):
    f = open("Save/DS.txt",'w')
    f.write("Matiere date\n")
    for i in ListeDS:
        f.write("{} {} {}\n".format(i[0],i[1],i[2]))
    f.close()

###Regarde si un ds est passé ou non###

def DsFait(ListeDS):
    L = []
    dateJour = time.localtime()
    for i in ListeDS:
        dateDS = time.strptime(i[1],"%d-%m-%Y")
        if dateDS < dateJour and int(i[2]) == 0:
            i[2] = 1
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
    l = LabelFrame(selec,text='DS total:')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    for i in range(n):
        Checkbutton(l,text="{}, le {}".format(ListeDS[i][0],ListeDS[i][1]),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
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
        date.append([time.strptime(ListeDS[i][1],"%d-%m-%Y"),i])
    date = sorted(date)
    Iter = []
    for i in date:
        Iter.append(i[1])
    for i in Iter:
        ListeTriee.append(ListeDS[i])
    return ListeTriee

###Panneau principal###

def MainFenetreDS(ListeDS):
    k1 = 0
    k2 = 0
    fenetre = Tk()
    Label(fenetre,text="---Information sur les DS---").pack()
    L = DsFait(ListeDS)
    L = DSTri(L)
    l = LabelFrame(fenetre,text="DS à venir:")
    l.pack(padx=[20,10],pady=[0,10])
    fait = LabelFrame(fenetre,text="Ds déjà fait:")
    fait.pack(side=TOP,padx=[20,10],pady=[0,10])
    for i in L:
        if int(i[2]) == 0:
            Label(l,text="{} le {}".format(i[0],i[1])).pack(padx=[0,100])
            k1 += 1
        else:
            Label(fait,text="{} le {}".format(i[0],i[1])).pack(padx=[0,100])
            k2 += 1
    if k1 == 0:
        Label(l,text="Pas de DS à venir!").pack()
    if k2 == 0:
        Label(fait,text="Pas encore de DS fait").pack()
    Ajout = IntVar()
    supp = IntVar()
    Button(fenetre,text="Supprimer un DS",command=lambda: ActionBouton(fenetre,supp)).pack(side=TOP,pady=[0,10])
    Button(fenetre,text="Quitter", fg='red',command=fenetre.destroy).pack(side=LEFT)
    Button(fenetre,text="Ajouter un DS",command=lambda: ActionBouton(fenetre,Ajout)).pack(side=RIGHT)
    fenetre.mainloop()
    if Ajout.get() == 1:
        insert = AjoutDS()
        if not(insert == None):
            insert.append(0)
            L.append(insert)
        L = MainFenetreDS(L)
    if supp.get() == 1:
        insert = suppDS(L)
        if not(insert == None):
            L = insert
        L = MainFenetreDS(L)
    return L

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
    ListeDS = loadDS()
    print(ListeDS)
    ListeDS = MainFenetreDS(ListeDS)
    saveDS(ListeDS)

    # time.strptime("date","format"), %Y = annee, %m = mois, %d = jour
    # time.localtime() = date du jour