import speech_recognition as sr
listener = sr.Recognizer

try:
    with sr.Microphone() as source:
        print("listening....")
        voice = listener.listen(source)
       # #calling your microphone to listen to the sourse
        command = listener.recognize_google(voice)
        print(command)
except:
    pass