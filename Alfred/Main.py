from System import System
import Funcionalities

System.iniciaPrograma() # pedir modo super usuario

system = System() # Instância da classe microfone. Não usa a classe diretamente.

audio = system.Captura_Audio()
palavras_chave = system.Audio_Para_String(audio) # Se não identificar, retorna -1

while palavras_chave != -1:
    audio = system.Captura_Audio()
    palavras_chave = system.Audio_Para_String(audio)

    if palavras_chave == "Alfred" or palavras_chave == "Alfredo": # Listas de palavras possíveis?
        Funcionalities.alfred()
    elif palavras_chave == "atualizar":
        Funcionalities.atualizar()
    elif palavras_chave == "data":
        Funcionalities.data()
    elif palavras_chave == "rebootar" or palavras_chave == "reboot":
        Funcionalities.rebootar()
    elif palavras_chave == "suspender":
        Funcionalities.suspender()
    elif palavras_chave == "desligar":
        Funcionalities.desligar()
    elif palavras_chave == "encerrar":
        System.encerraPrograma(palavras_chave)
        break
    else:
        Funcionalities.erro()

