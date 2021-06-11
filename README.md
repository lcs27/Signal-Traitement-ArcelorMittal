# cours-EI-ST4GSI
Ce dossier contient les codes d'EI - Industrial Challenge ArcelorMittal - ST4GSI à *CentraleSupélec* pour le groupe 2: Chensheng Luo, Gabriel Martin, Yue Wang

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
[separation.py](separation.py), [utils.py](utils.py),  [write_data.py](write_data.py)
- Manipulation     
[signaux_reel.py](signaux_reel.py): Manipulation sur les signaux réels, qui comprend tous les 4 étapes.
## Fichiers de support et données
### Code de support
[draw_data.py](draw_data.py): Visualisation de résultat   
### Support de Github Action
Comme de nombreux calculs sont demandés, Github Action est utilisée par nous pour effectuer certains tests.   
[GithubActionFile.py](GithubActionFile.py): Script soumettre à Github Action pour le calcul     
[./.github/workflows](./.github/workflows): Script sert à la communication avec Github Action
[requirement.txt](requirement.txt): Environnement demandé
### Dossier de support
#### data
Ce dossier contient des données réelles d'ArcelorMittal. Il y a 84 capteurs au total, dont chacun contient 96019 données.   
[fichier_mesures.txt](./data/fichier_mesures.txt) contient les données brutes de toutes les capteurs  
[fichier_mesures_variable_N.txt](./data/fichier_mesures_variable_0.txt) contient les données brutes du N<sup>e</sup> capteur   
[fichier_mesures_variable_N_echan.txt](./data/fichier_mesures_variable_0_echan.txt) contient les données échantillonnées du N<sup>e</sup> capteur, avec la fréquence d'échantillonage = 100   
[ecart_N_echan.txt](./data/ecart_0_echan.txt) contient les écarts entre les consignes et les mesures échantillonnées de la N<sup>e</sup> variable   
#### correction
[correction](./correction): Ce dossier contient une partie du corrigé des questions de l'énoncé  
#### fichiers
[fichiers](./fichiers): Ce dossier contient des fichiers audio utilisés dans les tests sur les effets de l'échentillonage au son  
#### image
[image](./image): Ce dossier contient toutes les images pour la visualisation de données et de résultats de détection  
#### result
[result](./result): Ce dossier contient des fichiers qui enregistrent les paramètres choisis et les résultats de détection correspondants

