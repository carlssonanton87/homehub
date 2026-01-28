from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

from documents.models import Document
from contacts.models import Contact
from expenses.models import Expense

subscription = getattr(request.user, "subscription", None)
is_premium = bool(subscription and subscription.is_premium)


def home(request):
    if not request.user.is_authenticated:
        return render(request, "core/home_public.html")

    today = date.today()

    document_count = Document.objects.filter(owner=request.user).count()
    contact_count = Contact.objects.filter(owner=request.user).count()

    month_expenses = Expense.objects.filter(
        owner=request.user,
        date__year=today.year,
        date__month=today.month,
    )
    month_expense_count = month_expenses.count()
    month_expense_total = month_expenses.aggregate(total=Sum("amount"))["total"] or 0

    context = {
        "document_count": document_count,
        "contact_count": contact_count,
        "month_expense_count": month_expense_count,
        "month_expense_total": month_expense_total,
        "current_month": date(today.year, today.month, 1),
    }
    return render(request, "core/dashboard.html", context)
