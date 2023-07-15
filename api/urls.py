from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api_overview'),
    path('car_list/', views.carlist, name='car_list'),
    path('car_detail/<str:pk>', views.cardetail, name='car_detail'),    
    path('car_create/', views.carcreate, name='car_create'),    
    path('car_update/<str:pk>', views.carupdate, name='car_update'),    
    path('car_delete/<str:pk>', views.cardelete, name='car_delete'),    
]