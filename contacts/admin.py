from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "role_type", "owner", "updated_at")
    list_filter = ("role_type", "owner")
    search_fields = ("name", "phone", "email", "notes")
