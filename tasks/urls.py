from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView),
    path('newtask/', views.newTask),
    path('edit/<int:id>', views.editTask),
    path('delete/<int:id>', views.deleteTask),
    path('yourname/<str:name>', views.yourname)
]
