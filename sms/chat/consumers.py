import json

from random import randint
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_group_name = 0
        self.room_group_name_list = []

    def connect(self):
        if self.room_group_name in self.room_group_name_list:
            self.room_group_name = str(randint(1, 999999999))
            self.room_group_name_list.append(self.room_group_name)
        else:
            self.room_group_name = str(randint(1, 999999999))

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({
            'group_name': self.room_group_name,
            'set_id': True
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        userID = text_data_json['userID']

        async_to_sync(self.channel_layer.group_send)(
            userID,
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
