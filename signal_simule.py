from numpy.lib.polynomial import _polyint_dispatcher
import numpy as np
import matplotlib.pyplot as plt

def simulation_rupture_moyenne(points=1000,mean1=0,mean2=3,std1=0.1,std2=0.1):
    # construction et connexion de deux parties
    samples1 = np.random.normal(mean1 , std1 , size=points )
    samples2 = np.random.normal(mean2 , std2 , size=points )
    samples = np.concatenate((samples1,samples2),axis=0)
    return samples

def simulation_rupture_pente(points=1000,debut=0,pente1=0,pente2=0.005,std1=0.1,std2=0.1):
    # construction et connexion de deux parties
    vTime = np.arange(0, points, 1, dtype=int)
    samples1 = debut + vTime*pente1
    samples2 = samples1[-1] + vTime*pente2
    bruit = np.random.normal(0, std1, size=2*points)
    samples = np.concatenate((samples1,samples2),axis=0)+bruit
    return samples

def simulation_rupture_intermittente(points=1000,mean1=0,mean2=3,std=0.1):
    # construction et connexion de deux parties
    samples = np.random.normal(mean1 , std , size=points)
    sum = 0
    valeur = mean1
    total = mean1+mean2
    while sum<points:
        longueur = np.random.randint(15,high=250)
        valeur = total - valeur
        samples_add = np.random.normal(valeur , std , size=min(longueur,points-sum))
        sum += longueur
        samples = np.concatenate((samples,samples_add),axis=0)
    return samples

def plot_signal(samples,nom):
    plt.figure(1)
    plt.plot(samples)
    plt.xlabel('time')
    plt.ylabel('signal')
    plt.savefig(nom)
    plt.show()

if __name__=="__main__":
    samples = simulation_rupture_intermittente()
    plot_signal(samples,'image/simule3.png')
