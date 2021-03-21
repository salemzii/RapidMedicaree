from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    phoneNumber = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phoneNumber']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
