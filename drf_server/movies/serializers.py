from rest_framework import serializers
from .models import Actor, Director, Movie, Comment, Rating, Similar

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'adult', 'poster_path')

        
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'like_comment_users',)


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ('user', 'movie',)


class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Director
        fields = '__all__'


class SimilarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Similar
        fields = '__all__'