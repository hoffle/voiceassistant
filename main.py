##
## Mainclass
##
## Personal Assistent
## by Hoffle

import speech_recognition as sr
import os
import re
import webbrowser
#from speech import speak




def talkToMe(audio):
    # speech to text
    print(audio)
    os.system("say" + audio)


def myCommand():
    #listen to your command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ready to listen!')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        r.adjust_for_ambient_noise()
    try:
        command = r.recognize_google(audio, language="de-DE").lower()
        print('Du hast gesagt: ' + command)
    except sr.UnknownValueError:
        print('Ich konnte dich leider nicht verstehen!')
        command = myCommand()#;

    return command

"""
def assistent(command):
    # if statements, to controll for commands
    if 'öffne seite' in command:
        reg_ex = re.search('öffne seite(.*), command')
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://' + domain
            webbrowser.open(url)
            print('Die Seite wurde nun in deinem Browser geöffnet!')
        elif 'was geht' in command:
            talkToMe('Bin gerade am chillen!')
"""



talkToMe('Ich höre dir zu und bin bereit für deine Anweisungen!')
while True:
    #
    myCommand()
    print(command)
