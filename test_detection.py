from detection import *
from signal_simule import *
from math import *
import numpy as np

def apprentissage_seuil(x_detect,pourcentage=0.9,multiple=1):
    n = len(x_detect)
    k = int(pourcentage*n)
    sigma = (np.partition(x_detect,k-1))[k-1]
    return sigma*multiple

def detection_variation(x_moyenne_time,x_moyenne_valeur,seuil, validation_tolerance=21):
    changement = []
    for t in range(len(x_moyenne_time)):
        if (x_moyenne_valeur[t]>seuil) and \
            (t > 0 and t < len(x_moyenne_time)-1) and \
            ((x_moyenne_valeur[t] >= x_moyenne_valeur[t-1] and x_moyenne_valeur[t] > x_moyenne_valeur[t+1]) or \
            (x_moyenne_valeur[t] > x_moyenne_valeur[t-1] and x_moyenne_valeur[t] >= x_moyenne_valeur[t+1])):
                if  (len(changement) == 0 ) or (len(changement) != 0 and x_moyenne_time[t]-changement[-1] >validation_tolerance):
                    changement.append(x_moyenne_time[t])

    return changement

def comptage_resultat(changement_detecte,changement_reel,tolerance=10):
    #resultat = [nombre de bonnes détections, nombre de fausses alarmes, nombre de détections manquées]
    n, m = len(changement_detecte), len(changement_reel)
    resultat = [0,0,0]
    j, i = 0, 0
    
    while i + j < (n + m-1):
        #print(i,j)
        if changement_detecte[i] - tolerance <= changement_reel[j] <= changement_detecte[i] + tolerance:
            resultat[0] += 1
            i +=1
            j += 1
            if i == n:
                resultat[2] += m-j
                return resultat
            if j == m:
                resultat[1] += n-i
                return resultat
        elif changement_detecte[i] < changement_reel[j] - tolerance:
            resultat[1] += 1
            i +=1
            if i == n:
                resultat[2] += m-j
                return resultat
        else :
            resultat[2] += 1
            j += 1
            if j == m:
                resultat[1] += n-i
                return resultat
    return resultat


def test_detection(pourcentage,std,w=100,tolerance=10,nombre=100):
    result = np.array([0,0,0])
    for _ in range(nombre):
        signal,changement = simulation_rupture_moyenne_3(std1=std,std2=std,std3=std)
        x_time = np.arange(0,len(signal))
        x_detect_time,x_detect = detection_moyenne(x_time,signal,w=w)
        seuil = apprentissage_seuil(x_detect,pourcentage=pourcentage)
        changement_detecte = detection_variation(x_detect_time,x_detect,seuil,validation_tolerance=2*tolerance)
        result += np.array(comptage_resultat(changement_detecte,changement,tolerance))
    return result

if __name__=="__main__":
    results = []
    conditions = []
    for pourcentage in [0.7,0.8,0.9]:
        for std in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6]:
            for w in [50,100,200]:
                for tolerance in [10,15,20]:
                    result = test_detection(pourcentage,std,w=w,tolerance=tolerance)
                    print([pourcentage,std,w,tolerance],result)
                    conditions.append([pourcentage,std,w,tolerance])
                    results.append(result)
    print(results)
    print(conditions)
    np.savetxt("./result/conditions.txt",conditions)
    np.savetxt("./result/results.txt",results)

    #print(test_detection(0.9,0.1))
    #print(test_detection(0.9,1.5))
    #changement_detect = [945,1001,2004,2015,2030]
    #changement_reel = [1000,1500,2000]
    #print(comptage_resultat(changement_detect,changement_reel))