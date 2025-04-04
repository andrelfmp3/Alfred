from Sounds import Sounds
import time
import threading
import os # nativo

key = False # variavel global "key", para ativar funcinalidades
duracaoKey = 12 # tempo que key fica ativada. Duração do programa após comando "alfred"

'''
Ativar "key", para permitir que funcionalidades funcionem.
Chama thread que ativa key por 12 segundo, após ativar alfred.
Após esse tempo, é necessário ativar novamente.
'''

class Funcionalities:

    @staticmethod
    def desativaKey():
        global key
        key = True
        print(f'~ Key ativada por {duracaoKey} segundos')
        time.sleep(duracaoKey)
        key = False

    @staticmethod
    def alfred():
        Sounds.play_startup()
        global key
        key = True
        print('~ Alfred ativado.')
        # thread = threading.Thread(target=desativaKey)
        # thread.start()

    @staticmethod
    def teste():
        if key == True:
            print('~ Testado. Alfred ativado')
        else:
            print('~ Testado. Key desativada.')

    @staticmethod
    def rebootar():
        if key == True:
            Sounds.play_positive()
            os.system('reboot')
        else:
            print('~ Tentativa de reboot. Key desativada.')

    @staticmethod
    def suspender():
        if key == True:
            Sounds.play_positive()
            os.system('systemctl suspend')
        else:
            print('~ Tentativa de suspender. Key desativada.')

    @staticmethod
    def desligar():
        if key == True:
            Sounds.play_positive()
            os.system('poweroff')
        else:
            print('~ Tentativa de desligar. Key desativada.')

    @staticmethod
    def encerrar():
        if key == True:
            print('~ Encerrando programa.')
            Sounds.play_turndown()
        else:
            print('~ Tentativa de encerrar. Key desativada.')

    @staticmethod
    def erro():
        if key == True:
            Sounds.play_erro()
            print('~ Retorno de "erro"')
        else:
            print('~ Tentativa de retornar "erro". Key desativada.')

