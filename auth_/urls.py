from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register_request, name='auth_reg'),
    path('login/', views.login_request, name='auth_login'),
    path('logout/', views.logout_request, name='auth_logout'),
]