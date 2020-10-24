from django.shortcuts import render

# Create your views here.
def list(request):
    message = "はろーなわーるど"
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