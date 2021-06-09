# -*- coding: utf-8 -*-
"""
2019

testbruitsblancs_moyenne_statistiques.py

@author: Stéphane Rossignol
"""

import scipy
import math
import numpy as np
import matplotlib.pyplot as plt

# construction du signal simulé, qui contient 3 parties, soit 2 transitions
# à détecter ; chaque partie contient "points" échantillons, répartis
# selon une gaussienne de moyenne mean(i) et de variance std(i)^2
points = 1000

# partie 1
mean1 = 0
std1 = 0.5

# partie 2
mean2 = 3
std2 = std1

# partie 3
mean3 = 0
std3 = std1


nn = 10  # erreur max acceptée sur la position des ruptures trouvées
bonnesdetections = 0
faussesalarmes = 0
detectionsmanquees = 0

result = []
for ll in range(1, 101):  # boucle sur le nombre d'essais
    rupttheorique = [1000]
    rupttheorique.append(2000)  # position des ruptures simulées
    alli = [0]
    alli.append(0)

    # construction et concaténation des 3 parties du signal
    samples1 = np.random.normal(mean1, std1, size=points)
    samples2 = np.random.normal(mean2, std2, size=points)
    samples3 = np.random.normal(mean3, std3, size=points)

    samples = np.concatenate((samples1, samples2, samples3), axis=0)

#   plt.plot(samples)
#   plt.show()

    # on analyse le signal

    lll = 100  # taille des fenêtres d'analyse

    temps = []
    diffmean = []
    for k in range(1, len(samples)-2*lll-1):
        temps.append(k+lll)

        fen2 = samples[k:k+lll]  # ATTENTION : le dernier élément du tableau
        # n'est pas inclus
        fen3 = samples[k+lll:k+2*lll]

        fit2 = np.mean(fen2)
        fit3 = np.mean(fen3)

        # calcul de la distance
        val = math.fabs(fit2 - fit3)
        diffmean.append(val)

    # on seuille la caractéristique
    diffmeantri = sorted(diffmean)
    shortdiffmean = diffmeantri[0:int(0.9*len(diffmeantri))]
    sigma = np.std(shortdiffmean)
    # ici, on prend la règle des 3 sigmas,
    seuil = 3*sigma+np.mean(shortdiffmean)
    # ce qui n'est sans doute pas optimal

    ppp = []
    sss = []
    ppp.append(temps[0])
    ppp.append(temps[len(temps)-1])
    sss.append(seuil)
    sss.append(seuil)

    ruptures = []
    for i in range(1, len(diffmean)-1):
        if ((diffmean[i] > diffmean[i-1] and diffmean[i] >= diffmean[i+1]) or
                (diffmean[i] >= diffmean[i-1] and diffmean[i] > diffmean[i+1])) and \
                diffmean[i] >= seuil:
            ruptures.append(temps[i])
            rrr = []
            vvv = []
            rrr.append(temps[i])
            rrr.append(temps[i])
            vvv.append(0)
            vvv.append(max(diffmean))
#         plt.plot(rrr,vvv)

    print(len(ruptures))
    print(ruptures, rupttheorique)

    # on teste la validité des ruptures trouvées
    for j in range(0, len(ruptures)):
        allocation = 0      # l'allocation de la rupture trouvée à une rupture
        # théorique n'est pas faite
        for i in range(0, len(rupttheorique)):
            distance = math.fabs(rupttheorique[i]-ruptures[j])

            # si la rupture trouvée a déjà été allouée à une rupture
            # théorique, ce n'est plus à faire
            if distance <= nn and allocation == 0 and alli[i] == 0:
                bonnesdetections = bonnesdetections+1
                allocation = 1  # l'allocation de la rupture trouvée à une rupture
                # théorique est faite
                alli[i] = 1    # l'allocation à une rupture théorique est faite
        if allocation == 0:
            faussesalarmes = faussesalarmes+1
    for i in range(0, len(rupttheorique)):
        if alli[i] == 0:
            detectionsmanquees = detectionsmanquees+1
    result.append(
        np.array([bonnesdetections, faussesalarmes, detectionsmanquees]))

    print(bonnesdetections, faussesalarmes, detectionsmanquees)
np.savetxt("./images/moyenne1.txt", result)
#   plt.plot(temps,diffmean)
#   plt.plot(ppp,sss)
#   plt.show()
