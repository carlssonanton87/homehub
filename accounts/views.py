from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome to Homehub! Your account has been created.")
            return redirect("core:home")
        messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})
