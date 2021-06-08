# This test contains the test about the 
from test_detection import test_detection
import numpy as np
import argparse

# To get the name of task
parser = argparse.ArgumentParser()
parser.add_argument('--task', required=True, help='task number')
args = parser.parse_args()
task_number: int = args.task

results = []
conditions = []
for pourcentage in [0.7,0.8,0.9]:
    for std in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6]:
        for w in [50,100,200]:
            for tolerance in [10,15,20]:
                result = test_detection(pourcentage,std,w=w,tolerance=tolerance,nombre=100)
                print([pourcentage,std,w,tolerance],result)
                conditions.append([pourcentage,std,w,tolerance])
                results.append(result)
print(results)
print(conditions)
np.savetxt("./result/conditions1"+str(task_number)+".txt",conditions,fmt='%10.5f')
np.savetxt("./result/results1"+str(task_number)+".txt",results,fmt='%i')