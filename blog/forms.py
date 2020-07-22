from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Post, UserContact



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'autofocus': True, 'strip': False,'class': 'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['id', 'title', 'desc']
        labels = {'title': 'Title','desc':'Description'}
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
            }

class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username':'Username', 'first_name': 'First Name', 'last_name':'Last Name','email': 'Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class PasswordChangeCustomForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # def __init__(self, user, *args, **kwargs):
    #     super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
    #     self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
   
class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = ['name', 'email', 'phone', 'desc']
        labels = {'name':'Name', 'email':'Email', 'phone':'Phone Number', 'desc': 'Your Message'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control','rows':'4'})
        }
