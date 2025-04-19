import eel
import pyttsx3
import speech_recognition
from GreetMe import greetMe
from utils import speak
import os

eel.init("frontend")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

@eel.expose
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

@eel.expose
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Error:", e)
        return ""

@eel.expose
def processCommand():
    query = takeCommand()
    if not query:
        return {"status": "error", "message": "Could not understand audio"}

    if "wake up" in query:
        greetMe()
        return {"status": "success", "message": "awake"}
    
    elif "go to sleep" in query:
        speak("Ok sir, you can call me anytime")
        return {"status": "success", "message": "sleep"}
    
    elif "hello" in query:
        speak("Hello sir, how are you?")
        return {"status": "success", "message": "Hello response"}
    
    elif "i am fine" in query:
        speak("That's great sir")
        return {"status": "success", "message": "Fine response"}
    
    elif "how are you" in query:
        speak("Perfect sir")
        return {"status": "success", "message": "How are you response"}
    
    elif "thank you" in query:
        speak("You're welcome sir")
        return {"status": "success", "message": "Welcome response"}
    
    else:
        speak("I didn't understand that")
        return {"status": "success", "message": "Unknown command"}

if __name__ == "__main__":
    os.system('start msedge.exe --app="http://127.0.0.1:8000/index.html"')
    
    
    
    eel.start("index.html", mode=None, host="localhost", block=True) 
