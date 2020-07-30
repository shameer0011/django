from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
    path('address/', views.addresstest,name='blog-address'),
]