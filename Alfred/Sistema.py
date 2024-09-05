import speech_recognition 

from Audios import Audios

class Sistema:

    # Abrir o microfone e capturar o áudio
    def CapturaAudio():
        with speech_recognition.Microphone() as source:
            Audios.play_startup()
            recognizer.adjust_for_ambient_noise(source)  # Ajustar para o ruído ambiente
            print("Fale.")
            audio = recognizer.listen(source) # variavel local (audio)

    # Usar o reconhecedor para converter o áudio em texto
    def Audio_Para_String():
        try:
            string = recognizer.recognize_google(audio, language='pt-BR') # variavel local (string)
            print(f"Eu entendi {string}. O que você quis dizer?")
        except speech_recognition.UnknownValueError:
            print("Mensagem incompreensível. Repita..") 
        except:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento; {speech_recognition.RequestError}")