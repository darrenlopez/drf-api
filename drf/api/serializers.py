from . import models
from rest_framework import serializers


class CustomersSerializer(serializers.ModelSerializer):
  class Meta:
        fields = ('id', 'first_name', 'last_name', 'address_1', 'address_2', 'city', 'state', 'created_at', 'updated_at',)
        model = models.Customers

class SubscriptionSerializer(serializers.ModelSerializer):
  class Meta:
        fields = ('id', 'plan_name', 'price',)
        model = models.Subscription

class GiftsSerializer(serializers.ModelSerializer):
  class Meta:
        fields = ('id', 'plan_name', 'price', 'recipient_email',)
        model = models.Gifts
