from django import forms
from apps.categories.models import Topic
from django.contrib.auth.forms import UserCreationForm


class AddTopicForm(forms.ModelForm):

     class Meta:
         model = Topic
         fields = ['title', 'description', 'category', 'status']
         widgets = {
             'category': forms.HiddenInput()
         }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')




    class Meta:
        fields = ('username', 'email', 'password1', 'password2' )

