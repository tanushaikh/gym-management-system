from django.db import models
from users.models import Member

class Device(models.Model):
    STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    registered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")

class HealthMetrics(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    heart_rate = models.IntegerField()
    calories_burned = models.DecimalField(max_digits=10, decimal_places=2)
    steps = models.IntegerField()
    distance_km = models.DecimalField(max_digits=10, decimal_places=2)
    active_minutes = models.IntegerField()
    sleep_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class ExerciseLog(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    calories_burned = models.DecimalField(max_digits=10, decimal_places=2)
    avg_heart_rate = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
