import re

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


from .utils import unique_slugify


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
