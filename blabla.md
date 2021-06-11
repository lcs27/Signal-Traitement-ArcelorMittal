
## Flux principal de travail
### Analyse sur les signaux simulés
- Signal simulé  
[signal_simule.py](signal_simule.py): Génération de signal simulé qui sert à test ci-après
- Calcul de caractéristique      
[moyenne_mobile.py](moyenne_mobile.py): Calcul de moyenne mobile ainsi que une bande d'interval de confiance    
[detection.py](detection.py): Calcul de caractéristique pour le modélisation par la moyenne, modélisation linéaire et modélisation AR   
- Prise de décision
[test_detection.py](test_detection.py): Calcul de seuil et faire sortir les moments de rupture détectés, plusieurs fonction de test sont aussi mise à disposition.   
- Vote majoritaire
[multisignal.py](multisignal.py): Vote majoritaire ainsi que les fonctions de support, les fonction d'érosion (appelé ```lissage``` dans le fichier)   
- Prediction
[prediction.py](prediction.py): Prédiction avec apprentissage de seuil en temps réel   
### Analyse de sous-échantillonnage
[genere_son.py](genere_son.py): Génération de son pour l'analyse   
[echantillonnage.py](echantillonnage.py): Fonction d'échantillonnage   
### Analyse sur les signaux réels
- Lecture, visualisation et sépration de données
[separation.py](separation.py) [utils.py](utils.py) [write_data.py](write_data.py)
- Manipulation 
[signaux_reel.py](signaux_reel.py): Manipulation sur les signaux réels, qui comprend tous les 4 étapes.
## Fichiers de support et données
### Code de support
[draw_data.py](draw_data.py): Visualisation de résultat   
### Support de Github Action
Comme de nombreux calculs sont demandés, Github Action est utilisée par nous pour effectuer certains tests.
[GithubActionFile.py](GithubActionFile.py): Script soumettre à Github Action pour    




