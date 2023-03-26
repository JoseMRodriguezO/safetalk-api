from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='index'),
    path('activities/', views.activity_list, name='activity-list'),
    path('resources/', views.resource_list, name='resource-list'),
]
