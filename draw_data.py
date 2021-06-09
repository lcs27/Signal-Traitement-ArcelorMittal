import numpy as np
import matplotlib.pyplot as plt

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