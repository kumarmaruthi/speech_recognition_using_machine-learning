import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
engine = pyttsx3.init()
engine.setProperty('rate', 150)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Could not connect to Google Speech Recognition.")
        return ""
def execute_command(command):
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        speak(f"Searching for {query}")
        pywhatkit.search(query)
    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        summary = wikipedia.summary(topic, sentences=1)
        speak(summary)
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "exit" in command:
        speak("Goodbye!,  K Maruthi see to Tommorrow")
        exit()
    else:
        speak("I didn't understand that command.")
speak("Hello K Maruthi, how can I assist you today?  ")
while True:
    command = listen()
    if command:
        execute_command(command)