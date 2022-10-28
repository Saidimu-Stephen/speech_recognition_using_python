import speech_recognition as sr
from time import  ctime
import time
import  webbrowser
import playsound
import os
import  random
from gtts import gTTS
r = sr.Recognizer()


def saidimu_speak(audio_string):
    tts=gTTS(text=audio_string, lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-' + str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


#  audio_file = os.path.dirname(__file__) + 'audio.mp3'
#  playsound(audio_file)


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            saidimu_speak(ask)
        print("say something")
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            saidimu_speak("Soory i did not get that")
        except sr.RequestError:
            saidimu_speak("Soory, my speech service is down")

        return voice_data


def respond(voice_data):
    if "what is your name" in voice_data:
        saidimu_speak ("My name is Saidimu")
    if "what time is it" in  voice_data:
        saidimu_speak(ctime())

    if "search" in voice_data:
        search=record_audio("what do you want to search for")
        url="https://google.com/search?q=" + search
        webbrowser.get().open(url)
        saidimu_speak("Here is what i found for " + search)


        if "Find location" in voice_data:
            location = record_audio("What is the locatio")
            url = "https://google.nl/maps/place/" +location +'&amp;'
            webbrowser.get().open(url)
            saidimu_speak("here is the location " +location)

        if 'exit' in voice_data:
            exit();


time.sleep(1)
saidimu_speak("how can i help you")

while 1:
    voice_data = record_audio()
    respond(voice_data)