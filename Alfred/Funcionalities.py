from Sounds import Sounds
import time 
import os


@staticmethod
def erro(): # Func teste (método?)
    Sounds.play_erro()
    print("Comando desconhecido.") # Tente novamente
    
@staticmethod
def teste():
    print("Programa testado")

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
