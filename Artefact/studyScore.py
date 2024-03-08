def studyscore(sound,time,temp,water):
    studyscore = 50
    hyrdration=0 
    if sound > 32:
        studyscore-=20
    else: 
        studyscore+=20
    
    if temp > 20 and temp<23:
        studyscore+=20
    else:
        studyscore-=20
    for i in time:

        if i > 0: 
            if i>= (791628094):
                studyscore+= 5
            if i>= (791628094*2):
                studyscore-= 5
     
    for i in range(0,3):    
        if water >= 2500:
            hyrdration+=1
        if hyrdration>0:
            studyscore=studyscore+(hyrdration*5)
    
    return studyscore
    
