import subprocess
import psutil
import pygetwindow as gw
from speech import speak


system_apps = {
    "task manager": "taskmgr",
    "control panel": "control",
    "settings": "start ms-settings:",
    "file explorer": "explorer",
    "command prompt": "cmd",
    "powershell": "powershell",
    "notepad": "notepad",
    "calculator": "calc",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "firefox": "firefox",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "outlook": r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE",
    "access": r"C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE",
    "onenote": r"C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE"
}


def open_application(app_name):
    app_command = system_apps.get(app_name)
    if app_command:
        try:
            if app_name == "settings":
                subprocess.run(app_command, shell=True)
            else:
                subprocess.Popen(app_command, shell=True)
            speak(f"Opening {app_name}...")
            return True
        except Exception as e:
            print(f"Error opening {app_name}: {e}")
            speak(f"Sorry, I couldn't open {app_name}.")
            return False
    else:
        speak(f"Sorry, I do not have the command for {app_name}.")
        return False

def close_application(app_name):

    process_names = {
    "task manager": "taskmgr.exe",
    "control panel": "control.exe", #for some reason the control panel closing was not working So I had to add the function for it
    "settings": "SystemSettings.exe",  
    "file explorer": "explorer.exe",
    "command prompt": "cmd.exe",
    "powershell": "powershell.exe",
    "notepad": "notepad.exe",
    "calculator": "ApplicationFrameHost.exe",
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
    "firefox": "firefox.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "outlook": "outlook.exe",
    "access": "msaccess.exe",
    "onenote": "onenote.exe"
}
    
    if app_name == "control panel":
        try:
            windows = gw.getWindowsWithTitle("Control Panel")
            if windows:
                for win in windows:
                    win.close()
                speak("Closing Control Panel...")
                return True
            else:
                speak("Control Panel is not currently open.")
                return False
        except Exception as e:
            speak(f"Failed to close Control Panel: {str(e)}")
            return False

   

    process_name = process_names.get(app_name.lower())
    if process_name:
        found_process = False
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'].lower() == process_name.lower():
                try:
                    proc.terminate()
                    speak(f"Closing {app_name}...")
                    found_process = True
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    print(f"Error closing {app_name}: Access Denied or Process Not Found.")
                    speak(f"Error closing {app_name}.")
        if not found_process:
            speak(f"{app_name} is not currently running.")
        return found_process

    speak(f"Sorry, I do not have a close command for {app_name}.")
    return False
