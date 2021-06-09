from numpy.lib.type_check import _nan_to_num_dispatcher
from signal_simule import *
from detection import *
from test_detection import *
import copy

def detect2changement(x_detect,x_detect_time):
    x_detect = np.array(x_detect) * np.array(x_detect_time)
    changement=[]
    a = []
    for i in x_detect:
        if i == 0:
            if len(a) != 0:
                d = copy.deepcopy(a)
                changement.append(d)
                a = []
        else:
            a.append(i)
    if len(a) != 0:
        changement.append(a)

    result = []
    for i in changement:
        result.append(i[int(len(i)/2)])
    return result
    

def vote_majoritaire_moyenne(signaux,x_time,mode=1,w=100,pourcentage = 0.9,tolerance = 10):
    m = len(signaux)
    if mode == 1:
        v = m
    elif mode == 2:
        v = m - 1
    elif mode == 3:
        v = int(m/2) + 1
    else:
        print('Mode indéfini')
        return None
    x_pass = []
    for signal in signaux:
        x_detect_time,x_detect = detection_moyenne(x_time,signal,w=w)
        seuil = apprentissage_seuil(x_detect,pourcentage= pourcentage)
        x_pass.append(test_pass_seuil(x_detect,seuil))
    x_pass = np.sum(x_pass,axis=0)
    x_detect = test_pass_seuil(x_pass, v)
    if tolerance != 0:
        x_detect= detect_lissage(x_detect,tolerance = tolerance)
    changement_detect = detect2changement(x_detect,x_detect_time)
    return changement_detect

def vote_majoritaire_coupture(signaux,x_time,mode=1,w=100,pourcentage = 0.9,tolerance = 10):
    m = len(signaux)
    if mode == 1:
        v = m
    elif mode == 2:
        v = m - 1
    elif mode == 3:
        v = int(m/2) + 1
    else:
        print('Mode indéfini')
        return None
    x_pass = []
    for signal in signaux:
        x_detect_time,x_detect = detection_coupture(x_time,signal,w=w)
        seuil = apprentissage_seuil(x_detect,pourcentage= pourcentage)
        x_pass.append(test_pass_seuil(x_detect,seuil))
    x_pass = np.sum(x_pass,axis=0)
    x_detect = test_pass_seuil(x_pass, v)
    if tolerance != 0:
        x_detect= detect_lissage(x_detect,tolerance = tolerance)
    changement_detect = detect2changement(x_detect,x_detect_time)
    return changement_detect

def detect_lissage(x_detect,tolerance=10):
    x_lissage = np.ones_like(x_detect)
    n = len(x_detect)
    for i in range(n):
        if x_detect[i] == 0:
            bande_basse = max(0,i-tolerance)
            bande_haute = min(i+tolerance+1,n)
            x_lissage[bande_basse:bande_haute] = 0
    return x_lissage
'''
def lissage(changement,tolerance=10):
    result = []
    precedent = changement[0]
    for i in changement:
        if abs(i-precedent)<=tolerance:
            precedent = (precedent + i)/2
        else:
            result.append(precedent)
            precedent = i
    result.append(precedent)
'''

def test_multivote_moyenne(std,mode=1,nombre=100):
    result = np.array([0,0,0])
    for _ in range(nombre):
        signal1,changement = simulation_rupture_moyenne_3(mean2=3,std1=std,std2=std,std3=std)
        signal2,_ = simulation_rupture_moyenne_3(mean2=4,std1=std,std2=std,std3=std)
        signal3,_ = simulation_rupture_moyenne_3(mean2=5,std1=std,std2=std,std3=std)
        signal4,_ = simulation_rupture_moyenne_3(mean2=3.5,std1=std,std2=std,std3=std)
        signal5,_ = simulation_rupture_moyenne_3(mean2=4.5,std1=std,std2=std,std3=std)
        signaux = [signal1,signal2,signal3,signal4,signal5]
        x_time = np.arange(0,len(signal1))

        changement_detect = vote_majoritaire_moyenne(signaux,x_time,mode = mode,w = 100,pourcentage=0.7,tolerance=5)

        result += np.array(comptage_resultat(changement_detect,changement))
    return result


def test_multivote_coupture(std,mode=1,nombre=100):
    result = np.array([0,0,0])
    for _ in range(nombre):
        signal1,changement = simulation_rupture_pente(pente2=0.005,std1=std,std2=std)
        signal2,_ = simulation_rupture_pente(pente2=0.0055,std1=std,std2=std)
        signal3,_ = simulation_rupture_pente(pente2=0.006,std1=std,std2=std)
        signal4,_ = simulation_rupture_pente(pente2=0.004,std1=std,std2=std)
        signal5,_ = simulation_rupture_pente(pente2=0.0045,std1=std,std2=std)
        signaux = [signal1,signal2,signal3,signal4,signal5]
        x_time = np.arange(0,len(signal1))

        changement_detect = vote_majoritaire_coupture(signaux,x_time,mode = mode,w = 100,pourcentage=0.7,tolerance=5)

        result += np.array(comptage_resultat(changement_detect,changement))
    return result


if __name__ == "__main__":
    results = []
    conditions = []
    for std in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6]:
        for mode in [1,2,3]:
                result = test_multivote(std=std,mode=mode,nombre=2)
                print([std,mode,100,0.7,5],result)
                conditions.append([std,mode,100,0.7,5])
                results.append(result)
    np.savetxt("./result/conditionsB1.txt",conditions,fmt='%10.5f')
    np.savetxt("./result/resultsB1.txt",results,fmt='%d')


    



