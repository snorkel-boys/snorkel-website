from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import ChatRoom
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)
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

# 회원가입
def signup(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email, password)
    return render(request, "signup.html", {})
    # 나중에 구현할 내용 : 회원정보 입력하고 sing up 버튼 누르면 팝업창으로 "회원가입 완료" -> 확인 누르면 메인페이지로

# 로그인
def login(request):
    ctx = {}
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            ctx.update({"error" : "회원가입 정보가 없습니다"})
    return render(request, "login.html", {})
