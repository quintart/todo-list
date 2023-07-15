from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task_list/',
        'Detail View': '/task_detail/<str:pk>',
        'Create': '/task_create/',
        'Update': '/task_update/<str:pk>',
        'Delete': '/task_delete/<str:pk>'
    }

    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response('data no valid')

@api_view(['POST'])
def taskupdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response('data no valid')

@api_view(['DELETE'])
def taskdelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('deleted')