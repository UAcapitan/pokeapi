from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main_page'),
    path('account/', views.personal_account, name='account'),
    path('change/<int:page>/', views.change_pokemon, name='change_pokemon'),
    path('choice/<int:id>/', views.choice_pokemon, name='choice_pokemon'),
    path('delete/<int:id>/', views.delete_pokemon, name='delete_pokemon')
]
