# Generated by Django 5.0.6 on 2024-09-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
