# Space_invader

Languille Antoine
Micheli Sébastien 

Répertoire GIT : https://github.com/MaximilianTyan/Space_invader

Emplacement d'une liste : Alien.py line 13
Emplacement d'une pile : Spaceship.py line 10 
Emplacement d'une file : Alien.py line 186


Lancement du jeu, exécuter le programme main.py et le jeu se lancera. Une fois la partie terminée, le bouton NEW GAME permet de relancer une partie, sinon le bouton QUITTER permet de fermer la fenêtre


Règles du jeu : notre jeu reprend les règles  du jeu Space Invaders avec un thème plus actuel...
Votre vaisseau antivirus doit empêcher différentes personnalités de répendre le virus qui se propage sur notre Terre. Tirez des seringues contenant le vaccin afin de les "guérir" et d'arrêter l'épidémie. Vous remportez la partie et sauvez l'humanité lorsque tout le monde a été vacciné. 

Utilisez les flèches de gauche et de droite pour déplacer votre vaisseau. 
La barre espace vous permet de tirer. 
Les ennemis se déplacent de gauche à droite jusqu'au bord de l'écran, décende d'un cran, se déplace de droite à gauche vers l'autre côté de l'écran, décendent de nouveau, et répètent ces actions. 
Les ennemis vous tirent dessus de manière aléatoire, se prendre un tir vous retire une vie.
Si vous n'avez plus de vie ou que les ennemis arrivent en bas de l'écran, vous avez perdu. 


Problème éventuel : dans Window.py, la bibliothèque PIL est utilisée. Elle n'est pas forcément reconnue sur Visual Studio Code (la bibliothèque est reconnue sur l'ordinateur d'Antoine mais pas sur celui de Sébastien). Si ce problème arrive lors du lancement du programme principal, essayez de le lancer avec Spider, il ne devrait pas y avoir de problème. 