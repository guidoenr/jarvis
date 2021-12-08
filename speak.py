import speech_recognition as sr
import warnings

def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio)
        print(data)
    except:
        print('nothig')
