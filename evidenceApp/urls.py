from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('close/', views.close, name='close'),
    path('profile/', views.profile, name='profile'),
    path('createCad/', views.createCad, name='createCad'),
    path('editCad/', views.editCad, name='editCad'),
    path('deleteCad/', views.deleteCad, name='deleteCad'),
    path('updateCad/', views.updateCad, name='updateCad'),
]
