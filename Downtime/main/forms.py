from django import forms
from main.models import Movie


class MovieForm(forms.Form):
    model = Movie
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))
