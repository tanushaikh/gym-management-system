from django.db import models
from users.models import Member

class MembershipPlan(models.Model):
    name = models.CharField(max_length=50)
    duration_months = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.duration_months} months)"

class Payment(models.Model):
    STATUS_CHOICES = [('Paid', 'Paid'), ('Pending', 'Pending'), ('Failed', 'Failed')]
    METHOD_CHOICES = [('Cash', 'Cash'), ('Card', 'Card'), ('UPI', 'UPI'), ('Bank Transfer', 'Bank Transfer')]

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

