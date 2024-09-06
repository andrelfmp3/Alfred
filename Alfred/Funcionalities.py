from Sounds import Sounds
import time

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
def atualizar(): # func terminal
    Sounds.play_positive()
    os.system("sudo pacman -Sy") # Solicita senha :()
    time.sleep(5)
    os.system("void")

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
