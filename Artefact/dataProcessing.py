import statistics as stat
import matplotlib.pyplot as plt         #importing whats required 
import collections 
import random
from studyScore import studyscore as study
from nosieToHigh import noiseToHigh as noise
from tempToHigh import tempreture as temp
from listSorter import dataProcess as process

studyscores = []
'''''
soundlevel = []
time=[]                 # estabhlising lists 
tempreture = []
waterTakenIn = []
tmpSound = []
tmpTime=[]
tmpTemp=[]
TmpWater=[]
'''

file=open("tmp.csv","r")
dataIn=file.read()
file.close
print(dataIn)

tmpList= dataIn.split(",")
tmpList.remove(tmpList[-1])
print(tmpList)

waterTakenIn,tempreture,time,soundlevel= process(tmpList)

soundlevelmean= stat.mean(soundlevel)
print(soundlevelmean)
timeMean= stat.mean(time)
print(timeMean)
tempretureMean= stat.mean(tempreture)
print(tempretureMean)
waterTakenInMean= stat.mean(waterTakenIn)
print(waterTakenInMean)


if soundlevelmean > 32:
     print("The Sound Level is to loud", soundlevelmean)
else: 
     print("the sound level is good for studying", soundlevelmean)
if tempretureMean > 23:
     print("The Average tempreture is to hot",tempretureMean)
elif tempretureMean<18:
     print("The Average Tempreture is to cold", tempretureMean)
else: 
     print("The Tempreture is just right: ",tempretureMean)          

'''
print(soundlevel)
print(time)
print(tempreture)
print(waterTakenIn)
print(soundlevelmean)
print(tempretureMean)
print(waterTakenInMean)
'''


for i in range(20):
     studyscore=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
     print(studyscore)
     studyscores.append(studyscore)
# Avanced requirments 


#What if 1: What if the noise level is to high
dataSet1=noise()
#print(dataSet1)
waterTakenIn,tempreture,time,soundlevel= process(dataSet1)

soundlevelmean= stat.mean(soundlevel)
print(soundlevelmean)
tempretureMean= stat.mean(tempreture)
print(tempretureMean)
waterTakenInMean= stat.mean(waterTakenIn)
print(waterTakenInMean)

for i in range(20):
     studyscore=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
     print(studyscore)
     studyscores.append(studyscore)
print(studyscores)
plt.plot(studyscores, label="Study Score", color="green")
plt.plot(soundlevel, label="Sound Level")
plt.show()

# What If question 2 what if the tempreture is to high 
dataSet2 = temp()
print(dataSet2)
waterTakenIn,tempreture,time,soundlevel= process(dataSet2)

soundlevelmean= stat.mean(soundlevel)
print(soundlevelmean)
tempretureMean= stat.mean(tempreture)
print(tempretureMean)
waterTakenInMean= stat.mean(waterTakenIn)
print(waterTakenInMean)
for i in range(20):
     studyscore=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
     print(studyscore)
     studyscores.append(studyscore)


