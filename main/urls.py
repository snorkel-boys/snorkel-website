from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^chatroom/$', views.room, name='room'),
    url(r'^chatroom/(?P<room_id>\d+)`/$', views.detail, name='detail'),
]
