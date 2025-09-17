import json
import os
import csv
from django.conf import settings
from analyzer.models.task import Task

class TaskFileHandler:
    FILE_PATH = os.path.join(settings.BASE_DIR, "tasks_backup.json")

    @staticmethod
    def save_tasks(tasks):
        try:
            with open(TaskFileHandler.FILE_PATH, "w") as f:
                json.dump([{
                    "id": t.taskID,
                    "title": t.title,
                    "description": t.description,
                    "status": t.status,
                    "dueDate": str(t.dueDate),
                } for t in tasks], f, indent=4)
        except Exception as e:
            print("Error writing to file:", e)

    @staticmethod
    def load_tasks():
        try:
            if not os.path.exists(TaskFileHandler.FILE_PATH):
                return []
            with open(TaskFileHandler.FILE_PATH, "r") as f:
                return json.load(f)
        except Exception as e:
            print("Error reading file:", e)
            return []