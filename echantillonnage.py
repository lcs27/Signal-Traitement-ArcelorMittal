import wave
import math
import numpy as np
from scipy.io import wavfile
from moyenne_mobile import moyenne_ecart_type_mobile




def echantillonnage_brutal(samplarate,data,N):
    n = len(data)
    new_data = []
    for i in range(int(n/N)):
        new_data.append(data[i*N+int(N/2)])
    rate = samplarate // N
    return rate,new_data

def echantillonnage_moyenne(samplarate,data,N):
    n = len(data)
    new_data = []
    for i in range(int(n/N)):
        new_data.append(np.mean(data[i*N:(i*N+N-1)]))
    rate = samplarate // N
    return rate,new_data


if __name__=="__main__":
    nomfichier='./fichiers/sonbruit.wav'
    samplarate,data = wavfile.read(nomfichier)
    samplarate,data = echantillonnage_brutal(samplarate,data,15)
    wavfile.write('./fichiers/sonbruitnew.wav', samplarate, np.array(data))

    samplarate,data = wavfile.read(nomfichier)
    samplarate,data = echantillonnage_moyenne(samplarate,data,15)
    wavfile.write('./fichiers/sonbruitmoyenne.wav', samplarate, np.array(data))

'''
wavefile = wave.open(nomfichier,'rb')
length = wavefile.getnframes()
for i in range(length):
    wavedata = wavefile.readframes(i)
    data = wave.struct.unpack('<h',wavedata)
    print(int(data[0]))
'''