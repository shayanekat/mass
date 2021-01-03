import matplotlib.pyplot as pp
import numpy as np

#=====BACKEND=====
#init var
mounth = []
mass = []
objectif = []
choice = "tout"

data = open("data.txt","r")
for line in data:
    row = line.split(",")
    mounth.append(row[0])
    mass.append(float(row[1].replace("\n","")))
data.close()

X = []
Y = []
if choice == "annuel":
    for i in range(len(mounth)-12,len(mounth)):
        X.append(mounth[i])
        Y.append(mass[i])
        objectif.append(60)

if choice == "tout":
    for i in range(len(mounth)):
        X.append(i)
        Y.append(mass[i])
        objectif.append(60)

#=====FRONTEND=====
pp.grid()
ax = pp.axes()        
ax.yaxis.grid() # vertical lines

# curves
pp.plot(X, Y, label="Masse")
pp.plot(X, objectif, "g", label="objectif")
pp.axhspan(45, 50, alpha=0.5, color='red', label="Minimum limit")

# diplay 
pp.legend(loc=1)
pp.xlabel("temps (mois)")
pp.ylabel("masse (kg)")
pp.title("Monthly Mass Tracking")
pp.xticks(rotation="vertical",fontsize=7)


pp.show()