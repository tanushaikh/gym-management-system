from rest_framework import serializers
from .models import Class, ClassBooking

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class ClassBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassBooking
        fields = '__all__'
