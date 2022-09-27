from tkinter import *
from tkinter.messagebox import showerror
import os 

class note:
    def __init__(self,matiere,note,pourcent,ECTS):
        self.matiere = matiere
        self.note = note
        self.pourcent = pourcent
        self.ECTS = ECTS

#Liste des matières

def listMat(ListeNotes):
    ListeMat = []
    for i in ListeNotes:
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

#Chargement des notes

def loadNotes():
    ListeNotes = []
    f = open("Save/Note.txt",'r')
    ln = f.readline()
    while(1):
        ln = f.readline()
        if ln == '':
            break
        data = ln.split()
        ListeNotes.append(note(data[0],data[1],data[3],data[4]))
    f.close()
    return ListeNotes

###Savegarde des notes###

def saveNote(ListeNotes):
    f = open("Save/Note.txt",'w')
    f.write("Matiere Note Pourcentage\n")
    for i in ListeNotes:
        f.write("{} {} {}\n".format(i.matiere,i.note,i.pourcent,i.ECTS))
    f.close()


#Calcul de la moyenne générale

def CalculeMoyenneG(ListeNotes):
    a = 0
    b = 0
    for i in ListeNotes:
        note = int(i.note)
        #a += int(i[1])
        ECTS = int(i.ECTS)
        coeff = ECTS*(int(i.pourcent)/100)
        a += (note/20)*coeff
        b += coeff
    if b == 0:
        MoyenneG = None
    else:
        MoyenneG = (a/b)*20
    return MoyenneG

#Ajouter une note

def verifAjout(matiere,note,pourcentage):
    b = 1
    c = 1
    a = 0
    mat = matiere.split()
    if len(mat) == 1:
        a = 1
    else:
        showerror("Saisie incorrect","La saisie comporte des espaces, écrire sous la forme: truc_bidule à la place de: truc bidule")
    if int(note) > 20:
        showerror("Note trop haute","La note {} dépasse 20! C'est pas possible!".format(note))
        b = 0
    if int(pourcentage) > 100:
        showerror("Pourcentage trop haut","{}% est au dessus de 100%, ce qui est imposible!".format(pourcentage))
        c = 0
    if a == 1 and b == 1 and c == 1:
        return 1
    else:
        return 0


def AjoutNote():
    selec = Tk()
    selec.title("Ajouter une note")
    f = LabelFrame(selec,text="Saisir la note:")
    f.pack()
    matiere = StringVar()
    matiere.set("Matière")
    note = StringVar()
    note.set("Note")
    pourcentage = StringVar()
    pourcentage.set("Pourcentage")
    ECTS = StringVar()
    ECTS.set("ECTS")
    ajouter = IntVar()
    Entry(f,textvariable=matiere).pack(side=LEFT)
    Entry(f,textvariable=note).pack(side=LEFT)
    Entry(f,textvariable=pourcentage).pack(side=LEFT)
    Entry(f,textvariable=ECTS).pack(side=LEFT)
    Button(selec,text="Annuler",command=selec.destroy,fg="red").pack(side=LEFT)
    Button(selec,text="Ajouter",command=lambda: ActionBouton(selec,ajouter),fg="green").pack(side=RIGHT)
    selec.mainloop()
    if ajouter.get() == 1:
        verif = 0
        while(verif == 0):
            verif = verifAjout(matiere.get(),note.get(),pourcentage.get())
            if not(verif == 1):
                insert = AjoutNote()
                if insert == None:
                    break
                else:
                    matiere.set(insert.matiere)
                    note.set(insert.note)
                    pourcentage.set(insert.pourcentage)
                    ECTS.set(insert.ECTS)
        if verif == 1:
            return note(matiere.get(),note.get(),pourcentage.get(),ECTS.get())


#Fenetre principale

def FenetreNote(ListeNotes):
    L = ListeNotes
    MoyenneG = CalculeMoyenneG(ListeNotes)
    fenetre = Tk()
    fenetre.title("Informations sur les moyennes")
    Label(fenetre,text="Information sur les moyennes").pack()
    f1 = LabelFrame(fenetre,text="Moyenne générale:")
    f1.pack(padx=10,pady=10)
    if not(MoyenneG == None): 
        Label(f1,text="Moyenne: {}/20".format(round(MoyenneG,2))).pack(padx=50)
    else:
        Label(f1,text="Pas encore de notes").pack(padx=45)
    f2 = LabelFrame(fenetre,text="Moyenne par matière:")
    f2.pack(padx=10,pady=[0,10])
    for i in listMat(ListeNotes):
        a = 0
        b = 0
        for j in ListeNotes:
            if i == j[0]:
                ECTS = int(j.ECTS)
                note = int(j.note)
                coeff = ECTS*int(j.pourcent)
                a += (note/20)*coeff
                b += coeff
        if b == 0:
            Label(f2,text="Pas de notes pour le {}".format(i),justify=LEFT).pack(padx=[0,20])
        else:
            Moyenne = (a/b)*20
            Label(f2,text="Moyenne {}: {}/20".format(i,round(Moyenne,2)),justify=LEFT).pack(padx=[0,40])
    Ajouter = IntVar()
    Button(fenetre,text="Quitter",command=fenetre.destroy,fg="red").pack(side=LEFT)
    Button(fenetre,text="Ajouter une note",command=lambda: ActionBouton(fenetre,Ajouter),fg="green").pack(side=RIGHT)
    fenetre.mainloop()
    if Ajouter.get() == 1:
        insert = AjoutNote()
        if not(insert == None):
            L.append(insert)
        return [1,L]
    return [0,L]

def MainFenetreNote():
    ListeNotes = loadNotes()
    v = [0,ListeNotes]
    while(1):
        v = FenetreNote(v[1])
        if v[0] == 0:
            break
    saveNote(v[1])

###Vérification des sauvegardes###

def verifSave():
    if not(os.path.exists("Save")):
        os.mkdir("Save")
        f = open("Save/Note.txt",'w')
        f.close()
    if not(os.path.exists("Save/Note.txt")):
        f = open("Save/Note.txt",'w')
        f.close()

if __name__ == "__main__":
    MainFenetreNote()