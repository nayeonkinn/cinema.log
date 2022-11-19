from rest_framework import serializers

from .models import User
from articles.models import Article
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'poster_path',)


class ArticleSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    likes_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'content', 'spoiler', 'created_at', 'likes_count', 'movie')


class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)
    articles_count = serializers.IntegerField(source='article_set.count', read_only=True)
    articles_list = ArticleSerializer(source='article_set', many=True, read_only=True)
    wishes_count = serializers.IntegerField(source='wish_movies.count', read_only=True)
    wishes_list = MovieSerializer(source='wish_movies', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'followers_count', 'followings_count', 'articles_count', 'articles_list', 'wishes_count', 'wishes_list')
