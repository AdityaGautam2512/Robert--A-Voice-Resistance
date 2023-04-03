import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser 
import wolframalpha
import json
import os
from urllib.request import urlopen
import subprocess
import requests
import winshell
import smtplib

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning Master')
        speak("Good Morning,,,master")

    elif hour>=12 and hour<18:
        print('Good afternoon Master')
        speak("Good afternoon,,,master")

    else:
        print('Good evening Master' )
        speak("Good evening,,,Master")

    print("My name is Robert. Please tell me how can i help you?")
    speak("My name is Robert. Please tell me how can i help you?")
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n") 

    except Exception as e:
        print("Say that again please...")   
        return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
  
    server.login('your-email', 'password')
    server.sendmail('email of receiver', to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() 
     
        if "stop" in query or "ok bye" in query or "quit" in query:
            print('Robert is shutting down now, Good bye Master')
            speak('Robert is shutting down now, Good bye Master')
            break

        elif 'wikipedia' in query: 
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            print("According to Wikipedia")
            speak("According to Wikipedia: ")
            print(results)
            speak(results)

        elif 'charge' in query:
            print("Ok Master, Charging now!")
            speak("Ok Master, Charging now!")  
            time.sleep(10)  
            print("Charging Complete! Master")
            speak("Charging Complete!, , Master")

        elif 'update' in query:
            print("Ok Master, Updating now!")
            speak("Ok Master, ,Updating now!")  
            time.sleep(10)  
            print("Updation Complete! Master")
            speak("Updation Complete!, , Master")

        elif 'pause' in query:
            print("Ok Master")
            speak("Ok Master")  
            time.sleep(30)       

        elif 'mail to aditya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver email"
                sendEmail(to, content)
                print("Email has been sent !")
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'favourite video' in query:
            print("Playing your favourite  video on Youtube\n")
            speak("Playing your favourite  video on Youtube\n")
            webbrowser.open("https://www.youtube.com/watch?v=UiiqUL0Adfc")

        elif 'powerpoint presentation' in query:
            print("opening Power Point presentation, master")
            speak("opening Power Point presentation master")
            power = r"location of the file/ file path"
            os.startfile(power)

        elif 'word' in query:
            print("opening word master")
            speak("opening Word master")    
            word = r"location of the file/ file path"
            os.startfile(word)

        elif 'notepad' in query:
            print("opening notepad master")    
            speak("opening Notepad master")    
            note = r"location of the file/ file path"
            os.startfile(note)


        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            print("Opening YouTube Master\n")
            speak("Opening YouTube Master")
            webbrowser.open("https://www.youtube.com/")

        elif 'search on browser' in query:
            print("Master, what should i search for?")
            speak("Master, what should i search for?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")



        elif 'open instagram' in query:
            speak("opening instagram\n")
            webbrowser.open("instagram.com")

        elif 'open my college portal' in query:
            speak("opening your college portal\n")
            webbrowser.open("web url of yoyr college portal (if any) ")

        elif 'open blackboard' in query:
            print("opening Blackboard. You should check for assignments master!!")
            speak("opening Blackboard")
            speak("You should check for assignments Master!!\n")
            webbrowser.open("web url of course example: udemy/coursera or any others")

        elif 'open spotify' in query:
            speak("Opening Spotify\n")
            webbrowser.open("spotify.com")

        elif 'open stack overflow' in query:
            speak("opening stackoverflow; Happy coding Master!")
            webbrowser.open("stackoverflow.com")

        elif 'open hackerrank' in query:
            speak("opening hacker rank")
            webbrowser.open("hackerrank.com")

        elif 'open codechef' in query:
            speak("opening code chef Master;")
            webbrowser.open("https://www.codechef.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Master, the time is {strTime}")

        elif 'friday' in query:
            speak("My name is not friday, I am Robert!!")

        elif 'sorry' in query:
            speak("It's okay master.")

        elif 'hello' in query:
            print("Hi, Master how are you doing today?")
            speak("Hi Master,, How are you doing today?")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you Master?")

        elif 'thank you' in query:
            print("your welcome Master")
            speak("your welcome Master")

        elif 'who are you' in query:
            speak("I am Robert.")  
         
        elif "who made you" in query or "who created you" in query or "who invented you" in query:
            print("I was created by Master Aditya in 2022")
            speak("I was created by Master ADITYA, , in 2022")

        elif 'fine' in query:
            speak("It's good to know that you are fine")

        elif 'good' in query:
            speak("It is good to know that Master!")

        elif 'bad' in query:
            speak("What Happened Master!?")
            speak("Is there anything i can help with?")

        elif 'do' in query:
            speak("How can i cheer you up Master?")
            speak("Do you want me to play music or open youtube?")

        elif 'yes' in query or 'yeah' in query:
            speak("How can i cheer you up Master?")
            speak("Do you want me to play music or open youtube?")


        elif 'lazy' in query:

            speak("Being lazy is not good for you Master!")


        elif 'calculate' in query:
             
            app_id = 'API-ID' 
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&apiKey=dd5cc826f91e492fa8570277793a821f''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("searching your Location")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "shutdown system" in query:
                speak("Hold On a Second ! Your system is on its way to shut down")
                subprocess.call('shutdown /s')
                 
        elif "empty recycle bin" in query:
            winshell.recycle_bin().empty(confirm = True, show_progress = True, sound = True)
            speak("Bin Recycled")
        
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "write a note" in query:
            print("What should i write Master?")
            speak("What should i write, Master?")
            note = takeCommand()
            file = open('Robert.txt', 'w')
            print("Master, Should i include date and time?")
            speak("Master, Should i include date and time?")
            snfm = takeCommand()
            if 'yes' in snfm or 'yeah' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                print("Note created! Master")
                speak("Note created!,  ,Master")
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("Robert.txt", "r")
            print(file.read())
            speak(file.read(6))  

        elif "weather" in query:
            api_key="API-ID"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x['main']
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'play music' in query:
            music_dir = "your music directory"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'open visual studio' in query:
            print("Opening Visual studio codes")
            speak("Opening Visual studio codes")
            codePath = "your Directory"
            os.startfile(codePath)    

        elif 'open gmail' in query:
            print("Google Mail open now")
            speak("Google Mail open now")
            webbrowser.open_new_tab("gmail.com")