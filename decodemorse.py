import wave
import numpy as np

# Morse code dictionary
morse_code = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0'
}

def decode_morse_code(morse):
    words = morse.split(' / ')
    decoded_message = ''
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in morse_code:
                decoded_message += morse_code[letter]
        decoded_message += ' '
    return decoded_message.strip()

def decode_morse_from_wav(filename):
    with wave.open(filename, 'rb') as wav_file:
        # Get audio properties
        framerate = wav_file.getframerate()
        nframes = wav_file.getnframes()

        # Read audio data
        audio_data = np.frombuffer(wav_file.readframes(nframes), dtype=np.int16)

        # Compute threshold for detecting Morse code signal
        threshold = np.max(np.abs(audio_data)) * 0.6

        # Process audio data and extract Morse code
        morse_signal = ''
        is_signal = False
        for sample in audio_data:
            if abs(sample) >= threshold:
                is_signal = True
            else:
                if is_signal:
                    morse_signal += ' ' if morse_signal else ''
                    morse_signal += '.' if sample > 0 else '-'
                is_signal = False

    print("Morse: "+morse_signal)
    # Decode Morse code
    decoded_text = decode_morse_code(morse_signal)

    return decoded_text

# Usage example
wav_file_path = '/home/reinold/test/morse_code.wav'
decoded_text = decode_morse_from_wav(wav_file_path)
print(decoded_text)

