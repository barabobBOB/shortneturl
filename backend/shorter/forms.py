import email
from math import remainder
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
        
class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "이메일"}),
        max_length=100,
        required=True
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={"class": "form-control","placeholder":"패스워드"}),
        max_length=20,
        required=True
    )
    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class":"custom-control-input", "id": "_loginRememberMe"}),
        required=False,
        disabled=False 
    )
    