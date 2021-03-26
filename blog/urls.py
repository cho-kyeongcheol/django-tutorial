from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('regist', views.regist, name='regist'),
    path('login', views.login, name='login'),
    path('<int:pk>', views.post_detail, name='detail'),
    path('<int:pk>/update', views.post_update, name='update'),
    path('<int:pk>/delete', views.post_delete, name='delete'),
    path('user_insert', views.user_insert, name='user_insert'),


 
]
