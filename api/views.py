from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CarSerializer
from .models import Car

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/car_list/',
        'Detail View': '/car_detail/<str:pk>',
        'Create': '/car_create/',
        'Update': '/car_update/<str:pk>',
        'Delete': '/car_delete/<str:pk>'
    }

    return Response(api_urls)

@api_view(['GET'])
def carlist(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def cardetail(request, pk):
    cars = Car.objects.get(id=pk)
    serializer = CarSerializer(cars, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def carcreate(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response('data no valid')

@api_view(['POST'])
def carupdate(request, pk):
    car = Car.objects.get(id=pk)
    serializer = CarSerializer(instance=car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response('data no valid')

@api_view(['DELETE'])
def cardelete(request, pk):
    car = Car.objects.get(id=pk)
    Car.delete()
    return Response('deleted')