import wave
import math
import numpy as np


##Ce document sert à générer le son utilisé pour analyse spéctral de sous-échantillonnage.

nomfichier='./fichiers/sonbruit.wav'
monson=wave.open(nomfichier,'wb')
ncanal=1
noctet=2
fe=16000
duree=2
f0=440 
nechantillon = int(duree*fe)
parametres=(ncanal,noctet,fe,nechantillon,'NONE','notcompressed')
monson.setparams(parametres)
phaz=2*math.pi*np.random.uniform(0,1,size=1)

val=[]
for i in range(0,nechantillon):
    if noctet==1:
        val.append(int(128.0+127.*math.sin(2.0*math.pi*f0*i/fe+phaz)+np.random.normal(0,100,size=1)))
    if  noctet==2:
        val.append(max(-32768,min(32767,int(32767.*math.sin(2.0*math.pi*f0*i/fe+phaz)+np.random.normal(0,500,size=1)))))
signal=[]
for i   in range(0,nechantillon):
    if  noctet==1:
        signal=wave.struct.pack('<B',val[i]) 
    if noctet==2:
        signal=wave.struct.pack('<h',val[i]) 
    monson.writeframes(signal) 
monson.close()