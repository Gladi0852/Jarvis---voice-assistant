import speech_recognition as sr
import requests
from dotenv import load_dotenv
import os
from utils import speak


# load .env file
load_dotenv()


recognizer = sr.Recognizer()

# fetch variable from env file
apiKey = os.getenv("news_api_key")

def fetchNews():
  try:
    with sr.Microphone() as source:
      audio = recognizer.listen(source)
    topic = recognizer.recognize_google(audio)
    data = requests.get(f"https://newsdata.io/api/1/news?apikey={apiKey}&q={topic}&language=en")
    if data.status_code == 200:
      news = data.json()
      result = news.get("results",[])[:3]

      for ind,article in enumerate(result,start=1):
        title = article.get("title")
        # description = article.get("description")

        # speak(f" article number {ind}")
        speak(f" title number {ind} is  {title}")
        # speak(f" description is  {description}")
        # print(f"Title {ind} = {title}\nDescription {ind} = {description}")
        
    else:
      speak(" no data found")
  except Exception as e:
    speak(" didn't understand")