import csv
import os
from django.conf import settings
from analyzer.models.task import Task

class TaskCSVHandler:
    FILE_PATH = os.path.join(settings.BASE_DIR, "tasks_export.csv")

    @staticmethod
    def export_tasks():
        tasks = Task.objects.all()
        with open(TaskCSVHandler.FILE_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(["ID", "Title", "Description", "Status", "DueDate", "CreatedAt", "UpdatedAt"])
            # Write rows
            for t in tasks:
                writer.writerow([
                    t.taskID,
                    t.title,
                    t.description,
                    t.get_status_display(),
                    t.dueDate,
                    t.created_at,
                    t.updated_at
                ])
        return TaskCSVHandler.FILE_PATH