import listen 
import requests
import webbrowser
import speech_recognition as sr 

from apps import open_application as oa, close_application as ca
from processCommand import processCommand
from log import setup_logging, log_command_and_response as cr
from timeout import listen_with_timeout
from speech import speak, recognizer



def main():
    setup_logging()
    speak("Hello, I am alice. How can I assist you today?")
    is_active = True
    
    while True:
        try:
            if is_active:
                command = listen_with_timeout(timeout=30)
                if command:
                    response = None
                    cr(command, "Received command")
                    if 'open' in command:
                        app_name = command.split('open')[-1].strip()
                        if oa(app_name):
                            response = print(f"Opened {app_name}.")
                        else:
                            response = f"Could not find {app_name}, searching on Google..."
                            webbrowser.open(f"https://google.com/search?q={app_name}")
                    
                    elif 'close' in command:
                        app_name = command.split('close')[-1].strip()
                        if ca(app_name):
                            response = print(f"Closed {app_name}.")
                        else:
                            response = f"Could not close {app_name}. Please check if it's running."
                    
                    elif 'exit' in command or 'quit' in command:
                        response = "Goodbye!"
                        speak(response)
                        break
                    
                    else:
                        speak("Wait: ")
                        processCommand(command)
                    
                    if response:
                        speak(response)

                else:
                    is_active = False
                    cr("System", "Went to sleep, waiting for initialization.")
                    print("No command received. Entering sleep mode.")
            else:
                print("Waiting for wake word...")
                with sr.Microphone() as source:
                    try:
                        audio = recognizer.listen(source, timeout=None)
                        wake_word = recognizer.recognize_google(audio)
                        if "alice" in wake_word.lower():
                            is_active = True
                            speak("I am ready. Please give your command.")
                            print("Wake word detected. Re-activating...")
                    except sr.UnknownValueError:
                        pass
                    except sr.RequestError:
                        print("Error with the speech service. Retrying...")

        except Exception as e:
            print(f"Error occurred: {e}")
            speak(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
