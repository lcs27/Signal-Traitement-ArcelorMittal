import datetime
import re
import numpy as np

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

    # On alloue un tableau de nb_observations x (nb_variables - 1)
    x = np.zeros((nb_observations, nb_variables - 1))
    x_time = []
    compteur_ligne = 0
    for ligne in lignes:
        ligne = re.sub(r"\n", r"", ligne)
        # On charge les lignes suivantes du fichier dans le tableau x
        if compteur_ligne >= 1:
            liste_valeur_variables = ligne.split('\t')
            date_object = datetime.datetime.strptime(liste_valeur_variables[0],

                                                     '%Y-%m-%d %H:%M:%S')
            str_date_time = date_object.strftime('%H:%M:%S')
            str_date = date_object.strftime('%d.%m.%Y')
            date_time_object = datetime.datetime.strptime(str_date + " " +

                                                          str_date_time, '%d.%m.%Y %H:%M:%S')
            x_time.append(date_time_object)
            i = 1
            while i <= len(liste_valeur_variables) - 1:
                x[compteur_ligne - 1][i - 1] = float(liste_valeur_variables[i])
                i = i + 1
        compteur_ligne = compteur_ligne + 1

    print('Nombre de lignes :', len(x))
    print('Nombre de colonnes :', len(nom_variables))
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


def ecriture_fichier(x_time, x, nom_fichier, nom_var):
    # On ouvre un nouveau fichier en écriture
    fichier = open(nom_fichier, "w", encoding='utf-8')
    print(fichier)

    fichier.write('time'+'\t'+nom_var+'\n')
    # On enregistre les valeurs contenues dans x_time et x
    compteur_ligne = 0
    for i in range(0, len(x)):
        compteur_ligne = compteur_ligne + 1
        ligne = str(x_time[i])
        ligne = ligne + "\t" + str(x[i])
        ligne = ligne + "\n"
        fichier.write(ligne)

    fichier.close()
    print("Nombre de lignes dans le fichier ", compteur_ligne)

    print('Ecriture dans le fichier :', nom_fichier)
# Fin de la fonction ecriture_fichier
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# Début du programme principal
# --------------------------------------------------------------------------------

# Lecture du fichier de données
if __name__ == "__main__":
    nom_fichier = 'data/fichier_mesures.txt'
    x_time, x, liste_nom_variables = lecture_fichier(nom_fichier)

    # Affichage des variables
    for i in range(0, len(liste_nom_variables)):
        # for i in range(0, 3):
        nom_fichier = 'data/fichier_mesures_variable_' + str(i) + '.txt'
        ecriture_fichier(x_time, x[:, i], nom_fichier, liste_nom_variables[i])
        #print('Variable :[', i, ']', liste_nom_variables[i])

        # Ecriture dans un fichier des valeurs de la variable n°20

    '''
    for numero_variable in range(0, 85):
        nom_fichier = 'fichier_mesures_variable_' + str(numero_variable) + '.txt'
        ecriture_fichier(x_time, x[:, numero_variable], nom_fichier)
    '''
