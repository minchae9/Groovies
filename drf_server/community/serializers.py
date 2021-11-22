from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import UserSerializer

class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source='user.username')
    class Meta:
        model = Article
        fields = ('id', 'title', 'user', 'created_at', 'username')
        read_only_fields = ('user', 'created_at', 'username')

      
class CommentSerializer(serializers.ModelSerializer):
    profile_path = serializers.IntegerField(read_only=True, source='user.profile_path')
    username = serializers.CharField(read_only=True, source='user.username')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','article', 'profile_path', 'username')


class ArticleSerializer(serializers.ModelSerializer):
    profile_path = serializers.IntegerField(read_only=True, source='user.profile_path')
    comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_article_users',)