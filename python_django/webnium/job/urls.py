from django.urls import path
from . import views

urlpatterns = [
    path('world/', views.hellofunction, name='hello')
]