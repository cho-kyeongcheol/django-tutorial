from django import forms
from .models import users

class UserForm(forms.ModelForm):

    class Meta:
        model = users
        # fields = ['user_id','password','name','email']
        fields = "__all__"
