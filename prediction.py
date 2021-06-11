from signal_simule import *
import numpy as np
from test_detection import *
from detection import *
from multisignal import *
import math
# Ce document sert à réaliser les prédictions 

def seuil_mobile(x_detect, pourcentage=0.9, multiple=3):
    seuil = [0]
    for i in range(1, len(x_detect)):
        seuil.append(apprentissage_seuil(
            x_detect[:i], pourcentage=pourcentage, multiple=multiple))
    return seuil


def detection_variation_mobile(x_moyenne_time, x_moyenne_valeur, seuil, validation_tolerance=21):
    changement = []
    for t in range(len(x_moyenne_time)):
        if (x_moyenne_valeur[t] > seuil[t]) and \
            (t > 0 and t < len(x_moyenne_time)-1) and \
            ((x_moyenne_valeur[t] >= x_moyenne_valeur[t-1] and x_moyenne_valeur[t] > x_moyenne_valeur[t+1]) or
             (x_moyenne_valeur[t] > x_moyenne_valeur[t-1] and x_moyenne_valeur[t] >= x_moyenne_valeur[t+1])):
            if (len(changement) == 0) or (len(changement) != 0 and x_moyenne_time[t]-changement[-1] > validation_tolerance):
                changement.append(x_moyenne_time[t])

    return changement


def calcul_retards(x_detect, x_time, retard_tolere=200):
    bonne_detections = []
    non_detections = []
    fausse_alarmes = []
    retards = []
    for multiple in np.arange(3, 21):
        seuil = seuil_mobile(x_detect, multiple=multiple)
        pass_seuil = test_pass_seuil(x_detect, seuil)
        pass_seuil = detect_lissage(pass_seuil)
        changement_detect = detect2changement(pass_seuil, x_time, mode=1)
        fausse_alarme = 0
        bonne_detection = 0
        non_detection = 1
        retard = 0
        for i in changement_detect:
            if i >= 1000 and i < 1000 + retard_tolere:
                non_detection = 0
                bonne_detection = 1
                if retard == 0:
                    retard = i-1000
                else:
                    fausse_alarme += 1
            else:
                fausse_alarme += 1
        retards.append(retard)
        bonne_detections.append(bonne_detection)
        fausse_alarmes.append(fausse_alarme)
        non_detections.append(non_detection)
    return retards, bonne_detections, fausse_alarmes, non_detections


def test_prediction(nombre=100):
    retard_moyenne = np.zeros_like(np.arange(3, 21))
    retard_max = np.zeros_like(np.arange(3, 21))
    retard_min = np.ones_like(np.arange(3, 21)) * 1000
    toutes_bonne = np.zeros_like(np.arange(3, 21))
    toutes_fausse = np.zeros_like(np.arange(3, 21))
    toutes_non = np.zeros_like(np.arange(3, 21))
    for i in range(nombre):
        signal, _ = simulation_rupture_pente()
        x_time, x_detect = detection_pente(range(len(signal)), signal)
        x_time = np.array(x_time)+100
        retards, bonne_detections, fausse_alarmes, non_detections = calcul_retards(
            x_detect, x_time, retard_tolere=200)
        retard_max = np.max([retard_max, retards], axis=0)
        retard_min = np.min([retard_min, retards+1000*np.ones_like(np.arange(3, 21))
                             * (np.ones_like(np.arange(3, 21))-bonne_detections)], axis=0)
        retard_moyenne = np.add(retard_moyenne, np.array(
            retards), out=retard_moyenne, casting="unsafe")

        toutes_bonne += np.array(bonne_detections)
        toutes_fausse += np.array(fausse_alarmes)
        toutes_non += np.array(non_detections)
    retard_moyenne = retard_moyenne / \
        np.max([toutes_bonne, np.ones_like(np.arange(3, 21))], axis=0)
    return retard_moyenne, retard_max, retard_min, toutes_bonne, toutes_fausse, toutes_non


if __name__ == "__main__":
    print(test_prediction(nombre=3))

    '''

    fig, ax = plt.subplots()
    ax.plot(np.arange(start=0,stop=len(signal)),signal,
            color = 'b', linewidth = 0.5,label="signal")
    ax.set(xlabel='temps', ylabel='signal')
    ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    # we already handled the x-label with ax1
    ax2.set_ylabel('feature&seuils', color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.plot(x_time, x_detect, color='r', linewidth = 1,label='feature')
    ax2.plot(x_time, seuil_1,color='c', linewidth = 1,label='seuil1=3sigma')
    ax2.plot(x_time, seuil_2, color='k', linewidth = 1,label='seuil2=5sigma')

    # Le label qui est affiché sur l'axe des abscisses

    ax.grid()

    # On affiche la légende du 2ème graphique
    ax.legend(fontsize=5,loc=1)
    ax2.legend(fontsize=5,loc=2)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    # plt.savefig('./image/prediction_moyenne3_AR.png')
    plt.show()
    '''
