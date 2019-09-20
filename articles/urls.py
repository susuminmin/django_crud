from django.urls import path
from . import views

app_name = 'articles' # url name space 를 만든 것 
# ==> url 들이 articles 에 있는 ___ 페이지가 된다
urlpatterns = [
    # 입력 페이지 제공
    # path('new/', views.new, name='new'),
    # 데이터를 전달받아서 article 생성
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    # 댓글 예: /article/3/comments/
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
]
