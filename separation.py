import datetime
import re
import numpy as np
import utils

# Ce document sert à séparer les données en plusieurs fichier
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
        x.append(ligne[2])
    return x_time, x


if __name__ == '__main__':
    nom_fichier = './data/fichier_mesures.txt'

    # Lecture du fichier de données
    x_time, x, liste_nom_variables = utils.lecture_fichier(nom_fichier)
    
    for numero_variable in range(8,9):
        nom_fichier = './data/fichier_mesures_variable_' + str(numero_variable) + '.txt'
        utils.ecriture_fichier(x_time, x[:,numero_variable], nom_fichier)
    '''
    # example: for variable 20
    num_var = 20
    var_name = var_num_nom('fichier_mesures.txt')[num_var]
    x_time, x = lecture_fichier_1var(num_var)

    print(x_time[0:5])
    print(x[0:5])
    print(var_name)
    '''
