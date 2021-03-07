from transitions.extensions import GraphMachine

from utils import send_text_message

import random


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "eat"

    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "drink"

    def is_going_to_state5(self, event):
        if event.message.text:
            text = event.message.text
            return text.lower() == "movie"
        else:
            return False

    

    #reply

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

#2
    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

#3
    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token

        food = ['fried rice','chips','hot dog','beef soup','nooodles','hamburger']
        ran = random.randint(0,5)
        send_text_message(reply_token,food[ran])
#        send_text_message(reply_token, "Trigger eat")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

#4
    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        drinks = ['black tea','bubble tea','water']
        ran = random.randint(0,2)
        send_text_message(reply_token, drinks[ran])
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")


#5
    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        movies = ['TOYS STORY','FROZEN','HUNGER GAME','AVENGERS']
        ran = random.randint(0,3)
        send_text_message(reply_token, movies[ran])
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")
