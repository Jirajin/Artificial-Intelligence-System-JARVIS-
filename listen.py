import speech_recognition as sr

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.energy_threshold = 4000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in').lower()
        print(f'You said: {query}')

    except:
        return ""
       # print('Please try again')

    query = str(query)
    return query.lower()