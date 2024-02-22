def studyscore(sound,time,temp,water):
    studyscore = 100
    for i in sound: 
        counter =0 
        if i > 40:
            counter+=1
        else: 
            counter = 0 
        if counter == 5: 
            studyscore= studyscore-2 
    for i in time:
        if time > 0: 
            if time>= (30*6000):
                studyscore+= 5
    
