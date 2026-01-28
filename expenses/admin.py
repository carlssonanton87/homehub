from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("date", "category", "amount", "owner")
    list_filter = ("category", "owner")
    search_fields = ("note",)
