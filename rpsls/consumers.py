from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if 'opponent' in text_data_json:
            opponent = text_data_json['opponent']

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'opponent_message',
                    'opponent': opponent
                }
            )
            print('creator')
        elif 'creator' in text_data_json:
            creator = text_data_json['creator']

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'creator_message',
                    'creator': creator
                }
            )
            print('creator')
        elif 'opponent_selection' in text_data_json:
            selection = text_data_json['opponent_selection']

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'opponent_selection_message',
                    'opponent_selection': selection
                }
            )
        elif 'creator_selection' in text_data_json:
            selection = text_data_json['creator_selection']

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'creator_selection_message',
                    'creator_selection': selection
                }
            )

        elif 'message' in text_data_json:

            message = text_data_json['message']

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
    
    def opponent_message(self, event):
        opponent = event['opponent']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'opponent': opponent
        }))
    def creator_message(self, event):
        creator = event['creator']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'creator': creator
        }))

    def creator_selection_message(self, event):
        selection = event['creator_selection']
        self.send(text_data=json.dumps({
            'creator_selection': selection
        }))
    
    def opponent_selection_message(self, event):
        selection = event['opponent_selection']
        self.send(text_data=json.dumps({
            'opponent_selection': selection
        }))
        