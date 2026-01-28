from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DocumentForm
from .models import Document


@login_required
def document_list(request):
    documents = Document.objects.filter(owner=request.user)
    return render(request, "documents/document_list.html", {"documents": documents})


@login_required
def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk, owner=request.user)
    return render(request, "documents/document_detail.html", {"document": document})


FREE_DOCUMENT_LIMIT = 5


@login_required
def document_create(request):
    subscription = getattr(request.user, "subscription", None)
    is_premium = bool(subscription and subscription.is_premium)

    if not is_premium:
        current_count = Document.objects.filter(owner=request.user).count()
        if current_count >= FREE_DOCUMENT_LIMIT:
            messages.error(
                request,
                f"Free accounts can save up to {FREE_DOCUMENT_LIMIT} documents. Upgrade to Premium to add more."
            )
            return redirect("documents:list")

    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.owner = request.user
            document.save()
            messages.success(request, "Document created.")
            return redirect("documents:detail", pk=document.pk)
        messages.error(request, "Please correct the errors below.")
    else:
        form = DocumentForm()

    return render(request, "documents/document_form.html", {"form": form, "mode": "create"})

@login_required
def document_update(request, pk):
    document = get_object_or_404(Document, pk=pk, owner=request.user)

    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, "Document updated.")
            return redirect("documents:detail", pk=document.pk)
        messages.error(request, "Please correct the errors below.")
    else:
        form = DocumentForm(instance=document)

    return render(request, "documents/document_form.html", {"form": form, "mode": "update", "document": document})


@login_required
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk, owner=request.user)

    if request.method == "POST":
        document.delete()
        messages.success(request, "Document deleted.")
        return redirect("documents:list")

    return render(request, "documents/document_confirm_delete.html", {"document": document})
