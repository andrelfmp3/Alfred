import playsound # baixar

class Sounds:

    # Retorna som de aceitação do comando solicitado
    @staticmethod
    def play_positive():
        playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/positive.mp3')

    # Retorna som de negação do comando solicitado
    @staticmethod
    def play_negative():
        playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/negative.mp3')

    # Retorna som de erro do programa
    @staticmethod
    def play_erro():
        playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/erro.mp3')

    # Retorna som ao programa ser iniciado
    @staticmethod
    def play_startup():
        playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/startup.mp3')

    # Retorna som ao programa ser encerrado
    @staticmethod
    def play_turndown():
        playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/turndown.mp3')

