from rest_framework import viewsets
from .models import WorkoutPlan, WorkoutExercise, DietPlan, DietMeal
from .serializers import WorkoutPlanSerializer, WorkoutExerciseSerializer, DietPlanSerializer, DietMealSerializer

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer

class DietPlanViewSet(viewsets.ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

class DietMealViewSet(viewsets.ModelViewSet):
    queryset = DietMeal.objects.all()
    serializer_class = DietMealSerializer
