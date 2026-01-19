from .models import Profile
from django import forms
from django.contrib.auth.models import User


 # Why is Meta class needed
        # Because a ModelForm needs instructions about: 
        # Which model it represents
        # Which fields to include
        # Which fields to exclude
        #  How to map model fields → form field
 
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class UserRegistrationForm(forms.ModelForm): 

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'email', 'first_name', 'last_name'}

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)
    

            


    

