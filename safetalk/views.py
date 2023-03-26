from django.shortcuts import render
from django.http import JsonResponse
from .models import Activity, Resource


def my_view(request):
    my_string = "Hello World!"
    return JsonResponse(my_string, safe=False)


def activity_list(request):
    if request.method == 'GET':
        activities = Activity.objects.all()
        data = {'activities': list(activities.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        # code to create a new activity
        pass


def resource_list(request):
    if request.method == 'GET':
        resources = Resource.objects.all()
        data = {'resources': list(resources.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        # code to create a new resource
        pass
