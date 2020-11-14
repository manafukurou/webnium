from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('detail/', views.detail, name='detail'),
    path('new_job/', views.new_job, name='new_job'),
    path('confirm/', views.confirm, name='confirm'),
    path('edit/<int:job_id>', views.edit, name='edit')
]