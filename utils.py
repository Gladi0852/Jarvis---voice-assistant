import pyttsx3
from gtts import gTTS
import pygame

engine  = pyttsx3.init() #text to speech engine

# text to speech function
# def speak_old(text):
#   engine.say(text)
#   engine.runAndWait()  # Wait for speech to finish



def speak(text):
    # Generate the MP3 file with gTTS
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize pygame mixer for sound playback
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Prevents the program from closing too early

    pygame.mixer.music.unload()
