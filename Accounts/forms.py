from django import forms

from .models import Profile
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

# UserRegistrationForm, UserUpdationForm, ProfileUpdationFOrm



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    # specifies - which model the form will interact with and which fields should be included
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']        # username, password1, password2 already specified by UserCreationForm



