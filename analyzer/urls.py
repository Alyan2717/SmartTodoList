from django.urls import path
from analyzer import views

# URL Config
urlpatterns = [
    path('tasks/', views.list_tasks, name='list_tasks'),
    path('tasks/get/', views.get_task, name='get_task'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/update/<int:task_id>/', views.update_task, name='update_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('tasks/weather/', views.weather_task, name='weather_task'),
    path('tasks/parse/', views.parse_task, name='parse_task'),
    path('tasks/export/csv/', views.export_tasks_csv, name='export_tasks_csv'),
]