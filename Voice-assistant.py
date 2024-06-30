import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia
import webbrowser as wb
import time as tm
import requests

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold=1
        r.energy_threshold=5000
        r.adjust_for_ambient_noise(source)
        try:
            audio=r.listen(source,timeout=2) 
            print('recognizing...')
            text=r.recognize_google(audio)
            return text
        except Exception as e:
            print(e)
            say("Please say that again")
            return "Try Again"
def say(word):
    engine.say(word)
    engine.runAndWait()

def time():
    Time = datetime.now().strftime("%I:%M %p")
    print(f"Current time is {Time}")
    say("Current time is ,")
    say(Time)

def date():
    D=datetime.now().strftime("%d %b %Y")
    print(f"TODAYS DATE IS {D}")
    say("TODAYS DATE IS ,")
    say(D)

def get_wikipedia_summary(query, sentences=1):
    try:
        print(f"Querying Wikipedia for: '{query}'")  # Print the query
        result = wikipedia.summary(query, sentences=sentences)
        return result
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{query}'"
    except Exception as e:
        return f"An error occurred: {e}"

def tell_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke = response.json()
    setup=joke["setup"]
    punchline=joke["punchline"]
    say(setup)
    print(setup)
    tm.sleep(2)
    print(punchline)
    say(punchline)
    
    
      
engine=pyttsx3.init()
say("Initializing voice Assistant ")
while True:
    query = take_command().lower()
    print(f"you said : {query}")
    if "time" in query:
        time()

    elif "date" in query:
        date()

    elif "who are you" in query:
        say("I'm a desktop voice assistant.")
        print("I'm a desktop voice assistant.")

    elif "joke" in query:
        say("Here is a joke for you.")
        tell_joke()

    elif "wikipedia" in query:
        try:
            say("Ok wait sir, I'm searching...")
            query = query.replace("wikipedia","").strip()
            print(query)
            result=wikipedia.summary(title=query, sentences=1)
            print(result)
            say(result)
        except:
            say("Can't find this page sir, please ask something else")
        
    elif "open youtube" in query:
        wb.open("www.youtube.com")
        say("YouTube is now open. I will wait 5 seconds.")
        tm.sleep(5)
        say("5 seconds are over. How can I assist you further?")

    elif "open google" in query:
        wb.open("www.google.com") 
        say("google is now open. I will wait 5 seconds.")
        tm.sleep(5)
        say("5 seconds are over. How can I assist you further?")
   
    elif "search on web" in query or "search on google" in query:
        try:
            say("What should I search?")
            print("What should I search?")
            search = take_command()
            print(search)
            if search == "Try Again":
                raise Exception
            wb.open(f"https://www.google.com/search?q={search}")
            say("google is now open. I will wait 5 seconds.")
            tm.sleep(5)
            say("5 seconds are over. How can I assist you further?")

        except Exception as e:
            say("Can't open now, please try again later.")
            print("Can't open now, please try again later.",e)
            
    elif "offline" in query or "exit" in query:
        say("Goodbye! If you have any more questions in the future, feel free to ask. Have a great day!")
        quit()



