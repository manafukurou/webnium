from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from job.models import Job
from .forms import JobForm
import datetime


# Create your views here.
def list(request):
    job_list = Job.objects.all()
    job_paginator = Paginator(job_list, 10)

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
    job_form = JobForm(request.GET or None, initial=initial_dict)

    params = {
        'message': "edit",
        'job_form': job_form
    }
    return render(request, 'new_job.html', params)


def update(request, job_id):
    job_job = Job.objects.all().filter(id=job_id).first()
    initial_dict = dict(
        job_name=job_job.job_name,
        job_id=job_job.id,
    )
    job_form = JobForm(request.GET or None, initial=initial_dict)

    params = {
        'message': "edit",
        'job_form': job_form
    }
    return render(request, 'new_job.html', params)


def edit(request, job_id):
    job_job = Job.objects.all().filter(id=job_id).first()

    context = {
        'job_id': job_id,
        'job_job': job_job
    }
    return render(request, 'edit.html', context)


def delete(request, job_id):
    # job_job = Job.objects.all().filter(id=job_id).first()
    Job.objects.filter(id=job_id).delete()
    context = {
        'result': True
    }
    return render(request, 'delete.html', context)


def confirm(request, *args, **kwargs):
    job_name = request.POST['job_name']
    job_id = request.POST['job_id']
    if job_id is None or job_id == "":
        job_object = Job(
            job_name=job_name,
            pub_date=datetime.datetime.now()
        )
        job_object.save()
        result = "created"
    else:
        job_object = Job.objects.all().filter(id=job_id).first()
        job_object.job_name = job_name
        job_object.save()
        result = "updated"

    context = {
        'job_name': job_name,
        'result': result
    }
    return render(request, 'confirm.html', context)
