from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, HealthMetricsViewSet, ExerciseLogViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'health-metrics', HealthMetricsViewSet)
router.register(r'exercise-logs', ExerciseLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
