import random
def noiseToHigh():

    dataset=[]
    for i in range(0,1000):
        tempreture= str((random.randint(10,30))) + "C"
        dataset.append(tempreture)
        water = str((random.randint(950,3000)) )+ "A"
        dataset.append(water)
        sound = str((random.randint(25,50))) + "S"
        dataset.append(sound)
    return dataset


