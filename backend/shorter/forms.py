from django import forms
from django.contrib.auth.forms import UserCreationForm
from shorter.models import User

class RegistForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=False, help_text="Optional", label="이름")
    username = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=250, help_text="Required Information Email")
    
    class Meta: # 의무 X
        model = User
        field = (
            'username',
            'full_name',
            'email',
            'password1',
            'password2',
        )