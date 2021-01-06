from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.selector, name='selector'),
    path('add_note', views.add_note),
    path('search', views.search),
    path('change', views.change),
    path('edit', views.edit),
    path('about', views.about)
]
