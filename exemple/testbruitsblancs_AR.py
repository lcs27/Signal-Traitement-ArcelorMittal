# -*- coding: utf-8 -*-
"""
2019

testbruitsblancs_AR.py
- énoncé : table 3

@author: Stéphane Rossignol
"""

import scipy
import math
import numpy as np
import matplotlib.pyplot as plt
import nitime    # pour la méthode 1
import audiolazy # pour la méthode 2


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

plt.figure(1)
plt.plot(samples)
plt.xlabel('time')
plt.ylabel('signal')
plt.savefig('images/2transitionsar.pdf')
#plt.show()


### on analyse le signal

lll=100; ### taille des fenêtres d'analyse
meth=2;  ### méthode pour le calcul des coefficients AR

temps=[]
brandt=[]
for k in range(1,len(samples)-2*lll-1):
    temps.append(k+lll)

    fen1=samples[k:k+2*lll];  # ATTENTION : le dernier élément du tableau
                              # n'est pas inclus
    fen1=fen1-np.mean(fen1)
    fen2=samples[k:k+lll]
    fen2=fen2-np.mean(fen2)
    fen3=samples[k+lll:k+2*lll];
    fen3=fen3-np.mean(fen3)

    if meth==1:
       ### méthode 1 -- rapide, mais ne donne pas les coefficients de réflexion,
       ###    qui sont nécessaires pour le traitement de la parole
       [ak1, sig_sq1] = nitime.algorithms.autoregressive.AR_est_LD(fen1, 2, rxx=None)
       [ak2, sig_sq2] = nitime.algorithms.autoregressive.AR_est_LD(fen2, 2, rxx=None)
       [ak3, sig_sq3] = nitime.algorithms.autoregressive.AR_est_LD(fen3, 2, rxx=None)

    if meth==2:
       ### méthode 2 -- lente,  mais donne aussi les coefficients de réflexion,
       ###    qui sont nécessaires pour le traitement de la parole
       acdata1 = audiolazy.acorr(fen1)
       acdata2 = audiolazy.acorr(fen2)
       acdata3 = audiolazy.acorr(fen3)
       ldfilt1 = audiolazy.levinson_durbin(acdata1, 2)
       ldfilt2 = audiolazy.levinson_durbin(acdata2, 2)
       ldfilt3 = audiolazy.levinson_durbin(acdata3, 2)
       sig_sq1=ldfilt1.error/len(fen1)
       sig_sq2=ldfilt2.error/len(fen2)
       sig_sq3=ldfilt3.error/len(fen3)

    ### calcul de la distance de Brandt
    ## version1
    v1 = math.log(math.sqrt(sig_sq1))
    v2 = math.log(math.sqrt(sig_sq2))
    v3 = math.log(math.sqrt(sig_sq3))
    val = math.fabs ( (2*lll)*v1 - lll*v2 - lll*v3 )

    ## version2
    #v1 = math.log(sig_sq1)
    #v2 = math.log(sig_sq2)
    #v3 = math.log(sig_sq3)
    #val = math.fabs ( (2*lll)*v1 - lll*v2 - lll*v3 )

    brandt.append(val)

print(len(brandt))

plt.figure(2)
plt.plot(temps, brandt)
plt.xlabel('time')
plt.ylabel('caracteristique')
plt.savefig('images/brandt.pdf')
plt.show()

