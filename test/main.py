import speech_recognition as sr

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('ready to listen!')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="de_DE")
        print('Du hast gesagt: ' + command)
    except sr.UnknownValueError:
        print('Etwas ist schief gelaufen!')

myCommand()

