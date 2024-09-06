import string
from django.utils.crypto import get_random_string


def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug + "-" + get_random_string(length=2, allowed_chars="0123456789")
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = (
            slug + "-" + get_random_string(length=2, allowed_chars="0123456789")
        )
    return unique_slug
