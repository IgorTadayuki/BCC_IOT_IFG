from __future__ import absolute_import, division, print_function, unicode_literals
from gpiozero import InputDevice, OutputDevice
from time import sleep, time


class UltraSonic(object):

    def __init__(self):

        self.trig = OutputDevice(22)
        self.echo = InputDevice(27)

    def get_pulse_time(self):
        self.trig.on()
        sleep(0.00001)
        self.trig.off()

        pulse_start = 0
        pulse_end_time = 0

        while self.echo.is_active == False:
            pulse_start = time()

        while self.echo.is_active == True:
            pulse_end_time = time()

        sleep(0.06)
        return pulse_end_time - pulse_start

    def calculate_distance(self, duration):
        velocidade = 343
        dist = velocidade * duration / 2
        # return dist * 100 # transform to meters
        return dist

    def getDist(self, normal=False):
        distInitial = 0.0
        print('get dist Initial')
        distInitial = round(self.calculate_distance(self.get_pulse_time()), 2)

        if normal:  # se quiser normalizado entre 0 e 1
            return (4 - distInitial) / (4 - 0.02)
        else:
            return distInitial * 100