from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Customers, Subscription, Gifts
from .serializers import CustomersSerializer, SubscriptionSerializer, GiftsSerializer


class CustomersViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = [AllowAny]

class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [AllowAny]

class GiftsViewSet(ModelViewSet):
    queryset = Gifts.objects.all()
    seriaoizer_class = GiftsSerializer
    permission_classes = [AllowAny]