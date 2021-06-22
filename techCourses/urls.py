from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.mainPage, name='mainPage'),
    path('about/', views.about, name='about'),
    path('listcourses/', views.list, name='listCourses'),
    path('visionmision/', views.visionmision, name='misionVision'),
    path('contact/', views.contact, name='contactInfo'),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('course/', views.course, name='course'),
]
