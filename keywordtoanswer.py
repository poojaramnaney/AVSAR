import csv
from rake_nltk import Rake
from random import randint
import os
import time
import playsound
import sys
import pyttsx3

engine=pyttsx3.init()
engine.say("Good Afternoon")
engine.say("What is your name")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()

import speech_recognition as sr
from gtts import gTTS

sys.getrecursionlimit() # Prints 1000
print("speak now")
def speak(text):
    tts=gTTS(text=all, lang="en",tld="com")
    filename="onlymp3.to - One of the Greatest Speeches Ever  Steve Jobs-Tuw8hxrFBH8-192k-1659983637536"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

text = get_audio()
#if "hello" in text:
 #   speak("hello how are you")

engine.say("Tell me something about yourself")

engine.runAndWait()
#engine.talk(text)
#engine.runAndWait()

print("listening.........")
text=get_audio()

r = Rake()
file = open('C:/Users/Dell/Dropbox/PC/Desktop/COLLEGE/chatbot/venv/dataset.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)

print(rows)


print("listening.........")
text=get_audio()

for qno in range(0,3):
    index = randint(0,29)
    question =rows[index][0]
    engine.say(question)
    engine.runAndWait()
    answer = rows[index][1]
    print("Give answer")
    text = get_audio()
    r=Rake()
    r.extract_keywords_from_text(answer)

    for rating,keyword in r.get_ranked_phrases_with_scores():
        ans = keyword.split()
        for keyword1 in ans:
            if keyword1 not in text:
                print("please speak these keyword too",keyword1)

        if rating > 5:
            print(rating, ans)


engine.say("nice to meet you")
print("nice to meet you")



