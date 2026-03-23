from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.adicionar),
    path('zerar/', views.zerar),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('exportar/', views.exportar, name="exportar")
]

