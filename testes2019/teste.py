from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from time import sleep, time

motor0 = PWMOutputDevice(6)
motor1 = PWMOutputDevice(24)
motor2 = PWMOutputDevice(19)
motor3 = PWMOutputDevice(26)

i0 = 0.0002
i00 = 0.0001
i1 = 0.15
i11 = 0.0001
i2 = 0.0002
i22 = 0.0001
i3 = 0.0002
i33 = 0.0001
i = 0.0001
token = 0
while(True):
    if(i0 > 0.0001 and token == 0):
        i0 = i0 + i00
    elif(i00 < 0 and  i0 > 0.0001):
        i0 = i0 + i00
    if(i0 > 0.9):
        i00 = -i
        token = 1
        print("1")
    if(i0 < 0.0001 and token == 0):
        i0 = i
        i00 = i
    
    if(i1 > 0.0001 and token == 1):
        i1 = i1 + i11
    elif(i11 < 0 and i1 > 0.0001):
        i1 = i1 + i11
    if(i1 > 0.9):
        i11 = -i
        token = 2
        print("2")
    if(i1 < 0.0001 and token == 1):
        i1 = i
        i11 = i

    if(i2 > 0.0001 and token == 2):
        i2 = i2 + i22
    elif(i22 < 0 and i2 > 0.0001):
        i2 = i2 + i22
    if(i2 > 0.9):
        i22 = -i
        token = 3
        i3 = 0.0002
        i33 = i
        print("3")
    if(i2 < 0.0001 and token == 2):
        i2 = i
        i22 = i

    if(i3 > 0.0001 and token == 3):
        i3 = i3 + i33
    elif(i33 < 0 and i3 > 0.0001):
        i3 = i3 + i33
    if(i3 > 0.9):
        i33 = -i
        token = 0
        i0 = 0.0002
        i00 = i
        i1 = 0.0002
        i11 = i
        i2 = 0.0002
        i22 = i
        print("0")
    if(i3 < 0.0001 and token == 3):
        i3 = i
        i33 = i
    
    motor0.value = i0
    motor1.value = i1
    motor2.value = i2
    motor3.value = i3

        