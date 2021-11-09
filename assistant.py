
import pyttsx3
import datetime
# import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil

import wolframalpha
# import tkinter
import json
import random
import operator
from twilio.rest import Client
from clint.textui import progress

from ecapture import ecapture as ec
from bs4 import BeautifulSoup
# import win32com.client as wincl
from urllib.request import urlopen


import speech_recognition as sr
import wikipedia
import webbrowser
import os
import wave 
import subprocess
import playsound
from os import path

from gtts import gTTS


from pydub import AudioSegment

from bnbphoneticparser import BengaliToBanglish
b2b=BengaliToBanglish()

from banglacmd import *

from translate import *

# b_or_e=""

# import waiting

# vocal = pyttsx3.init('sapi5')          #for windows
# voices = vocal.getProperty('voices')
# print(voices[1].id)
# vocal.setProperty('voice', voices[0].id)

vocal = pyttsx3.init('espeak')            #for linux 
vocal.setProperty('rate', 170)
vocal.setProperty('volume', 0.9)
vocal.setProperty('voice','f4')
# vocal.say("My name is Forkan.")
# vocal.runAndWait()



def bwish():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        bspeak("শুভ সকাল স্যার")
    elif(hour>=12 and hour<18):
        bspeak("শুভ অপরাহ্ন স্যার")
    else:
        bspeak("শুভ সন্ধ্যা স্যার")
    # speak("I'm Jarvis How may I help you?")
    bspeak("আমি কিভাবে আপনাকে সাহায্য করতে পারি ? ")



def wish():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Morning Sir")

    elif(hour>=12 and hour<18):
        speak("Afternoon Sir") 
    else:
        speak("Evening Sir")
    
    speak(" How may I help you?")
    # bspeak("আমি কিভাবে আপনাকে সাহায্য করতে পারি ? ")


def vasa():
    speak("        Which language you prefer 'Bangla' or 'English'")
    langu=cmd()
    print(langu)
    print("dhukse")
    
    return langu


def langselect():
    kotha=vasa().lower()
    if "english" in kotha:
        wish()
        b_or_e="1"
        print(kotha)
        return "english"
    elif "bangla" in kotha: 
        bwish()
        b_or_e="2"
        print(kotha)
        return "bangla"
    else:
        speak("please speak again Sir")
        # vasa()
        return langselect()




def openweb():
    # webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("//usr//share//applications//firefox"))

if __name__ == "__main__":

    out=langselect()


    while True:
        if out == "bangla":
            query=cmd2()
            query=transb(query)
            print(query)
        else:
            query=cmd()
           
            

        openweb()

        # if(out=="bangla"):
        query=query.lower()   

        if "wikipedia" in query:
            print("Searching wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            # if out == "bangla":
            #     bspeak("")
            # else:
            speak("According to wikipedia ... ")
            speak(results)



        elif "what's your name:" in query:
            if out == "bangla":
                bspeak("আমার নাম প্রিয়াঙ্কা")
            else:
                speak("my name is prianka")
            




        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            speak(f"Sir, the time is {strTime}")



        elif 'how are you' in query:
            if out=="english":
                speak("I am fine, Thank you")
                speak("How are you, Sir")
            else:
                bspeak(transe("I am fine, Thanks"))
                bspeak(transe("How are you, sir"))
            
        elif 'fine' in query or "good" in query:
            if out=='english':
                speak("It's good to know that your fine")
            else:
                bspeak("শুনে ভালো লাগলো যে আপনি ভাল আছেন")


        elif "who made you" in query or "who created you" in query:
            ans="I have been created by Forkan."
            if out=="english":
                speak(ans)
            else:
                bspeak(transe(ans))


        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif "i love you" in query:
            speak("It's hard to understand")


        elif "language change" in query:
            if out == "bangla":
                out="english"
                speak("converted to english")
            else:
                out="bangla"
                bspeak("বাংলায় রূপান্তর করা হলো")
            # speak("Done sir")


        elif "open youtube" in query:
            if out == "bangla":
                bspeak("ইউটিউব খোলা হচ্ছে স্যার")
            else:
                speak("opening youtube sir.......")
            # ss="youtube.com"
            ss="https://www.youtube.com/watch?v=PgCliOxl41o&ab_channel=Yohani"
            webbrowser.get("google-chrome").open(ss)  #for linux
            # webbrowser.get('chrome').open(ss)
            # break

        elif "open google" in query:
            if out == "bangla":
                bspeak("গুগল খোলা হচ্ছে স্যার")
            else:
                speak("opening google sir.......")
            ss="google.com"
            webbrowser.get("google-chrome").open(ss)  #for linux
            # webbrowser.get('chrome').open(ss)

        elif "open gmail" in query:
            if out == "bangla":
                bspeak("জিমেইল খোলা হচ্ছে স্যার")
            else:
                speak("opening gmail sir.......")
            ss="gmail.com"
            webbrowser.get("google-chrome").open(ss)  #for linux
            # webbrowser.get('chrome').open(ss)

        elif "open stackoverflow" in query:
            if out == "bangla":
                bspeak("স্ট্যাকওভারফ্লো খোলা হচ্ছে স্যার")
            else:
                speak("opening stcakoverflow sir.......")
            ss="stackoverflow.com"
            webbrowser.get("google-chrome").open(ss)  #for linux
            # webbrowser.get('chrome').open(ss)

        # elif "play music" in query:
        #     music_dir="F:\\Forkan mobile backup\\zayeef music\\music forkan"
        #     songs=os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))

        elif "open sublime" in query:
            if out == "bangla":
                bspeak("সাবলাইম টেক্সট খোলা হচ্ছে স্যার")
            else:
                # speak("opening google sir.......")
                speak("Opening sublime text sir...........")
            # os.startfile("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")  #for windows
            os.system("/opt/sublime_text/sublime_text %F") #for linux
            
            
        elif "open calculator" in query:
            if out == "bangla":
                bspeak("ক্যালকুলেটর খোলা হচ্ছে স্যার")
            else:
                # speak("opening google sir.......")
                speak("Opening calculator sir...........")
            os.system("gnome-calculator")#for linux
            # os.startfile("C:\\Program Files\\WindowsApps\\Calculator.exe")  #for windows

        elif "open visual studio" in query:
            if out == "bangla":
                bspeak("ভিসুয়াল স্টুডিও খোলা হচ্ছে স্যার")
            else:
                speak("opening visual studio sir.......")
            # os.startfile("C:\\Users\\Forkan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe") #for windows
            os.system("/usr/share/code/code --no-sandbox --unity-launch %F") #for linux


        elif "exit"  in query:
            exit()


        elif "stop" in query:
            os.close()



        del query
    # speak("Forkan is a bad boy")
    