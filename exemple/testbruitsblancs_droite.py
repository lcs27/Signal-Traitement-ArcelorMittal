# -*- coding: utf-8 -*-
"""
2019

testbruitsblancs_droite.py
- énoncé : table 2

@author: Stéphane Rossignol
"""

import scipy
import math
import numpy as np
import matplotlib.pyplot as plt


### construction du signal simulé, qui contient 3 parties, soit 2 transitions
### à détecter ; chaque partie contient "points" échantillons, répartis
### selon une gaussienne de moyenne mean(i) et de variance std(i)^2
points=1000

# partie 1
mean1 = 0
std1 = 0.1

# partie 2
mean2 = 3
std2 = 0.1

# partie 3
mean3 = 0
std3 = 0.1

# construction et concaténation des 3 parties
samples1 = np.random.normal(mean1,std1,size=points)
samples2 = np.random.normal(mean2,std2,size=points)
samples3 = np.random.normal(mean3,std3,size=points)

samples = np.concatenate((samples1,samples2,samples3), axis = 0)

plt.plot(samples)
plt.xlabel('time')
plt.ylabel('signal')
plt.savefig('images/2transitionsdroite.pdf')
plt.show()


### on analyse le signal

lll=100; ### taille des fenêtres d'analyse

temps=[]
pente=[]
for k in range(1,len(samples)-2*lll-1):
    temps.append(k+lll)

    fen2=samples[k:k+lll]  # ATTENTION : le dernier élément du tableau n'est
                           # pas inclus
    fen2=fen2-np.mean(fen2)
    fen3=samples[k+lll:k+2*lll];
    fen3=fen3-np.mean(fen3)

    fit2 = np.polyfit(np.arange(lll), fen2, 1)
    fit3 = np.polyfit(np.arange(lll), fen3, 1)
    

    ### calcul de la distance ; attention : "highest power first"
    val = math.fabs(fit2[0] - fit3[0])   ### pente
#    val = math.fabs(fit2[1] - fit3[1])   ### coordonnée à l'origine
    pente.append(val)

plt.plot(temps,pente)
plt.xlabel('time')
plt.ylabel('caracteristique')
plt.savefig('images/diffdroite.pdf')
plt.show()

