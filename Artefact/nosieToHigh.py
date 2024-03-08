import random
def noiseToHigh():

    dataset=[]
    for i in range(60):
        tempreture= str((random.randint(10,35))) + "C"
        dataset.append(tempreture)
        water = str((random.randint(950,3000)) )+ "A"
        dataset.append(water)
        sound = str((random.randint(50,75))) + "S"
        dataset.append(sound)
    return water,tempreture, sound


