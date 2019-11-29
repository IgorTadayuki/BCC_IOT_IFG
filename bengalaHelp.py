from Bussola.bussola import CommandsBussola
from Ultrassom.UltraSonic import UltraSonic
from SensorVibracao.vibracaoMotor import Vibration
from Botoes import helpBotao
from gpiozero import PWMOutputDevice
import time
import threading
import RPi.GPIO as GPIO

class Helps(object):
    def __init__(self, gpioMotor=4, tolerancia=8):
        self.gpioMotor = gpioMotor
        self.motor = PWMOutputDevice(self.gpioMotor)
        self.tolerancia = tolerancia
        self.stopped = True
        self.commands = CommandsBussola()
        self.distancia = 99999

    def getVariation(self, anguloInicial):

        angle = self.commands.getAngleHorizontal()

        torelanciaAnterior = self.tolerancia
        vibracao = 0
        numVariacoes = 5
        variacaoVibracao = 1 / numVariacoes - 0.01
        variacaoTolerancia = 10
        for i in range(numVariacoes):
            if anguloInicial - self.tolerancia <= angle <= anguloInicial + self.tolerancia:
                self.tolerancia = torelanciaAnterior
                return vibracao
            elif anguloInicial + self.tolerancia > 360 or anguloInicial - self.tolerancia < 0:
                if anguloInicial + self.tolerancia > 360:
                    if angle + 360 > anguloInicial + self.tolerancia:
                        vibracao += variacaoVibracao
                        self.tolerancia += variacaoTolerancia
                elif anguloInicial - self.tolerancia < 0:
                    if angle - 360 < anguloInicial - self.tolerancia:
                        vibracao += variacaoVibracao
                        self.tolerancia += variacaoTolerancia
            else:
                vibracao += variacaoVibracao
                self.tolerancia += variacaoTolerancia

        self.tolerancia = torelanciaAnterior
        return vibracao

    def atualizarDist(self, ultrassom):
        while True:
            self.distancia = ultrassom.getDist()

    def run(self):
        # print('Started run function:')
        ultrassom = UltraSonic()
        # print('Started run UltraSonic:')
        respostaTatil = Vibration()
        # print('Started run Vibration:')
        botaoPressionado = True
        botaoPressionadoAnterior = False
        # print('Started main while')

        try:
            t = threading.Thread(target=self.atualizarDist, args=(ultrassom,))
            t.start()
        except:
            print("Error: unable to start thread")

        try:
            while True:

                # print('distancia:' + str(self.distancia))
                botaoPressionado = helpBotao.getEstado(botaoPressionado)
                print('botaoPressionado' + str(botaoPressionado))
                if botaoPressionado:
                    if not botaoPressionadoAnterior:
                        anguloInicial = self.commands.getAngleHorizontal()
                        botaoPressionadoAnterior = True
                    # print('angulo inicial:' + str(anguloInicial))
                    vibrationValue = self.getVariation(anguloInicial)
                    # print('vibrationValue:' + str(vibrationValue))
                    print('emite_vibracao_linha_reta' + str(vibrationValue))
                    respostaTatil.emite_vibracao_linha_reta(vibrationValue)
                else:
                    respostaTatil.emite_vibracao_linha_reta(0.001)
                    botaoPressionadoAnterior = False
                print('distancia:' + str(self.distancia))
                respostaTatil.olhando_frente(self.distancia)
                # anguloVertical = self.commands.getAngleVertical()
                time.sleep(0.1)
        except:
            print('erro na execucao')
        finally:
            GPIO.cleanup()
