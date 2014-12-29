from django import forms
from accounts.models import AvailableLine,Account, Game, Team, WagerMade
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model= User
        fields = ('username', 'email',  'password')

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields = ('name','balance', )
        
class WagerForm(forms.ModelForm):
    class Meta:
        model=WagerMade
        fields = ('amount',)