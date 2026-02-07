import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Subscription


@login_required
def upgrade(request):
    # I keep the upgrade page as a normal GET page and handle Stripe in a separate POST view.
    subscription = getattr(request.user, "subscription", None)
    is_premium = bool(subscription and subscription.is_premium)

    return render(
        request,
        "payments/upgrade.html",
        {
            "is_premium": is_premium,
        },
    )


@login_required
def create_checkout_session(request):
    # I only allow POST here so the user can't trigger payments by accidentally opening a link.
    if request.method != "POST":
        return redirect("payments:upgrade")

    stripe.api_key = settings.STRIPE_SECRET_KEY

    # I create absolute URLs for Stripe redirects so it works in production on Heroku.
    success_url = request.build_absolute_uri(reverse("payments:success"))
    cancel_url = request.build_absolute_uri(reverse("payments:cancel"))

    try:
        session = stripe.checkout.Session.create(
            mode="subscription",
            payment_method_types=["card"],
            customer_email=request.user.email or None,
            line_items=[
                {
                    "price": settings.STRIPE_PRICE_ID,  # e.g. price_12345
                    "quantity": 1,
                }
            ],
            success_url=success_url + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=cancel_url,
            metadata={
                "user_id": str(request.user.id),
            },
        )
        return redirect(session.url)

    except Exception:
        # I send the user back with a friendly message if Stripe fails for any reason.
        from django.contrib import messages
        messages.error(request, "Something went wrong. Please try again in a moment.")
        return redirect("payments:upgrade")


@login_required
def success(request):
    # Minimal success page. (Your webhook should set is_premium=True.)
    return render(request, "payments/success.html")


@login_required
def cancel(request):
    return render(request, "payments/cancel.html")
