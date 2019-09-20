from django.shortcuts import render, redirect, get_object_or_404
from .models import Job

# random 과 비슷한 역할 
from faker import Faker

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')


def past_job(request):
    # 만약 POST 요청으로 들어오면 사용자 데이터 받아서 article 생성
    fake = Faker('ko_kr')
    name = request.POST.get('name')
    if Job.objects.filter(name=name):
        job = Job.objects.get(name=name)
    else: 
        job = Job()
        job.name = name
        job.past_job = fake.job()
        job.save()
    context = {'job':job}
    return render(request, 'jobs/past_job.html', context)
