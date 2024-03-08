import statistics as stat
import matplotlib.pyplot as plt         #importing whats required 
import collections 
import random
from studyScore import studyscore as study
from nosieToHigh import noiseToHigh as noise
from tempToHigh import tempreture as temp
from listSorter import dataProcess as process

studyscores = []
soundlevelmeans=[]
tempretureMeans =[]

graphs, ax = plt.subplots(nrows=2,ncols=2) ###https://pieriantraining.com/matplotlib-tutorial-how-to-have-multiple-plots-on-same-figure/#:~:text=In%20Matplotlib%2C%20subplots%20are%20a,is%20used%20to%20create%20subplots.
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
for i in range(20):
     soundlevelmean= stat.mean(soundlevel)
     print(soundlevelmean)
     soundlevelmeans.append(soundlevelmean) ## for loop for the graphs 
     tempretureMean= stat.mean(tempreture)
     print(tempretureMean)
     tempretureMeans.append(tempretureMean)
timeMean= stat.mean(time)
print(timeMean)
waterTakenInMean= stat.mean(waterTakenIn)
print(waterTakenInMean)


if soundlevelmean > 32:
     print("The Sound Level is to loud", soundlevelmean)
else: 
     print("the sound level is good for studying", soundlevelmean)
if tempretureMean > 23:
     print("The Average tempreture is to hot",tempretureMean)              # advising future events
elif tempretureMean<18:
     print("The Average Tempreture is to cold", tempretureMean)
else: 
     print("The Tempreture is just right: ",tempretureMean)          



for i in range(20):
     studyscore=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
     print(studyscore)
     studyscores.append(studyscore)
studyscoresTempreture = studyscores
ax[0,0].bar(height=range(len(studyscores)),x=1, color="green")
ax[0,0].bar(height = range(len(soundlevel)),x=2)
ax[1,0].bar(height= range(len(studyscores)),x=1)
ax[1,0].bar(height = range(len(tempreture)),x=2)

# Avanced requirments 


#What if 1: What if the noise level is to high
dataSet1=noise()
#print(dataSet1)
waterTakenIn,tempreture,time,soundlevel= process(dataSet1)
for i in range(20):
     soundlevelmean= stat.mean(soundlevel)
     print(soundlevelmean)
     soundlevelmeans.append(soundlevelmean)
     tempretureMean= stat.mean(tempreture)
     print(tempretureMean)
     tempretureMeans.append(tempretureMean)
waterTakenInMean= stat.mean(waterTakenIn)
print(waterTakenInMean)

for i in range(20):
     studyscoresTest=[]
     studyscore=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
     print(studyscore)
     studyscores.append(studyscore)
     studyscoresTest.append(studyscore)
print(studyscores)


ax[0,1].bar(height=range(len(studyscores)),x=1 , color="green")
ax[0,1].bar(height=range(len(soundlevel)),x=2)



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
     studyscoresTempreture.append(studyscore)

ax[1,1].bar(height=range(len(studyscores)),x=1)
ax[1,1].bar(height=range(len(tempreture)),x=2)

ax[0,0].set_title('Base Study Score')
ax[0,1].set_title('Higer Sound Levels')
ax[1,0].set_title('Base Study Score')
ax[1,1].set_title('Higher Temp Levels')
plt.show()

print(studyscoresTest)


