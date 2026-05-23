import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command =""
    try:
        with sr.Microphone() as source:
            print("Listening.......")

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except Exception as e:
        print(e)
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('curent time is' + time )

    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('Sorry I Have A Headec')

    elif 'are you single' in command:
        talk('I Am A RelationShip With Wifi')

    elif 'jokes' in command:
        talk(pyjokes.get_joke())

    else:
        talk('please say the command again')

while True:
 run_alexa()