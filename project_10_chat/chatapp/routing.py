from django.urls import re_path
from . import consumers
from django.urls import path

print("WEBSOCKET ROUTING LOADED")

websocket_urlpatterns = [
    path("ws/<str:room_name>/", consumers.ChatConsumer.as_asgi())
]