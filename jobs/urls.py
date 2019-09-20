from django.urls import path
from . import views

app_name = 'jobs' # url name space 를 만든 것 
# ==> url 들이 jobs 에 있는 ___ 페이지가 된다
urlpatterns = [
    path('', views.index, name='index'),
    path('past_job/', views.past_job, name='past_job'),
]
