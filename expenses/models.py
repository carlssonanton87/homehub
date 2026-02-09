from django.conf import settings
from django.db import models


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("groceries", "Groceries"),
        ("utilities", "Utilities"),
        ("repairs", "Repairs"),
        ("rent", "Rent / Fee"),
        ("insurance", "Insurance"),
        ("other", "Other"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="expenses",
    )
    date = models.DateField()
    category = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default="other"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-updated_at"]

    def __str__(self) -> str:
        return f"{self.date} - {self.amount} ({self.get_category_display()})"
