from Sounds import Sounds

@staticmethod
def alfred(): # Func teste (método?)
    Sounds.play_positive()
    print("Patrão bruce.")

@staticmethod
def erro(): # Func teste (método?)
    Sounds.play_erro()
    print("Comando desconhecido.") # Tente novamente

import os
@staticmethod
def atualizar():
    Sounds.play_positive()
    os.system("yay") # Solicita senha :()

@staticmethod
def data():
    Sounds.play_positive()
    os.system("date") # Solicita senha :()

@staticmethod
def rebootar():
    Sounds.play_positive()
    os.system("reboot")

@staticmethod
def suspender():
    Sounds.play_positive()
    os.system("systemctl suspend")

@staticmethod
def desligar():
    Sounds.play_positive()
    os.system("poweroff")