from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Friends
from django.core import validators


class FriendForm(forms.ModelForm):
    user_id = forms.CharField(required=True, label='Discord User ID', validators=[validators.MinLengthValidator(
        18), validators.MaxLengthValidator(18)], widget=forms.TextInput(attrs={'class': 'form-control w-50'}))
    username = forms.CharField(
        max_length=255, required=True, label='Discord Username', widget=forms.TextInput(attrs={'class': 'form-control w-50'}))
    tag = forms.CharField(required=True, label='Discord Tag', validators=[validators.MinLengthValidator(
        4), validators.MaxLengthValidator(4)], widget=forms.TextInput(attrs={'class': 'form-control w-50'}))

    class Meta:
        model = Friends
        fields = '__all__'


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter username', 'style': 'width: 90%;'}), help_text='Acceptable characters: [letters][alphabets][ @ . + i _ ]\n\n\t Characters must be 150 or less!')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email',
                                                            'style': 'width: 90%;'}), help_text='Enter any email you want as long as it flows the valid rules and patterns')
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password', 'style': 'width: 90%;'}), label='Password', help_text='❌\tYour password can\'t be too similar to your username.\n❌\tYour password must contain at least 8 characters\n❌\tYour password can\'t be commonly used and can\'t be entirely numeric')
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Re-enter password', 'style': 'width: 90%;'}), label='Confirm password', help_text='Howdy, enter same password as before to create your brand new account!')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
