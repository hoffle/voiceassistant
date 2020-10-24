##
## speech output
##
## Personal Voice Assistent
## by Hoffle

import os
import subprocess
from gtts import gTTS


def voice_output(text):
    tts = gTTS(text=text, lang='de')
    if os.path.exists('./audiodateien/output.mp3'):
        os.remove('./audiodateien/output.mp3')
    tts.save('./audiodateien/output.mp3')
    subprocess.call(['afplay', './audiodateien/output.mp3'])
