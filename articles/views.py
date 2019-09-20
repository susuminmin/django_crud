from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.

# 자원은 다 create 로만 나눠놓고 / 오로지 method 로만 구분하는 것
# GET /articles/create : 페이지만 받아가겠다
# def new(request):
#     return render(request, 'articles/new.html')


# POST /articles/create/
def create(request):
    # 만약 POST 요청으로 들어오면 사용자 데이터 받아서 article 생성
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article()
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)
    # 아니라면 html 페이지 rendering
    else:
        return render(request, 'articles/create.html')


def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
    # return render(request, 'detail', context)


# 사용자로부터 받은 article_pk 값에 해당하는 article 을 삭제한다.
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 보안문제: 들어온 요청이 POST 일 때만 삭제해
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article_pk)


# /articles/5/update/ 로 들어옴
def update(request, article_pk):
    # 어떤 메소드가 들어왔는지 안쪽에서 확인
    article = get_object_or_404(Article, pk=article_pk)
    # POST : 실제 Update 로직 수행
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 원래 있던 자리에 넣어주고 save하는 것
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)

    # GET : Update 를 하기 위한 Form 을 제공하는 페이지 렌더링
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)
