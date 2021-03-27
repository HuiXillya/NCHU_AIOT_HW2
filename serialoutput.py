import serial
from time import sleep
import sys
import json

COM_PORT = 'COM3'  # 請自行修改序列埠名稱
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)

f=open(r"C:\Users\Hui\Desktop\AIoT\badapple.json",'r')
all_d=json.loads(f.read())
f.close()


try:
    i=0
    # ser.write(bytearray([0,0,0]))
    for k in range(8):
        ser.write(bytearray([0,0,0,0,0,0,0,0]))
    sleep(5)
    for key, value in all_d.items():
        i+=1
        for x in value:
            ser.write(bytearray(x))
            # print(bytearray(x))
        sleep(1/4)
        if(i>3):
            pass

        
except KeyboardInterrupt:
    ser.close()    # 清除序列通訊物件
    print('再見！')

