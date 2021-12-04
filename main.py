"""
    Shayane Katchera
    Suivit de ma masse
"""

import matplotlib.pyplot as plt

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
if choice == "tout":
    for i in range(len(mounth)):
        X.append(i)
        Y.append(mass[i])

#=====FRONTEND=====
plt.grid()
# ax = plt.axes()        
# ax.yaxis.grid() # vertical lines

# curves
plt.plot(X, Y, label="Masse")
plt.axhspan(45, 50, alpha=0.5, color='red', label="Minimum limit")
plt.axhspan(59, 61, alpha=0.5, color="blue", label="Objective")

# diplay 
plt.legend(loc=1)
plt.xlabel("temps (mois)")
plt.ylabel("masse (kg)")
plt.title("Monthly Mass Tracking")
plt.xticks(rotation="vertical",fontsize=7)

plt.show()


    
    