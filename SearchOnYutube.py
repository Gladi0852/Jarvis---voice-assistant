from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import speech_recognition as sr
from utils import speak
import webbrowser

load_dotenv()
recognizer = sr.Recognizer()

api_key = os.environ.get("YOUTUBE_API_KEY")  # Replace with your YouTube API key
youtube = build('youtube', 'v3', developerKey=api_key)

video_url = ''

def searchOnYoutube():
  try:
    with sr.Microphone() as source:
      print(" listening...")
      audio = recognizer.listen(source)
    topic = recognizer.recognize_google(audio)
    query = topic
    print(topic)
    request = youtube.search().list(q=query, part='snippet', maxResults=1)
    response = request.execute()
    for item in response['items']:
      video_title = item['snippet']['title']

      global video_url  #this video url is not local, content will update in global one
      try:
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
      except Exception as e:
        video_url = f"https://www.youtube.com/watch?v={item['id']['playlistId']}"
      speak(f" content title is - {video_title}")
    
    speak(" do you want me to play it?")
    with sr.Microphone() as source:
      print(" listening...")
      audio = recognizer.listen(source)
    res = recognizer.recognize_google(audio)
    if "yes" in res.lower() or "ya" in res.lower() or "can play" in res.lower() or "do it" in res.lower():
      webbrowser.open(video_url)
      return True
    else:
      speak(" ok, i'm not playing it")
      return True

  except Exception as e:
    print(f"Error - {e}")
    return False
