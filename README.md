# Alice - The Virtual Assistant

Alice is a Python-based virtual assistant designed to make your daily tasks easier by responding to voice commands. Built with speech recognition, text-to-speech, and the OpenAI GPT-4o mini API, Alice can perform various tasks, such as opening and closing applications, fetching news, and much more.

## Key Features

- **Open and Close Applications**: Alice can launch or terminate common applications (e.g., Chrome, Notepad, Word) using simple voice commands.
- **Web Navigation**: Alice can open websites like Google, YouTube, LinkedIn, etc., instantly.
- **Get News Updates**: Stay updated with the latest news through integration with the News API.
- **Battery Status**: Alice can check and inform you about your device’s battery status.
- **AI-Powered Conversations**: Using OpenAI GPT-4o mini API, Alice processes commands and generates conversational responses.
- **Command Logging**: All commands and responses are logged for debugging purposes and to ensure that errors are addressed efficiently.
- **Modular Design**: The code is structured in a modular way for easier updates and feature additions.

## Installation

To use Alice, you'll need to have Python installed on your system along with the following dependencies:

- **pyttsx3**: Text-to-speech library
- **SpeechRecognition**: Converts speech to text
- **OpenAI**: For interaction with the GPT-4o mini API
- **requests**: For making HTTP requests (news updates)
- **pygetwindow**: For interacting with system windows (e.g., closing applications)
- **psutil**: For interacting with system processes (e.g., battery status)

You can install the dependencies using `pip`:
The libraries needed are mentioned in the requirements.txt

## How It Works
**1. Speech Recognition:**
Alice listens for voice commands using the speech_recognition library. Commands are recognized and converted to text.

**2. AI Processing:**
Once a command is recognized, it is processed using the OpenAI GPT-4o mini API. Alice generates intelligent responses based on the user's input.

**3. Executing Commands:**
Based on the recognized command, Alice can perform different tasks like opening applications, navigating the web, or fetching news. The subprocess and psutil libraries help in interacting with system applications.

**4. Text-to-Speech:**
Alice responds to the user using text-to-speech powered by pyttsx3. The assistant communicates with the user in a friendly and natural voice.

**5. Logging:**
All interactions are logged into a file (command_history.txt), which helps track commands and errors for troubleshooting.


# Code Breakdown
The core functions of the program are:

**speak(text)**
Converts the provided text to speech and speaks it aloud using the pyttsx3 engine.

**listen_with_timeout(timeout=10)**
Listens for voice commands for a specified timeout (default is 10 seconds). If no command is detected, it returns None.

**aiProcess(command)**
Sends the command to the OpenAI GPT-4o mini API and returns the generated response.

**processCommand(command)**
Processes the command and executes corresponding actions such as:

Opening or closing applications
Navigating to websites
Fetching news articles
open_application(app_name)
Opens an application if it's recognized from the system_apps dictionary.

**close_application(app_name)**
Closes a running application by matching its name to a list of process names.

**check_battery()**
Checks the battery status of the system and speaks the current battery percentage.

**setup_logging()**
Initializes logging to keep track of all commands and responses.

**log_command_and_response(command, response)**
Logs the command and response into the command_history.txt file.


## Contributing
Feel free to open issues or contribute by submitting a pull request! Any suggestions or improvements are highly appreciated.


**Note:** Don't forget to put "api_key" in the aiProcess() function with your actual OpenAI API key for the assistant to work properly.










