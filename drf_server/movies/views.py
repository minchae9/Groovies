from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from movies.serializers import MovieListSerializer, MovieSerializer, CommentSerializer, RatingSerializer, ActorSerializer, DirectorSerializer, SimilarSerializer
from .models import Comment, Rating, Movie, Similar, Cart
import random


# 전체 댓글      
@api_view(['GET'])
def comment_list(request, movie_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Comment, movie=movie_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

# 댓글 조회, 수정, 삭제    
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, movie=movie_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    if request.user != comment.user:
        return Response({'error': '권한이 없습니다.'})
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

# 댓글 생성    
@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 한마디 좋아요
@api_view(['POST'])
def comment_like(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.like_comment_users.filter(pk=request.user.pk).exists():
        comment.like_comment_users.remove(request.user)
        liked = False
    else:
        comment.like_comment_users.add(request.user)
        liked = True
    like_status = {
        'liked': liked,
        'count': comment.like_comment_users.count(),
    }
    return Response(like_status)

# 영화 목록
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 영화 세부정보
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



# 별점    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def rating(request, movie_pk):
    
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        rating = get_object_or_404(Rating, movie=movie_pk, user=request.user)
        if request.method == 'GET':
            serializer = RatingSerializer(rating)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = RatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        elif request.method == 'DELETE':
            rating.delete()
            data = {
                'delete': f'영화 {movie_pk}에 대한 평점이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)


# 검색
@api_view(['GET'])
def search(request, keyword):
    # keyword = request.GET.get('searchKeyword')
    if keyword:
        search_list1 = Movie.objects.filter(title__contains=keyword)
        search_list2 = Movie.objects.filter(original_title__contains=keyword)
        search_list3 = Movie.objects.filter(genres__contains=keyword)
        search_list = search_list1 | search_list2 | search_list3
        serializer = MovieListSerializer(search_list, many=True)
        return Response(serializer.data)
    return Response({'error': 'No keyword.'})


# 추천
@api_view(['GET'])
def recommendation(request):
    movie_list = Rating.objects.filter(user=request.user.pk, rate__gte=4)
    result = Similar.objects.none()  # 빈 쿼리셋
    if movie_list and request.user.is_authenticated:
        for movie in movie_list:
            # movies_similar 테이블에서 original_movie로 필터링 후
            similar_movies = Similar.objects.filter(original_movie=movie.movie_id)
            # 목록에 추가
            result = result | similar_movies   
    else:
        result = Movie.objects.all()
    random_picked = random.sample(list(result), 15)
    carousel_picked = random.sample(list(result), 5)
    serializer1 = MovieListSerializer(random_picked, many=True)
    serializer2 = MovieSerializer(carousel_picked, many=True)
    return Response({"recommendations": serializer1.data, "carousel_items": serializer2.data})


@api_view(['POST'])
def add_cart(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if Cart.objects.filter(movie=movie, user=request.user).exists():
            Cart.objects.filter(movie=movie, user=request.user).delete()
            return Response({'message': '찜한 목록에서 삭제되었습니다.'})
        else:
            cart = Cart(movie=movie, user=request.user)
            cart.save()
            return Response({'message': '찜한 목록에 추가되었습니다.'})
    return Response({'error': '로그인 후 이용 가능한 기능입니다.'})
    