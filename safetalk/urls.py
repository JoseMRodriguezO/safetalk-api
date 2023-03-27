from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='index'),
    path('resources/', views.resource_list, name='resource_list')

]
