from analyzer.helper.taskFileHandler import TaskFileHandler
from analyzer.models.task import Task

class TaskRepository:

    @staticmethod
    def get_task(task_id):
        try:
            return Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return None

    @staticmethod
    def add_task(title, description, due_date, status=0):
        try:
            task = Task(title=title, description=description, dueDate=due_date, status=status)
            task.save()
            TaskFileHandler.save_tasks(Task.objects.all())
            return task
        except Exception:
            return None

    @staticmethod
    def update_task(task_id, **kwargs):
        try:
            task = Task.objects.get(pk=task_id)
            for key, value in kwargs.items():
                setattr(task, key, value)
            task.save()
            TaskFileHandler.save_tasks(Task.objects.all())
            return task
        except Task.DoesNotExist:
            return None

    @staticmethod
    def delete_task(task_id):
        try:
            task = Task.objects.get(pk=task_id)
            task.delete()
            TaskFileHandler.save_tasks(Task.objects.all())
            return True
        except Task.DoesNotExist:
            return None

    @staticmethod
    def list_tasks():
        return Task.objects.all()