from morse_audio_decoder.morse import MorseCode
import sys

argc = len(sys.argv)
if argc == 1:
    print("decodemorse2 [file]")
    exit
wavfile = sys.argv[1]  
morse_code = MorseCode.from_wavfile(wavfile)
out = morse_code.decode()
print(out)
