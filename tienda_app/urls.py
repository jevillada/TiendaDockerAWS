from django.urls import path
from .views import comprar

urlpatterns = [
    path('comprar/', comprar, name='comprar'),
]