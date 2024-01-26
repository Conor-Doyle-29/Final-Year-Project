import statistics as stat
import matplotlib.pyplot as plt         #importing whats required 
import collections 
soundlevel = []
time=[]                 # estabhlising lists 
tempreture = []
waterTakenIn = []
tmpSound = []
tmpTime=[]
tmpTemp=[]
TmpWater=[]

file=open("tmp.csv","r")
dataIn=file.read()
file.close
print(dataIn)

tmpList= dataIn.split(",")
tmpList.remove(tmpList[-1])
print(tmpList)

for i in tmpList: # goes through temp data list and figures out what final list to assign them to 
    if "S" in i: 
        tmpSound.append(i)
    elif "T" in i: 
        tmpTime.append(i)
    elif "C" in i: 
        tmpTemp.append(i)
    elif "A" in i:
        TmpWater.append(i)


for i in tmpSound:
    tmpSound.remove(i)
    i=i[:-1]
    soundlevel.append(i)
    if i == "":
        soundlevel.remove(i) # valitdating  again 
for i in tmpTime:
    tmpTime.remove(i)
    i=i[:-1]
    time.append(i)
    if i =="":
        time.remove(i)
for i in tmpTemp:
    tmpTemp.remove(i)
    i=i[:-1]
    tempreture.append(i)
    if i=="":
        tempreture.remove(i)
for i in TmpWater:
    TmpWater.remove(i)
    i=i[:-1]
    waterTakenIn.append(i)
    if i== "":
        waterTakenIn.remove(i)

print(soundlevel)
print(time)
print(tempreture)
print(waterTakenIn)

