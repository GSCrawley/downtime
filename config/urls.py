# encoding=utf-8

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

urlpatterns = [
    # Pages
    path(
        "",
        TemplateView.as_view(template_name="pages/index.html"),
        name="index",
    ),
    path(
        "library/",
        TemplateView.as_view(template_name="pages/pick-library.html"),
        name="library",
    ),
    path(
        "library/new/",
        TemplateView.as_view(template_name="pages/create-collection.html"),
        name="new_category",
    ),
    path(
        "library/music/",
        TemplateView.as_view(template_name="pages/music-library.html"),
        name="music_library",
    ),
    path(
        "library/music/card",
        TemplateView.as_view(template_name="pages/music-card.html"),
        name="music_card",
    ),
    path(
        "library/movies/",
        TemplateView.as_view(template_name="pages/movie-library.html"),
        name="movie_library",
    ),
    path(
        "library/movies/card",
        TemplateView.as_view(template_name="pages/movie-card.html"),
        name="movie_card",
    ),
    path(
        "library/books/",
        TemplateView.as_view(template_name="pages/book-library.html"),
        name="book_library",
    ),
    path(
        "library/books/card",
        TemplateView.as_view(template_name="pages/book-card.html"),
        name="book_card",
    ),
    # User management
    path(
        "users/",
        include("downtime.users.urls", namespace="users"),
    ),
    path(
        "accounts/",
        include("allauth.urls"),
    ),
    # Django Admin, use {% url "admin:index" %}
    path(
        settings.ADMIN_URL,
        admin.site.urls,
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns
