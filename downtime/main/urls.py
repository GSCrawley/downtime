from django.urls import path
from django.views.generic import TemplateView
from main.views import (
    MovieLibraryView,
    MovieDetailView,
    MovieCreateView,
    MusicLibraryView,
    MusicDetailView,
    MusicCreateView,
    BookLibraryView,
    BookDetailView,
    BookCreateView,
)

app_name = "main"
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/index.html"), name="index"),
    path("library", TemplateView.as_view(template_name="pages/pick-library.html"), name="library"),
    path("library/movies", MovieLibraryView.as_view(), name="movie"),
    path("library/movies/create", MovieCreateView.as_view(), name="movie-create"),
    path("library/movies/<slug:slug>", MovieDetailView.as_view(), name="movie-detail"),
    path("library/music", MusicLibraryView.as_view(), name="music"),
    path("library/music/create", MusicCreateView.as_view(), name="music-create"),
    path("library/music/<slug:slug>", MusicDetailView.as_view(), name="music-detail"),
    path("library/books", BookLibraryView.as_view(), name="book"),
    path("library/books/create", BookCreateView.as_view(), name="book-create"),
    path("library/books/<slug:slug>", BookDetailView.as_view(), name="book-detail"),
]
