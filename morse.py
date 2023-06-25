#
#  Write morse code through the default audio interface
#
#  MIT (c) 2023 René Oudeweg
#

import subprocess
import time

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}


def text_to_morse(text):
    morse = []
    for char in text.upper():
        if char in morse_code:
            morse.append(morse_code[char])
    return ' '.join(morse)

# speaker-test -p 1000 -t wav -c 6 -s 6 -w /home/reinold/morsedot.wav


def beep_morse_code(morse_code):
    for char in morse_code:
        if char == '.':
            subprocess.call(['speaker-test', '-p', '1000', '-t', 'wav', '-c', '6', '-s', '6', '-w', '/home/reinold/morsedot.wav'])
            #subprocess.call(['speaker-test', '-t', 'wav', '-w', '/home/reinold/morsedot.wav'])
        elif char == '-':
            subprocess.call(['speaker-test', '-p', '1000', '-t', 'wav', '-c', '6', '-s', '6', '-w', '/home/reinold/morsedash.wav'])
            #subprocess.call(['speaker-test', '-t', 'wav', '-w', '/home/reinold/morsedash.wav'])
        time.sleep(0.1)


text = input("Enter the text to translate to Morse code: ")
translated_text = text_to_morse(text)
print("Translated text in Morse code: ", translated_text)
repeat = input("Enter time to repeat: ")
n = int(repeat)

for i in range(n):
        beep_morse_code(translated_text)
        time.sleep(0.3)
        
