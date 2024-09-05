import playsound

class Sounds:
    
    @staticmethod
    def play_positive():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/positive.mp3')
    
    @staticmethod
    def play_negative():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/negative.mp3')
    
    @staticmethod
    def play_erro():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/erro.mp3')

    @staticmethod
    def play_startup():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/startup.mp3')
    
    @staticmethod
    def play_turndown():
            playsound.playsound('/home/andrelf/Documents/GitHub/Alfred/Sounds/turndown.mp3')
