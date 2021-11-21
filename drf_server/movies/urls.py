from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),   # 상세정보, 배우, 감독, 관련 영화
    path('<int:movie_pk>/comment/', views.comment_list),
    path('<int:movie_pk>/comment/create/', views.comment_create),
    path('<int:movie_pk>/comment/<int:comment_pk>/', views.comment_detail),
    path('<int:movie_pk>/comment/<int:comment_pk>/like/', views.comment_like),    
    path('<int:movie_pk>/rating/', views.rating),   # user의 rating
    path('<int:movie_pk>/cart/', views.add_cart, name='add_cart'),  # 찜하기
    path('search/<str:keyword>/', views.search, name='search'), # 검색 결과 반환
    path('recommendation/', views.recommendation, name='recommendation'),   # 추천영화 목록 반환
]
