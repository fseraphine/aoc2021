# Jour 1

Après avoir fait des versions simples, en utilisant des boucles classiques (for, while), j'ai tenté d'utiliser un peu plus _itertools_ et _more_itertools_ qui sont des outils magiques pour résoudre les puzzles de l'Avent Of Code. Dans ce cas, _windowed_ m'a permis de générer les triplets pour les moyennes glissantes.

J'ai aussi découvert qu'un fichier était un _iterable_, ce qui en facilite la lecture et permet de le consommer au fur et à mesure. Reste à trouver une façon élégante de convertir les chaines de caractères lues du fichier en entier.
Pour l'instant j'utilise un map(int,fichier) pour convertir chaque élément en entier. Il faudra que je regarde si le Map Object retourné par map construit une liste en mémoire ou pas.

D'ailleurs j'ai ajouté des mesures de temps d'exécution grace à _time_ et une mesure de la mémoire utilisée grace à _malloc_. L'éxécution est plus rapide dans la version _more_itertools_ et consomme nettement moins de mémoire que la version de base.

    Version un peu améliorée avec windowed    : mémoire max 170963 et exécution 0.026999
    Version fonctionnelle avec des map et sum : mémoire max  40080 et exécution 0.017275
