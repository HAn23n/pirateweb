from django import forms
from .models import User

class LoginForm(forms.Form):
    user_id = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput, max_length=16)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'password', 'academy', 'sex', 'city', 'age']
        widgets = {
            'password': forms.PasswordInput(),
        }
