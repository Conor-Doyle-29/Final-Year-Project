import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port= 'COM19 '
ser.open()
#pg 93 
while True:
    data=str(ser.readline())
    data= data.replace("b", "")                 # task 2
    data= data.replace("'", "")
    data= data.replace(" ", "")
    data= data.replace("\\r\\n", "")
    if len(data) >0:
        print(data)
        file= open ("tmp.csv",'a')
        file.write(data+",")
        file.close()  