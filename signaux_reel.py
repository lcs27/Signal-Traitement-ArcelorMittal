from utils import *
from echantillonnage import *
import write_data
from detection import *
################Cette partie sert à échantillonnage et est déjà fait#################
'''

nbr_donne = 83
for i in range(1,nbr_donne+1):
    nom_fichier = 'data/fichier_mesures_variable_'+str(i)+'.txt'
    x_time,x,nom_variable=lecture_fichier(nom_fichier)
    N=100
    _,x_echan = echantillonnage_moyenne(100,x,N)
    _,time_echan = echantillonnage_brutal(100,x_time,N)
    write_data.ecriture_fichier(time_echan,x_echan,'data/fichier_mesures_variable_'+str(i)+'_echan.txt',nom_variable[0])
    '''
i=0
nom_fichier = 'data/fichier_mesures_variable_'+str(i)+'_echan.txt'
x_time,x,nom_variable=lecture_fichier(nom_fichier)

time_index, x_detect = detection_moyenne(np.arange(start=0,stop=len(x)),x,w=50)
time_index=time_index.astype(int)
time_index=time_index.tolist()
#print(time_index)
x_time = np.array(x_time)
x_time = x_time[time_index]

plot_signal(x_detect,save=False,title=nom_variable[0],x_time=x_time)
