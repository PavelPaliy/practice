from django import forms
from .models import *
from .widgets import *
from django.contrib.auth.models import User
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'description']

class MeetingDateForm(forms.ModelForm):
    class Meta:
        model = MeetingDate
        fields = ['date']
        widgets = {
            'date': DateTimeInput(attrs={ 'type': 'datetime-local',  'id':'1date', 'class': 'date'})
        }
class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['start', 'end']
        widgets = {
            'start': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end': DateTimeInput(attrs={'type': 'datetime-local'})
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')