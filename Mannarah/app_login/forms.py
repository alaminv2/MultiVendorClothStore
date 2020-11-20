from django import forms
from .models import Profile, MyUser
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class userSignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')
