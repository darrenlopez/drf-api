import uuid
from django.db import models

class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan_name = models.TextField()
    price = models.IntegerField()

class Gifts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan_name = models.TextField()
    price = models.IntegerField()
    recipient_email = models.EmailField()

class Customers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address_1 = models.TextField()
    address_2 = models.TextField()
    city = models.CharField(max_length=30)
    state = models.TextField(max_length=2)
    postal_code = models.TextField()
    subscription = models.OneToOneField( Subscription, on_delete=models.CASCADE)
    gifts = models.ForeignKey(Gifts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
        return self.title