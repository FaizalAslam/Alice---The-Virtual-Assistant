import speech_recognition as sr
import pyaudio
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')

def speak(text):
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()