from django.conf import settings
from django.db import models


class Subscription(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="subscription",
    )
    is_premium = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=255, blank=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        status = "Premium" if self.is_premium else "Free"
        return f"{self.owner.username} - {status}"
