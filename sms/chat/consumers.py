import json

from random import randint
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        #self.room_group_name = 'test'

        print(self.scope["user"])
        self.room_group_name = str(randint(1000, 9999))
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        userID = text_data_json['userID']

        print("Message:", message)
        print("userID:", userID)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'userID': userID
            }
        )

    def chat_message(self, event):
        message = event['message']
        userID = event['userID']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'userID': userID
        }))
