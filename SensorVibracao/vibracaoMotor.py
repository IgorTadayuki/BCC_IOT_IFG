from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from time import sleep, time


class Vibration(object):
    def __init__(self):
        self.motor0 = PWMOutputDevice(6)
        self.motor1 = PWMOutputDevice(24)
        self.motor2 = PWMOutputDevice(19)
        self.motor3 = PWMOutputDevice(26)
        self.vibracao_total = 0.9
        self.vibracao_media = 0.4
#         self.obstaculo_proximo = 0.2  # ~0.5 metros
#         self.distancia_media = 0.5  # ~2 metros
#         self.distancia_longa = 0.7  # ~3 metros

#     def olhando_frente_deprecated(self, distancia_corrente):
#         # objeto esta proximo, realiza vibração forte continua no motor 0 por 2 segundo
#         if (distancia_corrente <= self.obstaculo_proximo):
#             self.motor0.value = self.vibracao_total
#             sleep(4)
#         # objeto esta a uma distancia média, fara 2 vibrações fortes(por meio segundo cada) em intervalos de 0.05 segundo entre ambas.
#         elif (distancia_corrente <= self.distancia_media and distancia_corrente > self.obstaculo_proximo):
#             self.motor0.value = self.vibracao_total
#             sleep(6)
#             self.motor0.value = 0
#             sleep(2)
#             self.motor0.value = self.vibracao_total
#             sleep(6)
#             self.motor0.value = 0
#         # se o objeto esta a uma distancia longa, realizará uma vibração(média) no motor 3, de modo continuo
#         elif (distancia_corrente >= self.distancia_longa):
#             self.motor0.value = self.vibracao_media
#         # se não tiver nada em frente.
#         else:
#             self.motor0.value = 0

#     # entre 0 e 1,, onde 0 esta em linha, reta... e de acordo que se aproxima de 1! esta se desviando da linha reta.
#     def emite_vibracao_linha_reta_deprecated(self, distancia):
#         self.motor1.value = round(distancia, 2)

#     # entre 0 e 1 (1 é pq tem um buraco grande)
#     def olhando_chao_deprecated(self, distancia):
#         self.motor2.value = round(distancia, 2)
        
    def olhando_chao(self, distancia):
        
        if       distancia >= 1:
            self.motor0.value = self.vibracao_total
            self.motor1.value = self.vibracao_total
            self.motor2.value = self.vibracao_total
        elif     distancia > 0.75:
            self.motor0.value = self.vibracao_total
            self.motor1.value = self.vibracao_total
            self.motor2.value = self.vibracao_media
        elif     distancia == 0.75:       
            self.motor0.value = self.vibracao_total
            self.motor1.value = self.vibracao_total
            self.motor2.value = 0.0     
        elif     distancia > 0.5:        
            self.motor0.value = self.vibracao_total
            self.motor1.value = self.vibracao_media
            self.motor2.value = 0.0                
        elif     distancia == 0.5:          
            self.motor0.value = self.vibracao_total
            self.motor1.value = 0.0
            self.motor2.value = 0.0              
        elif     distancia > 0.25:       
            self.motor0.value = self.vibracao_media
            self.motor1.value = 0.0
            self.motor2.value = 0.0     
        elif     distancia <= 0.25:       
            self.motor0.value = 0.0
            self.motor1.value = 0.0
            self.motor2.value = 0.0     
