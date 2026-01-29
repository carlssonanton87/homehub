# Homehub

Homehub is a full-stack Django web application that helps users manage home-related information in one secure place.
Users can store documents, keep a directory of important contacts (e.g., electrician, plumber), track expenses by month,
and upgrade to Premium via Stripe to unlock additional capacity.

Live site: (production link after deployment)  
Repository: ( GitHub link)

---

## Table of Contents
- [Project Goals](#project-goals)
- [Target Audience](#target-audience)
- [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design Choices](#design-choices)
  - [Accessibility](#accessibility)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Data Model](#data-model)
- [Security](#security)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Project Goals
### Business Goals
- Provide a simple, intuitive platform to store home information securely.
- Encourage upgrades by offering a meaningful Premium benefit (increased document capacity).

### User Goals
- Store and find home documents quickly.
- Maintain a reliable list of home-related contacts.
- Track expenses by month and see totals.
- Upgrade to Premium with clear purchase feedback.

---

## Target Audience
- Home owners and renters who want one place for home information.
- Families managing recurring household costs and services.
- Users who want a lightweight “home admin” tool that is easy to use.

---

## User Experience

### User Stories
**Authentication**
- As a user, I can register, log in and log out so that my data is private.
- As a logged-out user, I can see a landing page prompting me to log in/sign up.

**Documents**
- As a user, I can create, view, edit and delete my documents.
- As a free user, I can store up to 5 documents.
- As a Premium user, I can store more than 5 documents.

**Contacts**
- As a user, I can create, view, edit and delete contacts.
- As a user, I must provide at least one contact method (phone or email).

**Expenses**
- As a user, I can add, edit and delete expenses.
- As a user, I can filter expenses by month and see a monthly total.

**Payments**
- As a user, I can upgrade to Premium via Stripe.
- As a user, I receive clear feedback on successful or cancelled payments.

### Design Choices
- **Information hierarchy:** Dashboard provides a monthly overview and shortcuts.
- **User control:** Clear navigation, confirmations and feedback messages.
- **Consistency:** Reusable base template with shared navigation and layout.

### Accessibility
- A “Skip to main content” link is included in the base layout.
- Semantic HTML is used (headings, lists, navigation landmarks).
- Forms use labels and clear error messages.

---

## Features

### Existing Features
- User registration, login and logout.
- Dashboard with:
  - Document count
  - Contact count
  - Current month expense count + total
  - Quick actions
- Documents CRUD with owner-only permissions and validation.
- Contacts CRUD with owner-only permissions and validation.
- Expenses CRUD with month filtering and totals.
- Premium gating: Free users limited to 5 documents.
- Stripe Checkout for Premium upgrade with success/cancel feedback.
- Automated tests for key logic (auth, permissions, gating, subscription creation).

### Future Features
- File uploads for documents (PDF/images) with categories.
- Search and filtering for documents/contacts.
- Webhooks for Stripe to handle asynchronous payment events robustly.
- Export monthly expense report (CSV/PDF).
- User profile settings (household members, shared access).

---

## Data Model
Homehub uses a relational database. Each user owns their own data.

### Entity Relationship Overview
- **User**
  - has many **Document**
  - has many **Contact**
  - has many **Expense**
  - has one **Subscription**

### Models
**Document**
- owner (FK → User)
- title
- description
- created_at / updated_at

**Contact**
- owner (FK → User)
- name
- role_type (choice)
- phone / email
- notes
- created_at / updated_at

**Expense**
- owner (FK → User)
- date
- category (choice)
- amount
- note
- created_at / updated_at

**Subscription**
- owner (OneToOne → User)
- is_premium
- stripe_customer_id (optional)
- stripe_subscription_id (optional)
- updated_at

---

## Security
- Authentication is required for all user data features.
- Owner-only permissions are enforced by filtering objects by `owner=request.user`.
- Sensitive configuration (SECRET_KEY, Stripe keys) is stored in environment variables.
- Production settings disable DEBUG and use ALLOWED_HOSTS from the environment.
- POST is used for logout and payments to reduce CSRF risk.

---

## Technologies Used
- Python / Django
- HTML / CSS
- SQLite (development)
- PostgreSQL (production)
- Stripe (payments)
- Gunicorn (production server)
- Whitenoise (static file serving)
- Git / GitHub (version control)

---

## Testing
Automated tests are implemented using Django’s test framework.

### Automated Tests
- Authentication: signup flow and login-required redirects
- Documents: CRUD behaviour and owner-only access protection
- Subscription: automatic creation for new users
- Premium gating: free users blocked from creating a 6th document



### Manual Tests

 - Register, login, logout

 - Create/edit/delete documents, contacts, expenses

 - Verify user cannot access another user’s data

 - Verify free limit blocks after 5 documents

 - Stripe upgrade test (test card 4242 4242 4242 4242)

 - Success/cancel messaging visible to user
---

## Deployment
The project is configured for cloud hosting.

### Environment Variables
Required:
- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DATABASE_URL (production)
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_PRICE_ID

### Local Setup
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

### Production (high-level steps)

Set environment variables on the hosting platform

Configure DATABASE_URL for the managed Postgres database

Run migrations on the platform

Collect static files:

python manage.py collectstatic

Start the web process using Gunicorn (Procfile)

### Credits

Django documentation for authentication and testing patterns.

Stripe documentation for Checkout integration.

All code in this project was written for this application and is not copied from a walkthrough project.