# This is api app's urls.py file

from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("customers", views.CustomersViewSet, "customers")
router.register("subscription", views.SubscriptionViewSet, "subscription")
router.register("gifts", views.GiftsViewSet, "gifts")

urlpatterns = router.urls