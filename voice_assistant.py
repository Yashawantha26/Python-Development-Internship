import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

try:
    command = r.recognize_google(audio)
    print("You said:", command)

    if "hello" in command.lower():
        speak("Hello, how can I help you?")

    elif "time" in command.lower():
        from datetime import datetime
        speak(str(datetime.now().strftime("%H:%M")))
except:
    speak("Sorry, I could not understand.")