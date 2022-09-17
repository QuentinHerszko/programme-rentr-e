# Programme de rentrée

Ce programme python vous permettra de rester organiser lors de votre année. On peut y renseigner nos DS, nos fiches à faire, nos TP, etc...
Le but est d'avoir une liste résumant tout ce que vous avez à faire pour rester à jour dans vos leçons et être sûr de ne pas être au retard.

__Principe__ : Vos devoirs sont liés à un tamagotchi. Celui-ci est plus ou moins content en fonction de la charge de travail que vous avez à faire.
Plus vous avez de travail, plus le tamagotchi sera triste, moins vous en avez, plus il sera heureux ! Le but du jeu est de le maintenir le plus joyeux que possible.

## Récupération du programme

__Prérequis__ : Avoir une clé SSH et avoir installer pyinstaller avec `pip install pyinstaller`

* Créer un dossier sur votre ordinateur où vous voulez mettre le programme.
* Dans ce dossier, exécuter via un terminal sous bash : `git clone git@github.com:QuentinHerszko/programme-rentr-e.git`
* Puis rentrer dans le dossier : `cd programme-rentr-e`
* Ensuite, créer l'exécutable en tapant : `pyinstaller --onefile main.py`
* Déplacer l'exécutable `main` dans le dossier `programme-rentr-e` (`mv -f dist/main .`)

Et voilà, vous pouvez maintenant lancer le programme en cliquant sur l'exécutable `main`.

## Raccourcis par le terminal

Vous pouvez directement accéder et mettre à jour le programme en créant des alias:

* Faire le raccourcis :
  `* Ouvrir le fichier .bashrc : `sudo nano .bashrc` `
  `* Ajouter l'alias suivant : `alias NomAlias='cd TonChemin ; ./main'` où le chemin correspond au chemin où se trouve l'executable `main` `

* Faire les mises à jours :
  `* Ouvrir le fichier .bashrc : `sudo nano .bashrc` `
  `* Ajouter l'alias suivant : `alias NomAlias='cd TonChemin ; git pull ; rm main ; pyinstaller --onefile main.py ; mv -f dist/main . ; rm -rf dist ; rm -rf build ; ./main'` où le chemin correspond au chemin où se trouve l'executable `main` `