import random
def tempreture():
    dataset=[]
    for i in range(60):
        
        temps=str(random.randint(30,40)) + "C"
        dataset.append(temps)
        water = str(random.randint(950,3500)) + "A"
        dataset.append(water)
        sound = str(random.randint(10,50)) + "S"
        dataset.append(sound)
    return water, temps , sound 