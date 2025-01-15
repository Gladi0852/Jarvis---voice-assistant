Jarvis is a voice assistant built with Python, designed to simplify your daily tasks and enhance your digital experience. Equipped with a wide range of features, it responds to voice commands and performs various actions seamlessly.

Key Features:
Wake Word Activation: Responds only to the command "Hey Jarvis" or "Jarvis," ensuring it listens and performs tasks only when prompted, adding a layer of control and efficiency.
Smart Web Navigation: Opens any link you request, making browsing hands-free and efficient.
YouTube Integration: Searches and plays videos directly on YouTube with just your voice commands.
AI-Powered Knowledge Retrieval: Provides accurate and concise answers to any topic you inquire about using AI.
Music Playback: Plays songs from your local music library by simply mentioning the song's title.
News Updates: Delivers real-time news on any topic of interest, keeping you informed and updated.

Jarvis combines voice recognition, natural language processing to create an intuitive and interactive user experience. It’s the perfect assistant for enhancing productivity, entertainment, and convenience.

Steps to run it on your pc:
1. download the zip file and open it with code editor after extracting the zip file
2. create a virtual environment on that folder.
3. pip install -r packagesInfo.txt  to install all the used packages
4. now make a (.env) file and then get these 4 api
5.     news_api_key = 'your_api_key'  (newsdata.io)
6.     OPENAI_API_KEY = 'your_api_key' (i used gemini, it's free, and openAi is paid so you can skip openAi)
7.     GEMINI_API_KEY = 'your_api_key'
8.     YOUTUBE_API_KEY = 'your_api_key'

   if you can't then get help from ai.

** see processCommand.py - if at the last geminiAi is comment out then enable that.

And now you are ready to run it.


***UI will be added soon
