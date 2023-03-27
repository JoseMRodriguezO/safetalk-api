
from .models import Activity, Resource
from django.http import JsonResponse


def my_view(request):
    if request.method == 'GET':
        activities = Activity.objects.all()
        data = {'activities': list(activities.values())}
        response = JsonResponse(data)
        print(response.content)
        return response


def resource_list(request):
    resources = Resource.objects.all()
    data = {'resources': list(resources.values())}
    response = JsonResponse(data)
    print(response.content)
    print("Resource list view called")

    return response
