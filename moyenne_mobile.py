from re import I
from numpy.lib.function_base import median
from utils import *


# Ce document sert à calculer les moyennes mobiles etc. qui sont demandé comme task 1 dans notre fichier. 
def moyenne_ecart_type_mobile(x_time,x,d,w,delta = 1):
    n = len(x)
    nb = int((n-w)/d)+1
    x_moyenne_time = []
    x_moyenne_valeur = []
    x_borne_sup_valeur = []
    x_borne_inf_valeur = []
    for i in range(nb):
        x_moyenne_time.append(x_time[d*i+w//2])
        mean = np.mean(x[i*d:(i*d+w)])
        std = np.std(x[i*d:(i*d+w)])
        x_moyenne_valeur.append(mean)
        x_borne_sup_valeur.append(mean + delta * std)
        x_borne_inf_valeur.append(mean - delta * std)
    return x_moyenne_time,x_moyenne_valeur,x_borne_sup_valeur,x_borne_inf_valeur

def moyenne_max_min_mobile(x_time,x,d,w,delta = 1):
    n = len(x)
    nb = int((n-w)/d)+1
    x_moyenne_time = []
    x_moyenne_valeur = []
    x_borne_sup_valeur = []
    x_borne_inf_valeur = []
    for i in range(nb):
        x_moyenne_time.append(x_time[d*i+w//2])
        mean = np.mean(x[i*d:(i*d+w)])
        max = np.amax(x[i*d:(i*d+w)])
        min = np.amin(x[i*d:(i*d+w)])
        x_moyenne_valeur.append(mean)
        x_borne_sup_valeur.append(max)
        x_borne_inf_valeur.append(min)
    return x_moyenne_time,x_moyenne_valeur,x_borne_sup_valeur,x_borne_inf_valeur

def plot_band(x_time,y1,x_time_mobile,y2,y3,y4,labels):
    fig, ax = plt.subplots()
    ax.plot(x_time, y1, color = 'b', linewidth = 0.5,label=labels[0])
    print("Plot 1er réussite")
    ax.plot(x_time_mobile, y2, color='r', linewidth = 0.5,label=labels[1])
    print("Plot 2e réussite")
    ax.plot(x_time_mobile, y3, color='gray', linewidth = 0.5,label=labels[2])
    print("Plot 3e réussite")
    ax.plot(x_time_mobile, y4, color='gray', linewidth = 0.5,label=labels[3])
    print("Plot 4e réussite")
    ax.fill_between(x_time_mobile,y3,y4,facecolor='silver')

    # L'axe des abscisses est l'axe temporel
    xfmt = mdates.DateFormatter('%H:%M (%d-%m-%y)')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(5)
    ax.xaxis.set_major_formatter(xfmt)
    #ax.xticks(fontsize=5)
    #ax.yticks(fontsize=6)

    # Le label qui est affiché sur l'axe des abscisses
    ax.set(xlabel='temps', ylabel='degré')

    # On affiche la légende du 2ème graphique
    ax.legend(fontsize=5)

    # On enregistre la figure dans un fichier png
    #nom_figure = 'figure' + '_' + nom_variable_mesure + 'moyenne_mobile.png'
    #plt.savefig(nom_figure)
    #plt.show()
    nom_figure = 'image/figure_q6.png'
    plt.savefig(nom_figure)

if __name__=="__main__":
    # Lecture du fichier de données
    x_time, x_20,nom_variable_mesure = lecture_fichier('data/fichier_mesures_variable_20.txt')
    x_time, x_21,nom_variable_consigne = lecture_fichier('data/fichier_mesures_variable_21.txt')
    nom_variable_consigne = nom_variable_consigne[0]
    nom_variable_mesure = nom_variable_mesure[0]
  
    x_difference = x_20 - x_21
    x_1800_time,x_1800_moyenne, x_1800_sup,x_1800_inf = moyenne_max_min_mobile(x_time,x_difference,600,1800)
    print(x_1800_moyenne[0:5],x_1800_sup[0:5],x_1800_inf[0:5])
    #labels=['Ecart entre "' + nom_variable_mesure + '" et "' + nom_variable_consigne + '"','Moyenne mobile sur 1/2 heure',
            #'Moyenne + écart-type mobile sur 1/2 heure','Moyenne - écart-type mobile sur 1/2 heure']

    labels=['Ecart entre "' + nom_variable_mesure + '" et "' + nom_variable_consigne + '"','Moyenne mobile sur 1/2 heure','Max sur 1/2 heure','Min sur 1/2 heure']
    plot_band(x_time,x_difference,x_1800_time,x_1800_moyenne,x_1800_sup,x_1800_inf,labels)