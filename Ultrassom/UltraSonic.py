from __future__ import absolute_import, division, print_function, unicode_literals
from gpiozero import InputDevice, OutputDevice, Buzzer
from time import sleep, time
from math import sin, cos
import RPi.GPIO as GPIO

class UltraSonic(object):

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        
        self.trig = 17
        self.echo = 27
        self.connect = True
        while self.connect:
            try:
                GPIO.setup(self.trig, GPIO.OUT)
                GPIO.setup(self.echo, GPIO.IN)
            except:
                GPIO.cleanup()
            finally:
                GPIO.setup(self.trig, GPIO.OUT)
                GPIO.setup(self.echo, GPIO.IN)
                self.connect = False

    def get_pulse_time(self):
        GPIO.setup(self.trig, False)
        GPIO.setup(self.trig, True)
        sleep(0.0001)
        GPIO.setup(self.trig, False)

        pulse_start = 0
        pulse_end_time = 0

        while GPIO.input(self.echo) == 0:
            pulse_start = time()

        while GPIO.input(self.echo) == 1:
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
        distEnd = 0.0
        print('get dist Initial')
        distInitial = round(self.calculate_distance(self.get_pulse_time()), 2)
        sleep(0.06)
        distEnd = round(self.calculate_distance(self.get_pulse_time()), 2)
        print('if get Dist')
        if abs(distEnd - distInitial) >= 0.02 and distEnd < 4:  # tolerancia de erro do sensor

            if normal:  # se quiser normalizado entre 0 e 1
                return (4 - distEnd) / (4 - 0.02)
            else:
                return distEnd * 10
        return 0

class UltraSonic2(object):

    def __init__(self):
        self.trig = OutputDevice(17)
        self.echo = InputDevice(27)

    def get_pulse_time(self):
        self.trig.on()
        sleep(0.0001)
        self.trig.off()

        pulse_start = 0
        pulse_end_time = 0

        while not self.echo.is_active:
            pulse_start = time()

        while self.echo.is_active:
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
        distEnd = 0.0
        print('get dist Initial')
        distInitial = round(self.calculate_distance(self.get_pulse_time()), 2)
        sleep(0.06)
        distEnd = round(self.calculate_distance(self.get_pulse_time()), 2)
        print('if get Dist')
        if abs(distEnd - distInitial) >= 0.02 and distEnd < 4:  # tolerancia de erro do sensor

            if normal:  # se quiser normalizado entre 0 e 1
                return (4 - distEnd) / (4 - 0.02)
            else:
                return distEnd * 10
        return 0

