from django.http import HttpResponse
from django.shortcuts import render
from main.models import ChatRoom
# Create your views here.

def index(request):
    return render(request, "index.html", {})

# 채팅방 리스트
def room(request):
    room_list = ChatRoom.object.all().order_by(create_time)
    context = {'room_list': room_list}
    return render(request, 'chatroom/room.html', context)

# 채팅방 입장
def detail(request):
    return render(request, 'chatroom/detail.html', context)