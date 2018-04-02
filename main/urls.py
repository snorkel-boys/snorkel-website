from django.urls import path, include, re_path
# 헌수 궁금증) include 왜 넣는 거지? 
from . import views
from . views import signup
from . views import login

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('chatroom/', views.room, name='room'),
    path('chatroom/(?P<room_id>\d+)`/$', views.detail, name='detail'),
]