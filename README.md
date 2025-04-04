# Alfred

**[Versão em Português](README-PT.md)**

## Description

'**Alfred**' is the prototype of a voice command virtual assistant developed in Python, focused on facilitating interaction with the computer through voice commands. **Only compatible with Linux systems**.

## Features

- **Keyword Activation:** The assistant is activated by the word "Alfred" and is always running.
  
- **Available Commands:**
  - **Alfred:** voice command to activate other programs.
  - **Test:** voice command to test if the program is functional.
  - **Reboot:** Reboots the computer.
  - **Suspend:** Puts the computer in suspend mode.
  - **Shutdown:** Shuts down the computer.
  - **Exit:** Terminates the assistant.

## Output

The assistant provides information via terminal and voice command, offering a rich and interactive experience.

## Getting Started

1. **Linux Installation:**
   - Clone this repository:
    ```
    git clone https://github.com/andrelfmp3/alfred
    cd alfred
    ```

2. **Dependencies:**
   - Install the necessary dependencies:
    ```
    pip install SpeechRecognition
    conda install conda-forge::speechrecognition

    pip install playsound

    pip install pyaudio
    
    pip install playaudio
    ```

3. **Run:**
   - Start the assistant:
    ```
    python alfred.py
    ```
