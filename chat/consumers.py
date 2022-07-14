# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.sessions import CookieMiddleware, SessionMiddleware

from .models import Channel_names, Room

from asgiref.sync import sync_to_async



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chatting_%s' % self.room_name 


        if self.scope.get('user').is_authenticated:
            await Room.add(self.room_name, self.scope.get('user'))
            await Channel_names.add(self.channel_name, self.scope.get('user'))

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # session = self.scope["session"]
        
        # print('>>>>>', self.scope)

        # print('스코프유저 > ', self.scope.get('user'))
        # print('채널레이어 : ', self.channel_layer)
        # print("현재세션 : ", session)        
        # print("스코프 url 주소", self.scope['url_route'])
        # # print(self.scope['kwargs'])
        # print("방제 : ", self.room_name)
        # print("그룹네임 : ", self.room_group_name)
        # print("채널네임 : ", self.channel_name)

        

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        print('연결끊김 : ',self)

        if self.scope.get('user').is_authenticated:
            await Room.remove(self.room_name, self.scope.get('user'))
            await Channel_names.remove(self.channel_name)
            

    # Receive message from WebSocket 
    # 누군가 웹소켓에서 send한 내용을 받는다.
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        method_type = text_data_json['method_type']
        username = text_data_json['username']
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': method_type, #async def method_type(self, event):
                'username': username,
                'message': message,
            }
        )

    # Receive message from room group
    async def chat_message_func(self, event):
        username = event['username']
        message = event['message']
        
        if(message == 'whoami'):
            print("채널네임을 프린트합니다. : ", self.channel_name)


        # Send message to WebSocket
        await self.send(text_data=json.dumps({
           'username':username, 
           'message':message,
           'channel_name': self.channel_name
        }))

    async def kick_user_func(self, event):
        username = event['username']
        message = event['message']
        kick_user = await Channel_names.get(username)
        
        await self.send(text_data=json.dumps({
        'username':username, 
        'message':message,
        'channel_name': self.channel_name
        }))

        await self.channel_layer.group_discard(
        self.room_group_name,
        kick_user
        )
        await Channel_names.remove(kick_user)


        # if self.scope.get('user').is_authenticated:
        #     await Room.remove(self.room_name, 1)
            





