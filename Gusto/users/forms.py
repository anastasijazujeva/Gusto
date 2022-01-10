from django.contrib.auth.models import User
from django import forms
from django.forms.fields import CharField, EmailField
from .models import Profile

# profile form from User model for profile update 
class UpdateProfileForm(forms.ModelForm):
    first_name = CharField(max_length = 150, required = False)
    last_name = CharField(max_length = 150, required = False)
    email = EmailField(required = False)

    # display specific fields of the form
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

# additional profile form from Profile model for profile update
class UpdateProfileForm_Add(forms.ModelForm):
    # display specific fields of the form
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'city', 'country']