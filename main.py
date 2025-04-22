import datetime
import webbrowser
import eel
import pyttsx3
import speech_recognition
from GreetMe import greetMe
from utils import speak
import os
import pyautogui

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
    
    elif "pause" in query:
        pyautogui.press("k")
        speak("video paused")
    elif "play" in query:
        pyautogui.press("k")
        speak("video played")
    elif "mute" in query:
        pyautogui.press("m")  
        speak("video muted")
    elif "volume up" in query:
        from keyboard import volumeup
        speak("Turning volume up ,sir")
        volumeup()
        from keyboard import volumedown 
        speak("Turning volume down ,sir")
        volumedown()
    
    elif "open" in query:
        from Dictapp import openappweb
        openappweb(query)
    elif "close" in query:
        from Dictapp import closeappweb
        closeappweb(query)
        
    elif "google" in query:
        from SearchNow import searchGoogle
        searchGoogle(query)
        
    elif "youtube" in query:
        from SearchNow import searchYoutube
        searchYoutube(query) 
    
    elif "wikipedia" in query:
        from SearchNow import searchWikipedia
        searchWikipedia(query)
        
    elif "news" in query:
        from NewsRead import latestnews
        latestnews()
        
    elif "temperature" in query:
        search = "temperature in Mumbai"
        url = f"https://www.google.com/search?q={search}"
        webbrowser.open(url)
        speak("Here is the current temperature in Mumbai")
        
    elif "weather" in query:
        search = "temperature in Mumbai"
        url = f"https://www.google.com/search?q={search}"
        webbrowser.open(url)
        speak("Here is the current temperature in Mumbai")
        
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir , the time is {strTime}")
    
    else:
        speak("I didn't understand that")
        return {"status": "success", "message": "Unknown command"}

if __name__ == "__main__":
    os.system('start msedge.exe --app="http://127.0.0.1:8000/index.html"')
    
    
    
    eel.start("index.html", mode=None, host="localhost", block=True) 
