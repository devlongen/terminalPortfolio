
from django.urls import path
from app_python import views

urlpatterns = [
    path('', views.portfolio, name='portfolio_home'), # Define a URL raiz como a view 'portfolio' e atribui o nome 'portfolio_home'
    path('post',views.help_python,name='help_python') # Define a URL '/post' para a view 'help_python' e atribui o nome 'help_python'
]