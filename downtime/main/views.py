from django.shortcuts import render
from main.models import Movie, Music, Book
from django.views.generic import CreateView, DetailView, ListView


class MovieLibraryView(ListView):
    model = Movie

    def get(self, request):
        movie = self.get_queryset().all()
        return render(request, "pages/movie-library.html", {"movie": movie})


class MovieDetailView(DetailView):
    model = Movie
    query_pk_and_slug = True

    def get(self, request, slug):
        movie = self.get_queryset().get(slug__iexact=slug)
        return render(request, "pages/movie-card.html", {"movie": movie})


class MovieCreateView(CreateView):
    model = Movie
    fields = "__all__"
    template_name = "pages/movie-form.html"


class MusicLibraryView(ListView):
    model = Music

    def get(self, request):
        music = self.get_queryset().all()
        return render(request, "pages/music-library.html", {"music": music})


class MusicDetailView(DetailView):
    model = Music
    query_pk_and_slug = True

    def get(self, request, slug):
        music = self.get_queryset().get(slug__iexact=slug)
        return render(request, "pages/music-card.html", {"music": music})


class MusicCreateView(CreateView):
    model = Music
    fields = "__all__"
    template_name = "pages/music-form.html"


class BookLibraryView(ListView):
    model = Book

    def get(self, request):
        book = self.get_queryset().all()
        return render(request, "pages/book-library.html", {"book": book})


class BookDetailView(DetailView):
    model = Book
    query_pk_and_slug = True

    def get(self, request, slug):
        book = self.get_queryset().get(slug__iexact=slug)
        return render(request, "pages/book-card.html", {"book": book})


class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    template_name = "pages/book-form.html"
