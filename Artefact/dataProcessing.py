import statistics as stat
#import matplotlib.pyplot as plt         #importing whats required 
import collections 
import random
from studyScore import studyscore as study
from listGenerator import noiseToHigh as noise
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
def dataProcess(dataset):
    for i in dataset: # goes through temp data list and figures out what final list to assign them to 
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
        i=int(i)
        soundlevel.append(i)
        if i == "":
            soundlevel.remove(i) # valitdating  again 
    for i in tmpTime:
        tmpTime.remove(i)
        i=i[:-1]
        i=int(i)
        time.append(i)
        if i =="":
            time.remove(i)
    for i in tmpTemp:
        tmpTemp.remove(i)
        i=i[:-1]
        i=int(i)
        tempreture.append(i)
        if i=="":
            tempreture.remove(i)
    for i in TmpWater:
        TmpWater.remove(i)
        i=i[:-1]
        i=int(i)
        waterTakenIn.append(i)
        if i== "":
            waterTakenIn.remove(i)
    return waterTakenIn,tempreture,time, soundlevel
processedList= dataProcess(tmpList)

print(processedList)
soundlevelmean= stat.mean(soundlevel)
print(soundlevelmean)
timeMean= stat.mean(time)
print(timeMean)
tempretureMean= stat.mean(tempreture)
print(tempretureMean)
waterTakenInMean= stat.mean(waterTakenIn)
print(waterTakenInMean)




print(soundlevel)
print(time)
print(tempreture)
print(waterTakenIn)
print(soundlevelmean)
print(timeMean)
print(tempretureMean)
print(waterTakenInMean)




# Avanced requirments 
studyscores=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
print(studyscores)

#What if 1: What if the noise level is to high
dataSet1=noise()
print(dataSet1)
dataProcess(dataSet1)
