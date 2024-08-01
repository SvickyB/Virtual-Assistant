import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser as web
import os
import smtplib
import subprocess
import psutil
import pywhatkit
import requests
from bs4 import BeautifulSoup
import operator
import sys
print("Hi Everyone")
MASTER = "vicky"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
# This funtion will wish you as per the current time
def wishMe():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour < 12:
        speak("good morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("good afternoon" + MASTER)
    else:
        speak("good Evening" + MASTER)
        speak("Hi Everyone... ")
        speak(f"current time is {strTime}")
        speak("i am your assistant. How may I help you?")
def phnumber(my_string):
    print(my_string)
    phonenum = ("91" + my_string.replace(" ", ""))
    url("http://apilayer.net/api/validate?access_key=cd3af5f7d1897dc1707c47d05c3759fd&number=" + phonenum)
    resp = requests.get(url)
    details = resp.json()
    speak("collecting data")
    print('')
    print("Country : " + details['country_name'])
    speak("Country : " + details['country_name'])
    print("Location : " + details['location'])
    speak("Location : " + details['location'])
    print("Carrier : " + details['carrier'])
    speak("Carrier : " + details['carrier'])
def mail():
    speak("what message do you want to send sir ")
    content = takeCommand()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("xyz@gmail.com", "875fyfg97898687")#Provide login details of email address from where the mail should send 
    server.sendmail("xyz@gmail.com", "abc@gmail.com",
    content)#Provide receiver email address to whom the mail should receive
    server.close()
    speak("sending mail")
    print("message sent")
    speak("message sent")
def calc(my_string):
    print(my_string)
    def get_operator_fn(op):
        return {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        'divided': operator. truediv ,
        }[op]
    def eval_binary_expr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)
        speak("Your result is")
        print(eval_binary_expr(*(my_string.split())))
        speak(eval_binary_expr(*(my_string.split())))
# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        query = None
        return query
    

# main program starting
def main():
    query = takeCommand()
# Logic for executing tasks as per the query
if 'wikipedia' in query.lower():
    query = query.replace("wikipedia", "")
    speak('searching wikipedia...')
    results = wikipedia.summary(query, sentences=2)
    speak('According to wikipedia')
    print(results)
    speak(results)
elif 'wikipedia brief' in query.lower():
    query = query.replace("wikipedia", "")
    speak('searching wikipedia...')
    results = wikipedia.summary(query, sentences=10)
    speak('According to wikipedia')
    print(results)
    speak(results)
elif 'trace' in query.lower():
    speak("say the phone number sir ill trace for you")
    my_string = takeCommand()
    phnumber(my_string)
elif 'play song' in query.lower():
    speak("what song do you want to play sir")
    song = takeCommand()
    speak('playing ' + song)
    pywhatkit.playonyt(song)
elif "can you calculate" in query.lower():
    speak("what you want to calculate sir")
    my_string = takeCommand()
    calc(my_string)
elif 'how much power left' in query.lower():
    battery =psutil.sensors_battery()
    per = battery.percent
    speak(f"sir your system have{per} percent battery")
if per >= 75:
    speak("we have enough juice to continue our work")
elif per >= 40 and per <= 75:
    speak("not yet full but its ok , we have enough power for couple of hours")
elif per <= 15 and per <= 30:
    speak("we dont have enough power to manage. please connect your charger")
elif per > 15:
    speak("system in critical stage. please connect to charging or else the system will shutdown in few minutes")
elif 'search' in query.lower():
    speak("what you want to search sir")
    my_string = takeCommand()
    speak('ok sir ill search that for you in google')
    print('oks ir ill search that for you in google')
    pywhatkit.search(my_string.replace('search', ''))
elif 'open youtube' in query.lower():
    # webbrowser.open('youtube.com')
    print('opening youtube')
    speak('opening youtube')
    web.open("https://www.youtube.com/")
elif 'open google' in query.lower():
    # webbrowser.open('google.com')
    print('opening google')
    speak('opening google')
    subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe')
elif 'instagram' in query.lower():
    print('opening instagram')
    speak('opening instagram')
    web.open("https://www.instagram.com/")
elif 'whatsapp' in query.lower():
    print('opening whatsapp')
    speak('opening whatsapp')
    web.open("https://web.whatsapp.com/")
elif 'who are you' in query.lower():
    speak('im jarvis an virtual artificial intelligence developed to assist with your task since best i can')
elif 'what can you do' in query.lower():
    speak('i can say the current time , weather , i can play songs from youtube , i can google anything from wikipedia , i do some maths, also i can send mail to a specific person through voice and many more')
elif "temperature" in query.lower():
    speak("Say the location")
    location=takeCommand()
    search="temperature in"
    url = f"https://www.google.com/search?q={search} {location}"
    r = requests.get(url)
    data=BeautifulSoup(r.text, "html.parser")
    temp=data.find("div",class_="BNeawe").text
    speak(f"current temperature in {location} is {temp}")
elif 'angry' in query.lower():
    speak("calm down sir, no matter how angry you get , you end up forgiving the people you love ")
elif 'sing' in query.lower():
    speak('I see treeeees of greeeen. red roses tooooo, I watch them bloooom for me and you . And I think to ''myself. what a wonderful wooorld')
elif "who created you" in query:
    speak("im virtual artificial intelligence developed by vignesh and jegan to assist with some task which programmed by him ")
elif ' gmail' in query.lower():
    print('opening gmail')
    speak("opening gmail sir")
    web.open_new("https://mail.google.com/mail/u/0/#inbox")
elif 'google meet' in query.lower():
    print('opening google meet sir')
    speak("opening google meet sir")
    web.open_new("https://meet.google.com/lookup/gzbdzqag3p?authuser=0&hs=179")
elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\bhuva\\audio"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")
elif 'open code' in query.lower():
    codePath="C:\\Users\\Dell\\AppData\\Local\\Programs\\MicrosoftVSCode\\Code.exe"
    os.startfile(codePath)
elif 'send mail' in query.lower():
    try:
        speak("ok sir ill do it for you")
        mail()
    except Exception as e:
        print(e)
elif 'go back' in query.lower():
    print("i am always available")
    speak("i am always available")
    sys.exit()
elif '' in query.lower():
    print('still listening... ')
    wishMe()
while True:
    main()