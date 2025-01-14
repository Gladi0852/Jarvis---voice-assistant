# importing libraries
import speech_recognition as sr
from processCommand import processCommand
from utils import speak


recognizer = sr.Recognizer()  #recognizer object to help speech recog func

count=0

if __name__ == "__main__":
  print("Initiating jarvis...")
  while True:
    try:
      # obtain audio from the mic
      with sr.Microphone() as source:
        print(" I am listening ...")
        audio = recognizer.listen(source, timeout=2)
      # recognize speech using google speech recognition
      word = recognizer.recognize_google(audio)
      if word.lower() == "hey jarvis":
        speak(" yes boss, what is it?")
        print("waked up...")
        while count<3:
          try:
            with sr.Microphone() as source:
              print("...listening...")
              audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            count = 0
            processCommand(command)
          except Exception as e:
            count+=1
            print(f"Error - {e}")

      elif word.lower() == "terminate":
          speak(" bye bye")
          break
    
    except Exception as e:
      print(f"Error: {e}")