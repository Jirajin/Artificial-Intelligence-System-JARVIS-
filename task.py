import datetime
import random
import wikipedia
import pywhatkit
import wolframalpha
import requests
import webbrowser
import os
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
from speak import Say

try:
    app = wolframalpha.Client("YJA7G8-W3YWH7TT7P")
except Exception:
    Say("Can't reach A I server")

GREETINGS_RES1 = ["Ok Sir , Wait A Second!", "as you wish sir", "give me a moment sir", "on it sir", "hang on a second",
                  "okay sir"]
GREETINGS_RES2 = ["Your Command Has Been Completed Sir!", "task has been executed sir",
                  "task has been completed successfully", "Your Command Has Been executed Sir",
                  "task has been executed successfully"]


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)


def Date():
    date = datetime.date.today()
    Say(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def CloseAPPS(query):
    query = str(query)
    Say("Ok Sir , Wait A second!")

    if 'youtube' in query:
        os.system("TASKKILL /F /im Chrome.exe")

    elif 'chrome' in query:
        os.system("TASKKILL /f /im Chrome.exe")

    elif 'telegram' in query:
        os.system("TASKKILL /F /im Telegram.exe")

    elif 'code' in query:
        os.system("TASKKILL /F /im code.exe")

    elif 'instagram' in query:
        os.system("TASKKILL /F /im chrome.exe")

    Say("Your Command Has Been Succesfully Completed!")


def OpenApps(query):
    query = str(query)
    Say("Ok Sir , Wait A Second!")

    if 'code' in query:
        os.startfile("E:\\Applications\\Microsoft VS Code\\Microsoft VS Code\\Code.exe")

    elif 'telegram' in query:
        os.startfile("E:\\Applications\\Telegram Desktop\\Telegram Desktop\\Telegram.exe")

    elif 'chrome' in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'facebook' in query:
        webbrowser.open('https://www.facebook.com/')

    elif 'instagram' in query:
        webbrowser.open('https://www.instagram.com/')

    elif 'maps' in query:
        webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

    elif 'youtube' in query:
        webbrowser.open('https://www.youtube.com')

    Say("Your Command Has Been Completed Sir!")


def Temp():
    search = "temperature in khulna"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    Say(f"The Temperature Outside Is {temperature} celcius")


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "temperature" in query:
        Temp()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

    elif "introduction" in query:
        Say("I am Jarvis, an Artificial Intelligence System. I was created to automate your device and make your life a lot easier. I can do many tasks just on your voice command and many tasks and features can be added with time. So let the journey to the future begin")


# input-----------------------------------------
#

def InputExecution(tag, query):
    if "wikipedia" in tag:
        try:
            name = str(query).replace("who is", "").replace("what is", "").replace("which is", "").replace(
                "tell me about", "").replace("wikipedia", "")
            result = wikipedia.summary(name, sentences=1)
            Say(result)
        except Exception:
            Say("sorry,sir. no matches found.")

    if "calculate" in tag:
        try:
            name = str(query).replace("calculate", "")
            res = app.query(name)
            print(next(res.results).text)
            Say("the result is")
            Say(next(res.results).text)
        except Exception:
            print('Internet connection error...')

    elif "google" in tag:
        Say(random.choice(GREETINGS_RES1))
        query = str(query).replace("search", "").replace("search in google", "").replace("google", "").replace(
            "google search", "")
        pywhatkit.search(query)
        Say(random.choice(GREETINGS_RES2))

    elif "play" in tag:
        query = str(query).replace("play", "").replace("play on youtube", "")
        pywhatkit.playonyt(query)
        Say(f'Playing {query}')

    elif "open" in tag:
        query = str(query).replace("open", "")
        Say(random.choice(GREETINGS_RES1))

        if 'code' in query:
            os.startfile("C:\\Users\\J.I.Rajin\\AppData\\Local\\Programs\\Microsoft VS Code.exe")

        elif 'telegram' in query:
            os.startfile("E:\\Applications\\Telegram Desktop\\Telegram Desktop\\Telegram.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Say(random.choice(GREETINGS_RES2))

    elif "close" in tag:
        query = str(query).replace("close", "")
        Say(random.choice(GREETINGS_RES1))

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'facebook' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        Say(random.choice(GREETINGS_RES2))

    elif 'how to' in tag:
        Say("Getting Data From The Internet !")
        op = query.replace("jarvis", "")
        max_result = 1
        how_to_func = search_wikihow(op, max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Say(how_to_func[0].summary)
