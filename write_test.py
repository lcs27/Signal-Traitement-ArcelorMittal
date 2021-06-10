import numpy as np

resultat = [[370, 422,1], [845, 867, 895]]
print(resultat)
np.savetxt("./signaux_reel_mul3.txt", resultat, fmt='%i')

'''
for i in resultat:
    f = open("./signaux_reel_mul3.txt", 'w')
    f.write(str(i) + '\n')
f.close()


f=file("./signaux_reel_mul3.txt", "a+")
for i in range(1,100):
    if i % 2 == 0:
        new_context = "C++" + '\n'
        f.write(new_context)
    else:
        new_context = "Python" + '\n'
        f.write(new_context)
f.close()
'''
