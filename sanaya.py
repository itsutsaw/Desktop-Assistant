import pyttsx3

import datetime
import speech_recognition as sr
import wikipedia
#import pyaudio

engine = pyttsx3.init('sapi5')
voice= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voice[1].id)


def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Welcome Utsaw ! Sanaaya Here Your Personal Assistant ! Please Enter Password")

def takecommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")

    except Exception as e:
        print(" I didnt Understand ")

        return "None"

    return query


    

if __name__ == "__main__" :

    print(" Hey ", chr(3))
    wishme()

    password = takecommand().lower()
    print(password)

    if password != 'hare krishna':
        speak(" Wrong Password Sir ! Closing the Program ")
        exit()

    else:
        speak('Welcome Utsaw ! Give me Command')
    #takecommand()

    while True:
        query= takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)



input()