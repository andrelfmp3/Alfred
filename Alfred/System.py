import speech_recognition as sr
from Sounds import Sounds
import time

'''
Sounds.play_startup()
Sounds.play_turndown()
Sounds.play_negative()
Sounds.play_positive()
Sounds.play_erro()
'''

class System:

    def __init__(self):
        self.recognizer = sr.Recognizer() # ReconhecedorDeFala
        self.microphone = sr.Microphone() 

    def iniciaPrograma():

        Sounds.play_startup() # toca no meio da "animação"

        print('    ___    ______              __ ')
        time.sleep(0.02)
        print('   /   |  / / __/_______  ____/ / ')
        time.sleep(0.02)
        print('  / /| | / / /_/ ___/ _ \/ __  /  ')
        time.sleep(0.02)
        print(' / ___ |/ / __/ /  /  __/ /_/ /   ')
        time.sleep(0.02)
        print('/_/  |_/_/_/ /_/   \___/\__,_/    \n') 




    def Captura_Audio(self):
        recognizer = sr.Recognizer() # Necessita construtor
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source) # Necessita construtor
            Sounds.play_positive() # retorno em audio
            print("~ Ouvindo.")   
            audio = self.recognizer.listen(source) # Necessita construtor
        return audio

    def Audio_Para_String(self, keyword):
        recognizer = sr.Recognizer()
        try:
            palavraChave = recognizer.recognize_google(keyword, language='pt-BR') 
            print(f"Mensagem: {palavraChave}")
            return  palavraChave
        except sr.UnknownValueError:
            Sounds.play_negative()
            print("Mensagem incompreensível. Repita.")
            return -1
        except sr.RequestError:
            Sounds.play_erro()
            print(f"Erro ao solicitar serviço: {sr.RequestError}")
            return -1