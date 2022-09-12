from tkinter import *
from tkinter.messagebox import showerror

#Coeff/matiere

def ECTSMat(matiere):
    a = {"MA0913":30,"MA0914":30,"SEP0921":30,"SEP0922":30,"MA0934":60,"MA0944":30,"CHPS0703":30,"AN0904":30,"MA0953":30}
    return a[matiere]

#Liste des matières

def listMat():
    return ["MA0913","MA0914","SEP0921","SEP0922","MA0934","MA0944","CHPS0703","AN0904","MA0953"]

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
        ListeNotes.append(ln.split())
    f.close()
    return ListeNotes

###Savegarde des notes###

def saveNote(ListeNotes):
    f = open("Save/Note.txt",'w')
    f.write("Matiere Note Pourcentage\n")
    for i in ListeNotes:
        f.write("{} {} {}\n".format(i[0],i[1],i[2]))
    f.close()


#Calcul de la moyenne générale

def CalculeMoyenneG(ListeNotes):
    a = 0
    b = 0
    for i in ListeNotes:
        note = int(i[1])
        #a += int(i[1])
        ECTS = ECTSMat(i[0])
        coeff = ECTS*(int(i[2])/100)
        a += (note/20)*coeff
        b += coeff
    if b == 0:
        MoyenneG = None
    else:
        MoyenneG = (a/b)*20
    return MoyenneG

#Ajouter une note

def verifAjout(matiere,note,pourcentage):
    verifMat = listMat()
    a = 0
    b = 1
    c = 1
    for i in verifMat:
        if i == matiere:
            a = 1
    if a == 0:
        showerror("Matière pas reconnue","La matière: {} n'est pas reconnue. Attention au matière comme SEP0922 ou CHPS0703!".format(matiere))
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
    f = LabelFrame(selec,text="Saisir la note:")
    f.pack()
    matiere = StringVar()
    matiere.set("Matière")
    note = StringVar()
    note.set("Note")
    pourcentage = StringVar()
    pourcentage.set("Pourcentage")
    ajouter = IntVar()
    Entry(f,textvariable=matiere).pack(side=LEFT)
    Entry(f,textvariable=note).pack(side=LEFT)
    Entry(f,textvariable=pourcentage).pack(side=LEFT)
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
                    matiere.set(insert[0])
                    note.set(insert[1])
                    pourcentage.set(insert[2])
        if verif == 1:
            return [matiere.get(),note.get(),pourcentage.get()]


#Fenetre principale

def MainFenetreNote(ListeNotes):
    L = ListeNotes
    MoyenneG = CalculeMoyenneG(ListeNotes)
    fenetre = Tk()
    Label(fenetre,text="Information sur les moyennes").pack()
    f1 = LabelFrame(fenetre,text="Moyenne générale:")
    f1.pack(padx=10,pady=10)
    if not(MoyenneG == None): 
        Label(f1,text="Moyenne: {}/20".format(round(MoyenneG,2))).pack(padx=50)
    else:
        Label(f1,text="Pas encore de notes").pack(padx=45)
    f2 = LabelFrame(fenetre,text="Moyenne par matière:")
    f2.pack(padx=10,pady=[0,10])
    for i in listMat():
        ECTS = ECTSMat(i)
        a = 0
        b = 0
        for j in ListeNotes:
            if i == j[0]:
                note = int(j[1])
                coeff = ECTS*int(j[2])
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
        L = MainFenetreNote(L)
    return L

if __name__ == "__main__":
    ListeNotes = loadNotes()
    ListeNotes = MainFenetreNote(ListeNotes)
    saveNote(ListeNotes)