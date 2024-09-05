from Microfone import Microfone

microfone = Microfone() # Instância da classe microfone. Não usa a classe diretamente.

audio = microfone.Captura_Audio()
valor = microfone.Audio_Para_String(audio) # Se não identificar, retorna -1

while valor == -1:
    audio = microfone.Captura_Audio()
    valor = microfone.Audio_Para_String(audio)
