from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False, max_length=200)

    def get_absolute_url(self):
        kwargs = {
            "slug": self.slug
        }
        return reverse("main:movie-detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Music(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False, max_length=200)

    def get_absolute_url(self):
        kwargs = {
            "slug": self.slug
        }
        return reverse("main:music-detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False, max_length=200)

    def get_absolute_url(self):
        kwargs = {
            "slug": self.slug
        }
        return reverse("main:book-detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
