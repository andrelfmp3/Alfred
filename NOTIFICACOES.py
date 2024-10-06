'''
from plyer import notification # IMPLEMENTAR DEPOIS
import time

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Seu Programa',
        timeout=10  # Duração da notificação em segundos
    )

if __name__ == "__main__":
    # Exemplo de uso
    send_notification("Alerta!", "Esta é uma notificação de exemplo.")
    time.sleep(5)  # Espera para mostrar outra notificação
    send_notification("Atualização!", "Seu programa está em execução.")
'''