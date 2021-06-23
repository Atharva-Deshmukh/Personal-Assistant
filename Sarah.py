import pyttsx3
import pythoncom
import datetime
import os
import threading
import webbrowser
import smtplib
import wikipedia
#import speechrecognition  as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#print("voice choosen: " voices[1].id)
rate=engine.getProperty('rate')                   #getting details of current speaking rate
#print("My speech rate: " +str(rate))                                       #prints the current voice rate
engine.setProperty('rate',200)

volume=engine.getProperty('volume')               #getting to know current level of volume (0= min and 1= max)
#print("My volume: " +str(volume))                                     #printing the current volume level
engine.setProperty('volume',1.0)                  #setting up volume level bertween 0 and 1



def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #takes voice as an input and gives string as an output.

    r=sr.Recognizer()                         #recognizer is a class
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=2                  #so that if I take a pause of 2 sec, it won't stop the recording.
        audio=r.listen(source)

    try:                                                  #in case if there is an error.
        print("recognizing.......")
        command=r.recognize_google(audio,language='en-in')
        print(f"You said : {command}\n" )

    except Exception as e:
        #print(e)
        print("Sorry, could you please repeat that again, sir?")
        return "None"                                                               # this is not the "none" of python.
    return command




def wishMe():
        hour=int(datetime.datetime.now().hour)  #typecasted in integer.
        if hour>=0 and hour<12:
            speak("Good morning Sir!")
        elif hour>=12 and hour <18:
            speak("Good Afternoon Sir!")
        else:
            speak("Good Evening sir!")





    


#you can interact with Sarah 1.0 here.
if __name__=='__main__':

    speak("Reboot successfull!,\nLogging on\n getting ready")
    speak("Drivers...Checked!")
    speak("server connections...secured")
    speak("System settings..")
    speak("Current speech rate is " + str(rate))  # only concatenate str and not int. therefore str is used.
    speak("The volume is set to: " + str(volume))
    speak("All set!")
    speak("Ready to serve you!")

    wishMe()
    speak("This is Sarah version 1 point 0!")
    speak("What are my next orders Sir?")

    while True:
        command=takeCommand().lower()                      #in order to match every possible entry
        takeCommand()

# ---------------------------------
                                                                                               #Wikipedia and web  part
if 'open wikipedia' or 'Hey sarah, open Wikipedia'  in command:
    speak("Searching for it, Sir!")
    query=query.replace("wikipedia","")      #find out WHY??
    results=wikipedia.summary(query,sentences=2)  #WHY 2??
    speak("The search was done from wikipedia")
    print("The search in In text: \n" +str(results))
    speak(results)

elif 'Hey sarah, open youtube' in command:                 #query ki jagah command kar diya
    webbrowser.open("youtube.com")

elif "Hey sarah, open google" in command:
    webbrowser.open("google.co.in")

#-----------------------------------------------------------------------
                                                                                                    #music part   ((KAL))
elif "Hey sarah,Play some music"  in command:

# -----------------------------------------------------------------------
                                                                                                     # Time part

elif "Hey sarah, Whats the time now?" or "Hey sarah, whats the time?" in command:
    Time = datetime.datetime.now().strftime("%H hours %M minutes!")
    speak("The time is " + str(Time) + ",sir!")                   #there was a f here.

# -----------------------------------------------------------------------
                                                                                                     # SOURCE CODE

elif "Hey sarah, open your source code" or "Show me the source code" in command:
    speak("Here is my source code!,sir!")
    path="C:\\Users\\Acer\\PycharmProjects\\SARA\\Sarah.py"


# -----------------------------------------------------------------------
#allow less secured apps first                                                                        #email part                                               # email
#make a new sarah email id

elif "Hey sarah, send an email" in command:
    def sendmail(to,content):
        mail=smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls
        mail.login("mail id of sarah","password")
        mail.sendmail("mail id of sarah",to,content)
        mail.close()


