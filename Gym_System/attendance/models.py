from django.db import models
from users.models import Member

class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField(null=True, blank=True)

