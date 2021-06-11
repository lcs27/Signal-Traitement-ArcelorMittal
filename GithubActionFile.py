# Ce document comprend tous les codes à faire tourner sur la machine de Github Action
from prediction import test_prediction
from signal_simule import *
from detection import *
from test_detection import *
import numpy as np
import argparse

# To get the name of task
parser = argparse.ArgumentParser()
parser.add_argument('--task', required=True, help='task number')
args = parser.parse_args()
task_number: int = args.task
task_number = int(task_number)
print(task_number)
'''
result = test_prediction(nombre=1000)
print(result)
np.savetxt("./result/resultsD"+str(task_number)+".txt", result, fmt = '%10.5f')

if task_number == 1:
    results = []
    conditions = []
    for std in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6]:
        for mode in [1,2,3]:
                result = test_multivote_moyenne(std=std,mode=mode,nombre=100)
                print([std,mode,100,0.7,5],result)
                conditions.append([std,mode,100,0.7,5])
                results.append(result)
    np.savetxt("./result/conditionsB"+str(task_number)+".txt",conditions,fmt='%10.5f')
    np.savetxt("./result/resultsB"+str(task_number)+".txt",results,fmt='%i')
elif task_number == 2:
    results = []
    conditions = []
    for std in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6]:
        for mode in [1,2,3]:
                result = test_multivote_coupture(std=std,mode=mode,nombre=100)
                print([std,mode,100,0.7,5],result)
                conditions.append([std,mode,100,0.7,5])
                results.append(result)
    np.savetxt("./result/conditionsB"+str(task_number)+".txt",conditions,fmt='%10.5f')
    np.savetxt("./result/resultsB"+str(task_number)+".txt",results,fmt='%i')
'''

def multitask_test_detection(multiple,std,w=100,tolerance=10,nombre=250,task = 1):
    result = np.array([0,0,0])
    for _ in range(nombre):
        if task == 1:
            signal,changement = simulation_rupture_moyenne_3(
                std1=std,std2=std,std3=std)
        elif task == 2:
            signal,changement = simulation_rupture_pente(std1=std,std2=std)
        x_time = np.arange(0,len(signal))
        if task == 1:
            x_detect_time,x_detect = detection_moyenne(x_time,signal,w=w)
        elif task == 2:
            x_detect_time,x_detect = detection_pente(x_time,signal,w=w)
        seuil = apprentissage_seuil(x_detect,multiple=multiple)
        changement_detecte = detection_variation(
            x_detect_time,x_detect,seuil,validation_tolerance=2*tolerance)
        result += np.array(comptage_resultat(changement_detecte,
                           changement,tolerance))
    return result

results = []
conditions = []
for multiple in [3,5,7,9,11,15,20]:
    for std in [0.1,0.15,0.2,0.25,0.3,0.35,0.40,0.45,0.5,0.55,0.6]:
        for w in [50,100,200]:
            for tolerance in [10,15,20]:
                result = multitask_test_detection(
                    multiple,std,w=w,tolerance=tolerance,nombre=60,task = task_number)
                print([multiple,std,w,tolerance],result)
                conditions.append([multiple,std,w,tolerance])
                results.append(result)
np.savetxt("./result/conditionsE"+str(task_number)+".txt",conditions,fmt='%10.5f')
np.savetxt("./result/resultsE"+str(task_number)+".txt",results,fmt='%i')
