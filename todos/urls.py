from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:id>/', views.todo_update, name='todo_update'),
    path('delete/<int:id>/', views.todo_delete, name='todo_delete'),
    path('complete/<int:id>/', views.todo_complete, name='todo_complete'),
]
