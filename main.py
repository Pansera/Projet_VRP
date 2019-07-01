import os
from random import *

nb_sommet = int(input('Entrez le nombre de sommets souhaité: '))
#print(nb_sommet)

matrice = [[0 for j in range(nb_sommet)] for i in range(nb_sommet)]

for i in range(0, nb_sommet):
    for j in range(i+1, nb_sommet):
        matrice[i][j] = randint(1,9)
        matrice[j][i] = matrice[i][j]

for i in range(nb_sommet):
    for j in range(nb_sommet):
        print(matrice[i][j], end='')
    print("\n")
#os.system("pause")