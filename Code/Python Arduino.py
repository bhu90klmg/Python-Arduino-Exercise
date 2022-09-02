# -*- coding: utf-8 -*-
import serial 
import time
ser = serial.Serial('COM3', 9600, timeout=0.5)
ser.open
time.sleep(3)
try:
    while True:
        for i in range(20):
            line=ser.readline()
            if line!=b'':
                print("datal:",line)
except KeyboardInterrupt:
    ser.close()    
            

