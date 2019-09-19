from django.urls import path
from . import views


urlpatterns= [
    # 입력 페이지 제공
    path('new/', views.new),
    # 데이터를 전달받아서 article 생성
    path('create/', views.create),
    path('', views.index),
    path('<int:article_pk>/', views.detail),
    path('<int:article_pk>/delete/', views.delete),
]