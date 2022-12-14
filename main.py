import os
import time
import numpy as np
import webbrowser
from tkinter import *
from tkinter.messagebox import showerror, askyesno, showinfo
from FicheRev import loadCours, MainFenetreFiche
from InfoDs import loadDS, DSTri, MainFenetreDS
from InfoProjet import loadProjet, ProjetTri, MainFenetreProjet
from InfoTP import loadTP, TPTri, MainFenetreTP, saveTP, AjoutRapide
from Moyenne_Gen import loadNotes, MainFenetreNote, CalculeMoyenneG

class Devoir:
    def __init__(self,matiere,date,desc):
        self.matiere = matiere
        self.date = date
        self.desc = desc

class TP:
    def __init__(self,matiere,date,test):
        self.matiere = matiere
        self.date = date
        self.test = test

###Action sur les boutons###<<

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
    for ligne in [1,2,4,5,6]:
        if ligne == 2:
            a = Button(frame,background=couleur,command=BoboYeux)
            b = Button(frame,background=couleur,command=BoboYeux)
            a.grid(row=ligne,column=2)
            b.grid(row=ligne,column=4)
            for colonne in [0,1,3,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 4:
            c = Button(frame,background=couleur)
            d = Button(frame,background=couleur)
            c.grid(row=ligne,column=1)
            d.grid(row=ligne,column=5)
            for colonne in [0,2,3,4,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 5:
            e = Button(frame,background=couleur)
            f = Button(frame,background=couleur)
            g = Button(frame,background=couleur)
            e.grid(row=ligne,column=2)
            f.grid(row=ligne,column=3)
            g.grid(row=ligne,column=4)
            for colonne in [0,1,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        else:
            for colonne in range(7):
                Button(frame).grid(row=ligne,column=colonne)
    for colonne in range(7):
        if (colonne == 3):
            Button(frame,command=lambda: nezTama(a,b,c,d,e,f,g)).grid(row=3,column=colonne)
        else:
            Button(frame).grid(row=3,column=colonne)

def TamaTriste(frame):
    for ligne in [1,2,4,5,6]:
        if ligne == 2:
            a = Button(frame,background="red",command=BoboYeux)
            b = Button(frame,background="red",command=BoboYeux)
            a.grid(row=ligne,column=2)
            b.grid(row=ligne,column=4)
            for colonne in [0,1,3,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 5:
            c = Button(frame,background="red")
            d = Button(frame,background="red")
            c.grid(row=ligne,column=1)
            d.grid(row=ligne,column=5)
            for colonne in [0,2,3,4,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 4:
            e = Button(frame,background="red")
            f = Button(frame,background="red")
            g = Button(frame,background="red")
            e.grid(row=ligne,column=2)
            f.grid(row=ligne,column=3)
            g.grid(row=ligne,column=4)
            for colonne in [0,1,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        else:
            for colonne in range(7):
                Button(frame).grid(row=ligne,column=colonne)
    for colonne in range(7):
        if (colonne == 3):
            Button(frame,command=lambda: nezTama(a,b,c,d,e,f,g)).grid(row=3,column=colonne)
        else:
            Button(frame).grid(row=3,column=colonne)

def TamaMoyen(frame):
    for ligne in [1,2,4,5,6]:
        if ligne == 2:
            a = Button(frame,background="orange",command=BoboYeux)
            b = Button(frame,background="orange",command=BoboYeux)
            a.grid(row=ligne,column=2)
            b.grid(row=ligne,column=4)
            for colonne in [0,1,3,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 4:
            c = Button(frame,background="orange")
            d = Button(frame,background="orange")
            e = Button(frame,background="orange")
            f = Button(frame,background="orange")
            g = Button(frame,background="orange")
            c.grid(row=ligne,column=1)
            d.grid(row=ligne,column=2)
            e.grid(row=ligne,column=3)
            f.grid(row=ligne,column=4)
            g.grid(row=ligne,column=5)
            for colonne in [0,6]:
                Button(frame).grid(row=ligne,column=colonne)
        else:
            for colonne in range(7):
                Button(frame).grid(row=ligne,column=colonne)
    for colonne in range(7):
                if (colonne == 3):
                    Button(frame,command=lambda: nezTama(a,b,c,d,e,f,g)).grid(row=3,column=colonne)
                else:
                    Button(frame).grid(row=3,column=colonne)

def BoboYeux():
    showerror("","aïe ça fait super mal!!!\n~(>_<。)＼")

def nezTama(a,b,c,d,e,f,g):
    id = {0:'red',1:'green',2:'yellow',3:'blue',4:'pink',5:'cyan',6:'lime',7:'violet',8:'magenta',9:'orange',10:'purple'}
    oldCol = 20
    while(1):
        newCol = id[np.random.randint(11)]
        while(newCol == oldCol):
             newCol = id[np.random.randint(11)]
        a['bg'] = newCol
        b['bg'] = newCol
        c['bg'] = newCol
        d['bg'] = newCol
        e['bg'] = newCol
        f['bg'] = newCol
        g['bg'] = newCol
        a.update()
        oldCol = newCol
        time.sleep(0.1)

### Gestion des devoirs###

def saveDevoir(ListeDevoir):
    f = open("Save/Devoir.txt",'w')
    for i in ListeDevoir:
        f.write("{};{};{};\n".format(i.matiere,i.date,i.desc))
    f.close()

def loadDevoir():
    ListeDevoir = []
    f = open("Save/Devoir.txt",'r')
    while(1):
        data = f.readline()
        if data == '':
            break
        insert = data.split(';')
        ListeDevoir.append(Devoir(insert[0],insert[1],insert[2]))
    return ListeDevoir

def AjoutDevoir():
    ListeMois = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    fenetre = Tk()
    fenetre.title("Ajouter un devoir")
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
    selec.title("Rendre un devoir")
    l = LabelFrame(selec,text='Devoir réalisé(s):')
    l.pack(side=TOP,padx=10,pady=5)
    checklist = [IntVar() for x in range(n)]
    for i in range(n):
        Checkbutton(l,text="{}, pour le {}".format(ListeDevoir[i].matiere,ListeDevoir[i].date),variable=checklist[i],justify=LEFT).pack(padx=[5,50])
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

def FenetreDevoir(ListeDevoir):
    L = ListeDevoir
    fenetre = Tk()
    fenetre.title("Informations devoirs")
    frame1 = Frame(fenetre,bg = '#433e3f')
    frame1.pack()
    ftit = Frame(frame1,bg="#1d3557")
    ftit.grid(row=0,sticky='nwes')
    Label(ftit,text="Informations Devoir",bg="#1d3557",fg="#f4ebe8",font=('calibri',25,'bold','underline'),pady=20,padx=10).pack()
    ligne = 1
    for i in ListeDevoir:
        if i.date == '?':
            Label(frame1,text="{}".format(i.matiere),font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=ligne,sticky="nsew")
            ligne += 1
        else:
            Label(frame1,text="{} pour le {}".format(i.matiere,i.date),font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=ligne,sticky="nsew")
            ligne += 1
        Label(frame1,text="{}".format(i.desc),bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,sticky='nswe')
        ligne += 1
    if ListeDevoir == []:
        Label(frame1,text="Pas de Devoir à faire!",bg="#f4ebe8",font=('calibri',15),justify=LEFT).grid(row=ligne,sticky='nswe')
        ligne += 1
    fbut = Frame(frame1,bg='#433e3f')
    fbut.grid(row=ligne,columnspan=2,sticky='nswe')
    ajouter = IntVar()
    rendre = IntVar()
    Button(fbut,text="Quitter",bg='#d62828',fg="#f4ebe8",highlightbackground='#433e3f',command=fenetre.destroy).pack(side=LEFT,pady=10,padx=5)
    Button(fbut,text="Ajouter",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,ajouter)).pack(side=RIGHT,pady=10,padx=[0,5])
    Button(fbut,text="Rendre",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,rendre)).pack(side=RIGHT,pady=10,padx=[0,5])
    fenetre.mainloop()
    if ajouter.get() == 1:
        insert = AjoutDevoir()
        if not(insert == None):
            L.append(Devoir(insert[0],insert[1],insert[2]))
        return [1,L]
    if rendre.get() == 1:
        L = RenduDevoir(L)
        return [1,L]
    return [0,L] 

def MainFenetreDevoir():
    ListeDevoir = loadDevoir()
    v = [0,ListeDevoir]
    while(1):
        v = FenetreDevoir(v[1])
        if v[0] == 0:
            break
    saveDevoir(v[1])

###Affichage des informations###

def PtsAffiche():
    [pts,nonv] = sysPoint() #n ne sert pas ici
    v = 5 - nonv
    showinfo("Nombre de points","Humeur: {}/{}".format(round(pts,2),v*25))

###Gestion de l'humeur du tamagotchi###

def sysPoint():
    Points = 0
    NbNonValid = 0
    ListeFiche = loadCours()
    if not(ListeFiche == []):
        comptFiche = 0
        for i in ListeFiche:
            if i.aJour == '0' and i.fait == '0':
                comptFiche += 1
        Points += (1-(comptFiche/6))*25
    else:
        NbNonValid += 1
    ListeTP = loadTP()
    comptTP = 0
    for i in ListeTP:
        if i.test == '0':
            comptTP += 1
    Points += (1-(comptTP/4))*25
    ListeProjet = loadProjet()
    comptProjet = 0
    for i in ListeProjet:
        if i.fait == '0':
            comptProjet += 1
    Points += (1 - comptProjet/6) * 25
    ListeNotes = loadNotes()
    if ListeNotes == []:
        NbNonValid += 1
    else:
        MoyenneG = CalculeMoyenneG(ListeNotes)
        Points += (MoyenneG/20)*25
    ListeDevoir = loadDevoir()
    n = len(ListeDevoir)
    Points +=  (1 - (n/5))*25
    return [Points,NbNonValid]

###Options###

def PrenomTamagotchi():
    fenetre = Tk()
    fenetre.title("Nouveau nom")
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

def paramCouleur():
    fenetre = Tk()
    fenetre.title("Paramètre Couleur")
    Label(fenetre,text="Paramètre Couleur",bg="#1d3557",fg="#f4ebe8",font=('calibri',20,'bold','underline'),pady=5).grid(row=0,columnspan=3,sticky='nsew')
    Label(fenetre,text="Couleur",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=1,column=0,sticky='nsew')
    Label(fenetre,text="Nouvelle Couleur",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=1,column=1,sticky='nsew')
    Label(fenetre,text="Couleur par défaut",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8").grid(row=1,column=2,sticky='nsew')
    Label(fenetre,text="Pas fini pour l'instant!").grid(row=2,columnspan=3,sticky='nsew')
    fenetre.mainloop()

def Config():
    fenetre = Tk()
    fenetre.title("Options")
    Prenom = IntVar()
    Couleur = IntVar()
    Label(fenetre,text="Options",bg="#1d3557",fg="#f4ebe8",font=('calibri',20,'bold','underline'),pady=5).grid(row=0,columnspan=2,sticky='nsew')
    Button(fenetre,text="Changer le prénom",highlightbackground="#1d3557",bg="#c73e1d", fg="#f4ebe8",command=lambda: ActionBouton(fenetre,Prenom)).grid(row=1,column=0,sticky='nsew')
    Button(fenetre,text="Changer le style",highlightbackground="#1d3557",bg="#c73e1d", fg="#f4ebe8",command=lambda: ActionBouton(fenetre,Couleur)).grid(row=1,column=1,sticky='nsew')
    fbut = Frame(fenetre,bg='#433e3f')
    fbut.grid(row=2,columnspan=2,sticky='nswe')
    Button(fbut,text="Quitter",bg='#d62828',fg="#f4ebe8",highlightbackground='#433e3f',command=fenetre.destroy).pack(padx=5)
    fenetre.mainloop()
    if Prenom.get() == 1:
        PrenomTamagotchi()
    if Couleur.get() == 1:
        paramCouleur()

###fenetre principale###

def MainFenetre():
    #systeme de pts
    [pts,nonV] = sysPoint()
    TamaNom = loadPrenom()
    #création fenetre
    fenetre = Tk()
    fenetre.title("Mon assistant {}".format(TamaNom))
    #Les variables d'actions
    Fiche = IntVar()
    Moyenne = IntVar()
    DS = IntVar()
    tps = IntVar()
    Projet = IntVar()
    edt = IntVar()
    RapideTP = IntVar()
    Option = IntVar()
    devoir = IntVar()
    frame1 = Frame(fenetre,bg="#f4ebe8")
    frame1.pack()
    frame2 = Frame(frame1,bg="#f4ebe8")
    frame2.grid(row=0,column=0,sticky='nsew')
    separation = Frame(frame1,bg="#f4ebe8")
    separation.grid(row=0,column=1,sticky='nswe')
    frame3 = Frame(frame1,bg="#f4ebe8")
    frame3.grid(row=0,column=2,sticky='nsew')
    #Frame2
    Label(frame2,text=TamaNom,bg="#1d3557",fg="#f4ebe8",font=('calibri',20,'bold','underline'),pady=5).grid(row=0,sticky='nsew',columnspan=7)
    nbValide = 5 - nonV
    coeffHumeur = [0.75*nbValide*25,0.5*nbValide*25,0.25*nbValide*25]
    if pts >= coeffHumeur[0]:
        humeur = "heureux"
        TamaContent(frame2,"green")
    elif coeffHumeur[0] > pts >= coeffHumeur[1]:
        humeur = "content"
        TamaContent(frame2,"lime")
    elif coeffHumeur[1] > pts >= coeffHumeur[2]:
        humeur = "stressé"
        TamaMoyen(frame2)
    else:
        humeur = "triste"
        TamaTriste(frame2)
    couleur = {"heureux":"green","content":"lime","stressé":"orange","triste":"red"}
    Button(frame2,text="{} est {}".format(TamaNom,humeur),bg="#f4ebe8",fg=couleur[humeur],bd=0,padx=0,pady=0,activeforeground=couleur[humeur],activebackground=frame2['bg'],command=PtsAffiche,font=('calibri',15)).grid(row=7,columnspan=7,sticky='nswe')
    #separation '#433e3f' "#c73e1d" #3993dd
    Label(separation,text="  ",bg="#c73e1d",fg="#f4ebe8",font=('calibri',20,'bold'),pady=5).grid(row=0,sticky='nsew',columnspan=7)
    for i in range(1,8):
        Label(separation,text="  ",font=('calibri',15,'bold'),justify=LEFT,bg="#c73e1d",fg="#f4ebe8",pady=4,padx=2).grid(row=i,sticky="nsew")
    #Frame3
    Label(frame3,text="Informations principales",bg="#1d3557",fg="#f4ebe8",font=('calibri',20,'bold','underline'),pady=5,padx=18).grid(row=0,columnspan=2,sticky='nsew')
    ListeFiche = loadCours()
    comptFiche = 0
    for i in ListeFiche:
        if i.aJour == '0' and i.fait == '0':
            comptFiche += 1
    Label(frame3,text="Fiche de révision à faire: {}".format(comptFiche),bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=1,column=0,sticky='nswe')
    ListeDevoir = loadDevoir()
    comptDevoir = len(ListeDevoir)
    Label(frame3,text="Devoir à faire: {}".format(comptDevoir),bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=2,column=0,sticky='nsew')
    ListeNotes = loadNotes()
    MoyenneG = CalculeMoyenneG(ListeNotes)
    if MoyenneG == None:
        Label(frame3,text="Pas de notes",bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=3,column=0,sticky='nsew')
    else:
        MoyenneG = round(MoyenneG,2)
        Label(frame3,text="Moyenne générale: {}/20".format(MoyenneG),bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=3,column=0,sticky='nswe')
    ListeDS = loadDS()
    ListeDS = DSTri(ListeDS)
    FutureDS = None
    for i in ListeDS:
        if i.fait == '0':
            FutureDS = i
            break;
    if FutureDS == None:
        Label(frame3,text="Pas de futur DS prévu",bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=4,column=0,sticky='nswe')
    else:
        Label(frame3,text="Futur DS: {}, {}".format(FutureDS.matiere,FutureDS.date),bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=4,column=0,sticky='nswe')
    ListeProjet = loadProjet()
    ListeProjet = ProjetTri(ListeProjet)
    FutureProjet = None
    for i in ListeProjet:
        if i.fait == '0':
            FutureProjet = i
            break;
    if FutureProjet == None:
        Label(frame3,text="Pas de projet à rendre",bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=5,column=0,sticky='nswe')
    else:
        Label(frame3,text="Futur projet à rendre: {}, {}".format(FutureProjet.matiere,FutureProjet.date),bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=5,column=0,sticky='nswe')
    ListeTP = loadTP()
    ListeTP = TPTri(ListeTP)
    FutureTP = None
    FutureTPTest = None
    for i in ListeTP:
        if i.test == '1':
            FutureTPTest = i
            break
    for i in ListeTP:
        if i.test == '0':
            FutureTP = i
            break
    if FutureTP == None:
        Label(frame3,text="Pas de TP à rendre",bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=6,column=0,sticky='nswe')
    else:
        Label(frame3,text="Futur TP à rendre: {}, {}".format(FutureTP.matiere,FutureTP.date),bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=6,column=0,sticky='nswe')
    if FutureTPTest == None:
        Label(frame3,text="Pas de TP test à venir",bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=7,column=0,sticky='nswe')
    else:
        Label(frame3,text="Future TP test: {}, {}".format(FutureTPTest.matiere,FutureTPTest.date),bg="#f4ebe8",font=('calibri',15),justify=LEFT,pady=4).grid(row=7,column=0,sticky='nswe')
    frame4 = Frame(frame1,bg="#f4ebe8")
    frame4.grid(row=1,columnspan=3,sticky='nsew')
    Label(frame4,text="Plus d'informations",bg="#1d3557",fg="#f4ebe8",font=('calibri',20,'bold','underline'),pady=5,padx=187).grid(row=0,sticky='nsew',columnspan=3)
    Button(frame4,text="Fiche de révision",highlightbackground="#1d3557",bg="#c73e1d", fg="#f4ebe8",command=lambda: ActionBouton(fenetre,Fiche)).grid(row=1,column=0,sticky='nsew')
    Button(frame4,text="Informations TP",highlightbackground="#1d3557",bg="#c73e1d", fg="#f4ebe8",command=lambda: ActionBouton(fenetre,tps)).grid(row=1,column=1,sticky='nsew')
    Button(frame4,text="Devoir à faire",highlightbackground="#1d3557",bg="#c73e1d", fg="#f4ebe8",command=lambda: ActionBouton(fenetre,devoir)).grid(row=1,column=2,sticky='nsew')
    Button(frame4,text="Informations DS",highlightbackground="#1d3557",bg="#c73e1d", fg="#f4ebe8",command=lambda: ActionBouton(fenetre,DS)).grid(row=2,column=0,sticky='nsew')
    Button(frame4,text="Informations projets",highlightbackground="#1d3557",bg="#c73e1d", fg="#f4ebe8",command=lambda: ActionBouton(fenetre,Projet)).grid(row=2,column=1,sticky='nsew')
    Button(frame4,text="Moyenne Générale",highlightbackground="#1d3557",bg="#c73e1d", fg="#f4ebe8",command=lambda: ActionBouton(fenetre,Moyenne)).grid(row=2,column=2,sticky='nsew')
    fbut = Frame(frame1,bg='#433e3f')
    fbut.grid(row=2,columnspan=3,sticky='nswe')
    Button(fbut,text="Quitter",bg='#d62828',fg="#f4ebe8",highlightbackground='#433e3f',command=fenetre.destroy).pack(side=LEFT,pady=10,padx=5)
    Button(fbut,text="Ajout Rapide TP",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,RapideTP)).pack(side=RIGHT,pady=10,padx=[0,5])
    Button(fbut,text="Emploi du temps",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,edt)).pack(side=RIGHT,pady=10,padx=[0,5])
    Button(fbut,text="Options",highlightbackground='#433e3f',bg="#f4ebe8",command=lambda: ActionBouton(fenetre,Option)).pack(side=RIGHT,pady=10,padx=[0,5])
    fenetre.mainloop()
    if Fiche.get() == 1:
        MainFenetreFiche()
        return 1
    if DS.get() == 1:
        MainFenetreDS()
        return 1
    if Projet.get() == 1:
        MainFenetreProjet()
        return 1
    if tps.get() == 1:
        MainFenetreTP()
        return 1
    if Moyenne.get() == 1:
        MainFenetreNote()
        return 1
    if RapideTP.get() == 1:
        ListeTP = loadTP()
        insert = AjoutRapide()
        if not(insert == None):
            ListeTP.append(TP(insert[0],insert[1],insert[2]))
            saveTP(ListeTP)
        return 1
    if Option.get() == 1:
        Config()
        return 1
    if devoir.get() == 1:
        MainFenetreDevoir()
        return 1
    if edt.get() == 1:
        webbrowser.open("https://calendar.google.com/calendar/u/0/embed?src=vve57hbt6d2sm7kc3c82l6td4g@group.calendar.google.com&ctz=Europe/Paris&pli=1")
        return 1
    return 0
    

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
    ###Chemin vers l'executable###
    cheminDepart = os.getcwd()
    prenom = cheminDepart.split('/')[2]
    if prenom == 'quentin':
        NomProgramme = 'assistantjoseph'
    elif prenom == 'lehastir':
        NomProgramme = 'assistantsquishy'
    else:
        NomProgramme = 'assistantsimpy'
    Nomapp = "/usr/share/applications/"+NomProgramme+".desktop"
    f = open(Nomapp,'r')
    while(1):
        ln = f.readline()
        if ln.split("=")[0] == 'Exec':
            break
    cheminExec = ln.split("=")[1]
    chemin = ''
    for i in cheminExec.split("/"):
        if not(i == 'main\n'):
            chemin += i +'/'
    os.chdir(chemin)

    ###Programme###
    vSave = verifSave()
    vProg = verifProg()
    if vSave == 0:
        Tuto()
        PrenomTamagotchi()
    if vProg == 1:
        while(1):
            v = 0
            v = MainFenetre()
            if (v == 0):
                break
        

#pyinstaller --onefile main.py