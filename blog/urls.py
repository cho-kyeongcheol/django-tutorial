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
    path('logout', views.logout, name='logout'),
    path('datatable', views.datatable, name='datatable'),
    path('usertable', views.usertable, name='usertable'),
    path('userdetail/<int:id>', views.userdetail, name='userdetail'),
    # path('userview', views.userview, name='userview'),
    # path('show', views.show, name='show'),
    
    path('user_insert', views.user_insert, name='user_insert'),

    path('upload_file', views.upload_file, name='upload_file'),
    
    path('upload_file', views.upload_file, name='upload_file'),
 
]
