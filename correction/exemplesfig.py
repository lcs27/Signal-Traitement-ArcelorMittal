# -*- coding: utf-8 -*-
"""
2019

exemplesfig.py
- énoncé : figure 1, rupture de moyenne

@author: Stéphane Rossignol
"""

# modules de python utilisés dans ce code
# => si nécessaire, ajoutez les dans votre projet "pycharm" courant :
# File->Settings->Projet:(nomproj)->Project Interpreter->pip->(nommodule)->Install Package
import scipy
import math
import numpy as np
import matplotlib.pyplot as plt


# construction du signal simulé, qui contient 2 parties, soit
# une rupture à détecter ; chaque partie contient "points"
# échantillons, répartis selon une gaussienne de moyenne 
# mean(i) et de variance std(i)^2 (de plus, ce bruit est blanc,
# c'est-à-dire que son énergie se répartit sur toutes les
# fréquences)
points=1000

# partie 1
mean1 = 0
std1 = 0.1

# partie 2
mean2 = 3
std2 = 0.1

# construction et concaténation des 2 parties
samples1 = np.random.normal(mean1,std1,size=points)
samples2 = np.random.normal(mean2,std2,size=points)

samples = np.concatenate((samples1,samples2), axis = 0)

# on dessine la figure et on la sauve dans un fichier qu'on
# peut ensuite inclure dans notre énoncée, dans un rapport
# ou dans une présentation (par exemple, celle que vous
# ferez à la fin de la semaine)
plt.figure(1)
plt.plot(samples)
plt.xlabel('time')   # label sur axe abscisses : doit toujours être préesent
plt.ylabel('signal') # label sur axe ordonnées : doit toujours être présent
plt.savefig('images/image1.pdf') # la figure est sauvée AUTOMATIQUEMENT dans
                                 # le fichier pdd nommé "image1.pdf", qui peut
                                 # être inclus dans un rapport, etc.
plt.show()

