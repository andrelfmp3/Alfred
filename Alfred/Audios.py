import playsound

class Audios:
    
    @staticmethod
    def play_positive():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Audios/positive.mp3')
    
    @staticmethod
    def play_negative():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Audios/negative.mp3')
    
    @staticmethod
    def play_erro():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Audios/erro.mp3')

    @staticmethod
    def play_startup():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Audios/startup.mp3')
    
    @staticmethod
    def play_turndown():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Audios/turndown.mp3')
