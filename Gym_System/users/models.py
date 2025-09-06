from django.db import models
from django.contrib.auth.models import AbstractUser

# Extend Django's User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Trainer', 'Trainer'),
        ('Member', 'Member'),
        ('Staff', 'Staff'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")
    is_active = models.BooleanField(default=True)

class Member(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Suspended', 'Suspended'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    emergency_contact = models.CharField(max_length=15)
    join_date = models.DateField(auto_now_add=True)
    membership = models.ForeignKey("memberships.MembershipPlan", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    phone = models.CharField(max_length=15, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    phone = models.CharField(max_length=15, unique=True)
