import pyttsx3  # Text to speech
import datetime
import speech_recognition as sr   #Speech to text
import wikipedia                  #for using wikipedia
import webbrowser       #for opening webbrowsers
import os
import smtplib    

engine = pyttsx3.init('sapi5')  # To use voice of our windows
voices = engine.getProperty('voices')  # To get all the voices of your windows
# print(voices)
engine.setProperty('voice', voices[0].id)  # To set the voice property of your engine
rates = engine.getProperty('rate')
# print(rates)
engine.setProperty('rate', 150)


# print(voices[0].id)

def speak(audio):  # Shera will speak what will be given in audio
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)  # Will output hour in int
    # print(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")


    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")


    else:
        speak("Good Evening!")
        print("Good Evening!")


    speak("My name is shera reporting from punjab speed one terabyte..How may i help you..")
    print("My name is shera reporting from punjab speed one terabyte..How may i help you..")



def takeCommand():
    # It will take microphone command from the user and will return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.5
        # r.energy_threshold= 100
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print("Please say it again")
        return "None"
    return query

def sendmail():
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)    #Will create a connection between you and smtp
    server.login("bkoraclee@gmail.com","Pb11bd3296")  #login process
    speak("What message i should give")
    message= takeCommand().title()                      #Message to give
    server.sendmail("bkoraclee@gmail.com","brahmkaran123@gmail.com",message) #syntax(from, to ,message)
    speak("Email has been sent successfully")
    server.quit()


if __name__ == "__main__":
    wishme()
    x= "yes"
    while x == "yes":
        print('Please tell me your query')
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")     #replacing wikipedia from query
            results = wikipedia.summary(query, sentences=2)   #will give us the summary of the search
            speak("According to wikipedia")
            print(results)
            speak(results)
            # break

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            # break

        elif "open stack overflow" in query:
            speak("Yes sure here is your result..")
            webbrowser.open("stackoverflow.com")
            # break

        elif "open google" in query:
            speak("Yes sure here is your result..")
            webbrowser.open("google.com")
            # break

        elif "play music" in query:
            music_dir="path de dena"      #give the path where your songs are present
            songs=os.listdir(music_dir)
            speak("Presenting song for you milot")
            os.startfile(os.path.join(music_dir,songs[0]))
            # break

        elif "the time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")    #for converting time into string to be able to speak
            speak("The time is ")
            speak(str(time))
            # break

        elif "open pycharm" in query:
            #for path simply go to app--> open file location-->properties-->copy target
            pycharm_path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe"
            speak("Opening pycharm..")
            os.startfile(pycharm_path)
            # break

        elif "email to karan" in query:
            try:
                sendmail()

            except Exception as e:
                print(e)
                speak("Sorry brother something unexpected occured please try again")
 
            # break

        elif "open whatsapp" in query:
            speak("Yes sure here is your result..")
            webbrowser.open("https://web.whatsapp.com/")
            # break

            

        speak("Do you want to continue")
        x=input()
        if(x=="yes"):
            continue
