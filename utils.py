import datetime
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# --------------------------------------------------------------------------------
# Fonction qui lit le contenu du fichier de données. Le paramètre de la fonction
# est :
#   - nom_fichier : le nom du fichier de données
#
# La fonction renvoie :
#    - x_time        : un tableau contenant le temps
#    - x             : un tableau à 2 dimensions contenant les valeurs des mesures
#    - nom_variables : une liste contenant le nom des variables
# --------------------------------------------------------------------------------
def lecture_fichier(nom_fichier):
    # Ouverture du fichier en lecture
    try:
        fichier = open(nom_fichier, "r", encoding='utf-8')
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

# --------------------------------------------------------------------------------
# Fonction qui enregistre dans un fichier texte le signal contenu dans la

# variable x. Les paramètres de la fonction sont :
#    - x_time      : une liste contenant des valeurs qui représentent le temps
#    - x           : un tableau à une dimension contenant les valeurs du signal

#                    à enregistrer dans le fichier
#    - nom_fichier : le nom du fichier dans lequel on enregistre les valeurs de x
# --------------------------------------------------------------------------------
def ecriture_fichier(x_time, x, nom_fichier):
    # On ouvre un nouveau fichier en écriture
    fichier = open(nom_fichier, "w", encoding='utf-8')
    print(fichier)

    # On enregistre les valeurs contenues dans x_time et x
    compteur_ligne = 0
    for i in range(0, len(x)):
        compteur_ligne = compteur_ligne + 1
        ligne = str(x_time[i])
        ligne = ligne + " " + str(x[i])
        ligne = ligne + "\n"
        fichier.write(ligne)

    fichier.close()
    print("Nombre de lignes dans le fichier ", compteur_ligne)

    print('Ecriture dans le fichier :', nom_fichier)
# Fin de la fonction ecriture_fichier
# --------------------------------------------------------------------------------



# --------------------------------------------------------------------------------
#  Fonction qui permet d’enregistrer dans un fichier .png deux graphiques.
#  Sur le 1er graphique, on affiche la mesure et la consigne et sur un
#  2ème graphique on affiche l'écart entre la mesure et la consigne.
#
#  Les paramètres de la fonction sont :
#      - x_time                : une liste contenant des valeurs qui
#                                représentent le temps
#      - x_mesure              : un tableau à une dimension contenant les valeurs
#                                de la mesure
#      - nom_variable_mesure   : le nom de la variable qui correspond à la mesure
#      - nom_variable_consigne : le nom de la variable qui correspond à la consigne
# --------------------------------------------------------------------------------
def ecriture_graphiques_signaux(x_time, x_mesure, x_consigne, nom_variable_mesure, nom_variable_consigne):
    # La fenêtre occupe la totalité de l'écran
    plt.rcParams["figure.figsize"] = [16, 9]

    # La fenetre contient deux graphiques qui auront la meme
    # echelle sur l'axe des ordonnees. Les deux graphiques
    # seront places l'un au dessus de l'autre dans la fenetre.
    # Sur le 1er graphique, on affiche le signal de mesure
    # et la consigne
    fig, ax = plt.subplots(2, 1, sharey=True)

    # On crée le signal de mesure et le signal de consigne
    ax[0].plot(x_time, x_mesure, label=nom_variable_mesure)
    ax[0].plot(x_time, x_consigne, label=nom_variable_consigne)

    # On définit le format de l'expression qui sera affichée
    #  sur l'axe des abscisses : Heure:Minute (Jour-Mois-Année)
    xfmt = mdates.DateFormatter('%H:%M (%d-%m-%y)')

    # On modifie la taille de la police de caractères
    # qui sera utilisée pour graduer l'axe des abscisses
    for tick in ax[0].xaxis.get_major_ticks():
        tick.label.set_fontsize(8)

    # L'axe des abscisses est l'axe temporel.
    ax[0].xaxis.set_major_formatter(xfmt)

    # Le label qui est affiché sur l'axe des abscisses
    ax[0].set_xlabel('time')

    # Le label qui est affiché sur l'axe des ordonnées
    ax[0].set_ylabel('degré')

    # On affiche la légende du 1er graphique
    ax[0].legend()

    # Dans la 2ème sous-fenêtre, on affiche le signal
    # qui représente la différence entre la mesure et la consigne
    x_difference = x_mesure - x_consigne

    # On crée le signal qui représente la différence en la
    # mesure et la consigne
    ax[1].plot(x_time, x_difference, label='Ecart entre "' + nom_variable_mesure + '" et "' + nom_variable_consigne + '"')

    # L'axe des abscisses est l'axe temporel
    xfmt = mdates.DateFormatter('%H:%M (%d-%m-%y)')
    for tick in ax[1].xaxis.get_major_ticks():
        tick.label.set_fontsize(8)
    ax[1].xaxis.set_major_formatter(xfmt)

    # Le label qui est affiché sur l'axe des abscisses
    ax[1].set_xlabel('time')

    # Le label qui est affiché sur l'axe des ordonnées
    ax[1].set_ylabel('degré')

    # On affiche la légende du 2ème graphique
    ax[1].legend()

    # On enregistre la figure dans un fichier png
    nom_figure = 'figure' + '_' + nom_variable_mesure + '.png'
    plt.savefig(nom_figure)
