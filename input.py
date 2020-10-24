##
## Input
##
## Personal Assistent
## by Hoffle

import speech_recognition as sr


def input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('ready to listen!')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="de_DE")
        print('Du hast gesagt: ' + command)
        return command
    except sr.UnknownValueError:
        input_error = 'Ich habe dich leider nicht verstanden!'
        print(input_error)
        return input_error
