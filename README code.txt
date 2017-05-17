Les fonctions à lancer sont: -main  -optimisation  -main_detector

Paramètres de main,optimisation et main_detector:

- xmax=abscisse maximale de la pièce
- ymax=oronnée maximale de la pièce

- facteur_echelle=paramètre diviseur pour ajuster les unités Python avec une longueur réelle en mètres
    ---> par exemple si xmax=ymax=250 et qu'on veut faire correspondre à une pièce de 12x12 m,
         alors facteur_echelle=250/12
    ---> ATTENTION il faut aussi initialiser facteur_echelle dans la fonction __init__ de
         la classe Ray

- txx=abscisse de l'émetteur
- txy=ordonnée de l'émetteur
- cat=chiffre de 1 à 5 permettant de choisir le type d'étage
    ---> cat=1: étage d'une maison
    ---> cat=2: pièce carrée avec 4 murs en briques
    ---> cat=3: mur en béton au milieu d'une pièce carrée (utilisé pour tests)
    ---> cat=4: simple mur en conducteur parfait (utilisé pour tests)
    ---> cat=5: cage de Faraday au milieu du plan. Attention à bien placer l'émetteur dedans
                ou à l'intérieur
    ---> cat=6: 6 murs pour faire des tests (obsolète)
    ---> cat=7: génération d'un mur aléatoire faisant office d'intrus pour la fonction de détection

- a=facteur permettant de diminuer les dimensions de l'étage d'une maison(cat=1),
  par rapport aux dimensions 250x250
    ---> ATTENTION il faut aussi initialiser a dans la fonction __init__ de
         la classe Ray

Paramètres de GUI (interface graphique):
-plot_type: permet de choisir ce qu'on veut afficher
    ---> plot_type=1: affiche tous les rayons (attention, à ne pas utiliser dans
         le cas de plusieurs points récepteurs à cause de la grande quantité de rayons).
    ---> plot_type=2: affiche la sensibilité en dBm
    ---> plot_type=3: affiche le débit binaire en Mb/s
    ---> plot_type=3: affiche 



