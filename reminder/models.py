from django.db import models
from django.utils import timezone

class Reminder(models.Model):

    schedule_at = models.DateTimeField()
    message = models.TextField()
    source = models.CharField(max_length=10,choices=[("SMS","SMS"),("Email","Email")],default="SMS")
    status = models.CharField(
        max_length=12,
        choices=[("SENT","Sent"),("CANCELLED","Cancelled"),("PENDING","Pending")],
        default= "PENDING"
    )
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"Reminder {self.id} {self.source} {self.status} {self.schedule_at}"
    