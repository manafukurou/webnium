from django.shortcuts import render

# Create your views here.
def hellofunction(request):
    message = "はろーなわーるど"
    params = {
        'message': message,
    }
    return render(request, 'list.html', params)