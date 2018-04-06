from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

# from django.urls import include, re_path
# from . import views
#
# urlpatterns = [
#     re_path(r'^$', views.about, name='about'),
#     re_path(r'^new/$', views.new_room, name='new_room'),
#     re_path(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
# ]
