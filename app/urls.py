
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('all_members',views.all_members,name='all_members'),
    path('add_members',views.add_members,name='add_members'),
    path('filter_members',views.filter_members,name='filter_members'),
]
