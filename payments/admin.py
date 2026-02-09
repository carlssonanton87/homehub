from django.contrib import admin
from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    # I show the important payment fields so I can quickly verify premium status in production.
    list_display = (
        "owner",
        "is_premium",
        "stripe_customer_id",
        "stripe_subscription_id",
        "updated_at",
    )
    list_filter = ("is_premium",)
    search_fields = (
        "owner__username",
        "owner__email",
        "stripe_customer_id",
        "stripe_subscription_id",
    )
