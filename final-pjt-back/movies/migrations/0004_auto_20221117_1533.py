# Generated by Django 3.2.13 on 2022-11-17 06:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_alter_movie_genre_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='wish_users',
            field=models.ManyToManyField(related_name='wish_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]