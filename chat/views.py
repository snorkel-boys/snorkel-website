from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .mask import search_list
from django.contrib.auth.models import User
from chat.models import Room 

def index(request):
    try:
        room_list = Room.objects.all().order_by('-create_time')
    except Room.DoesNotExist:
        room_list = None
        
    context = {'room_list': room_list}
    return render(request, 'chat/index.html', context)

def room(request, room_name):
    print("$$$$$$ 1 : ", request.user.get_username())
    #print("$$$$$$ 2 : ", User.get_username())
    #print("$$$$$$ 3 : ", User.get_username(self))

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'user_name': mark_safe(json.dumps(request.user.get_username()))
    })

def mask(request):
    ctx = {}
    if request.method == "GET":
        pass
    elif request.method == "POST":
        ask = request.POST.get("film")
        try:
            filmlist = search_list(ask)
            ctx.update({"filmlist": filmlist})
            return render(request, "chat/mask.html", ctx)
        except AttributeError:
            ctx.update({"error": "검색결과가 없습니다"})
            return render(request, "chat/mask.html", ctx)
    return render(request, 'chat/mask.html', ctx)
# import random
# import string
# from django.db import transaction
# from django.shortcuts import render, redirect
# from haikunator import Haikunator
# from .models import Room
#
# def about(request):
#     return render(request, "chat/about.html")
#
# def new_room(request):
#     new_room = None
#     while not new_room:
#         with transaction.atomic():
#             haikunator = Haikunator()
#             label = haikunator.haikunate()
#             if Room.objects.filter(label=label).exists():
#                 continue
#             new_room = Room.objects.create(label=label)
#     return redirect(chat_room, label=label)
#
# def chat_room(request, label):
#     room, created = Room.objects.get_or_create(label=label)
#
#     messages = reversed(room.messages.order_by('-timestamp')[:50])
#
#     return render(request, "chat/room.html", {
#         'room': room,
#         'messages': messages,
#     })
