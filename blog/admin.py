from django.contrib import admin

from .models import users #import class post from models.py

admin.site.register(users) #register calss post --> blog.post shows up in 'admin/' page
# Register your models here.
