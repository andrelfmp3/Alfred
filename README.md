# Alfred

**Like Jarvis, but cooler!**

## Descrição

'Alfred' é um assistente virtual de comando de voz desenvolvido em Python, focado em facilitar a interação com o computador através de comandos de voz.

## Objetivos

- **Interação por Voz:** O projeto visa proporcionar uma experiência de usuário fluida, onde o assistente responde a comandos de voz e também fornece feedback sonoro.

## Funcionalidades

- **Ativação por Palavra-Chave:** O assistente é ativado pela palavra "Alfred" e está sempre em execução. Ele também responde a ocorrências de "alfred" ou "alfredo" no meio de uma string (em letras minúsculas).
  
- **Comandos Disponíveis:**
  - **Alfred:** comando de voz para ativar outros programas.
  - **Teste:** comando de voz para testar funcionalidade do programa.
  - **Reboot:** Reinicia o computador.
  - **Suspender:** Coloca o computador em modo de suspensão.
  - **Desligar:** Desliga o computador.
  - **Encerrar:** Finaliza o assistente.

## Retorno

O assistente retorna informações via terminal, notificação, e comando de voz, proporcionando uma experiência rica e interativa.

## Como Começar

1. **Instalação:**
   - Clone este repositório:
    ```
    git clone https://github.com/andrelfmp3/alfred
    cd alfred
    ```

2. **Dependências:**
   - Instale as dependências necessárias:
    ```
    pip install SpeechRecognition
    pip install pyaudio
    pip install playaudio
    pip install plyer
    ```

3. **Executar:**
   - Inicie o assistente:
    ```
    python alfred.py
    ```

## Licença

Este projeto é licenciado sob a MIT License. 

---

