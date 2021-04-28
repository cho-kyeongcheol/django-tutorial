from django.db import models


class users(models.Model):   
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45) #사용자가 직접 입력하지 않아도 자동으로 시간 받아오기
    email = models.CharField(max_length=45) #default ='', content 에 아무것도 안써도 null에러 안나게

    def __str__(self): # idx 사용자가 입력한대로 String 받아오기
        return self.user_id

class audiofiles(models.Model):
    id = models.AutoField(primary_key=True)
    audio_script = models.TextField(null=True)

class Song(models.Model):
    name = models.CharField(max_length=125)
    audio_file = models.FileField()


# Create your models here.
