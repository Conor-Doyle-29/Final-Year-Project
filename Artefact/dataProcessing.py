import statistics as stat
import matplotlib.pyplot as plt         #importing whats required 
from mean import mean
import random
from studyScore import studyscore as study
from nosieToHigh import noiseToHigh as noise
from tempToHigh import tempreture as temp
from listSorter import dataProcess as process

studyscores = []
soundlevelmeans=[]
tempretureMeans =[]
studyscoresTempreture=[]

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
     print("The Sound Level is to loud", soundlevelmean)
else: 
     print("the sound level is good for studying", soundlevelmean)
if tempretureMean > 23:
     print("The Average tempreture is to hot",tempretureMean)              # advising future events
elif tempretureMean<18:
     print("The Average Tempreture is to cold", tempretureMean)
else: 
     print("The Tempreture is just right: ",tempretureMean)          





# Avanced requirments 
for i in range(20):
     studyscore=study(soundlevelmean,time,tempretureMean,waterTakenInMean)
     #print(studyscore)
     studyscores.append(studyscore)
#studyscoresTempreture = studyscores
ax[0,0].bar(height=studyscores,x=1, color="green")
ax[0,0].bar(height = soundlevelmeans,x=2)                   # setting up the graphs for the base study score
ax[1,0].bar(height= studyscores,x=1, color="green")
ax[1,0].bar(height = tempreture,x=2)

#What if 1: What if the noise level is to high
dataSet1=noise()
#print(dataSet1)
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

print("your studyscore has decreased due to the high sound levels ",studyscore )

ax[0,1].bar(height=range(len(studyscores)),x=1 , color="green")       # setting up the graph for the sound level comparison
ax[0,1].bar(height=range(len(soundlevelmeans)),x=2)



# What If question 2 what if the tempreture is to high 
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
     print(studyscore)
     studyscoresTempreture.append(studyscore)

print("your studyscore has decreased due to the high tempretures ",studyscore )

ax[1,1].bar(height=studyscoresTempreture,x=1, color="green")     # setting up the graph for the tempreture comprarison
ax[1,1].bar(height=tempretureMeans,x=2)

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



