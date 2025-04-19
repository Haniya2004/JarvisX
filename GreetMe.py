import datetime
from utils import speak

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon, sir")
    else:
        speak("Good Evening, sir")
    speak("Please tell me how can I help you?")
