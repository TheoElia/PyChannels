from channels.generic.websocket import AsyncWebsocketConsumer
import json
from Jake.lib.parser import Parser
from Jake.lib.tokenizer import *
from Jake.lib.models import Message
import time


class StartChat:
    # Asks user for input
    def __init__(self,):
        #self.command = input("Waiting for your input> ")
        self.name = "Jake"

    def start(self,userinput):
        tokens = Tokenizer().tokenize(userinput)
        res = []
        mes = []
        cat = []
        checker = ""
        for index,i in enumerate(tokens):
            if len(tokens)<2:
                checker +=i+""
            else:
                if not index == len(tokens)-1:
                    checker += i + " "
                else:
                    checker += i + ""
        #print(checker)
        all = Message.objects.filter(message=checker)
        if len(all) > 0:
            for i in all:
                res.append(i.response)
                mes.append(i.message)
                cat.append(i.category)
        else:
            mes = tokens
        message = []
        for i in mes:
            m = i.split(" ")
            for i in m:
                message.append(i)
        #print(message)
        if len(cat)>0:
            res = []
            all = Message.objects.filter(category=cat[0])
            if len(all) > 0:
                for i in all:
                    res.append(i.response)
        #print(res)
        #print(cat)
        return Parser().parse(res=res,snt=tokens)







class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        output = StartChat().start(message)
        time.sleep(2)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': output
            }

        )




    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    #async def reply_message(self, event):
    #    message = event['message']
        #output = StartChat().start(message)

        # Send message to WebSocket
        #await self.send(text_data=json.dumps({
         #   'output': output
        #}))