from django.urls import path
from .views import filmovi_lista

app_name = 'filmovi'

urlpatterns = [
    path('', filmovi_lista, name='filmovi_lista'),
]