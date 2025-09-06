from rest_framework import viewsets
from .models import Class, ClassBooking
from .serializers import ClassSerializer, ClassBookingSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassBookingViewSet(viewsets.ModelViewSet):
    queryset = ClassBooking.objects.all()
    serializer_class = ClassBookingSerializer
