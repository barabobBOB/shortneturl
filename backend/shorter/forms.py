import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from shorter.models import User

class RegistForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=False, help_text="Optional", label="이름") # label -> 필드 이름을 변경 시켜줌
    username = forms.CharField(max_length=30, required=False, help_text="Optional") 
    email = forms.EmailField(max_length=250, help_text="Require email")
    
    class Meta: # 의무 X
        model = User
        fields = (
            'username',
            'full_name',
            'email',
            'password1',
            'password2',
        )