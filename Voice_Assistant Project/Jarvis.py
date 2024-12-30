
import requests
import speech_recognition as sr     # 'as' keyword used to use sr instead of speechrecognition
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()    # Create a recognizer class
engine = pyttsx3.init()  # Initialize pyttsx
newsapi = "dad3adea24ef4a56a9f5719f5668479c"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif "news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        except requests.exceptions.RequestException as e:
            speak(e)
        if r.status_code == 200:
            data = r.json()
            
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])
                
    else:
        #let openAi handle the request
        pass

if __name__ == "__main__":
    speak("Initializing Siri....")
    while True:
        # Listen for the wake word Rock
        # Obtain audio from the microphone
        print("Listening...")
        try:
            with sr.Microphone() as source:
                print("Recognizing...")
                audio = recognizer.listen(source , timeout=2, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            if(word.lower() == "siri"):
                speak("Yesss?")
                
                #Listen for command
                with sr.Microphone() as source:
                    print("Siri Activated!")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Could not understand the audio")
            