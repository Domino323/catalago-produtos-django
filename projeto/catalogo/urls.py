from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.lista_produtos, name='lista'),
    path('<int:id>/', views.detalhe_produto, name='detalhe'),
]
