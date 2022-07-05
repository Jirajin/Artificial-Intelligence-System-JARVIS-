import pyttsx3


def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    #print(voices[2].id)
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 170)
    print("     ")
    print(f"Jarvis : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("     ")
