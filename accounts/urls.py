from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('create_account/', views.register_user, name='register_user'),
    path('logout/', views.Logout),
    path('log_user/', views.log_user_in)
]
