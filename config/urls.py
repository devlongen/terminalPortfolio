
from django.urls import path
from app_python import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'), 
    path('help/', views.isDirectHelpPage, name='help_python'), 
    path('projects/', views.isDirectProjectsPage, name='projects')
]