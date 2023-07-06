from django.db import models

# Create your models here.

class Task(models.Model):
    user = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # assigned_to = models.ForeignKey(name, on_delete=models.CASCADE, related_name='assigned_tasks')
    # created_by = models.ForeignKey(name, on_delete=models.CASCADE, related_name='created_tasks')
    deadline = models.DateTimeField()
    status = models.CharField(max_length=50, default='In Progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
