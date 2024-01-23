import statistics as stat
import matplotlib.pyplot as plt         #importing whats required 
import collections 
soundlevel = []
time=[]                 # estabhlising lists 
tempreture = []
waterTakenIn = []

file=open("tmp.csv","r")
dataIn=file.read()
file.close
print(dataIn)

tmpList= dataIn.split(",")
tmpList.remove(tmpList[-1])
print(tmpList)

for i in tmpList: # goes through temp data list and figures out what final list to assign them to 
    if "S" in i: 
        soundlevel.append(i)
    elif "T" in i: 
        time.append(i)
    elif "C" in i: 
        tempreture.append(i)
    elif "A" in i:
        waterTakenIn.append(i)
    
print(soundlevel)
print(time)
print(tempreture)
print(waterTakenIn)

