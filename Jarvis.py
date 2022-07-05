import datetime
import random
import json

import pyttsx3
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from jarvisUI import Ui_JarvisUI

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# ------------------------------------------------------------------------------------------
Name = "Jarvis"

import chat
from listen import Listen
from speak import Say
from task import NonInputExecution, InputExecution, OpenApps


# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty('voices')
# print(voices[2].id)

GREETINGS_RES = ["can I do anything else for you sir", "what else can i do for you sir",
                 "anything else sir", "can I help you with anything else?", "do you have any other wish sir"]

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Say('Good Morning,sir!')
    elif hour >= 12 and hour < 18:

        Say('Good Afternoon,Sir!')
    else:
        Say('Good Evening,sir!')

    Say('how may I help you?')


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        wishMe()
        while True:
            sentence = Listen()
            result = str(sentence)

            if sentence == "bye":
                sys.exit()

            sentence = tokenize(sentence)
            X = bag_of_words(sentence, all_words)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X).to(device)

            output = model(X)

            _, predicted = torch.max(output, dim=1)

            tag = tags[predicted.item()]

            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]

            if prob.item() > 0.75:
                for intent in intents['intents']:
                    if tag == intent["tag"]:
                        reply = random.choice(intent["responses"])

                        if "time" in reply:
                            NonInputExecution(reply)

                        elif "date" in reply:
                            NonInputExecution(reply)

                        elif "day" in reply:
                            NonInputExecution(reply)

                        elif "temperature" in reply:
                            NonInputExecution(reply)

                        elif "introduction" in reply:
                            NonInputExecution(reply)

                        # ----------------------------------------------------------------
                        # ----------------------------------------------------------------
                        elif "wikipedia" in reply:
                            InputExecution(reply, result)
                            Say(random.choice(GREETINGS_RES))

                        elif "google" in reply:
                            InputExecution(reply, result)
                            Say(random.choice(GREETINGS_RES))

                        elif "calculate" in reply:
                            InputExecution(reply, result)
                            Say(random.choice(GREETINGS_RES))

                        elif "play" in reply:
                            InputExecution(reply, result)
                            Say(random.choice(GREETINGS_RES))

                        elif "how to" in reply:
                            InputExecution(reply, result)

                        elif "open" in reply:
                            InputExecution(reply, result)
                            Say(random.choice(GREETINGS_RES))

                        elif "close" in reply:
                            InputExecution(reply, result)
                            Say(random.choice(GREETINGS_RES))

                        elif "chat" in reply:
                            Say('why not!')
                            chat.Chat()

                        else:
                            Say(reply)
                       # Say(random.choice(GREETINGS_RES))

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        # self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("KNNm.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("giphy.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout. \
            connect(self.showTime)
        timer.start(1000)
        self.ui.label.setPixmap(
            QPixmap("abstract-metallic-red-black-frame-layout-design-tech-innovation-concept-background_71775-998.jpg"))
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


apk = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(apk.exec_())
