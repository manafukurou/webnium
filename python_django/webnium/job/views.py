from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from job.models import Job
from .forms import JobForm
import datetime

# Create your views here.
def list(request):

    job_list = Job.objects.all()
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

    params = {
        'message': message,
    }
    return render(request, 'detail.html', params)

def new_job(request):

    initial_dict = dict(
        job_name=""
    )
    job_form = JobForm(request.GET or None,initial=initial_dict)

    params = {
        'message': "edit",
        'job_form': job_form
    }
    return render(request, 'new_job.html', params)


def edit(request,job_id):
    context = {
        'job_id': job_id
    }
    return render(request, 'edit.html', context)

    return "";

def confirm( request, *args, **kwargs):
    jobObject = Job(job_name=request.POST['job_name'],pub_date=datetime.datetime.now())
    jobObject.save()
    context = {
        'job_name': request.POST['job_name']
    }
    return render(request, 'confirm.html', context)