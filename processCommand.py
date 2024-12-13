import requests
import webbrowser
import ai_process as ai

from battery import check_battery
from speech import speak

newsapi = "9d1fef487094471ca4c0bc970b22beba"

def processCommand(c):
    if "google" in c.lower():
        webbrowser.open("https://google.com")
    elif "facebook" in c.lower():
        webbrowser.open("https://facebook.com")    
    elif "instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "search" in c.lower():
        query = c.lower().split("search")[1].strip()
        webbrowser.open(f"https://google.com/search?q={query}")
    elif "battery" in c.lower():
        check_battery()
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])[:5]
            for article in articles:
                speak(article['title'])
    else:
        output = ai.aiProcess(c)
        speak(output)