# Fin de la fonction ecriture_graphiques_signaux
# --------------------------------------------------------------------------------

def var_num_nom(nom_fichier):
    # Ouverture du fichier en lecture
    try:
        fichier = open(nom_fichier, "r", encoding='utf-8')
    except:
        print('Impossible de lire le fichier', nom_fichier)
        exit()
    ligne = fichier.readline()
    fichier.close()

    # Lecture des données contenues dans le fichier
    # La 1ère ligne du fichier contient le nom des variables

    ligne = re.sub(r"\n", r"", ligne)
    tab_ligne = ligne.split('\t')
    nb_variables = len(tab_ligne)
    # On enregistre le nom des variables dans une liste
    list_nom_variables = []
    for i in range(1, nb_variables):
        list_nom_variables.append(tab_ligne[i])
    return list_nom_variables


def lecture_fichier_1var(num_var):
    # Ouverture du fichier en lecture
    try:
        fichier = open("fichier_mesures_variable_" +
                       str(num_var)+".txt", "r", encoding='utf-8')
    except:
        print('Impossible de lire le fichier', "fichier_mesures_variable_" +
              num_var+".txt")
        exit()
    lignes = fichier.readlines()
    fichier.close()

    x = []
    x_time = []

    for ligne in lignes:
        #ligne = re.sub(r"\n", r"", ligne)
        ligne = ligne.split()
        x_time.append(ligne[0]+' '+ligne[1])
        x.append(float(ligne[2]))
    print('Lecture Réussite')
    return x_time, np.array(x)

# ----------------------------------------------------------------------------------
# Début du programme principal
# --------------------------------------------------------------------------------
if __name__=="__main__":
    nom_fichier = 'fichier_mesures.txt'

    # Lecture du fichier de données
    x_time, x, liste_nom_variables = lecture_fichier(nom_fichier)

    numero_variable = 20
    nom_fichier = 'fichier_mesures_variable_' + str(numero_variable) + '.txt'
    ecriture_fichier(x_time, x[:,numero_variable], nom_fichier)

    numero_variable = 21
    nom_fichier = 'fichier_mesures_variable_' + str(numero_variable) + '.txt'
    ecriture_fichier(x_time, x[:,numero_variable], nom_fichier)
    # On enregistre dans un fichier .png un graphique qui affiche la mesure
    # et la consigne,  et un graphique qui affiche la différence entre la
    # mesure et la consigne.
    # Variable 20 : température utile TIC0300
    # Variable 21 : Consigne en cours TIC0300
    numero_variable = 20
    
    ecriture_graphiques_signaux(x_time, x[:, numero_variable], x[:, numero_variable + 1], liste_nom_variables[numero_variable],
                 liste_nom_variables[numero_variable + 1])