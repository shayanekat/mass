"""
Shayane Katchera
Fichier python pour aller plus loin dans l'analyse de mes données de poids
"""

# TODO (03/01/2021): 
#   - plot dérivé du poids

import matplotlib.pyplot as pp
import numpy as np

#=====BACKEND=====
#init var
mounth = []
mass = []

data = open("data.txt","r")
for line in data:
    row = line.split(",")
    mounth.append(row[0])
    mass.append(float(row[1].replace("\n","")))
data.close()

X = []
Y = []

for i in range(len(mounth)-1):
    X.append(i)
    Y.append(mass[i+1]-mass[i])
X, Y = np.array(X), np.array(Y)
mean = np.zeros(X.shape) + np.mean(Y)
#=====FRONTEND=====

# curves
pp.bar(X, Y, label="Masse")
pp.plot(X, np.zeros((len(X), 1)), "k")
pp.plot(X, mean, "k:", label=f"valeur moyenne = {round(np.mean(Y), 2)}")

# diplay 
pp.legend(loc=1)
pp.xlabel("temps (mois)")
pp.ylabel("variation de masse (kg/mois)")
pp.title("Monthly Mass Analyst")
pp.axis("on")


pp.show()