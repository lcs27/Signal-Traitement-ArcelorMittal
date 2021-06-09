import numpy as np
import matplotlib.pyplot as plt
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

results = np.loadtxt('./result/resultsD1.txt')
'''
fig, ax = plt.subplots(1, 1)
ax.plot(np.arange(3,21),results[3]/(results[3]+results[5]),label='Bonne detection%',linewidth=1)
ax.plot(np.arange(3,21),results[4]/results[3],label='Fausse Alarm%',linewidth=1)
ax.set_ylabel('taux')
ax.grid()
ax.set_title('Prediction')
ax.set_xlabel('sigma')
ax.legend(fontsize=5)
plt.show()
'''
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