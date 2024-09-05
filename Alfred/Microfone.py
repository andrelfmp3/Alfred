import speech_recognition as sr
from Sounds import Sounds

'''
Sounds.play_startup()
Sounds.play_turndown()
Sounds.play_negative()
Sounds.play_positive()
Sounds.play_erro()
'''

class Microfone:

    def __init__(self):
        self.recognizer = sr.Recognizer() # ReconhecedorDeFala
        self.microphone = sr.Microphone() 

    def Captura_Audio(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            Sounds.play_startup()
            self.recognizer.adjust_for_ambient_noise(source)             
            audio = self.recognizer.listen(source) # Problema para reconhecer fala. Mais tempo? método construido errado? Rever          
            print("Fale.")
            Sounds.play_positive() 
        return audio

    def Audio_Para_String(self, audio):
        recognizer = sr.Recognizer()
        try:
            palavraChave = recognizer.recognize_google(audio, language='pt-BR') 
            Sounds.play_positive()
            print(f"Mensagem: {palavraChave}")
        except sr.UnknownValueError:
            Sounds.play_negative
            print("Mensagem incompreensível. Repita.")
            return -1
        except sr.RequestError:
            Sounds.play_erro
            print(f"Erro ao solicitar serviço: {sr.RequestError}")
            return -1