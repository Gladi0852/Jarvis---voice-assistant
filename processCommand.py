from utils import speak
import webbrowser #we can open any link on browser
import musicLibrary
from newsFunc import fetchNews
from geminiAi import geminiAi
from SearchOnYutube import searchOnYoutube


def processCommand(command):
  if "open" in command.lower() and "google" in command.lower():
    speak("opening Google")
    webbrowser.open("https://www.google.com")
  elif "open" in command.lower() and "linkedin" in command.lower():
    speak("opening LinkedIn")
    webbrowser.open("https://www.linkedin.com/feed/")
  elif "play" in command.lower():
    for key in musicLibrary.music.keys():
      if key in command.lower():
        webbrowser.open(musicLibrary.music[key])
      else:
        speak(" there is no song as you requested")
  elif "news" in command.lower():
    speak(" on which topic?")
    fetchNews()

  elif "search" in command.lower():
    speak(" what you want to search?")
    searchOnYoutube()

  else:
    # geminiAi(command)
    pass