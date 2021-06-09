import wave
import math
import numpy as np

nomfichier='./fichiers/sonbruit.wav'
monson=wave.open(nomfichier,'wb')
ncanal=1 #mono
noctet=2 #taille d'un échantillon : 1 octet = 8 bits
fe=16000 #frequenced'echantillonnage(enHz)
duree=2 #dureeduson(ens)
f0=440 #fréquence de la sinusoïde(enHz)
nechantillon = int(duree*fe)
#contenudel'entête
parametres=(ncanal,noctet,fe,nechantillon,'NONE','notcompressed')
#creationdel'entête (44 octets)
monson.setparams(parametres)
###phaseal'originealeatoireentre0et2pi
phaz=2*math.pi*np.random.uniform(0,1,size=1)
###oncreelesignal
val=[]
for i in range(0,nechantillon):
    if noctet==1:
        val.append(int(128.0+127.*math.sin(2.0*math.pi*f0*i/fe+phaz)+np.random.normal(0,100,size=1)))
    if  noctet==2:
        val.append(max(-32768,min(32767,int(32767.*math.sin(2.0*math.pi*f0*i/fe+phaz)+np.random.normal(0,500,size=1)))))
###onleconvertiten"son"
signal=[]
for i   in range(0,nechantillon):
    if  noctet==1:
        signal=wave.struct.pack('<B',val[i]) #<:littleendian
#B:unsignedchar(1octet)
    if noctet==2:
        signal=wave.struct.pack('<h',val[i]) #<:littleendian
#h:shortint(2octets)
    monson.writeframes(signal) #écriture de l'échantillon sono recourant
monson.close()