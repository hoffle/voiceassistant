##
## speech output
##
## Personal Assistent
## by Hoffle

import os
import subprocess
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang='de')
    if os.path.exists(r'output.mp3'):
        os.remove(r'output.mp3')
    tts.save('./output.mp3')
    subprocess.call(['afplay', './output.mp3'])
