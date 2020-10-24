from django.http import HttpResponse

# Create your views here.
def hellofunction(request):

    return HttpResponse('<h1>hello world</h1>')