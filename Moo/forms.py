from django import forms

class Cow_talk_input(forms.Form):
    text=forms.CharField(max_length=39)