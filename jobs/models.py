from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20)
    past_job = models.TextField()

    # Job 의 데이터가 어떻게 정의되는지 알려주는 함수
    def __str__(self):
        return self.name