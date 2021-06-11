import numpy as np
import matplotlib.pyplot as plt

### Ce document sert à visualiser les datas.

##### Visualisation 1
'''
results = np.loadtxt('./result/resultsA1.txt')
conditions = np.loadtxt('./result/conditionsA1.txt')


def draw_figure(fig,ax,conditions,results,pourcentage = 0.8,w = 100,tolerance = 10,color = 'b'):
    x = []
    bonne_detect = []
    fausse_alarm = []
    for i in range(len(conditions)):
        if conditions[i][0] == pourcentage and conditions[i][2] == w and conditions[i][3] == tolerance:
            x.append(conditions[i][1])
            bonne_detect.append(results[i][0]/(results[i][0]+results[i][2]))
            fausse_alarm.append(results[i][1]/(results[i][0]))

    ax[0].plot(x,bonne_detect,color=color,label='pourcentage = '+str(pourcentage)+',w='+str(w)+',tolerance='+str(tolerance),linewidth=1)
    ax[1].plot(x,fausse_alarm,color=color,label='pourcentage = '+str(pourcentage)+',w='+str(w)+',tolerance='+str(tolerance),linewidth=1)

    
color = ['b','g','r','c','m','y','gray','brown','blueviolet','darkorange']
fig, ax = plt.subplots(2, 1,sharex=True)
for pourcentage in [0.7,0.8,0.9]:
    for w in [50,100,200]:
        for tolerance in [20]:
            draw_figure(fig,ax,conditions,results,pourcentage = pourcentage,w = w,tolerance = tolerance,color=color.pop())
ax[0].set_ylabel('taux')
ax[0].grid()
ax[0].set_title('Bonne detection%')
ax[1].set_xlabel('sigma')
ax[1].set_ylabel('taux')
ax[1].set_title('Fausse Alarm%')
ax[0].legend(fontsize=5)
ax[1].grid()
plt.show()
'''
##### Visualisation 2
'''

results = np.loadtxt('./result/resultsD1.txt')

fig, ax = plt.subplots(1, 1)
ax.plot(np.arange(3,21),results[3]/(results[3]+results[5]),label='Bonne detection%',linewidth=1)
ax.plot(np.arange(3,21),results[4]/results[3],label='Fausse Alarm%',linewidth=1)
ax.set_ylabel('taux')
ax.grid()
ax.set_title('Prediction')
ax.set_xlabel('sigma')
ax.legend(fontsize=5)
plt.show()

fig, ax = plt.subplots()
ax.plot(np.arange(3,21), results[0], color = 'b', linewidth = 2,label='moyenne')
print("Plot 1er réussite")
ax.plot(np.arange(3,21), results[1], color='r', linewidth = 1,label='max')
print("Plot 2e réussite")
ax.plot(np.arange(3,21), results[2], color='k', linewidth = 1,label='min')
ax.fill_between(np.arange(3,21),results[1],results[2],facecolor='silver')

ax.set(xlabel='sigma', ylabel='retard')

ax.legend(fontsize=5)
ax.grid()
plt.show()
'''
##### Visualisation 3
'''
results = np.loadtxt('./result/resultsE2.txt')
results2 = np.loadtxt('./result/resultsF2.txt')

##### Merge data
all_result=[]
for i in range(len(results)):
    all_result.append([results2[i][0],results2[i][1],results2[i][2],results2[i][3],results[i][4]+results2[i][4],results[i][5]+results2[i][5],results[i][6]+results2[i][6]])

def draw_figure(fig,ax,fig2,ax2,results,multiple = 3,w = 100,tolerance = 10,color = 'b',marker='o'):
    x = []
    bonne_detect = []
    fausse_alarm = []
    for i in range(len(results)):
        if results[i][0] == multiple and results[i][2] == w and results[i][3] == tolerance:
            x.append(results[i][1])
            bonne_detect.append(results[i][4]/(results[i][4]+results[i][6]))
            fausse_alarm.append(results[i][5]/(results[i][4]+results[i][6]))

    ax[0].plot(x,bonne_detect,color=color,label='multiple = '+str(multiple)+',w='+str(w)+',tolerance='+str(tolerance),linewidth=1,marker=marker)
    ax[1].plot(x,fausse_alarm,color=color,label='multiple = '+str(multiple)+',w='+str(w)+',tolerance='+str(tolerance),linewidth=1,marker=marker)
    ax2.plot(bonne_detect,fausse_alarm,color=color,label='multiple = '+str(multiple)+',w='+str(w)+',tolerance='+str(tolerance),linewidth=1,marker=marker)
    
colors = ['b','g','r','c','m','y','gray','brown','blueviolet','darkorange']
linestyle = ['dashed',]
markers = [".",'1','|','x']
fig, ax = plt.subplots(2, 1,sharex=True)
fig2, ax2 = plt.subplots(1, 1)
k=0
for multiple in [3,5,7,9,11,15,20]:
    color = colors[k]
    k+=1
    for w in [50,100,200]:
        marker = markers[w//50-1]
        for tolerance in [20]:
            draw_figure(fig,ax,fig2,ax2,all_result,multiple=multiple,w = w,tolerance = tolerance,color=color,marker = marker)
ax[0].set_ylabel('taux')
ax[0].grid()
ax[0].set_title('Bonne detection%')
ax[1].set_xlabel('sigma')
ax[1].set_ylabel('taux')
ax[1].set_title('Fausse Alarm%')
ax[0].legend(fontsize=3,loc=0)
ax[1].grid()
ax2.set_xlabel('Bonne detection%')
ax2.set_ylabel('Fausse Alarm%')
ax2.legend(fontsize=5,loc=0)
ax2.grid()
plt.show()
'''
##### Visualisation 4
'''
results = np.loadtxt('./result/resultsG1.txt')
conditions = np.loadtxt('./result/conditionsG1.txt')


def draw_figure(fig,ax,ax2,conditions,results,mode,tolerance = 10,color = 'b',marker='.'):
    x = []
    bonne_detect = []
    fausse_alarm = []
    for i in range(len(conditions)):
        if conditions[i][1] == mode and conditions[i][4] == tolerance:
            x.append(conditions[i][0])
            bonne_detect.append(results[i][0]/(results[i][0]+results[i][2]))
            fausse_alarm.append(results[i][1]/(results[i][0]+results[i][2]))

    ax[0].plot(x,bonne_detect,color=color,label='mode'+str(mode)+',erosion='+str((tolerance == 5)),linewidth=1,marker=marker)
    ax[1].plot(x,fausse_alarm,color=color,label='mode'+str(mode)+',erosion='+str((tolerance == 5)),linewidth=1,marker=marker)
    ax2.plot(bonne_detect,fausse_alarm,color=color,label='mode'+str(mode)+',erosion='+str((tolerance == 5)),linewidth=1,marker=marker)

    
color = ['b','g','r','c','m','y','gray','brown','blueviolet','darkorange']
markers = ["+",'x','.','1']
fig, ax = plt.subplots(2, 1,sharex=True)
fig2, ax2 = plt.subplots(1, 1)
for mode in [1,2,3]:
    for tolerance in [0,5]:
        marker = markers[tolerance//5]
        draw_figure(fig,ax,ax2,conditions,results,mode=mode,tolerance=tolerance,color=color.pop(),marker=marker)
ax[0].set_ylabel('taux')
ax[0].grid()
ax[0].set_title('Bonne detection%')
ax[1].set_xlabel('sigma')
ax[1].set_ylabel('taux')
ax[1].set_title('Fausse Alarm%')
ax[0].legend(fontsize=5)
ax[1].grid()

ax2.set_xlabel('Bonne detection%')
ax2.set_ylabel('Fausse Alarm%')
ax2.legend(fontsize=5,loc=0)
ax2.grid()
plt.axis([-6,6,-10,10])
plt.show()
'''