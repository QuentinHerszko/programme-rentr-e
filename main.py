import os
import time
from tkinter import *
from tkinter.messagebox import showerror, askyesno
from FicheRev import loadCours, MainFenetreFiche,saveCours
from InfoDs import loadDS, DSTri, MainFenetreDS, saveDS
from InfoProjet import loadProjet, ProjetTri, MainFenetreProjet, saveProjet
from InfoTP import loadTP, TPTri, MainFenetreTP, saveTP, AjoutRapide
from Moyenne_Gen import loadNotes, MainFenetreNote, saveNote, CalculeMoyenneG

###Action sur les boutons###

def ActionBouton(fenetre,variable):
    variable.set(1)
    fenetre.destroy()

###Configuration du tamagotchi###

def loadPrenom():
    f = open("Save/main.txt","r")
    Prenom = f.readline()
    f.close()
    return Prenom

def TamaContent(frame,couleur):
    for ligne in range(6):
        if ligne == 1:
            Button(frame,background=couleur).grid(row=ligne,column=2)
            Button(frame,background=couleur).grid(row=ligne,column=4)
            for colonne in [0,1,3,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 3:
            Button(frame,background=couleur).grid(row=ligne,column=1)
            Button(frame,background=couleur).grid(row=ligne,column=5)
            for colonne in [0,2,3,4,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 4:
            Button(frame,background=couleur).grid(row=ligne,column=2)
            Button(frame,background=couleur).grid(row=ligne,column=3)
            Button(frame,background=couleur).grid(row=ligne,column=4)
            for colonne in [0,1,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        else:
            for colonne in range(7):
                Button(frame).grid(row=ligne,column=colonne)

def TamaTriste(frame):
    for ligne in range(6):
        if ligne == 1:
            Button(frame,background="red").grid(row=ligne,column=2)
            Button(frame,background="red").grid(row=ligne,column=4)
            for colonne in [0,1,3,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 4:
            Button(frame,background="red").grid(row=ligne,column=1)
            Button(frame,background="red").grid(row=ligne,column=5)
            for colonne in [0,2,3,4,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 3:
            Button(frame,background="red").grid(row=ligne,column=2)
            Button(frame,background="red").grid(row=ligne,column=3)
            Button(frame,background="red").grid(row=ligne,column=4)
            for colonne in [0,1,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        else:
            for colonne in range(7):
                Button(frame).grid(row=ligne,column=colonne)

def TamaMoyen(frame):
    for ligne in range(6):
        if ligne == 1:
            Button(frame,background="orange").grid(row=ligne,column=2)
            Button(frame,background="orange").grid(row=ligne,column=4)
            for colonne in [0,1,3,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 3:
            for colonne in [1,2,3,4,5]:
                Button(frame,background="orange").grid(row=ligne,column=colonne)
            for colonne in [0,6]:
                Button(frame).grid(row=ligne,column=colonne)
        else:
            for colonne in range(7):
                Button(frame).grid(row=ligne,column=colonne)

### Gestion des devoirs###

def saveDevoir(ListeDevoir):
    f = open("Save/Devoir.txt",'w')
    for i in ListeDevoir:
        f.write("{};{};{};\n".format(i[0],i[1],i[2]))
    f.close()

def loadDevoir():
    ListeDevoir = []
    f = open("Save/Devoir.txt",'r')
    while(1):
        data = f.readline()
        if data == '':
            break
        insert = data.split(';')
        ListeDevoir.append(insert)
    return ListeDevoir

def AjoutDevoir():
    ListeMois = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    fenetre = Tk()
    matiere = StringVar()
    matiere.set("Matière")
    jours = StringVar()
    jours.set('7')
    description = StringVar()
    description.set('Description')
    l = LabelFrame(fenetre,text="Ajout d'un devoir:")
    l.pack()
    Entry(l,textvariable=matiere).pack(side=LEFT)
    Entry(l,textvariable=jours).pack(side = LEFT)
    Entry(l,textvariable=description).pack(side=BOTTOM)
    Button(fenetre,text="Annuler",fg='red',command=fenetre.destroy).pack(side=LEFT)
    ajouter = IntVar()
    Button(fenetre,text="Ajouter",fg="green",command=lambda: ActionBouton(fenetre,ajouter)).pack(side=RIGHT)
    fenetre.mainloop()
    if ajouter.get() == 1:
        if not(jours.get() == '?'):
            temps = time.time()
            ajout = 86400 * int(jours.get())
            dateAjout = time.ctime(ajout+temps)
            dateAjout = dateAjout.split()
            [Jour,Mois,Annee] = [dateAjout[2],ListeMois[dateAjout[1]],dateAjout[4]]
            if int(Jour) < 10:
                Jour = "0"+Jour
            if Mois < 10:
                Mois = "0{}".format(Mois)
            date = "{}-{}-{}".format(Jour,Mois,Annee)
        else:
            date = jours.get()
        insert = [matiere.get(),date,description.get()]
        return insert

def RenduDevoir(ListeDevoir):
    n = len(ListeDevoir)
    selec = Tk()
    l = LabelFrame(selec,text='Devoir réalisé(s):')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    for i in range(n):
        Checkbutton(l,text="{}, pour le {}".format(ListeDevoir[i][0],ListeDevoir[i][1]),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
    valider = IntVar()
    Button(selec,text="Cancel",fg='red',command=selec.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(selec,text="Valider",fg='green',command=lambda: ActionBouton(selec,valider)).pack(side=RIGHT,padx=5,pady=5)
    selec.mainloop()
    if valider.get() == 1:
        NewListe = []
        k = 0
        for i in checklist:
            if i.get() == 0:
                NewListe.append(ListeDevoir[k])
            k+=1
    else:
        NewListe = ListeDevoir
    return NewListe

def MainFenetreDevoir(ListeDevoir):
    L = ListeDevoir
    fenetre = Tk()
    if not(ListeDevoir == []):
        for i in ListeDevoir:
            if i[1] == '?':
                l = LabelFrame(fenetre,text="{}:".format(i[0]))
            else:
                l = LabelFrame(fenetre,text="{} pour le {}".format(i[0],i[1]))
            l.pack()
            Label(l,text=i[2]).pack()
    else:
        Label(fenetre,text="Pas de travail à faire").pack()
    ajouter = IntVar()
    rendre = IntVar()
    Button(fenetre,text="Quitter",fg='red',command=fenetre.destroy).pack(side=LEFT)
    Button(fenetre,text="Ajouter un devoir",fg='green',command=lambda: ActionBouton(fenetre,ajouter)).pack(side=RIGHT)
    Button(fenetre,text="Rendre un devoir",command=lambda: ActionBouton(fenetre,rendre)).pack(side=RIGHT)
    fenetre.mainloop()
    if ajouter.get() == 1:
        insert = AjoutDevoir()
        if not(insert == None):
            L.append(insert)
        L = MainFenetreDevoir(L)
    if rendre.get() == 1:
        L = RenduDevoir(L)
        L = MainFenetreDevoir(L)
    return L 

###Affichage des informations###

def Informations(frame,humeur):
    couleur = {"heureux":"green","content":"lime","stressé":"orange","triste":"red"}
    prenom = loadPrenom()
    Label(frame,text="{} est {}".format(prenom,humeur),fg=couleur[humeur]).pack(pady=10)
    ListeFiche = loadCours()
    comptFiche = 0
    for i in ListeFiche:
        if i[2] == '0' and i[3] == '0':
            comptFiche += 1
    Label(frame,text="Fiche de révision à faire: {}".format(comptFiche),justify=LEFT).pack(padx=[0,110])
    ListeNotes = loadNotes()
    MoyenneG = CalculeMoyenneG(ListeNotes)
    if MoyenneG == None:
        Label(frame,text="Pas de notes",justify=LEFT).pack(padx=[0,200])
    else:
        MoyenneG = round(MoyenneG,2)
        Label(frame,text="Moyenne générale: {}/20".format(MoyenneG),justify=LEFT).pack(padx=[0,100])
    ListeDS = loadDS()
    ListeDS = DSTri(ListeDS)
    FutureDS = None
    for i in ListeDS:
        if i[2] == '0':
            FutureDS = i
            break;
    if FutureDS == None:
        Label(frame,text="Pas de future DS prévue",justify=LEFT).pack(padx=[0,125])
    else:
        Label(frame,text="Future DS: {}, {}".format(FutureDS[0],FutureDS[1]),justify=LEFT).pack(padx=[0,79])
    ListeProjet = loadProjet()
    ListeProjet = ProjetTri(ListeProjet)
    FutureProjet = None
    for i in ListeProjet:
        if i[2] == '0':
            FutureProjet = i
            break;
    if FutureProjet == None:
        Label(frame,text="Pas de projet à rendre",justify=LEFT).pack(padx=[0,143])
    else:
        Label(frame,text="Future projet à rendre: {}, {}".format(FutureProjet[0],FutureProjet[1]),justify=LEFT).pack()
    ListeTP = loadTP()
    ListeTP = TPTri(ListeTP)
    FutureTP = None
    FutureTPTest = None
    for i in ListeTP:
        if i[2] == '1':
            FutureTPTest = i
            break
    for i in ListeTP:
        if i[2] == '0':
            FutureTP = i
            break
    if FutureTP == None:
        Label(frame,text="Pas de TP à rendre",justify=LEFT).pack(padx=[0,165])
    else:
        Label(frame,text="Future TP à rendre: {}, {}".format(FutureTP[0],FutureTP[1]),justify=LEFT).pack(padx=[0,23])
    if FutureTPTest == None:
        Label(frame,text="Pas de TP test à venir",justify=LEFT).pack(padx=[0,145])
    else:
        Label(frame,text="Future TP test: {}, {}".format(FutureTPTest[0],FutureTPTest[1]),justify=LEFT).pack(padx=[0,52])

###Gestion de l'humeur du tamagotchi###

def sysPoint():
    Points = 0
    NbNonValid = 0
    ListeFiche = loadCours()
    comptFiche = 0
    for i in ListeFiche:
        if i[2] == '0' and i[3] == '0':
            comptFiche += 1
    if comptFiche <=2:
        Points += 25
    elif 2 < comptFiche <= 4:
        Points += 50/3
    elif 4 < comptFiche <= 6:
        Points += 25/3
    ListeTP = loadTP()
    comptTP = 0
    for i in ListeTP:
        if i[2] == '0':
            comptTP += 1
    if comptTP <= 1:
        Points += 25
    elif 1 < comptTP <= 2:
        Points += 50/3
    elif 2 < comptTP <= 3:
        Points += 25/3
    ListeProjet = loadProjet()
    comptProjet = 0
    for i in ListeProjet:
        if i[2] == '0':
            comptProjet += 1
    Points += (1 - comptProjet*(1/6)) * 25   
    if ListeFiche == []:
        NbNonValid += 1
    if ListeProjet == []:
        NbNonValid += 1
    if ListeTP == []:
        NbNonValid += 1
    ListeNotes = loadNotes()
    if ListeNotes == []:
        NbNonValid += 1
    else:
        MoyenneG = CalculeMoyenneG(ListeNotes)
        Points += (MoyenneG/20)*25
    return [Points,NbNonValid]

###Prénom tamagotcho###

def PrenomTamagotchi():
    fenetre = Tk()
    f = LabelFrame(fenetre,text="Donnez un nom à votre tamagotchi:")
    f.pack()
    Prenom = StringVar()
    Valider = IntVar()
    Prenom.set("Prénom")
    Entry(f,textvariable=Prenom).pack()
    Button(fenetre,text="Quiter",command=fenetre.destroy,fg="red").pack(side=LEFT)
    Button(fenetre,text="Confirmer",command=lambda: ActionBouton(fenetre,Valider),fg="green").pack(side=RIGHT)
    fenetre.mainloop()
    if Valider.get() == 1:
        f = open("Save/main.txt","w")
        f.write(Prenom.get())
        f.close()

###fenetre principale###

def MainFenetre():
    #systeme de pts
    [pts,nonV] = sysPoint()
    #création fenetre
    fenetre = Tk()
    #Les variables d'actions
    Fiche = IntVar()
    Moyenne = IntVar()
    DS = IntVar()
    TP = IntVar()
    Projet = IntVar()
    #Fenetres
    f = Frame(fenetre)
    f.pack()
    f1 = Frame(f)
    f2 = LabelFrame(f,text="Informations principales:")
    f3 = LabelFrame(f,text="Plus d'infomations:")
    f1.pack(side=LEFT)
    f2.pack(side=LEFT)
    f3.pack(side=LEFT)
    RapideTP = IntVar()
    ModifP = IntVar()
    devoir = IntVar()
    Button(fenetre,text="Quitter",command=fenetre.destroy,fg="red").pack(side = LEFT)
    Button(fenetre,text="Ajout Rapide TP",command=lambda: ActionBouton(fenetre,RapideTP)).pack(side=RIGHT)
    Button(fenetre,text="Devoir à faire",command=lambda: ActionBouton(fenetre,devoir)).pack(side=RIGHT)
    Button(fenetre,text="Modifier le prénom",command=lambda: ActionBouton(fenetre,ModifP)).pack(side=RIGHT)
    if pts >= (75 - nonV*25):
        humeur = "heureux"
        TamaContent(f1,"green")
    elif 75 > pts >= (50 - nonV*25):
        humeur = "content"
        TamaContent(f1,"lime")
    elif 50 > pts >= (25 - nonV*25):
        humeur = "stressé"
        TamaMoyen(f1)
    else:
        humeur = "triste"
        TamaTriste(f1)
    Informations(f2,humeur)
    Button(f3,text="Fiche de révision",command=lambda: ActionBouton(fenetre,Fiche),padx=20).pack(padx=10,pady=[6,0])
    Button(f3,text="Moyenne générale",command=lambda: ActionBouton(fenetre,Moyenne),padx=15).pack()
    Button(f3,text="Information DS",command=lambda: ActionBouton(fenetre,DS),padx=26.4).pack()
    Button(f3,text="Information Projet",command=lambda: ActionBouton(fenetre,Projet),padx=15.5).pack()
    Button(f3,text="Information TP",command=lambda: ActionBouton(fenetre,TP),padx=26.5).pack(pady=[0,6])
    fenetre.mainloop()
    if Fiche.get() == 1:
        ListeFiche = loadCours()
        ListeFiche = MainFenetreFiche(ListeFiche)
        saveCours(ListeFiche)
        MainFenetre()
    if DS.get() == 1:
        ListeDS = loadDS()
        ListeDS = MainFenetreDS(ListeDS)
        saveDS(ListeDS)
        MainFenetre()
    if Projet.get() == 1:
        ListeProjet = loadProjet()
        ListeProjet = MainFenetreProjet(ListeProjet)
        saveProjet(ListeProjet)
        MainFenetre()
    if TP.get() == 1:
        ListeTP = loadTP()
        ListeTP = MainFenetreTP(ListeTP)
        saveTP(ListeTP)
        MainFenetre()
    if Moyenne.get() == 1:
        ListeNotes = loadNotes()
        ListeNotes = MainFenetreNote(ListeNotes)
        saveNote(ListeNotes)
        MainFenetre()
    if RapideTP.get() == 1:
        ListeTP = loadTP()
        insert = AjoutRapide()
        if not(insert == None):
            ListeTP.append(insert)
            saveTP(ListeTP)
        MainFenetre()
    if ModifP.get() == 1:
        PrenomTamagotchi()
        MainFenetre()
    if devoir.get() == 1:
        ListeDevoir = loadDevoir()
        ListeDevoir = MainFenetreDevoir(ListeDevoir)
        saveDevoir(ListeDevoir)
        MainFenetre()

###Existence des sauvegardes###

def verifSave():
    v = 1
    if not(os.path.exists("Save")):
        os.makedirs("Save")
        f = open("Save/DS.txt",'w')
        f.write("Matiere Date")
        f.close()
        f = open("Save/Fiche.txt",'w')
        f.write("Matiere chp fichable fait")
        f.close()
        f = open("Save/Note.txt",'w')
        f.write("Matiere Note Pourcentage")
        f.close()
        f = open("Save/Projet.txt",'w')
        f.write("Matiere date")
        f.close()
        f = open("Save/TP.txt",'w')
        f.write("Matiere date test")
        f.close()
        f = open("Save/main.txt","w")
        f.write("Tamagotchi")
        f.close()
        f = open("Save/Devoir.txt",'w')
        f.close()
        v = 0
    return v

###Vérif des programmes###

def verifProg():
    v = 1
    for i in ["FicheRev.py","InfoDs.py","InfoProjet.py","InfoTP.py","Moyenne_Gen.py"]:
        if not(os.path.exists(i)):
            showerror("Programme manquant","Attention! Le programme {} n'as pas été trouvé!".format(i))
            v = 0
    return v
        
###Tuto###

def Tuto():
    if askyesno("Bonjour!","C'est la première fois que vous lancez le programme? Voulez-vous faire le tuto?"):
        fenetre = Tk()
        f1 = Frame(fenetre)
        f2 = LabelFrame(fenetre,text="Explications:")
        f1.pack(side = LEFT)
        f2.pack(side = RIGHT)
        TamaContent(f1,"green")
        Label(f2,text="Lui c'est ton tamagotchi, il change d'humeur en fonction de différents paramètres:\n-La moyenne générale\n-Le nombre de fiche de révision à faire\n-Le nombre de projet à rendre\n-Le nombre de TP à rendre\nLe but va être de bien travailler pour qu'il reste le plus heureux possible!\nLe programme sert surtout à voir de façon visuel le travail à faire.",justify=LEFT).pack()
        Button(f2,text="Ok",command=fenetre.destroy).pack()
        fenetre.mainloop()

if __name__ == "__main__":
    vSave = verifSave()
    vProg = verifProg()
    if vSave == 0:
        Tuto()
        PrenomTamagotchi()
    if vProg == 1:
        MainFenetre()
    #AjoutDevoir()

#pyinstaller --onefile test.py
