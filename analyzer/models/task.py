from django.db import models

# Create your models here.
class Task(models.Model):
    # class StatusChoices(models.IntegerChoices):
    #     Pending = 0, 'Pending'
    #     InProgress = 1, 'InProgress'
    #     Completed = 2, 'Completed'

    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'InProgress'),
        (2, 'Completed'),
    ]

    taskID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    dueDate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title