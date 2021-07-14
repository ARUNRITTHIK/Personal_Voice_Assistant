import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import subprocess


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("hi i am your alexa")
engine.runAndWait()


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)

    except:
        pass
    return command


def run_alexa():
    
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        talk("current time is" + time)


    elif "date" in command:
        date = datetime.datetime.now().strftime('%d:%B:%Y')
        talk("today's date is" + date)

    elif "about" in command:
        wiki = command.replace("about", "")
        info = wikipedia.summary(wiki, sentences=3)
        talk(info)

    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in command:
        talk("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")

    elif 'open spotify' in command:
        talk("Here you go to Spotify.enjoy your music")
        webbrowser.open("https://www.spotify.com/in/")

    elif 'open whatsapp' in command:
        talk("Here you go to whatsapp")
        webbrowser.open("web.whatsapp.com")

    elif 'open movies' in command:
        codePath = r"N:\movies"
        os.startfile(codePath)


    elif 'how are you' in command:
        talk("I am fine, Thank you")
        talk("How are you, Sir")

    elif 'fine' in command or "good" in command:
        talk("It's good to know that your fine")

    elif "who made you" in command or "who created you" in command:
        talk("I have been created by Team Firehawks.")

    elif 'turn off' in command:
        talk("Thanks for giving me your time")
        exit()

    elif 'search' in command :
        command = command.replace("search", "")
        pywhatkit.search(command)

    elif "who i am" in command:
        talk("If you talk then definately your human.")

    elif "why you came to world" in command:
        talk("Thanks to Team Firehawks.")
        talk("further It's a secret")

    elif 'shutdown system' in command:
        talk("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif "where is" in command:
        command = command.replace("where is", "")
        location = command
        talk("User asked to Locate")
        talk(location)
        webbrowser.open("https://www.google.com / maps / place/" +location )


    else:
        talk("sorry, i can't get you")
        talk("can you please repeat")



while True:
    run_alexa()
