from rest_framework import viewsets
from .models import Device, HealthMetrics, ExerciseLog
from .serializers import DeviceSerializer, HealthMetricsSerializer, ExerciseLogSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class HealthMetricsViewSet(viewsets.ModelViewSet):
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer

class ExerciseLogViewSet(viewsets.ModelViewSet):
    queryset = ExerciseLog.objects.all()
    serializer_class = ExerciseLogSerializer
