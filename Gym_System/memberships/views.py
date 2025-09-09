from rest_framework import viewsets
from .models import MembershipPlan, Payment
from .serializers import MembershipPlanSerializer, PaymentSerializer

class MembershipPlanViewSet(viewsets.ModelViewSet):
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipPlanSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
