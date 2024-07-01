from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members_list, name='members_list'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),  
]