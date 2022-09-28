# Programme de rentrée

Le but de ce programme est simple, il est de rendre son tamagotchi heureux! Pour cela, il faut bien travailler car son humeur dépend de la charge de travail qu'il reste à effectuer.
Le programme ne marche que pour __Linux__.

## Sous-programmes

Le programme principal est diviser en plusieur script et ne peut pas marcher sans:
* `FicheRev.py`
* `InfoDS.py`
* `InfoProjet.py`
* `InfoTP.py`
* `Moyenne_Gen.py`
Chaque sous programme peut marcher indépendamment des autres sauf `FicheRev.py` et `InfoDs.py` qui marchent ensemble. Cela est pratique si vous voulez qu'une seule fonctionnalité du programme.

## Humeur du tamagotchi

L'humeur du tamagotchi dépend des critères suivant :
Le nombre de fiche de révision à faire
* Le nombre de TP à faire
* Le nombre de projet à faire
* Le nombre de devoir à faire
* La moyenne générale

## Création de l'application

Créer l'application permet de l'avoir dans la liste des applications disponibles. De plus cela permet de pouvoir la mettre en favori pour qu'elle puisse apparaître dans la barre des tâches. Voici la commande:
    ```sudo python3 MaJ.py app```
Attention! Il faut déjà avoir choisi un nom pour votre tamagotchi car il va vous être demandé.

## Faire une mise à jour

Pour faire une mise à jour, il faut simplement lancer le programme python MaJ.py comme ceci:
    ```python3 Maj.py```
Cela va mettre à jour à partir du git puis, le programme recrée l’exécutable.