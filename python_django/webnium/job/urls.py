from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('detail/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('confirm/', views.confirm, name='confirm')
]