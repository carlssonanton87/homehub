from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "role_type", "phone", "email", "notes")

    def clean(self):
        cleaned = super().clean()
        phone = (cleaned.get("phone") or "").strip()
        email = (cleaned.get("email") or "").strip()

        if not phone and not email:
            raise forms.ValidationError(
                "Please provide at least a phone number or an email address."
            )
        return cleaned
