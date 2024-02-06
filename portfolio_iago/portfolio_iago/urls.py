
from django.urls import path
from app_python import views

urlpatterns = [
    path('', views.portfolio, name='portfolio_home'),
    path('post',views.help_python,name='help_python')
]