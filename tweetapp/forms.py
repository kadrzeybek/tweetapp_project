from django import forms
from django.forms import ModelForm
from tweetapp.models import tweet
class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="Nickname",max_length=10)
    message_input = forms.CharField(label="Message",
                                    widget=forms.Textarea(attrs={"class":"costumform"}))
    