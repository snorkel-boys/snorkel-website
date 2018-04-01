from django.urls import path, include
# include 왜 넣는 거지?
from . import views
from . views import signup
from . views import login


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login')
]
