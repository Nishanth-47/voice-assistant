import pyautogui
import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import wikipedia
import time

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Pleasw wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)
   
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()

    if 'open youtube' in text:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open("youtube.com")

    if  'open google' in text:
        a='opening google...'
        engine.say(a)
        engine.runAndWait()
        webbrowser.open('google.com')
    

    if  'gmail' in text:
        c='opening mail...'
        engine.say(c)
        engine.runAndWait()
        webbrowser.open('gmail.com')

    if  'college' in text:
        d='opening m.kumarasamy college website...'
        engine.say(d)
        engine.runAndWait()
        webbrowser.open('www.mkce.ac.in')  

    if  'information' in text:
        e=text.replace('the information of', '')
        engine.say(wikipedia.summary(e, 1))
        engine.runAndWait() 

        
    if 'youtube search' in text:
        text = text.replace("youtube search", "")
        pyautogui.hotkey('alt', 'd') 
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write(f"{text}")
        pyautogui.press('enter')

    if 'google search' in text:
        text = text.replace("google search", "")
        pyautogui.hotkey('alt', 'd') 
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write(f"{text}")
        pyautogui.press('enter')  

        
    if 'send message to sudhir' in text:
        pywhatkit.sendwhatmsg('+918825463649',"hi da",19,16)

    
while True:
    cmd()