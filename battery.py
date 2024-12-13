import speech_recognition as sr
import psutil 
from speech import speak

def check_battery():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"The battery is at {percent} percent.")
    else:
        speak("Sorry, I couldn't get the battery status.")
