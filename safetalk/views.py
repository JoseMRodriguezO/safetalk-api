from django.shortcuts import render
from django.http import JsonResponse
from .models import Activity, Resource


def index(request):
    return JsonResponse({"message": "Hello from jose"})
