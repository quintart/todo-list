from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api_overview'),
    path('task_list/', views.tasklist, name='task_list'),
    path('task_detail/<str:pk>', views.taskdetail, name='task_detail'),    
    path('task_create/', views.taskcreate, name='task_create'),    
    path('task_update/<str:pk>', views.taskupdate, name='task_update'),    
    path('task_delete/<str:pk>', views.taskdelete, name='task_delete'),    
]