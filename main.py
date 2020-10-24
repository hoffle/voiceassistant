##
## Mainclass
##
## Personal Voice Assistent
## by Hoffle

# own functions
from output import voice_output
from input import voice_input

import speech_recognition as sr

#input()
voice_command = str
input = voice_input(voice_command)
print(input)
#print(voice_command)

