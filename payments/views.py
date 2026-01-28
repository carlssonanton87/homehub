import stripe

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Subscription


def _stripe_is_configured() -> bool:
    return bool(settings.STRIPE_SECRET_KEY and settings.STRIPE_PRICE_ID)


@login_required
def upgrade(request):
    subscription, _ = Subscription.objects.get_or_create(owner=request.user)
    is_premium = subscription.is_premium

    context = {
        "is_premium": is_premium,
    }
    return render(request, "payments/upgrade.html", context)


@login_required
def start_checkout(request):
    # Security: Checkout should be POST only
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method.")

    subscription, _ = Subscription.objects.get_or_create(owner=request.user)

    if subscription.is_premium:
        messages.info(request, "You are already on Premium.")
        return redirect("payments:upgrade")

    if not _stripe_is_configured():
        messages.error(request, "Stripe is not configured. Please set STRIPE keys in environment variables.")
        return redirect("payments:upgrade")

    stripe.api_key = settings.STRIPE_SECRET_KEY

    success_url = request.build_absolute_uri(reverse("payments:success")) + "?session_id={CHECKOUT_SESSION_ID}"
    cancel_url = request.build_absolute_uri(reverse("payments:cancel"))

    try:
        session = stripe.checkout.Session.create(
            mode="payment",
            line_items=[{"price": settings.STRIPE_PRICE_ID, "quantity": 1}],
            success_url=success_url,
            cancel_url=cancel_url,
            client_reference_id=str(request.user.id),
            customer_email=request.user.email if request.user.email else None,
        )
    except Exception:
        messages.error(request, "Could not start Stripe checkout. Please try again.")
        return redirect("payments:upgrade")

    return redirect(session.url, permanent=False)


@login_required
def success(request):
    """
    Verifies the Stripe session and upgrades the user to Premium.
    """
    session_id = request.GET.get("session_id")
    if not session_id:
        messages.error(request, "Missing Stripe session information.")
        return redirect("payments:upgrade")

    if not _stripe_is_configured():
        messages.error(request, "Stripe is not configured.")
        return redirect("payments:upgrade")

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        session = stripe.checkout.Session.retrieve(session_id)
    except Exception:
        messages.error(request, "Unable to verify payment session.")
        return redirect("payments:upgrade")

    # Basic verification: ensure session is paid
    paid = getattr(session, "payment_status", None) == "paid"

    if not paid:
        messages.error(request, "Payment not completed.")
        return redirect("payments:upgrade")

    subscription, _ = Subscription.objects.get_or_create(owner=request.user)
    subscription.is_premium = True
    subscription.stripe_customer_id = session.get("customer") or ""
    subscription.save()

    messages.success(request, "Payment successful! You are now Premium.")
    return render(request, "payments/success.html")


@login_required
def cancel(request):
    messages.info(request, "Payment cancelled. You can try again anytime.")
    return render(request, "payments/cancel.html")
