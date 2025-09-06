from django.db import models
from users.models import Member, Trainer

class WorkoutPlan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    plan_name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class WorkoutExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time_seconds = models.IntegerField()

class DietPlan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    plan_name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class DietMeal(models.Model):
    MEAL_CHOICES = [('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')]
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    food_items = models.TextField()
    calories = models.IntegerField()
