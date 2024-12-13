import speech_recognition as sr 



def listen_with_timeout(timeout=10):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening for command...")
            audio = recognizer.listen(source, timeout=timeout)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.WaitTimeoutError:
            print(f"Listening timed out after {timeout} seconds.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I could not understand the command.")
            return None
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}")
            return None