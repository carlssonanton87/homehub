from django.contrib import messages
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Contact


@login_required
def contact_list(request):
    q = (request.GET.get("q") or "").strip()

    contacts = Contact.objects.filter(owner=request.user)

    if q:
        contacts = contacts.filter(
            Q(name__icontains=q)
            | Q(phone__icontains=q)
            | Q(email__icontains=q)
            | Q(notes__icontains=q)
        )

    return render(
        request,
        "contacts/contact_list.html",
        {"contacts": contacts, "q": q},
    )



@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    return render(request, "contacts/contact_detail.html", {"contact": contact})


@login_required
def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, "Contact created.")
            return redirect("contacts:detail", pk=contact.pk)
        messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, "contacts/contact_form.html", {"form": form, "mode": "create"})


@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated.")
            return redirect("contacts:detail", pk=contact.pk)
        messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm(instance=contact)

    return render(request, "contacts/contact_form.html", {"form": form, "mode": "update", "contact": contact})


@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)

    if request.method == "POST":
        contact.delete()
        messages.success(request, "Contact deleted.")
        return redirect("contacts:list")

    return render(request, "contacts/contact_confirm_delete.html", {"contact": contact})
