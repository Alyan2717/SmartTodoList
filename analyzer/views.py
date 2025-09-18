from django.http import JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from django.views.decorators.csrf import csrf_exempt
import json

from analyzer.helper.taskCSVHandler import TaskCSVHandler
from analyzer.models.task import Task
from analyzer.repositories.taskRepository import TaskRepository
from analyzer.services.taskParser import TaskParser
from analyzer.services.weatherAPI import WeatherAPI


# Create your views here.
@csrf_exempt
def get_task(request):
    if request.method == "GET":
        task_id = request.GET.get("id")
        task = TaskRepository.get_task(task_id)
        if task:
            return JsonResponse({
                "id": task.taskID,
                "title": task.title,
                "description": task.description,
                "status": task.get_status_display(),
                "dueDate": task.dueDate,
            })
        return JsonResponse({"error": "Task not found"}, status=404)
    return None

@csrf_exempt
def add_task(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        task = TaskRepository.add_task(
            title=data.get("title"),
            description=data.get("description"),
            due_date=data.get("dueDate"),
            status=data.get("status", 0),
        )
        return JsonResponse({"message": "Task created", "id": task.taskID}, status=201)
    return None

@csrf_exempt
def update_task(request, task_id):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        task = TaskRepository.update_task(task_id, **data)
        if task:
            return JsonResponse({"message": "Task updated"})
        return JsonResponse({"error": "Task not found"}, status=404)
    return None

@csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        success = TaskRepository.delete_task(task_id)
        if success:
            return JsonResponse({"message": "Task deleted"})
        return JsonResponse({"error": "Task not found"}, status=404)
    return None

@csrf_exempt
def list_tasks(request):
    if request.method == "GET":
        tasks = TaskRepository.list_tasks()
        tasks_data = [
            {
                "id": t.taskID,
                "title": t.title,
                "description": t.description,
                "status": t.get_status_display(),
                "dueDate": t.dueDate,
            }
            for t in tasks
        ]
        return JsonResponse(tasks_data, safe=False)
    return None

@csrf_exempt
def weather_task(request):
    if request.method == "GET":
        weather = WeatherAPI.get_weather(request.GET.get("city"))
        return JsonResponse(weather, safe=False)
    return None

@csrf_exempt
def parse_task(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        text = data.get("text")
        parsed = TaskParser.parse(text)
        task = TaskRepository.add_task(
            title=parsed["title"],
            description=parsed["description"],
            due_date=parsed["dueDate"]
        )
        return JsonResponse({"message": "Task created from text", "id": task.taskID}, status=201)
    return None

@csrf_exempt
def export_tasks_csv(request):
    if request.method == "GET":
        file_path = TaskCSVHandler.export_tasks()
        return FileResponse(open(file_path, "rb"), as_attachment=True, filename="tasks_export.csv")
    return None

def task_page(request):
    tasks = TaskRepository.list_tasks()
    weather = WeatherAPI.get_weather("Berlin")
    return render(request, "tasks.html", {"tasks": tasks, "weather": weather})
