from django import forms
from django.contrib.auth.models import User
from UserAuthentication.models import UserInfo


class UserInfoForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserInfoCustomFieldsForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)
    portfolio = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = UserInfo
        fields = ('portfolio', 'profile_pic')
