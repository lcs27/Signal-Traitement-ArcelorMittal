from utils import *
from echantillonnage import *
import write_data
from detection import *
from test_detection import *
################Cette partie sert à échantillonnage et est déjà fait#################

'''
nbr_donne = 83
for i in range(8,9):
    nom_fichier = './data/fichier_mesures_variable_'+str(i)+'.txt'
    x_time,x,nom_variable=lecture_fichier(nom_fichier)
    N=100
    _,x_echan = echantillonnage_moyenne(100,x,N)
    _,time_echan = echantillonnage_brutal(100,x_time,N)
    write_data.ecriture_fichier(time_echan,x_echan,'./data/fichier_mesures_variable_'+str(i)+'_echan.txt',nom_variable[0])

'''
'''
nbr_donne = 83

for i in range(4,(nbr_donne+1)//2):
    nom_fichier = 'data/fichier_mesures_variable_'+str(2*i)+'_echan.txt'
    x_time,x_mesure,nom_variable1=lecture_fichier(nom_fichier)
    nom_fichier2 = 'data/fichier_mesures_variable_'+str(2*i+1)+'_echan.txt'
    x_time,x_consigne,nom_variable2=lecture_fichier(nom_fichier2)
    x_difference = x_mesure-x_consigne
    x_difference = [i[0] for i in x_difference]
    write_data.ecriture_fichier(x_time,x_difference,'data/ecart_'+str(i)+'_echan.txt',nom_variable1[0]+' - '+nom_variable2[0])
'''

resultat = []
for i in range(42):
    nom_fichier = 'data/ecart_'+str(i)+'_echan.txt'
    x_time,x,nom_variable=lecture_fichier(nom_fichier)


    time_index, x_detect = detection_moyenne(np.arange(start=0,stop=len(x)),x,w=50)
    seuil = apprentissage_seuil(x_detect,multiple=3)
    time_index = detection_variation(time_index,x_detect,seuil,validation_tolerance=2*10)

    #plot_signal(x_detect,save=False,title=nom_variable[0],x_time=x_time)

    #### Transformer index aux temps
    time_index=np.array(time_index)
    time_index=time_index.astype(int)
    time_index=time_index.tolist()
    #x_time = np.array(x_time)
    #changement_detecte = x_time[time_index]

    resultat.append(time_index)
    print(i,time_index)
print(resultat)
np.savetxt("./result/signaux_reel_mul3.txt",resultat,fmt='%s')

