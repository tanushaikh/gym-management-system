from rest_framework import serializers
from .models import WorkoutPlan, WorkoutExercise, DietPlan, DietMeal

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = '__all__'

class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True, read_only=True, source='workoutexercise_set')

    class Meta:
        model = WorkoutPlan
        fields = '__all__'

class DietMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietMeal
        fields = '__all__'

class DietPlanSerializer(serializers.ModelSerializer):
    meals = DietMealSerializer(many=True, read_only=True, source='dietmeal_set')

    class Meta:
        model = DietPlan
        fields = '__all__'
