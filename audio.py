import pyaudio
import wave
import speech_recognition as sr
r = sr.Recognizer()
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=1024)
frames = []
print("Recording")

while True:
    data = stream.read(1024)
    frames.append(data)
    #try:
    text = r.recognize_google()
    print('You said:{}'.format(text))
    #except:
            #print("Speak again")
# except KeyboardInterrupt:
#     print("Recorded")
