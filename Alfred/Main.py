from System import System
import Funcionalities

System.iniciaPrograma() # pedir modo super usuario?

system = System() # Instância da classe microfone. Não usa a classe diretamente.

audio = system.Captura_Audio()
palavras_chave = system.Audio_Para_String(audio) # Se não identificar, retorna -1

while palavras_chave != -1:

    audio = system.Captura_Audio()
    palavras_chave = system.Audio_Para_String(audio)

    if palavras_chave == "alfred":
        Funcionalities.alfred()
    elif palavras_chave == "teste":
        Funcionalities.teste()
    elif palavras_chave == "rebootar":
        Funcionalities.rebootar()
    elif palavras_chave == "suspender":
        Funcionalities.suspender()
    elif palavras_chave == "desligar":
        Funcionalities.desligar()
    elif palavras_chave == "encerrar":
        Funcionalities.encerrar()
        break
    else:
        Funcionalities.erro()
    time.sleep(0.5) # "pausar" consumo de recursos

