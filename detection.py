from moyenne_mobile import moyenne_ecart_type_mobile
from signal_simule import *

def detection_moyenne(x_time,x,d=1,w=100):
    x_moyenne_time,x_moyenne,_,_=moyenne_ecart_type_mobile(x_time,x,d,w)
    d2=int(w/d)
    x_moyenne_decale = np.array(x_moyenne[d2:])
    x_moyenne = np.array(x_moyenne[:-d2])
    #plot_signal(x_moyenne,save=False,x_time=x_moyenne_time[:-d])
    #plot_signal(x_moyenne_decale,save=False,x_time=x_moyenne_time[:-d])
    x_time = (np.array(x_moyenne_time[d2:])+np.array(x_moyenne_time[:-d2]))/2
    return x_time,abs(x_moyenne-x_moyenne_decale)

if __name__=="__main__":
    signal = simulation_rupture_moyenne_3()
    x_time = np.arange(0,len(signal))
    x_time, x_detect = detection_moyenne(x_time,signal)
    plot_signal(x_detect,save=False,x_time=x_time)

