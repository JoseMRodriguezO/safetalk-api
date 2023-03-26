from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Activity, Resource


@csrf_exempt
def activity_list(request):
    if request.method == 'GET':
        activities = Activity.objects.all()
        data = {'activities': list(activities.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        # code to create a new activity
        pass


@csrf_exempt
def resource_list(request):
    if request.method == 'GET':
        resources = Resource.objects.all()
        data = {'resources': list(resources.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        # code to create a new resource
        pass
