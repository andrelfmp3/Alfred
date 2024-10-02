import speech_recognition as sr
from plyer import notification
from Sounds import Sounds
import time
import os

class System:

    def __init__(self):
        self.recognizer = sr.Recognizer() # ReconhecedorDeFala
        self.microphone = sr.Microphone()

    def iniciaPrograma():

        Sounds.play_startup() # toca no meio da "animação"

        print("\n")
        time.sleep(0.02)
        print('     ___    ______              __   ')
        time.sleep(0.02)
        print('    /   |  / / __/_______  ____/ /   | ')
        time.sleep(0.02)
        print('   / /| | / / /_/ ___/ _ \/ __  /    | Like Jarvis, but cooler')
        time.sleep(0.02)
        print('  / ___ |/ / __/ /  /  __/ /_/ /     | Developed by andrelfmp3')
        time.sleep(0.02)
        print(' /_/  |_/_/_/ /_/   \___/\__,_/      | https://andrelfmp3.github.io/')
        time.sleep(0.02)
        print('_____________________________________|')


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
            print(f"Mensagem: {palavraChave.lower()}")
            return  palavraChave.lower()
        except sr.UnknownValueError:
            Sounds.play_negative()
            print("Mensagem incompreensível. Repita.")
        except sr.RequestError:
            Sounds.play_erro()
            print(f"Erro ao solicitar serviço: {sr.RequestError}")
            return -1

    def encerraPrograma(self):
        Sounds.play_turndown()



