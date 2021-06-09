# -*- coding: utf-8 -*-
"""
2019

exemples2fig.py
- énoncé : figures 2 et 3, rupture de pente et rupture intermittente

@author: Stéphane Rossignol
"""

import scipy
import math
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import time


# construction du signal simulé -- pente
points=1000

# partie 1
mean1 = 0
std1  = 0.1
pente1= 0

# partie 2
mean2 = mean1
std2  = std1
pente2= 0.005

# construction et concaténation des 2 parties
samples1 = np.random.normal(mean1,std1,size=points) + pente1*np.arange(points)
samples2 = np.random.normal(mean2,std2,size=points) + pente2*np.arange(points)

samples = np.concatenate((samples1,samples2), axis = 0)

# on dessine la figure et on la sauve dans un fichier qu'on
# peut ensuite inclure dans notre énoncé
plt.figure(1)
#plt.ion()
plt.plot(samples)
plt.xlabel('time')
plt.ylabel('signal')
plt.savefig('images/image2.pdf')
plt.show()


# construction du signal simulé -- intermittent
points=1000

# partie 1
mean1 = 0
std1  = 0.1
pente1= 0

# partie 2
mean2 = 3
std2  = std1

# construction et concaténation des diverses parties du signal
samples1 = np.random.normal(mean1,std1,size=points)
samples  = samples1
for ii in range(1,10):
  points1=rd.randint(15,150)
  points2=rd.randint(15,150)
  samples1 = np.random.normal(mean1,std1,size=points1)
  samples2 = np.random.normal(mean2,std2,size=points2)
  samples = np.concatenate((samples,samples1,samples2), axis = 0)

# on dessine la figure et on la sauve dans un fichier qu'on
# peut ensuite inclure dans notre énoncé
plt.figure(2)
#plt.ion()
plt.plot(samples)
plt.xlabel('time')
plt.ylabel('signal')
plt.savefig('images/image3.pdf')
plt.show()


#time.sleep(15)
#plt.figure(1)
#plt.close()
#plt.figure(2)
#plt.close()

