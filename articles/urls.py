from django.urls import path
from . import views

app_name = 'articles' # url name space 를 만든 것 
# ==> url 들이 articles 에 있는 ___ 페이지가 된다 (/articles/_______)
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
    # comment의 pk 를 variable routing 으로 받을 것 (댓글 데이터에도 다 pk 값 달려 있음)

    # 댓글 삭제하기(190924) url 추가
    # /articles/3/comments/2/delete 형식으로 만들 것 
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
