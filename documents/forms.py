from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ("title", "description")

    def clean_title(self):
        title = (self.cleaned_data.get("title") or "").strip()
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title
