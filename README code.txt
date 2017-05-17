Les fonctions � lancer sont: -main  -optimisation  -main_detector

Param�tres de main,optimisation et main_detector:

- xmax=abscisse maximale de la pi�ce
- ymax=oronn�e maximale de la pi�ce

- facteur_echelle=param�tre diviseur pour ajuster les unit�s Python avec une longueur r�elle en m�tres
    ---> par exemple si xmax=ymax=250 et qu'on veut faire correspondre � une pi�ce de 12x12 m,
         alors facteur_echelle=250/12
    ---> ATTENTION il faut aussi initialiser facteur_echelle dans la fonction __init__ de
         la classe Ray

- txx=abscisse de l'�metteur
- txy=ordonn�e de l'�metteur
- cat=chiffre de 1 � 5 permettant de choisir le type d'�tage
    ---> cat=1: �tage d'une maison
    ---> cat=2: pi�ce carr�e avec 4 murs en briques
    ---> cat=3: mur en b�ton au milieu d'une pi�ce carr�e (utilis� pour tests)
    ---> cat=4: simple mur en conducteur parfait (utilis� pour tests)
    ---> cat=5: cage de Faraday au milieu du plan. Attention � bien placer l'�metteur dedans
                ou � l'int�rieur
    ---> cat=6: 6 murs pour faire des tests (obsol�te)
    ---> cat=7: g�n�ration d'un mur al�atoire faisant office d'intrus pour la fonction de d�tection

- a=facteur permettant de diminuer les dimensions de l'�tage d'une maison(cat=1),
  par rapport aux dimensions 250x250
    ---> ATTENTION il faut aussi initialiser a dans la fonction __init__ de
         la classe Ray

Param�tres de GUI (interface graphique):
-plot_type: permet de choisir ce qu'on veut afficher
    ---> plot_type=1: affiche tous les rayons (attention, � ne pas utiliser dans
         le cas de plusieurs points r�cepteurs � cause de la grande quantit� de rayons).
    ---> plot_type=2: affiche la sensibilit� en dBm
    ---> plot_type=3: affiche le d�bit binaire en Mb/s
    ---> plot_type=3: affiche 



