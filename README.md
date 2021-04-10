# TFJM² problème 3 : C'est pas trop tôt !

Ce repository contient quelques programmes utiles pour le problème 3 du TFJM² 2021

## Générations des données

Le programme C++ `tfjm.cpp` génère des solutions optimales en étudiant toutes les permutations.
Téléchargez le depuis depuis les releases ou compilez le code.

Executez le code avec le nombre de pizza en argument ou entrez le au début du programme.

```shell
gcc tfjm.cpp -lstdc++ -o tfjm
tfjm.exe [n]
```

Cela crée des fichiers dans le dossiers `data`

## Générations des graphes 

### Graphes de positions des pizzas

Utilisez le script `draw.py` pour générer des images png des différents plannings.
Elles sont crées dans le dossier `images/pizzas`.

### Graphes d'évolutions de A en fonction de d'

Utilisez le script `test.py` pour générer des graphes des fonctions A(d').
Elles sont crées dans le dossier `images/graphs`.