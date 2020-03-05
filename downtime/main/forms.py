from django import forms
from main.models import Movie, Music, Book


class MovieForm(forms.Form):
    model = Movie
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))


class MusicForm(forms.Form):
    model = Music
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))


class BookForm(forms.Form):
    model = Book
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))
