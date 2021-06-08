from moyenne_mobile import moyenne_ecart_type_mobile
from signal_simule import *
import nitime

def detection_moyenne(x_time,x,d=1,w=100):
    x_moyenne_time,x_moyenne,_,_=moyenne_ecart_type_mobile(x_time,x,d,w)
    d2=int(w/d)
    x_moyenne_decale = np.array(x_moyenne[d2:])
    x_moyenne = np.array(x_moyenne[:-d2])
    x_time = (np.array(x_moyenne_time[d2:])+np.array(x_moyenne_time[:-d2]))/2
    return x_time,abs(x_moyenne-x_moyenne_decale)

def detection_pente(x_time,x,d=1,w=100):
    x_pente_time,x_pente=pente_mobile(x_time,x,d,w)
    d2=int(w/d)
    x_pente_decale = np.array(x_pente[d2:])
    x_pente = np.array(x_pente[:-d2])
    x_time = (np.array(x_pente_time[d2:])+np.array(x_pente_time[:-d2]))/2
    return x_time,abs(x_pente-x_pente_decale)


def detection_coupture(x_time,x,d=1,w=100):
    x_coupture_time,x_coupture=coupture_mobile(x_time,x,d,w)
    d2=int(w/d)
    x_coupture_decale = np.array(x_coupture[d2:])
    x_coupture = np.array(x_coupture[:-d2])
    x_time = (np.array(x_coupture_time[d2:])+np.array(x_coupture_time[:-d2]))/2
    return x_time,abs(x_coupture-x_coupture_decale)

def detection_AR(x_time,x,d=1,w=100):
    _,sigma_2 = AR_mobile(x_time,x,d,w)
    d2=int(w/d)
    sigma_3 = np.array(sigma_2[d2:])
    sigma_2 = np.array(sigma_2[:-d2])
    x_time,sigma_1 = AR_mobile(x_time,x,d,2*w)
    sigma_1 = np.array(sigma_1)
    return x_time, np.abs(w*np.log(sigma_1)-w*1/2*np.log(sigma_2)-w*1/2*np.log(sigma_3))

def AR_mobile(x_time,x,d,w):
    n = len(x)
    nb = int((n-w)/d)+1
    x_AR_time = []
    x_sigma_valeur = []
    for i in range(nb):
        x_AR_time.append(x_time[d*i+w//2])
        x_prime = x[i*d:(i*d+w)]-np.mean(x[i*d:(i*d+w)])
        _,sigma = nitime.algorithms.autoregressive.AR_est_LD(x_prime, 2, rxx=None)
        x_sigma_valeur.append(sigma)
    return x_AR_time,x_sigma_valeur


def pente_mobile(x_time,x,d,w):
    n = len(x)
    nb = int((n-w)/d)+1
    x_pente_time = []
    x_pente_valeur = []
    for i in range(nb):
        x_pente_time.append(x_time[d*i+w//2])
        coeff = np.polyfit(x_time[i*d:(i*d+w)],x[i*d:(i*d+w)],1)
        x_pente_valeur.append(coeff[0])
    return x_pente_time,x_pente_valeur

def coupture_mobile(x_time,x,d,w):
    n = len(x)
    nb = int((n-w)/d)+1
    x_coupture_time = []
    x_coupture_valeur = []
    for i in range(nb):
        x_coupture_time.append(x_time[d*i+w//2])
        coeff = np.polyfit(x_time[i*d:(i*d+w)],x[i*d:(i*d+w)],1)
        x_coupture_valeur.append(coeff[1])
    return x_coupture_time,x_coupture_valeur

if __name__=="__main__":
    signal = simulation_rupture_moyenne_3()
    x_time = np.arange(0,len(signal))
    x_time, x_detect = detection_AR(x_time,signal)
    plot_signal(signal,save=False)
    plot_signal(x_detect,save=False,x_time=x_time)

