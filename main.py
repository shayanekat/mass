import matplotlib.pyplot as pp
import numpy as np

#=====BACKEND=====
#init var
mounth = []
mass = []
choice = "annuel"

data = open("data.txt","r")
for line in data:
    row = line.split(",")
    mounth.append(row[0])
    mass.append(float(row[1].replace("\n","")))

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
pp.grid()
ax = pp.axes()        
ax.yaxis.grid() # vertical lines

pp.plot(X,Y)
pp.xticks(rotation="vertical",fontsize=7)
pp.show()