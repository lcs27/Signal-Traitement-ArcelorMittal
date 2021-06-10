# -*- coding: utf-8 -*-
"""
2019

testbruitsblancs_moyenne.py

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
plt.savefig('images/2transitions.pdf')
plt.show()


### on analyse le signal

lll=100; ### taille des fenêtres d'analyse

temps=[]
diffmean=[]
for k in range(1,len(samples)-2*lll-1):
    temps.append(k+lll)

    fen2=samples[k:k+lll]  # ATTENTION : le dernier élément du tableau n'est
                           # pas inclus
    fen3=samples[k+lll:k+2*lll];

    fit2 = np.mean(fen2)
    fit3 = np.mean(fen3)
    

    ### calcul de la distance
    val = math.fabs(fit2 - fit3)
    diffmean.append(val)

plt.plot(temps,diffmean)
plt.xlabel('time')
plt.ylabel('caracteristique')
plt.savefig('images/diffmoy.pdf')
plt.show()

