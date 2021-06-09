# --------------------------------------------------------------------------------
#
# Corrigé des questions sur la partie "Calcul et affichage de descripteurs sur les signaux"
#
# Programme qui lit un fichier de mesure et qui effectue le calcul et
# l'affichage de la moyenne et de l'écart-type d'un signal sur une fenêtre glissante.
# Le programme calcule et affiche également la valeur minimale
# et la valeur maximale du signal sur cette même fenêtre glissante
#
# Dans cette version du programme :
#     1 - il peut y avoir un chevauchement entre les fenêtres qui sont
#     appliquées sur le signal.
#     2 - La fonction d'affichage utilise la fonction plot de Matplotlib.
#
# --------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import re
import datetime
import matplotlib.dates as mdates


# --------------------------------------------------------------------------------
# Fonction qui lit le contenu du fichier de données. Le paramètre de la fonction
# est :
#   - nom_fichier    : le nom du fichier de données
#
# La fonction renvoie :
#    - x_time        : une liste contenant des valeurs qui représentent le temps
#    - x             : un tableau à 2 dimensions contenant la valeur des mesures
#    - nom_variables : une liste contenant le nom des variables
# --------------------------------------------------------------------------------
def lecture_fichier(nom_fichier):
    # Ouverture du fichier en lecture
    try:
        fichier = open(nom_fichier, "r", encoding='latin-1')
    except:
        print('Impossible de lire le fichier', nom_fichier)
        exit()
    print(fichier)
    lignes = fichier.readlines()
    fichier.close()
    # Lecture des données contenues dans le fichier
    # La 1ère ligne du fichier contient le nom des variables
    ligne_entete = lignes[0]
    ligne_entete = re.sub(r"\n", r"", ligne_entete)
    tab_ligne = ligne_entete.split('\t')
    nb_observations = len(lignes) - 1
    nb_variables = len(tab_ligne)
    # On enregistre le nom des variables dans une liste
    nom_variables = []
    for i in range(1, nb_variables):
        nom_variables.append(tab_ligne[i])

    # On alloue un tableau de nb_observations x nb_variables
    x = np.zeros((nb_observations, nb_variables - 1))
    compteur_ligne = 0
    x_time = []
    for ligne in lignes:
        ligne = re.sub(r"\n", r"", ligne)
        # On charge les lignes suivantes du fichier dans le tableau x
        if compteur_ligne >= 1:
            liste_valeur_variables = ligne.split('\t')
            date_object = datetime.datetime.strptime(liste_valeur_variables[0], '%Y-%m-%d %H:%M:%S')
            str_date_time = date_object.strftime('%H:%M:%S')
            str_date = date_object.strftime('%d.%m.%Y')
            date_time_object = datetime.datetime.strptime(str_date + " " + str_date_time, '%d.%m.%Y %H:%M:%S')
            x_time.append(date_time_object)
            i = 1
            while i <= len(liste_valeur_variables) - 1:
                x[compteur_ligne - 1][i - 1] = float(liste_valeur_variables[i])
                i = i + 1
        compteur_ligne = compteur_ligne + 1

    print('Nombre de lignes contenues dans le fichier', len(x))
    print('Nombre de colonnes contenus dans le fichier', len(nom_variables))

    return x_time, x, nom_variables
# Fin de la fonction lecture_fichier
# --------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
#
# Fonction qui calcule des indicateurs statistique sur un signal (moyenne, écart-type, valeur
# minimale et valeur maximale). Ces indicateurs sont calculés sen utilisant le principe de
# la fenêtre glissante.
#
# Les paramètre de la fonction sont :
#    - x_time        : une liste contenant des valeurs qui représentent le temps
#    - x_difference  : un tableau contenant la difference entre la mesure et la consigne
#    - nombre_echantillons_fenetre : la largeur de la fenêtre
#    - decalage      : le décalage entre deux fenêtres successives
#
# La fonction renvoie :
#    - x_time_new   : un tableau contenant des valeurs qui représentent le temps
#    - lmean        : un tableau contenant les valeurs moyennes du signal
#    - lmin         : un tableau contenant les valeurs minimales du signal
#    - lmax         : un tableau contenant les valeurs maximales du signal
#    - lstd         : un tableau contenant les écart-types du signal
# ----------------------------------------------------------------------------------------------
def calcul_statistiques(x_time, x_difference, nombre_echantillons_fenetre, decalage):

    nombre_echantillons_signal = len(x_difference)
    nb_fenetres = int((nombre_echantillons_signal - nombre_echantillons_fenetre) / decalage + 1)
    lmax = np.zeros(nb_fenetres)
    lmin = np.zeros(nb_fenetres)
    lmean = np.zeros(nb_fenetres)
    lstd = np.zeros(nb_fenetres)
    x_time_new = []
    y = x_difference
    print('nb_fenetre =' , nb_fenetres)
    print('longueur x_time :', len(x_time))
    print('longueur x_difference :', len(x_difference))
    i = 0
    k = 0
    while i < nombre_echantillons_signal - nombre_echantillons_fenetre:
        y_tmp = y[i: i + nombre_echantillons_fenetre]
        lmax[k] = max(y_tmp)
        lmin[k] = min(y_tmp)
        lmean[k] = np.mean(y_tmp)
        lstd[k] = np.std(y_tmp)
        t = x_time[int(i + nombre_echantillons_fenetre / 2)]
        x_time_new.append(t)
        i = i + decalage
        k = k + 1
    return np.array(x_time_new), lmin, lmax, lmean, lstd
