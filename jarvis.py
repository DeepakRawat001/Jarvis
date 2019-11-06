import speech_recognition as sr#calnder
import os,time,pyglet,subprocess
import webbrowser as web
from gtts import gTTS
import speak,CurrentTime
import regard
import google


def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration =1)
        audio=r.listen(source)
        try:
            #return r.recognize_sphinx(a)
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            print("sorry i can't recognize what you spoke")
        except sr.RequestError as e:
                print("Recog Error; {0}".format(e))
def browser():    
    t="what you want to search"
    print("searching")
    try:
        #comp.speak(t)
        text=listen()
        print("searching")
        web.open("https://www.google.com/search?source=hp&ei=ieZ-W_CJCJr_9QOonay4Dw&q="+text+"&oq="+text+"&gs_l=psy-ab.3..0l9j0i131k1.1138.2025.0.2216.5.5.0.0.0.0.280.500.2-2.2.0..2..0...1.1.64.psy-ab..3.2.498....0._Y7CqcemL4Y")
        print(text)
        #mainfunction()
    except:
        pass
def youtube():
    try:
        text=listen()
        print("searching")
        web.open("https://www.youtube.com/results?search_query="+text)
    except:
        pass
    
def offline():
    speak.tts("i am going offline \n ")
    exit()

def question():
    try:
        text=listen()
        google.google(text)
        print(text)
    except :

        pass

def mainfunction():
    print("say something")
    r.pause_threshold=1
    r.adjust_for_ambient_noise(source, duration =1)
    audio=r.listen(source)
    #print("hello")
    try:
        #z=r.recognize_sphinx(a)
        z=r.recognize_google(audio)
        print(z)
        regard.respect(z)
        if (z=="search the browser"): #z== "search":
            speak.tts("what you want to search")
            browser()
            #os.remove("hello.mp3")
        #if (z=="search"):

             #browser()
        elif z=="jarvis go offline"or z=="go offline":
            offline()
        elif z=="how are you Jarvis"or z=="how are you":
            speak.tts("i am good")
        elif z=="OK Jarvis":
            speak.tts("ask me some question")
            question()
        elif(("what" in z or "show" or "tell" )and "time" in z):
            CurrentTime.currentTime()
        
        elif z=="Jarvis open Notepad":
            subprocess.check_output(["notepad.exe"],shell=True).decode('utf-8').split('\n')

            
       
      
        x=["go YouTube","search YouTube","search on YouTube","search in YouTube","start Youtube","Jarvis go YouTube",
           "Jarvis search YouTube","Jarvis search on YouTube","Jarvis search in YouTube","Jarvis start Youtube"]
        if z in x:
            speak.tts("what do you want to search")
            youtube()
        '''if z=="close the browser":
            print("hello")
            os.system("TASKKILL /F /IM Internet Explorer.exe")'''
        

    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    r = sr.Recognizer()
    #speak.tts("welcome sir how may i help you")
    while (True):
        with sr.Microphone() as source:
            #try:
            #os.remove(r"E:/python/New folder/jarvis/hello.mp3")
            mainfunction()
           # except:
                #print("i did not recognized you")
        
 

