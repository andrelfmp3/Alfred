# Alfred

## Descrição

'**Alfred**' é o protótipo de um assistente virtual de comando de voz desenvolvido em Python, focado em facilitar a interação com o computador através de comandos de voz. **Compatível apenas com sistemas Linux**.

## Funcionalidades

- **Ativação por Palavra-Chave:** O assistente é ativado pela palavra "Alfred" e está sempre em execução.
  
- **Comandos Disponíveis:**
  - **Alfred:** comando de voz para ativar outros programas.
  - **Teste:** comando de voz para testar se programa está funcional.
  - **Reboot:** Reinicia o computador.
  - **Suspender:** Coloca o computador em modo de suspensão.
  - **Desligar:** Desliga o computador.
  - **Encerrar:** Finaliza o assistente.

## Retorno

O assistente retorna informações via terminal e comando de voz, proporcionando uma experiência rica e interativa.

## Como Começar

1. **Instalação Linux:**
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
    pip install playsound
    pip install plyer
    ```

3. **Executar:**
   - Inicie o assistente:
    ```
    python alfred.py
    ```
