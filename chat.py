from chatterbot import ChatBot
import speak
import listen
from chatterbot.trainers import ListTrainer
import os

chatbot = ChatBot('Jarvis')
# trainer = ListTrainer(chatbot)

# for _file in os.listdir('chats'):
#   chats = open('chats/'+_file, 'r').readlines()
#   trainer.train(chats)


def Chat():
    while True:
        sentence = listen.Listen()
        print('ready!')
        query = str(sentence)
        speak.Say(chatbot.get_response(query))
        if 'exit' in query:
            break
