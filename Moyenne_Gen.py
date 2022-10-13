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
        ListeNotes.append(note(data[0],data[1],data[2],data[3]))
    f.close()
    return ListeNotes

###Savegarde des notes###

def saveNote(ListeNotes):
    f = open("Save/Note.txt",'w')
    f.write("Matiere Note Pourcentage\n")
    for i in ListeNotes:
        f.write("{} {} {} {}\n".format(i.matiere,i.note,i.pourcent,i.ECTS))
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
    Note = StringVar()
    Note.set("Note")
    pourcentage = StringVar()
    pourcentage.set("Pourcentage")
    ECTS = StringVar()
    ECTS.set("ECTS")
    ajouter = IntVar()
    Entry(f,textvariable=matiere).pack(side=LEFT)
    Entry(f,textvariable=Note).pack(side=LEFT)
    Entry(f,textvariable=pourcentage).pack(side=LEFT)
    Entry(f,textvariable=ECTS).pack(side=LEFT)
    Button(selec,text="Annuler",command=selec.destroy,fg="red").pack(side=LEFT)
    Button(selec,text="Ajouter",command=lambda: ActionBouton(selec,ajouter),fg="green").pack(side=RIGHT)
    selec.mainloop()
    if ajouter.get() == 1:
        verif = 0
        while(verif == 0):
            verif = verifAjout(matiere.get(),Note.get(),pourcentage.get())
            if not(verif == 1):
                insert = AjoutNote()
                if insert == None:
                    break
                else:
                    matiere.set(insert.matiere)
                    Note.set(insert.note)
                    pourcentage.set(insert.pourcentage)
                    ECTS.set(insert.ECTS)
        if verif == 1:
            return note(matiere.get(),Note.get(),pourcentage.get(),ECTS.get())

#Supp d'une note

def suppNote(ListeNotes):
    n = len(ListeNotes)
    selec = Tk()
    selec.title("Supprimer une note")
    l = LabelFrame(selec,text='Toute les notes:')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    if n == 0:
        Label(selec,text="Pas de note à supprimer").pack()
    for i in range(n):
        Checkbutton(l,text="{}, {}/20, {}% , {} ECTS".format(ListeNotes[i].matiere,ListeNotes[i].note,ListeNotes[i].pourcent,ListeNotes[i].ECTS),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
    supp = IntVar()
    Button(selec,text="Cancel",fg='red',command=selec.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(selec,text="Supprimer!",command=lambda: ActionBouton(selec,supp)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if supp.get() == 1:
        ListeNotesF = []
        for i in range(n):
            if checklist[i].get() == 0:
                ListeNotesF.append(ListeNotes[i])
        return ListeNotesF


#Fenetre principale

def FenetreNote(ListeNotes):
    L = ListeNotes
    MoyenneG = CalculeMoyenneG(ListeNotes)
    fenetre = Tk()
    fenetre.title("Informations sur les moyennes")
    frame1 = Frame(fenetre,bg="#433e3f")
    frame1.pack()
    ftit = Frame(frame1,bg="#1d3557")
    ftit.grid(row=0,sticky='nwes',columnspan=2)
    Label(ftit,text="Informations sur les notes",bg="#1d3557",fg="#f4ebe8",font=('calibri',25,'bold','underline'),pady=20,padx=10).pack()
    Label(frame1,text="Moyenne générale",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=1,columnspan=2,sticky="nsew")
    if MoyenneG == None:
        Label(frame1,text="Pas de notes",bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=2,columnspan=2,sticky='nswe')
    else:
        Label(frame1,text="{}/20".format(MoyenneG),bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=2,columnspan=2,sticky='nswe')
    Label(frame1,text="Moyenne par matières",bg="#1d3557",fg="#f4ebe8",font=('calibri',20,'bold','underline'),pady=5).grid(row=3,sticky='nsew',columnspan=2)
    Label(frame1,text="Matières",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=4,column=0,sticky="nsew")
    Label(frame1,text="Moyennes",font=('calibri',15,'bold'),padx=10,bg="#c73e1d",fg="#f4ebe8").grid(row=4,column=1,sticky='nswe')
    ligne = 5
    for i in listMat(L):
        a = 0
        b = 0
        for j in ListeNotes:
            if i == j.matiere:
                ECTS = int(j.ECTS)
                Note = int(j.note)
                coeff = ECTS*int(j.pourcent)
                a += (Note/20)*coeff
                b += coeff
        if b == 0:
            Label(frame1,text="Pas de notes",bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,column=0,sticky='nswe')
            ligne += 1
        else:
            Moyenne = (a/b)*20
            Label(frame1,text="{}".format(i),bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,column=0,sticky='nswe')
            Label(frame1,text="{}/20".format(Moyenne),bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,column=1,sticky='nswe')
            ligne += 1
    fbut = Frame(frame1,bg='#433e3f')
    fbut.grid(row=ligne,columnspan=3,sticky='nswe')
    Ajouter = IntVar()
    Supprimer = IntVar()
    Button(fbut,text="Quitter",bg='#d62828',fg="#f4ebe8",highlightbackground='#433e3f',command=fenetre.destroy).pack(side=LEFT,pady=10,padx=5)
    Button(fbut,text="Ajouter",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,Ajouter)).pack(side=RIGHT,pady=10,padx=[0,5])
    Button(fbut,text="Supprimer",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,Supprimer)).pack(side=RIGHT,pady=10,padx=[0,5])
    fenetre.mainloop()
    if Ajouter.get() == 1:
        insert = AjoutNote()
        if not(insert == None):
            L.append(insert)
        return [1,L]
    if Supprimer.get() == 1:
        L = suppNote(L)
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