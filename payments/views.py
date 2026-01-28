from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Subscription


@login_required
def upgrade(request):
    subscription, _ = Subscription.objects.get_or_create(owner=request.user)
    is_premium = subscription.is_premium

    context = {
        "is_premium": is_premium,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, "payments/upgrade.html", context)


@login_required
def start_checkout(request):
    """
    Placeholder for Stripe Checkout.
    Commit 11 will implement Stripe session creation.
    """
    subscription, _ = Subscription.objects.get_or_create(owner=request.user)

    if subscription.is_premium:
        messages.info(request, "You are already on Premium.")
        return redirect("payments:upgrade")

    messages.error(request, "Stripe is not configured yet. This will be added in the next milestone.")
    return redirect("payments:upgrade")


@login_required
def success(request):
    return render(request, "payments/success.html")


@login_required
def cancel(request):
    return render(request, "payments/cancel.html")
