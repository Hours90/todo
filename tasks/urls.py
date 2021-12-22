from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]