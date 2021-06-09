# -*- coding: utf-8 -*-
"""
2019

testpentes_droite.py

@author: Stéphane Rossignol
"""


import scipy
import math
import numpy as np
import matplotlib.pyplot as plt



### construction du signal simulé, qui contient 2 parties, soit 1 transition
### à détecter ; chaque partie contient "points" échantillons, répartis
### selon une gaussienne de moyenne mean et de variance std^2 ; la pente de la
### 1ère partie est nulle, pas celle de la seconde
points=1000

# partie 1
mean1 = 0
std1  = 0.1
pente1= 0

# partie 2
mean2 = mean1
std2  = std1
pente2= 0.005

# construction et concaténation des 3 parties
samples1 = np.random.normal(mean1,std1,size=points) + pente1*np.arange(points)
samples2 = np.random.normal(mean2,std2,size=points) + pente2*np.arange(points)

samples = np.concatenate((samples1,samples2), axis = 0)

plt.plot(samples)
plt.show()


### on analyse le signal

lll=100; ### taille des fenêtres d'analyse

pente=[]
for k in range(1,len(samples)-2*lll-1):
    fen2=samples[k:k+lll]
    fen2=fen2-np.mean(fen2)
    fen3=samples[k+lll:k+2*lll];
    fen3=fen3-np.mean(fen3)

    fit2 = np.polyfit(np.arange(lll), fen2, 1)
    fit3 = np.polyfit(np.arange(lll), fen3, 1)
    

    ### calcul de la distance
    val = math.fabs(fit2[0] - fit3[0])
    pente.append(val)

plt.plot(pente)
plt.show()

