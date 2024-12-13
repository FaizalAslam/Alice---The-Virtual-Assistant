import speech_recognition  as sr
import pyaudio
import pyttsx3


recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the command.")
            return None
        except sr.RequestError:
            print("Sorry, I'm having trouble connecting to the service.")
            return None