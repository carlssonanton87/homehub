from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExpenseForm
from .models import Expense


@login_required
def expense_list(request):
    # Month filter via querystring: ?month=YYYY-MM
    month_str = request.GET.get("month")
    today = date.today()

    if month_str:
        try:
            year, month = month_str.split("-")
            year = int(year)
            month = int(month)
            current_month = date(year, month, 1)
        except (ValueError, TypeError):
            current_month = date(today.year, today.month, 1)
    else:
        current_month = date(today.year, today.month, 1)

    expenses = Expense.objects.filter(
        owner=request.user,
        date__year=current_month.year,
        date__month=current_month.month,
    )

    total = expenses.aggregate(total=Sum("amount"))["total"] or 0

    context = {
        "expenses": expenses,
        "current_month": current_month,
        "total": total,
    }
    return render(request, "expenses/expense_list.html", context)


@login_required
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.owner = request.user
            expense.save()
            messages.success(request, "Expense added.")
            return redirect("expenses:list")
        messages.error(request, "Please correct the errors below.")
    else:
        form = ExpenseForm()

    return render(request, "expenses/expense_form.html", {"form": form, "mode": "create"})


@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk, owner=request.user)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense updated.")
            return redirect("expenses:list")
        messages.error(request, "Please correct the errors below.")
    else:
        form = ExpenseForm(instance=expense)

    return render(request, "expenses/expense_form.html", {"form": form, "mode": "update", "expense": expense})


@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, owner=request.user)

    if request.method == "POST":
        expense.delete()
        messages.success(request, "Expense deleted.")
        return redirect("expenses:list")

    return render(request, "expenses/expense_confirm_delete.html", {"expense": expense})