# Fin de la fonction calcul_statistiques
# ----------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# Fonction qui effectue le calcul et l'affichage de la moyenne et de
# l'écart-type d'un signal sur une fenêtre glissante.
# Le programme calcule et affiche également la valeur minimale
# et la valeur maximale du signal sur cette même fenêtre glissante
#
# Les paramètre de la fonction sont :
#    - x_time        : une liste contenant des valeurs qui représentent le temps
#    - x_mesure      : un tableau contenant la valeur de la mesures
#    - x_consigne    : un tableau contenant la valeur de la consigne
#    - nom_variable_mesure : le nom de la variable qui correspond à la mesure
#    - nom_variable_consigne : le nom de la variable qui correspond à la consigne
#    - nombre_echantillons_fenetre : la largeur de la fenêtre
#    - decalage : le décalage entre deux fenêtres successives
#
# La fonction ne renvoie rien
#
# --------------------------------------------------------------------------------
def affichage_statistiques_temps(x_time,
                                 x_mesure,
                                 x_consigne,
                                 nom_variable_mesure,
                                 nom_variable_consigne,
                                 nombre_echantillons_fenetre,
                                 decalage):

    plt.rcParams["lines.linewidth"] = 1

    # On calcule le signal qui représente la différence entre la mesure et la consigne
    x_difference = x_mesure - x_consigne

    # On crée le signal qui représente la difference entre la mesure et la consigne
    plt.plot(x_time, x_difference, label='Ecart entre "' + nom_variable_mesure + '" et "' + nom_variable_consigne + '"')

    # On calcule les indicateurs sur le signal avec une largeur de fenetre = 3600 échantillons (1/2 heure)
    x_time_new, l_min, l_max, l_mean, l_std = calcul_statistiques(x_time, x_difference, nombre_echantillons_fenetre, decalage)

    # On crée le signal moyenné
    plt.plot(x_time_new, l_mean, color='red', label='Moyenne mobile sur 1/2 heure')

    # On crée le signal moyenne + ecart_type
    plt.plot(x_time_new, l_mean + l_std, color='black', label='Moyenne + écart-type mobile sur 1/2 heure')

    # On crée le signal moyenne - ecart_type
    plt.plot(x_time_new, l_mean - l_std, color='black', label='Moyenne - écart-type mobile sur 1/2 heure')

    # On remplit la surface se trouvant entre la moyenne + ecart-type et la moyenne - ecart-type
    plt.fill_between(x_time_new, l_mean - l_std, l_mean + l_std, where=l_mean + l_std > l_mean - l_std, facecolor='dimgrey', alpha=0.5)

    # On crée le signal moyenne + max
    plt.plot(x_time_new, l_max, color='grey', label='Valeur maximale mobile sur 1/2 heure')

    # On crée le signal moyenne - min
    plt.plot(x_time_new, l_min, color='grey', label='Valeur minimale mobile sur 1/2 heure')

    # On remplit la surface se trouvant entre la valeur maximale et la valeur minimale
    plt.fill_between(x_time_new, l_min, l_max, where=l_max > l_min,
                     facecolor='grey', alpha=0.5)

    # L'axe des abscisses est l'axe temporel
    xfmt = mdates.DateFormatter('%H:%M (%d-%m-%y)')
    ax = plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(8)
    ax.xaxis.set_major_formatter(xfmt)

    # Le label qui est affiché sur l'axe des abscisses
    ax.set_xlabel('time')

    # Le label qui est affiché sur l'axe des ordonnées
    ax.set_ylabel('degré')

    # On affiche la légende des courbes
    plt.legend()

    # On ouvre la fenêtre
    plt.show()


# ----------------------------------------------------------------------------------------------
# Début du programme principal
# ----------------------------------------------------------------------------------------------
nom_fichier = 'fichier_mesures.txt'

# Lecture du fichier de données
x_time, x, liste_nom_variables = lecture_fichier(nom_fichier)
# durée de la fenêtre = 30 min (pour 1800 échantillons)
nombre_echantillons_fenetre = 1800
# décalage entre 2 fenêtres = 10 min (pour 600 échantillons)
decalage = 600
# Variable 20 : température utile TIC0300
# Variable 21 : Consigne en cours TIC0300
numero_variable = 20
# Ouverture d'une fenêtre graphique.
affichage_statistiques_temps(x_time,
                             x[:, numero_variable],
                             x[:, numero_variable + 1],
                             liste_nom_variables[numero_variable],
                             liste_nom_variables[numero_variable + 1],
                             nombre_echantillons_fenetre,
                             decalage)
