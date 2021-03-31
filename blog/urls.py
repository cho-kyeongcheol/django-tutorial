from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('regist', views.regist, name='regist'),
    path('login', views.login, name='login'),
    path('userlist', views.userlist, name='userlist'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('login', views.login, name='login'),
    # path('userview', views.userview, name='userview'),
    # path('show', views.show, name='show'),
    
    path('user_insert', views.user_insert, name='user_insert'),


 
]
