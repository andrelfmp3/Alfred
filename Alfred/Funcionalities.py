from Sounds import Sounds
import time
import threading
import os

key = False # variavel global

@staticmethod
def erro():
    Sounds.play_erro()
    print("Comando desconhecido.") 
    
@staticmethod
def alfred():
    global key
    key = True
    print("Alfred ativado.")
    thread = threading.Thread(target=desativaKey)
    thread.start()
    # thread, chama por 10 segundo, e volta para ativado = False

@staticmethod
def desativaKey():
    time.sleep(10)
    global key
    key = False

@staticmethod
def teste():
    if key == True:
        print("Teste. Alfred ativado")
    elif key == False:
        print("Teste. Alfred desativado")

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

@staticmethod
def encerrar():
    print("Encerrando programa.")
    Sounds.play_turndown()



