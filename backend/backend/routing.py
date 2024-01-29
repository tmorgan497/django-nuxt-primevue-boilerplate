# backend/backend/routing.py

from . import consumers
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter


websocket_urlpatterns = [
    re_path(r'ws/test/$', consumers.TestConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        websocket_urlpatterns
    )
})
