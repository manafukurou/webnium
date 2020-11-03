from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from job.models import Job

# Create your views here.
def list(request):

    job_list = Job.objects.order_by('id').reverse()
    job_paginator = Paginator(job_list, 5)

    page = request.GET.get('page', 1)

    try:
        jobs = job_paginator.page(page)
    except PageNotAnInteger:
        jobs = job_paginator.page(1)
    except EmptyPage:
        jobs = job_paginator.page(1)

    params = {
        'message': "message",
        'jobs': jobs
    }
    return render(request, 'list.html', params)

def detail(request):

    jobData = Job.objects.get(id=3)
    message = jobData.job_name
    params = {
        'message': message,
    }
    return render(request, 'detail.html', params)

