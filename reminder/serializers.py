from datetime import datetime, date, time, timezone as dt_timezone
from django.utils import timezone
from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):

    schedule_date = serializers.DateField(write_only = True)
    schedule_time = serializers.TimeField(write_only = True)
    class Meta:
        model = Reminder
        fields = ["id", "schedule_date", "schedule_time", "source", "message", "schedule_at", "status", "time"]
        read_only_fields = ["id", "time", "status", "schedule_at"]

    def validate(self,data):
        d: date = data.pop("schedule_date")
        t: time = data.pop("schedule_time")
        schedule_at: datetime = datetime.combine(d, t).replace(tzinfo=dt_timezone.utc)
        if schedule_at < timezone.now():
            raise serializers.ValidationError("Cannot schedule reminder in the past")
        data["schedule_at"] = schedule_at
        return data
    