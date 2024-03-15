import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for p in ports:
    print(p.device)                 # task 1
print(len(ports), 'ports found') 

