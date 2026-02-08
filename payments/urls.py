from django.urls import path
from . import views


app_name = "payments"

urlpatterns = [
    path("upgrade/", views.upgrade, name="upgrade"),
    path("checkout/", views.create_checkout_session, name="checkout"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
    path("webhook/", views.stripe_webhook, name="webhook"),
]
