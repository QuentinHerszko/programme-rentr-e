# -*- coding: latin-1 -*-
from operator import truediv
from matplotlib.colors import ListedColormap
from pylab import savetxt, loadtxt

###Variables générales###
def listMat():
    return ["MA0913","MA0914","SEP0921","SEP0922","MA0934","MA0944","CHPS0703","AN0904","MA0953"]


def loadnotes():
    # récup des données déjà sauvegardées
    mat = []
    notes = []
    coeff = []
    f = open("save.txt", 'r')
    while (1):
        ch = f.readline()
        if ch == '':
            break
        liste = ch.split()
        mat.append(liste[0])
        notes.append(float(liste[1]))
        coeff.append(float(liste[2]))
    f.close()
    return(mat, notes, coeff)

### Tri des données ###
def tridonnee(mat, notes, coeff):
    mattri = []
    notestri = []
    coefftri = []
    Liste = listMat()
    n = len(mat)
    for i in Liste:
        for j in range(n):
            if mat[j] == i:
                mattri.append(mat[j])
                notestri.append(notes[j])
                coefftri.append(coeff[j])
    return(mattri, notestri, coefftri)

### Sauvegarde des données
def savenotes(mat, notes, coeff):
    # enregistrement des nouvelles données
    f = open("save.txt", 'w')
    n = len(mat)
    for i in range(n):
        chaine = format(mat[i], "10s")+format(notes[i], "10.0f")+format(coeff[i], "10.0f")+"\n"
        f.write(chaine)
    f.close()

def matmoy(matiere, mat, notes, coeff):
    notesmoy = []
    coeffmoy = []
    n = len(mat)
    for i in range(n):
        if mat[i] == matiere:
            notesmoy.append(notes[i])
            coeffmoy.append(coeff[i])
    l = len(notesmoy)
    s = 0
    for i in range(l):
        s += (notesmoy[i] / 20) * coeffmoy[i]
    moy = s / sum(coeffmoy) * 20
    return(moy)


### Programme principal ###
if __name__ == "__main__":

    ### Liste des matières ###
    listmat = listMat()
    
    ### Chargement des données ###
    [mat, notes, coeff] = loadnotes()

    ### Interface utilisateur ###
    print("___---===***   NOTES & MOYENNES   ***===---___\n")

    while(1):

        print("Quelle option voulez-vous choisir ?\n")
        print('Ajouter une nouvelle note ? (Taper "Ajout" dans le terminal)')
        print('Regarder les moyennes ? (Taper "Moyennes" dans le terminal)')
        print('Pour quiter, taper "quit" dans le terminal')
        option = input()
        print('\n')

        if option == 'Ajout':
            
            bool = 0

            while bool == 0:
                
                ajmat = input("Matiere : ")

                for i in range(len(listmat)):
                    if ajmat == listmat[i]:
                        bool = 1
            
                if bool == 0:
                    print("Cette matiere n'est pas valide, veulliez recommencer... \n")
            

            ajnotes = -1
            while ajnotes < 0 or ajnotes > 20:
                ajnotes = float(input("Note : "))

                if ajnotes > 20:
                    print("La saisie n'est pas valide : note supérieure à 20.")
                elif ajnotes < 0:
                    print("La saisie n'est pas valide : note inférieure à 0.")

            ajcoeff = -1
            while ajcoeff < 0:
                ajcoeff = float(input("Coefficient : "))

                if ajcoeff < 0:
                    print("La saisie n'est pas valide : coefficient négatif.")

            # enregistrement des données
            mat.append(ajmat)
            notes.append(ajnotes)
            coeff.append(ajcoeff)
            [mat, notes, coeff] = tridonnee(mat, notes, coeff)
            savenotes(mat, notes, coeff)

            print("\n")
            print("Votre note à bien ete ajoutee !\n")

        elif option == 'Moyennes':

            [mat, notes, coeff] = loadnotes()

            print('| Matiere    | Note  | Coeff |')
            print('+------------+-------+-------+')
            n = len(mat)
            for i in range(n):
                print('|  ', mat[i], '  |', notes[i], ' |', coeff[i], ' |')
        
            while(1):
                choix = input("Voulez-vous afficher une moyenne ? ('o' pour oui, 'n' pour non) : ")

                if choix == 'n':
                    print("\n")
                    break
                elif choix == 'o':

                    bool = 0
                    while bool == 0:
                        matiere = input("Afficher la moyenne de quelle matiere ? ")
                        for i in range(len(listmat)):
                            if matiere == listmat[i]:
                                bool = 1

                        if bool == 0:
                            print("Cette matière n'est pas valide, veulliez recommencer... \n")

                    moy = matmoy(matiere, mat, notes, coeff)
                    print("")
                    print("Votre moyenne de ",matiere, "est de", moy, "/ 20 \n")
                else:
                    print("Cette option n'est pas valide, veuillez recommencer... \n")

        elif option == 'quit':
            print("Vous quitter le programme")
            break

        else:
            print("Cette option n'est pas valide, veuillez recommencer... \n")