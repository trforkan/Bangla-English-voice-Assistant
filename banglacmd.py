import speech_recognition as sr
import playsound
from gtts import gTTS
from bnbphoneticparser import BengaliToBanglish
b2b=BengaliToBanglish()


def speak(text):
    output = gTTS(text=text, lang='en',slow=False)
    output.save("output.mp3")
    playsound.playsound('output.mp3', True)


def bspeak(text):
    output = gTTS(text=text, lang='bn',slow=False)
    output.save("output.mp3")
    playsound.playsound('output.mp3', True)



def cmd():  # for english
    
    '''
    take command
    '''
    r=sr.Recognizer()
    with sr.Microphone() as src:
        print("listening........")
        r.adjust_for_ambient_noise(src)
        r.pause_threshold=1
        audio=r.listen(src)
        # audio=r.listen(src,timeout=8,phrase_time_limit=8)
        
        try:
            print("Recognizing......")

            query=r.recognize_google(audio)
            print(f"user said : {query}\n")
            speak(query)


        except:
            print("please speak again Sir")
            speak("please speak again Sir")
            return "None"
        return query



def cmd2():  # for bangla

    '''
    take command
    '''
    r=sr.Recognizer()
    with sr.Microphone() as src:
        print("listening........")
        r.adjust_for_ambient_noise(src)
        r.pause_threshold=1
        audio=r.listen(src)
        # audio=r.listen(src,timeout=8,phrase_time_limit=8)
        
        try:
            print("Recognizing......")
           
            query=r.recognize_google(audio,language='bn')
            print(f"user said : {query}\n")
            bspeak(query)
            txtbanglish=b2b.parse(query.strip())
            txt=txtbanglish.lower()

        except:
            print("please speak again Sir")
            speak("please speak again Sir")
            return "None"
        return query