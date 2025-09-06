from django.db import models
from users.models import Trainer, Member

class Class(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    description = models.TextField()
    schedule_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    capacity = models.IntegerField()

class ClassBooking(models.Model):
    STATUS_CHOICES = [('Booked', 'Booked'), ('Cancelled', 'Cancelled'), ('Attended', 'Attended')]
    gym_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Booked")
