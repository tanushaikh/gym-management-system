from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, ClassBookingViewSet

router = DefaultRouter()
router.register(r'classes', ClassViewSet)
router.register(r'bookings', ClassBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
