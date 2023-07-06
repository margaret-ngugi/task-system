from django.db import models

# Create your models here.
class Notification(models.Model):
    # recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_received')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
