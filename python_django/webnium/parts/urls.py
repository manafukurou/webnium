from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='partslist'),
    path('new_parts/', views.new_parts, name='new_parts'),
    path('confirm/', views.confirm, name='parts_confirm'),
]