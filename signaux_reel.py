from utils import *
from echantillonnage import *
import write_data
nbr_donne = 83
for i in range(1,nbr_donne+1):
    nom_fichier = 'data/fichier_mesures_variable_'+str(i)+'.txt'
    x_time,x,nom_variable=lecture_fichier(nom_fichier)
    N=100
    _,x_echan = echantillonnage_moyenne(100,x,N)
    _,time_echan = echantillonnage_brutal(100,x_time,N)
    write_data.ecriture_fichier(time_echan,x_echan,'data/fichier_mesures_variable_'+str(i)+'_echan.txt',nom_variable[0])