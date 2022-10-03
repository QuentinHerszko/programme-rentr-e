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
    for ligne in [0,1,3,4,5]:
        if ligne == 1:
            a = Button(frame,background=couleur,command=BoboYeux)
            b = Button(frame,background=couleur,command=BoboYeux)
            a.grid(row=ligne,column=2)
            b.grid(row=ligne,column=4)
            for colonne in [0,1,3,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 3:
            c = Button(frame,background=couleur)
            d = Button(frame,background=couleur)
            c.grid(row=ligne,column=1)
            d.grid(row=ligne,column=5)
            for colonne in [0,2,3,4,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 4:
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
            Button(frame,command=lambda: nezTama(a,b,c,d,e,f,g)).grid(row=2,column=colonne)
        else:
            Button(frame).grid(row=2,column=colonne)

def TamaTriste(frame):
    for ligne in [0,1,3,4,5]:
        if ligne == 1:
            a = Button(frame,background="red",command=BoboYeux)
            b = Button(frame,background="red",command=BoboYeux)
            a.grid(row=ligne,column=2)
            b.grid(row=ligne,column=4)
            for colonne in [0,1,3,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 4:
            c = Button(frame,background="red")
            d = Button(frame,background="red")
            c.grid(row=ligne,column=1)
            d.grid(row=ligne,column=5)
            for colonne in [0,2,3,4,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 3:
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
            Button(frame,command=lambda: nezTama(a,b,c,d,e,f,g)).grid(row=2,column=colonne)
        else:
            Button(frame).grid(row=2,column=colonne)

def TamaMoyen(frame):
    for ligne in [0,1,3,4,5]:
        if ligne == 1:
            a = Button(frame,background="orange",command=BoboYeux)
            b = Button(frame,background="orange",command=BoboYeux)
            a.grid(row=ligne,column=2)
            b.grid(row=ligne,column=4)
            for colonne in [0,1,3,5,6]:
                Button(frame).grid(row=ligne,column=colonne)
        elif ligne == 3:
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
                    Button(frame,command=lambda: nezTama(a,b,c,d,e,f,g)).grid(row=2,column=colonne)
                else:
                    Button(frame).grid(row=2,column=colonne)

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
    if not(ListeDevoir == []):
        for i in ListeDevoir:
            if i.date == '?':
                l = LabelFrame(fenetre,text="{}:".format(i.matiere))
            else:
                l = LabelFrame(fenetre,text="{} pour le {}".format(i.matiere,i.date))
            l.pack()
            Label(l,text=i.desc).pack()
    else:
        Label(fenetre,text="Pas de travail à faire").pack()
    ajouter = IntVar()
    rendre = IntVar()
    quitter = IntVar()
    Button(fenetre,text="Quitter",fg='red',command=lambda: ActionBouton(fenetre,quitter)).pack(side=LEFT)
    Button(fenetre,text="Ajouter un devoir",fg='green',command=lambda: ActionBouton(fenetre,ajouter)).pack(side=RIGHT)
    Button(fenetre,text="Rendre un devoir",command=lambda: ActionBouton(fenetre,rendre)).pack(side=RIGHT)
    fenetre.mainloop()
    if quitter.get() == 1:
        return [0,L]
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

def Informations(frame,humeur):
    couleur = {"heureux":"green","content":"lime","stressé":"orange","triste":"red"}
    prenom = loadPrenom()
    #Label(frame,text="{} est {}".format(prenom,humeur),fg=couleur[humeur]).pack()
    Button(frame,text="{} est {}".format(prenom,humeur),fg=couleur[humeur],bd=0,padx=0,pady=0,activeforeground=couleur[humeur],activebackground=frame['bg'],command=PtsAffiche).pack()
    ListeFiche = loadCours()
    comptFiche = 0
    for i in ListeFiche:
        if i.aJour == '0' and i.fait == '0':
            comptFiche += 1
    Label(frame,text="Fiche de révision à faire: {}".format(comptFiche),justify=LEFT).pack(padx=[0,110])
    ListeDevoir = loadDevoir()
    comptDevoir = len(ListeDevoir)
    Label(frame,text="Devoir à faire: {}".format(comptDevoir),justify=LEFT).pack(padx=[0,180])
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
        if i.fait == '0':
            FutureDS = i
            break;
    if FutureDS == None:
        Label(frame,text="Pas de futur DS prévu",justify=LEFT).pack(padx=[0,145])
    else:
        Label(frame,text="Futur DS: {}, {}".format(FutureDS.matiere,FutureDS.date),justify=LEFT).pack(padx=[0,79])
    ListeProjet = loadProjet()
    ListeProjet = ProjetTri(ListeProjet)
    FutureProjet = None
    for i in ListeProjet:
        if i.fait == '0':
            FutureProjet = i
            break;
    if FutureProjet == None:
        Label(frame,text="Pas de projet à rendre",justify=LEFT).pack(padx=[0,143])
    else:
        Label(frame,text="Future projet à rendre: {}, {}".format(FutureProjet.matiere,FutureProjet.date),justify=LEFT).pack()
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
        Label(frame,text="Pas de TP à rendre",justify=LEFT).pack(padx=[0,165])
    else:
        Label(frame,text="Futur TP à rendre: {}, {}".format(FutureTP.matiere,FutureTP.date),justify=LEFT).pack(padx=[0,23])
    if FutureTPTest == None:
        Label(frame,text="Pas de TP test à venir",justify=LEFT).pack(padx=[0,145])
    else:
        Label(frame,text="Future TP test: {}, {}".format(FutureTPTest.matiere,FutureTPTest.date),justify=LEFT).pack(padx=[0,52])

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
    if not(ListeTP == []):
        comptTP = 0
        for i in ListeTP:
            if i.test == '0':
                comptTP += 1
        Points += (1-(comptTP/4))*25
    else:
        NbNonValid += 1
    ListeProjet = loadProjet()
    if not(ListeProjet == []):
        comptProjet = 0
        for i in ListeProjet:
            if i.fait == '0':
                comptProjet += 1
        Points += (1 - comptProjet/6) * 25
    else:
        NbNonValid += 1
    ListeNotes = loadNotes()
    if ListeNotes == []:
        NbNonValid += 1
    else:
        MoyenneG = CalculeMoyenneG(ListeNotes)
        Points += (MoyenneG/20)*25
    ListeDevoir = loadDevoir()
    if ListeDevoir == []:
        NbNonValid += 1
    else:
        n = len(ListeDevoir)
        Points +=  (1 - (n/5))*25
    return [Points,NbNonValid]

###Prénom tamagotcho###

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
    #maj = IntVar()
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
    #Button(fenetre,text="Mise à jour",command=lambda: ActionBouton(fenetre,maj),bg='red').pack(side=LEFT)
    Button(fenetre,text="Ajout Rapide TP",command=lambda: ActionBouton(fenetre,RapideTP)).pack(side=RIGHT)
    Button(fenetre,text="Devoir à faire",command=lambda: ActionBouton(fenetre,devoir)).pack(side=RIGHT)
    Button(fenetre,text="Emplois du temps",command=lambda: ActionBouton(fenetre,edt)).pack(side=RIGHT)
    Button(fenetre,text="Modifier le prénom",command=lambda: ActionBouton(fenetre,ModifP)).pack(side=RIGHT)
    nbValide = 5 - nonV
    coeffHumeur = [0.75*nbValide*25,0.5*nbValide*25,0.25*nbValide*25]
    if pts >= coeffHumeur[0]:
        humeur = "heureux"
        TamaContent(f1,"green")
    elif coeffHumeur[0] > pts >= coeffHumeur[1]:
        humeur = "content"
        TamaContent(f1,"lime")
    elif coeffHumeur[1] > pts >= coeffHumeur[2]:
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
    Button(f3,text="Information TP",command=lambda: ActionBouton(fenetre,tps),padx=26.5).pack(pady=[0,6])
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
    if ModifP.get() == 1:
        PrenomTamagotchi()
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