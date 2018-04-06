from django.http import HttpResponse
from django.shortcuts import render
from main.models import ChatRoom
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, "index.html", {})

# 채팅방 리스트
def room(request):
    room_list = ChatRoom.objects.all().order_by('-create_time')
    context = {'room_list': room_list}
    return render(request, 'chatroom/room.html', context)

# 채팅방 입장
def detail(request):
    return render(request, 'chatroom/detail.html', context)

def signup(request):
    ctx = {}
    return render(request, "signup.html", ctx)

def login(request):
    return render(request, "login.html", {})