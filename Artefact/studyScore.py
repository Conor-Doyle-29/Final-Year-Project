def studyscore(sound,time,temp,water):
    studyscore = 500
    hyrdration=0 
    if sound > 32:
        studyscore-=200
    else: 
        studyscore+=200
    
    if temp > 20 and temp<23:
        studyscore+=200
    else:
        studyscore-=200
    for i in time:

        if i > 0: 
            if i>= (791628094):
                studyscore+= 50
            if i>= (791628094*2):
                studyscore-= 50
     
    for i in range(0,3):    
        if water >= 2500:
            hyrdration+=1
        if hyrdration>0:
            studyscore=studyscore+(hyrdration*50)
    
    return studyscore
    
