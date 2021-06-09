import wave
import math
import numpy as np
nomfichier = 'fichiers/son.wav'
monson = wave.open(nomfichier, 'wb')

ncanal = 1  # mono
noctet = 2  # t a i l l e d 'un e c h a n t i l l o n : 1 o c t e t = 8 b i t s
fe = 16000  # f r e quence d ' e chant i l l onna g e ( en Hz)
duree = 2  # dure e du son ( en s )
f0 = 440  # f r e quence de l a s inus o  de ( en Hz)
nechantillon = int(duree*fe)
# contenudel'en􀀀t^ete
parametres = (ncanal, noctet, fe, nechantillon, 'NONE', 'notcompressed')
# creationdel'en􀀀t^ete(44octets)
monson.setparams(parametres)
# phaseal'originealeatoireentre0et2pi
phaz = 2*math.pi*np.random.uniform(0, 1, size=1)
# oncreelesignal
val = []
for i in range(0, nechantillon):
    if noctet == 1:
        val.append(int(128.0+127.*math.sin(2.0*math.pi*f0*i/fe+phaz)))
    if noctet == 2:
        val.append(int(32767.*math.sin(2.0*math.pi*f0*i/fe+phaz)))
# on l e c o n v e r t i t en " son"
signal = []
for i in range(0, nechantillon):
    if noctet == 1:
        signal = wave.struct.pack('<B', val[i])  # <: l i t t l e endian
        # B: uns igned char (1 o c t e t )
    if noctet == 2:
        signal = wave.struct.pack('<h', val[i])  # <: l i t t l e endian
        # h : sho r t i n t (2 o c t e t s )
        # e c r i t u r e de l ' e c h a n t i l l o n sonor e courant
        monson.writeframes(signal)
        a=signal.decode('UTF-8')
        print(a)
print(monson)
monson.close()
