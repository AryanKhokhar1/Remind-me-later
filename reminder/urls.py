from django.urls import path
from .views import ReminderCreateAPIView

urlpatterns = [
    path("reminder/", ReminderCreateAPIView.as_view(), name="Reminder_Create")
]
