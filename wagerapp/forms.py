from django import forms
from wagerapp.models import AvailableLine, Bettor, Game, Wager
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model= User
        fields = ('username', 'email',  'password')

class BettorForm(forms.ModelForm):
    class Meta:
        model=Bettor
        fields = ('balance',)