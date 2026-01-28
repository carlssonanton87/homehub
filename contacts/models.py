from django.conf import settings
from django.db import models


class Contact(models.Model):
    ROLE_CHOICES = [
        ("plumber", "Plumber"),
        ("electrician", "Electrician"),
        ("carpenter", "Carpenter"),
        ("painter", "Painter"),
        ("hvac", "HVAC"),
        ("other", "Other"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contacts",
    )
    name = models.CharField(max_length=120)
    role_type = models.CharField(max_length=30, choices=ROLE_CHOICES, default="other")
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
