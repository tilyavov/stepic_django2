from django.urls import path
from onetoone import views

urlpatterns = [
    path('', views.index, name='index'),
]

