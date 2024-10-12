import speech_recognition as sr
from Funcionalities import key
import Funcionalities
# from plyer import notification
from Sounds import Sounds
import time
import os

class System:

    def __init__(self):
        self.recognizer = sr.Recognizer() # ReconhecedorDeFala
        self.microphone = sr.Microphone()

    @staticmethod
    def iniciaPrograma():
        print("\n")
        time.sleep(0.02)
        print('     ___    ______              __   ')
        time.sleep(0.02)
        print('    /   |  / / __/_______  ____/ /   | ')
        time.sleep(0.02)
        print('   / /| | / / /_/ ___/ _ \/ __  /    | ')
        time.sleep(0.02)
        print('  / ___ |/ / __/ /  /  __/ /_/ /     | Developed by andrelfmp3')
        time.sleep(0.02)
        print(' /_/  |_/_/_/ /_/   \___/\__,_/      | Like Jarvis, but polished.')
        time.sleep(0.02)
        print('________________________________v1.0_|\n')


    def Captura_Audio(self):
        recognizer = sr.Recognizer() # Necessita construtor
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source) # Necessita construtor
            global key
            print("~ Tentativa de ouvir.")
            if key:
                Sounds.play_positive() # retorno em audio
                print("~ Ouvindo. (key ativada)")
            audio = self.recognizer.listen(source) # Necessita construtor
        return audio

    def Audio_Para_String(self, keyword):
        recognizer = sr.Recognizer()
        try:
            palavraChave = recognizer.recognize_google(keyword, language='pt-BR') 
            print(f"~ Mensagem: {palavraChave.lower()}")
            return  palavraChave.lower()
        except sr.UnknownValueError:
            if key:
                Sounds.play_negative()
                print("~ Mensagem incompreensível. Repita.")
        except sr.RequestError:
            if key:
                Sounds.play_erro()
                print(f"~ Erro ao solicitar serviço: {sr.RequestError}")
            return -1
