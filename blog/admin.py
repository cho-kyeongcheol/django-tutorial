from django.contrib import admin

from .models import Post #import class post from models.py

admin.site.register(Post) #register calss post --> blog.post shows up in 'admin/' page
# Register your models here.
