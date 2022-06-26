from django.urls import path, include, re_path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.UserViewSet.as_view(), name='users_api'),
    path('users/full/<int:page>/', views.UserFullViewSet.as_view(), name='users_full_api'),
]