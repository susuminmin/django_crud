from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    # 1. Article model class 를 명시해준다.(1:N 관계를 만들 때 반드시 1이 먼저 선언)
    # 2. on_delete=models.CASCADE : Article이 삭제되면 Comment 도 함께 삭제되도록
    # primary key 값만 남음 article_id 와 article(Model에 정의한 대로)을 같은 작업으로 받아들임
    # 3. related_name : Article instance 가 comment를 역참조하는 이름 정의
    content = models.CharField(max_length=200)
    # 데이터가 새로 추가됐을 때만 현재 시간 자동으로 생성됨
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)  # 추가나 수정이나 언제든지 시간 기록

    # 클래스 안에 또 클래스 (Django meta option 검색해보기)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content
