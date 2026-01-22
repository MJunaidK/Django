from django.shortcuts import render, get_object_or_404
from .models import ChatRoom

def index(request):
    rooms = ChatRoom.objects.all()
    return render(request, "chatapp/index.html", {"rooms": rooms})

def chat_room(request, room_slug):
    room = get_object_or_404(ChatRoom, slug=room_slug)
    username = request.user.username if request.user.is_authenticated else "Guest"
    return render(request, "chatapp/room.html", {"room": room, "username": username})