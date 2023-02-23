# from Body.Speak import Speak
# from Features.Clap import Tester

# def Main():
#     Tester()
#     Speak("Welcome Sir!")

# if __name__ == "__main__":
#     Main()


import speech_recognition as sr
import os
from Jaz import MainExe

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en")

    except:
        return ""
        
    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    query = Listen().lower()

    if "wake up" in query:
        print("I am awake sir")
        MainExe()

    else:
        pass

while True:
    WakeupDetected()
