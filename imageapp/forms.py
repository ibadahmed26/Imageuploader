from django import forms
from .models import ImageModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'
        labels = {'photo': ''}


class SingupForm(UserCreationForm):
    password2 = forms.CharField(label='Enter Password (again)',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}