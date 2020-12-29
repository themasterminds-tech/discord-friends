from django import forms
from django.core.exceptions import ValidationError
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
