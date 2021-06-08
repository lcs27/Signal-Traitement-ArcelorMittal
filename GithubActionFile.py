# This test contains the test about the 
from signal_simule import *
from detection import *
from test_detection import detection_variation,apprentissage_seuil,comptage_resultat
import numpy as np
import argparse

# To get the name of task
parser = argparse.ArgumentParser()
parser.add_argument('--task', required=True, help='task number')
args = parser.parse_args()
task_number: int = args.task
task_number = int(task_number)
print(task_number)


def test_detection(pourcentage,std,w=100,tolerance=10,nombre=250,task = 1):
    result = np.array([0,0,0])
    for _ in range(nombre):
        if task % 2 == 1:
            signal,changement = simulation_rupture_moyenne_3(std1=std,std2=std,std3=std)
        else:
            signal,changement = simulation_rupture_intermittente(std=std)
        x_time = np.arange(0,len(signal))
        if task <2:
            x_detect_time,x_detect = detection_moyenne(x_time,signal,w=w)
        else:
            x_detect_time,x_detect = detection_AR(x_time,signal,w=w)
        seuil = apprentissage_seuil(x_detect,pourcentage=pourcentage)
        changement_detecte = detection_variation(x_detect_time,x_detect,seuil,validation_tolerance=2*tolerance)
        result += np.array(comptage_resultat(changement_detecte,changement,tolerance))
    return result

results = []
conditions = []
if task_number<2:
    for pourcentage in [0.7,0.8,0.9]:
        for std in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6]:
            for w in [50,100,200]:
                for tolerance in [10,15,20]:
                    result = test_detection(pourcentage,std,w=w,tolerance=tolerance,nombre=100,task = task_number)
                    print([pourcentage,std,w,tolerance],result)
                    conditions.append([pourcentage,std,w,tolerance])
                    results.append(result)
else:
    for pourcentage in [0.7,0.8,0.9]:
        for std in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6]:
            for w in [50,100,200]:
                for tolerance in [10,15,20]:
                    result = test_detection(pourcentage,std,w=w,tolerance=tolerance,nombre=100,task = task_number)
                    print([pourcentage,std,w,tolerance],result)
                    conditions.append([pourcentage,std,w,tolerance])
                    results.append(result)
np.savetxt("./result/conditionsA"+str(task_number)+".txt",conditions,fmt='%10.5f')
np.savetxt("./result/resultsA"+str(task_number)+".txt",results,fmt='%i')