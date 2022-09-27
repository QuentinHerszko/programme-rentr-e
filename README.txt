Le but de ce programme est simple, il est de rendre son tamagotchi heureux! Pour cela, il faut bien travailler car son humeur dépend de la chage de travail qu'il reste à effectuer.
Le programme ne marche que pour Linux.

Sous-programmes:

Le programme principal est diviser en plusieur script et ne peut pas marcher sans:
    - FicheRev.py
    - InfoDS.py
    - InfoProjet.py
    - infoTP.py
    - Moyenne_Gen.py
Chaque sous programme peut marcher indépendament des autres sauf FicheRev et InfoDs qui marchent ensemble. Cela est pratique si vous voulez qu'une seule fonctionnalité du programme.

Humeur du tamagotchi:

L'humeur du tamagotchi dépend des critères suivant
    - Le nombre de fiche de révision à faire
    - Le nombre de TP à faire
    - Le nombre de projet à faire
    - Le nombre de devoir à faire
    - La moyenne générale

Création de l'application:

Créer l'application permet de l'avoir dans la liste des application disponible. De plus cela permet de pouvoir la mettre en favorie pour qu'elle puissent apparaitre dans la barre des tâches. Voici la commande:
    sudo python3 MaJ.py app
Attention! Il faut avoir déjà choisie un nom pour votre tamagotchi car il va vous être demandé.

Faire une mise à jour:

Pour faire une mise à jour, il faut simplement lancer le programme python MaJ.py comme ceci:
    python3 Maj.py
Cela va mettre à jour à partir du git puis, le programme recrée l'executable.