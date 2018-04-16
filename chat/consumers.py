from channels.generic.websocket import AsyncWebsocketConsumer
import json
from chat.models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        try:
            room = Room.objects.get(name = self.room_name)
        except Room.DoesNotExist:
            room = None
        
        print("$$$$$$$$11 : ", room)
        
        if room is None:
            room = Room(name = self.room_name, label = 'test_label', cnt_member = '1')
            room.save()
        else:
            print("######1 room.cnt_member : ", room.cnt_member)
            room.cnt_member += 1
            room.save()
            print("######2 room.cnt_member : ", room.cnt_member)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        try:
            room = Room.objects.get(name = self.room_name)
        except Room.DoesNotExist:
            room = None
        print("###### room.cnt_member : ", room.cnt_member)
        
        if room is not None and room.cnt_member == 1:
            room.delete()
        else:
            room.cnt_member -= 1
            room.save()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
