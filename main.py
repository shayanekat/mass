import matplotlib.pyplot as pp

#=====BACKEND=====
#init var
mounth = []
mass = []

data = open("data.txt","r")
for line in data:
    row = line.split(",")
    mounth.append(row[0])
    mass.append(float(row[1].replace("\n","")))

X = []
Y = []

for i in range(len(mounth)-12,len(mounth)):
    X.append(mounth[i])
    Y.append(mass[i])

#=====FRONTEND=====
pp.grid()
ax = pp.axes()        
ax.yaxis.grid() # horizontal lines


pp.plot(X,Y)
pp.xticks(rotation="vertical",fontsize=7)
pp.show()