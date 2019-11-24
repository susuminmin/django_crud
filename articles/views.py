from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment


def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


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
        # 방금 만든 article 의 상세보기 페이지로 보냄
        return redirect('articles:detail', article.pk)
    # GET 요청이면 생성 form 보여줄 것
    else:
        return render(request, 'articles/create.html')


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    # 현재 article 에 달린 모든 댓글 다 꺼내기
    # comments = article.comment_set.all()
    # related_names='comments' 이므로
    comments = article.comments.all()

    # 저장해서 context에 넣어서 넘김
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


# 사용자로부터 받은 article_pk 값에 해당하는 article 을 삭제한다.
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 보안문제: 들어온 요청이 POST 일 때만 삭제해
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')  # 글 목록으로 re-direct
    else:
        return redirect('articles:detail', article_pk)  # 삭제 불가능
        # 삭제되지 않은 채 삭제버튼이 존재하는 상세보기 페이지를 그대로 보여줌


# /articles/5/update/ 로 들어옴
def update(request, article_pk):
    # 어떤 메소드가 들어왔는지 안쪽에서 확인
    article = get_object_or_404(Article, pk=article_pk)
    # POST : 실제 Update 로직 수행
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 수정 후 save()
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)

    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)


# 댓글 다는 함수 / variable routing 있으면 request 말고 다른 변수 받는다.
def comment_create(request, article_pk):

    # article_pk 에 해당하는 article 에 새로운 comment 생성
    # 생성한 다음 article detail page 로 redirect
    article = get_object_or_404(Article, pk=article_pk)
    # 몇번 아티클에 달아줄지 정하는 것

    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment()
        comment.content = content
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)


# 첫번째 인자는 무조건 request, 다음 인자는 url에서 var routing으로 넘어오는 인자 순서대로 받는다.
def comment_delete(request, article_pk, comment_pk):
    # post 요청으로 들어왔다면 그 때만 댓삭!
    if request.method == 'POST':
        # comment_pk 해당 댓글 삭제
        # 어떤 모델에서 가져올지 받고, primary key 받아서 꺼내준다. (없으면 404 넘긴다.)
        comment = get_object_or_404(Comment, pk=comment_pk)
        # comment가 있으면 삭제
        comment.delete()

    # 댓삭 후 detail 페이지로 이동시킴
    # 어떤 페이지로 넘길지에 대한 article pk 가 필요하다. (마침 위에서 var routing으로 받았으므로 _ )
    return redirect('articles:detail', article_pk)
