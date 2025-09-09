from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutPlanViewSet, WorkoutExerciseViewSet, DietPlanViewSet, DietMealViewSet

router = DefaultRouter()
router.register(r'workout-plans', WorkoutPlanViewSet)
router.register(r'workout-exercises', WorkoutExerciseViewSet)
router.register(r'diet-plans', DietPlanViewSet)
router.register(r'diet-meals', DietMealViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
