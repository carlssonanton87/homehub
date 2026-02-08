import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
logger = logging.getLogger(__name__)


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

    except Exception as e:
        logger.exception("Stripe checkout failed: %s", e)
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

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")

    logger.info("Stripe webhook received. sig_header_present=%s payload_len=%s",
                bool(sig_header), len(payload))

    try:
        event = stripe.Webhook.construct_event(
            payload=payload,
            sig_header=sig_header,
            secret=settings.STRIPE_WEBHOOK_SECRET,
        )
    except ValueError as e:
        logger.exception("Stripe webhook invalid payload: %s", e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.exception("Stripe webhook signature verification failed: %s", e)
        return HttpResponse(status=400)

    logger.info("Stripe webhook verified. type=%s", event["type"])

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        user_id = session.get("metadata", {}).get("user_id")
        customer_id = session.get("customer")
        stripe_sub_id = session.get("subscription")

        logger.info("checkout.session.completed metadata.user_id=%s customer=%s subscription=%s",
                    user_id, customer_id, stripe_sub_id)

        if user_id:
            sub, created = Subscription.objects.get_or_create(owner_id=user_id)
            sub.is_premium = True
            sub.stripe_customer_id = customer_id or ""
            sub.stripe_subscription_id = stripe_sub_id or ""
            sub.save()
            logger.info("Subscription updated. user_id=%s created=%s is_premium=%s",
                        user_id, created, sub.is_premium)
        else:
            logger.warning("checkout.session.completed missing metadata.user_id")

    return HttpResponse(status=200)
