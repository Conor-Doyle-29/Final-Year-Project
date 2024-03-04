def dataProcess(dataset):
    soundlevel = []
    time=[]                 # estabhlising lists 
    tempreture = []
    waterTakenIn = []
    tmpSound = []
    tmpTime=[]
    tmpTemp=[]
    TmpWater=[]
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