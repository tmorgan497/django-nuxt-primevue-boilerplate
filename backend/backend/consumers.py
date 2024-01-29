# backend/backend/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "test",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "test",
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        await self.channel_layer.group_send(
            "test",
            {
                "type": "test_message",
                "message": message
            }
        )

    async def test_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            "message": message
        }))
