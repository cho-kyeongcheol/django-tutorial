from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True) #사용자가 직접 입력하지 않아도 자동으로 시간 받아오기
    content = models.TextField(default='') #default ='', content 에 아무것도 안써도 null에러 안나게

    def __str__(self): # title 사용자가 입력한대로 String 받아오기
        return self.title


# Create your models here.
