import statistics as stat
import matplotlib.pyplot as plt         #importing whats required 
from mean import mean
import random
from studyScore import studyscore as study
from nosieToHigh import noiseToHigh as noise
from tempToHigh import tempreture as temp
from listSorter import dataProcess as process

studyscores = []
soundlevelmeans=[]            # advanced 
tempretureMeans =[]
studyscoresTempreture=[]

graphs, ax = plt.subplots(nrows=2,ncols=2) # Advanced 3
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
print(dataIn)                 # basic 2 

tmpList= dataIn.split(",")
tmpList.remove(tmpList[-1])
#print(tmpList)

waterTakenIn,tempreture,time,soundlevel= process(tmpList)
for i in range(20):
     soundlevelmean= mean(soundlevel)
     print(soundlevelmean)
     soundlevelmeans.append(soundlevelmean) ## for loop for the graphs 
     tempretureMean= mean(tempreture)
     print(tempretureMean)
     tempretureMeans.append(tempretureMean)
timeMean= mean(time)
print(timeMean)
waterTakenInMean= mean(waterTakenIn)
print(waterTakenInMean)


if soundlevelmean > 32:
     print("The Sound Level is to loud, this may lead to ineffective study and can lead to increase in stress levels", soundlevelmean)
else: 
     print("the sound level is good for studying and will lead to reduced stress", soundlevelmean)  
if tempretureMean > 23:
     print("The Average tempreture is to hot this may lead to ineffective study and can lead to increase in stress levels",tempretureMean)              # basic 3
elif tempretureMean<18:
     print("The Average Tempreture is to cold this may lead to ineffective study and can lead to increase in stress levels", tempretureMean)
else: 
     print("The Tempreture is just right: ",tempretureMean)          





# Avanced requirments 
for i in range(20):
     studyscore=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
     #print(studyscore)
     studyscores.append(studyscore)
#studyscoresTempreture = studyscores
ax[0,0].bar(height=studyscores,x=1, color="green")
ax[0,0].bar(height = soundlevelmeans,x=2)                   #advanced 3 
ax[1,0].bar(height= studyscores,x=1, color="green")
ax[1,0].bar(height = tempreture,x=2)

#What if 1: What if the noise level is to high
dataSet1=noise()

waterTakenIn,tempreture,time,soundlevel= process(dataSet1)
for i in range(20):
     soundlevelmean= mean(soundlevel)
     #print(soundlevelmean)
     soundlevelmeans.append(soundlevelmean)
tempretureMean= mean(tempreture)
print(tempretureMean)
waterTakenInMean= int(mean(waterTakenIn))
print(waterTakenInMean)

for i in range(20):
     studyscore=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
     #print(studyscore)
     studyscores.append(studyscore)
     
print(studyscores)

print("your studyscore has decreased due to the high sound levels, this means that the study was less effective. This can lead to can lead to additonal stress" )

ax[0,1].bar(height=range(len(studyscores)),x=1 , color="green")       # advanced 3
ax[0,1].bar(height=range(len(soundlevelmeans)),x=2)



# What If question 2 what if the tempreture is ay heat wave levels
dataSet2 = temp()
#print(dataSet2)
waterTakenIn,tempreture,time,soundlevel= process(dataSet2)

soundlevelmean= mean(soundlevel)
print(soundlevelmean)
for i in range(20):
     tempretureMean= mean(tempreture)
     #print(tempretureMean)
     tempretureMeans.append(tempretureMean)
waterTakenInMean= int(mean(waterTakenIn))
print(waterTakenInMean)
for i in range(20):
     studyscore=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
     #print(studyscore)    
     studyscoresTempreture.append(studyscore)

print("your studyscore has decreased due to the high tempretures this means that the study was less effective. This can lead to can lead to additonal stress " )

ax[1,1].bar(height=studyscoresTempreture,x=1, color="green")     #advanced 3 

ax[0,0].set_title('Base Study Score')
ax[0,1].set_title('Higer Sound Levels')      # setting the titles for each graph
ax[1,0].set_title('Base Study Score')
ax[1,1].set_title('Higher Temp Levels')

ax[0, 0].set_ylim(0, max(studyscores) + 10)  
ax[0, 1].set_ylim(0, max(studyscores) + 10)  
ax[1, 0].set_ylim(0, max(studyscores) + 10)                 #setting the y axis limit for each graph
ax[1, 1].set_ylim(0, max(studyscores) + 10)  
ax[0,0].set_xticklabels([])
ax[0,1].set_xticklabels([])
ax[1,0].set_xticklabels([])
ax[1,1].set_xticklabels([])


plt.show()

# code left comment is left there was used to test outputs

