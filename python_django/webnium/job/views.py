from django.shortcuts import render
from job.models import Job

# Create your views here.
def list(request):
    jobData = Job.objects.get(id=3)
    message = jobData.job_name
    print(message)
    params = {
        'message': message,
    }
    return render(request, 'list.html', params)

def detail(request):
    message = "ディティール"
    params = {
        'message': message,
    }
    return render(request, 'detail.html', params)