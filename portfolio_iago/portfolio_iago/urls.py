
from django.urls import path
from app_python import views

urlpatterns = [
    path('', views.portfolio, name='portfolio_home'),
    path('post',views.help_python,name='help_python'),
    path('post',views.jogo_da_velha,name='jogo_da_velha'),
    path('post',views.calculadora_imc,name='calculadora_imc'),
    path('post',views.jogo_de_advinhar,name='jogo_de_advinhar'),
]