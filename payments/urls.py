from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path("", views.upgrade, name="upgrade"),
    path("checkout/", views.start_checkout, name="checkout"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
]
