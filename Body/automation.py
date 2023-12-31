import wikipedia  # pip install wikipedia
import webbrowser
import pywhatkit #for google search
import pyautogui #for shortcut
from speedtest import Speedtest
import datetime
import keyboard
import os 

import sys
sys.path.append("B:\Ai Assistant\Ai Voice Assistant")

from time import sleep
from utils.speak import speak
from Controls.control import Voice_ID_English
from Controls.control import Voice_ID_Hindi 
import Controls.control as ctr
from utils.command import takeCommand


def queryToTask(query):
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            query = query.replace("according to wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Searching Wikipedia...")
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'bing' in query:
            query= query.replace("bing","")
            query= query.replace("search","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(0.3)
            pyautogui.press("Enter")

        elif 'google' in query or 'search' in query.lower():
            query=str(query.replace("google",""))
            query=str(query.replace("search",""))
            pywhatkit.search(query)
            
        elif 'how far is' in query:
            query=str(query.replace("google",""))
            query=str(query.replace("search",""))
            query=str(query.replace("here",""))
            pywhatkit.search(f"{query} from Graphic Era Hill University google maps")
        
        elif 'on youtube' in query or 'play a video' in query:
            query=query.replace("on youtube","")
            query=query.replace("play a video","")
            query=query.replace("youube","")
            query=query.replace("play","")
            web=f"https://www.youtube.com/results?search_query={query}"
            speak("This is what I found on Youtube")
            webbrowser.open(web)
        
        # Youtube Commands
        elif 'pause' in query:
            pyautogui.press('k')
            speak("Video Paused")

        elif 'resume' in query:
            pyautogui.press('k')
            speak("Video Played")

        elif 'mute video' in query:
            pyautogui.press('m')
            speak("Video Muted")

        elif 'volume up' in query:
            pyautogui.press("up", presses=5)

        elif 'volume down' in query:
            pyautogui.press('down',presses=5)

        #Opening Sites

        elif 'open github' in query:
            webbrowser.open("github.com")

        #Browser control 
        elif 'open new tab' in query :
            pyautogui.hotkey("ctrl","t")
        
        elif 'close tab' in query or 'closed tab' in query:
            pyautogui.hotkey('ctrl','f4')

        # #Window Control 
        elif 'show task' in query :
            pyautogui.hotkey('win','tab')
        
        elif 'list task' in query:
            pyautogui.hotkey('ctrl','shift','esc')

        elif 'close window' in query or 'closed window' in query:
            pyautogui.hotkey('alt','f4')
 
        elif 'new desktop' in query:
            pyautogui.hotkey('ctrl','win','d')

        elif 'change layout' in query or 'snap layout' in query :
            pyautogui.hotkey('win','z')

     #Functionality 
        elif 'open clipboard' in query or 'open clip board' in query:
            pyautogui.hotkey('win','v')
 
        elif 'internet speed' in query or 'speed test' in query:
            speak("Please wait ! while I calculate upload and download speed")
            wifi=Speedtest()
            upload_speed=float(f'{wifi.upload()/(1024*1024):.2f}')   # 1MB = 1024 * 1024 bytes
            download_speed=float(f'{wifi.download()/(1024*1024):.2f}')
            
            print(f"Wifi Download Speed > {download_speed}Mb/s")
            print(f"Wifi upload Speed > {upload_speed} Mb/s")
            speak(f"Wifi Download Speed > {download_speed} MB per second")
            speak(f"Wifi upload Speed > {upload_speed} MB per second")

        elif 'take a screenshot' in query or 'capture screenshot' in query or 'take screenshot' in query:
            speak("Sir, tell me the name of this screenshot file")
            name=takeCommand().lower()
            speak("Sir, Please hold the screen . I'll be taking a screenshot")
            img=pyautogui.screenshot()
            img.save(f'DataStore/ScreenShot/{name}.png')
            speak("I am done sir, Screenshot is saved in ScreenShot folder")

        elif 'record screen' in query or 'screen record' in query or 'record the screen' in query:
            pyautogui.hotkey('win','alt','r')
            sleep(1)
            speak("Screen Recording started")

        elif 'stop recording' in query or 'stop capture' in query:
            pyautogui.click(1800,150)
            speak("Screen recording saved in Data Store")


        #Date ,time and day
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            date=datetime.datetime.today()
            speak(date)

        elif 'day' in query :
            day= datetime.datetime.now().strftime("%A")
            speak(f"Sir today it is {day}")

        #Opening Applications 
        elif 'open' in query:
            query= query.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(0.2)
            pyautogui.press("Enter")

        #Sending Whatsapp message 
        elif 'send message' in query or "send a message" in query:
            query= query.replace("send a message to","")
            query= query.replace("send message","")
            query= query.replace("send a message","")
            query= query.replace("to","")
            pyautogui.press("super")
            pyautogui.typewrite("whatsapp")
            sleep(0.2)
            pyautogui.press("Enter")
            sleep(2)
            pyautogui.hotkey("ctrl","f")
            sleep(1)
            pyautogui.typewrite(f"{query}")
            sleep(3)
            pyautogui.press("down")
            sleep(0.3)
            pyautogui.press("Enter")
            speak("Sir, What should the message be?")
            msg=takeCommand(10).lower()
            if (msg!='none'):
                pyautogui.typewrite(msg)
                sleep(0.1)
                pyautogui.press("Enter")
                speak("message sent")
            else:
                speak ("No message was sent")

        elif 'gpt' in query or "using artificial intelligence" in query or 'use artificial intelligence' in query or 'use ai' in query or 'using ai' in query:
            webbrowser.open("chat.openai.com")
            sleep(5)
            prompt="prompt='You are an Assistant that helps with my work. Respond in simple, concise sentences (maximum of two sentences, in one paragraph) , Avoid formatting the text. p.s. Respond with salutation like a assistant.'"
            sleep(2)
            pyautogui.typewrite(prompt)
            sleep(0.5)
            pyautogui.press("Enter")
            exitCode()
        
        #Switching Language
        elif 'switch language' in query or 'change language' in query or 'भाषा बदलें' in query:
            if ctr.lang == 'en-in':
                ctr.lang = 'hi-in'
                speak("अभिवादन, मैं आपकी निजी सहायक, बताइये मैं आपकी क्या मदद कर सकती हूं",Voice_ID_Hindi)
            else:
                ctr.lang = 'en-in'
                speak('Using English as mode of communication',Voice_ID_English)

        elif "exit" in query.lower() or "sleep" in query.lower() or "so ja" in query.lower() or 'take a break' in query:
            if ctr.lang =='en-in':
                speak('I will be signing off sir , shutting down in 3, 2, 1...... beep',Voice_ID_English)
            else:
                speak('ध्यान रखना, उम्मीद है कि आप जल्द ही मुझे मदद करने का मौका देंगे',Voice_ID_Hindi)
            os.startfile(f'{os.getcwd()}\Detection.py')
            pyautogui.hotkey('win','m')
            exit()

def exitCode():
        if ctr.lang =='en-in':
            speak('Initiating Artificial Intelligence',Voice_ID_English)
        else:                
            speak('अब प्रतिक्रिया के लिए कृत्रिम बुद्धिमत्ता का उपयोग किया जा रहा है',Voice_ID_Hindi)
        os.startfile(f'{os.getcwd()}\Detection.py')
        sleep(2)
        pyautogui.hotkey('win','down')
        sleep(1)
        pyautogui.click(1800,900)
        sleep(1.3)
        keyboard.press('space')
        exit()
