from datetime import date, timedelta
from django.contrib.auth import get_user_model

User = get_user_model()

# 1) Create or get demo user
username = "demo"
email = "demo@homehub.local"
password = "DemoPass123!"  # change if you want

user, created = User.objects.get_or_create(username=username, defaults={"email": email})
if created:
    user.set_password(password)
    user.save()
    print("✅ Created user:", username)
else:
    print("ℹ️ User already exists:", username)

# 2) Make user Premium
from payments.models import Subscription

sub, _ = Subscription.objects.get_or_create(owner=user)
sub.is_premium = True
sub.save()
print("✅ Set Premium = True")

# 3) Create sample documents
from documents.models import Document

docs = [
    ("Insurance policy", "Home insurance details, policy number, coverage notes."),
    ("Dishwasher warranty", "Warranty expires 2027-11-01. Serial number: ABC123."),
    ("Wi-Fi setup", "Router model, admin login stored securely elsewhere, guest network info."),
    ("Paint colors", "Living room: NCS S 0502-Y. Bedroom: NCS S 2005-B20G."),
    ("Emergency checklist", "Shut-off valves, fuse box location, emergency contacts."),
    ("Renovation notes", "Kitchen remodel timeline, contractor notes, receipts location."),
]
for title, description in docs:
    Document.objects.get_or_create(owner=user, title=title, defaults={"description": description})
print("✅ Documents ensured:", len(docs))

# 4) Create sample contacts
from contacts.models import Contact

contacts = [
    {"name": "Anna Electric", "role_type": "electrician", "phone": "070-111 22 33", "email": "anna@electric.example", "notes": "Fast response, used 2024."},
    {"name": "Plumbing Pro", "role_type": "plumber", "phone": "070-222 33 44", "email": "", "notes": "Handles leaks and drains."},
    {"name": "Home Insurance Support", "role_type": "insurance", "phone": "0771-123 456", "email": "support@insurance.example", "notes": "Policy questions."},
]

for data in contacts:
    # If your Contact model enforces at least phone OR email, this satisfies it.
    Contact.objects.get_or_create(
        owner=user,
        name=data["name"],
        defaults={
            "role_type": data["role_type"],
            "phone": data["phone"],
            "email": data["email"],
            "notes": data["notes"],
        },
    )
print("✅ Contacts ensured:", len(contacts))

# 5) Create sample expenses (current month-ish)
from expenses.models import Expense

today = date.today()
expenses = [
    {"date": today - timedelta(days=2), "category": "utilities", "amount": 349.00, "note": "Electricity"},
    {"date": today - timedelta(days=5), "category": "groceries", "amount": 892.50, "note": "Weekly groceries"},
    {"date": today - timedelta(days=9), "category": "repairs", "amount": 1200.00, "note": "Sink repair"},
    {"date": today - timedelta(days=12), "category": "internet", "amount": 399.00, "note": "Broadband"},
    {"date": today - timedelta(days=15), "category": "household", "amount": 149.90, "note": "Cleaning supplies"},
]

for e in expenses:
    Expense.objects.get_or_create(
        owner=user,
        date=e["date"],
        category=e["category"],
        amount=e["amount"],
        defaults={"note": e["note"]},
    )
print("✅ Expenses ensured:", len(expenses))

print("\n🎉 Done!")
print("Login:", username)
print("Password:", password)
