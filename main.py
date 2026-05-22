import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('command')
engine.say('I Am Your Alxa')
engine.say('What Can I Do For You')
try:
    with sr.Microphone() as source:
        print("Listening.......")

        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)

except Exception as e:
    print(e)