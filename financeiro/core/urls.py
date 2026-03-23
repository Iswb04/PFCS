from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.adicionar),
    path('zerar/', views.zerar),
]

