from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MemberViewSet, TrainerViewSet, StaffViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'members', MemberViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
