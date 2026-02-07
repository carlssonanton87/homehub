# Homehub 🏡
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/carlssonanton87/homehub)
![GitHub last commit](https://img.shields.io/github/last-commit/carlssonanton87/homehub)
![GitHub repo size](https://img.shields.io/github/repo-size/carlssonanton87/homehub)


**Homehub** is a full-stack Django web application designed to help users organize important home information in one place. Users can securely log in to manage **documents**, **contacts**, and **monthly expenses**, and optionally upgrade to **Premium** via Stripe to unlock unlimited document storage.

[Live Demo](https://homehub-anton-5399ce3434e0.herokuapp.com/)

[Homehub shown on a range of devices](readme_assets/images/devices.png)
---

## Key Features

- User authentication (registration, login, logout)
- Clean Tailwind UI (Notion-inspired)
- Documents:
  - Create / view / edit / delete
  - Search functionality
  - Free plan document limit (Premium removes the limit)
- Contacts:
  - Store home-related contacts (plumber, electrician, landlord etc.)
  - Full CRUD + search
- Expenses:
  - Monthly expense tracking
  - Month filter + monthly totals
- Payments:
  - Stripe checkout (test mode)
  - Premium status enabled after successful payment
- Feedback messages and confirmation flows
- Responsive design (mobile, tablet, desktop)

## Contents

1. [Features](#features)
2. [User Experience (UX)](#user-experience-ux)
   - [Design Choices](#design-choices)
   - [Typography](#typography)
   - [User Stories](#user-stories)
   - [Wireframes](#wireframes)
3. [Information Architecture](#information-architecture)
   - [Database Schema Diagram](#database-schema-diagram)
4. [Technologies Used](#technologies-used)
5. [Agile Methodology](#agile-methodology)
   - [Kanban Workflow](#kanban-workflow)
   - [Project Evolution](#project-evolution)
6. [Version Control](#version-control)
7. [Deployment](#deployment)
8. [Testing](#testing)
9. [Known Issues and Future Features](#known-issues-and-future-features)
10. [Credits](#credits)
    - [Resources Used](#resources-used)
    - [Code Used](#code-used)
    - [Acknowledgements](#acknowledgements)

---
## Features

### Existing Features

1. **User Registration & Authentication**
   - Secure signup, login, logout
   - User data is private (users can only access their own content)

2. **Documents Management**
   - Add, edit, view, and delete documents
   - Search documents by title and description
   - Free plan document limit (Premium removes the limit)

3. **Contacts Management**
   - Add, edit, and delete contacts
   - Store key household contacts (e.g. electrician, plumber)
   - Search contacts by name, role, or notes

4. **Expenses Tracking**
   - Add, edit, and delete expenses
   - Filter expenses by month
   - Monthly totals displayed clearly

5. **Payments & Subscription**
   - Upgrade to Premium through Stripe Checkout
   - Premium status displayed across the UI
   - Premium removes free plan document limit

6. **Admin Panel**
   - Django admin for user and content management

[Go to Contents](#contents)

---

## Target Audience
- Home owners and renters who want one place for home information.
- Families managing recurring household costs and services.
- Users who want a lightweight “home admin” tool that is easy to use.

---

## User Experience (UX)

### Design Choices

Homehub is designed as a clean digital home organizer with a calm, minimal interface inspired by productivity tools.

#### Color Scheme
- Neutral base with subtle borders and soft backgrounds
- Accent color used for primary actions and navigation focus

> Add screenshot:
`readme_assets/images/color_palette.png`

#### Typography
- Clean typography for readability (modern sans-serif / Inter-like)
- Clear hierarchy for headings, labels, and helper text

#### User Stories

##### Visitors
- As a visitor, I can view the landing page but cannot access private content.

##### Registered Users
- As a user, I can register an account.
- As a user, I can log in and log out securely.
- As a user, I can create, edit and delete my own documents.
- As a user, I can store key contacts for my household.
- As a user, I can track monthly household expenses.
- As a user, I receive confirmation messages when actions succeed or fail.
- As a user, I can upgrade to Premium to unlock unlimited documents.

##### Admin Users
- As an admin, I can manage users and data via Django admin.

#### Wireframes

<details>
<summary>Landing Page</summary>
<br>

![Landing Page](readme_assets/images/wireframes/landing.png)
</details>

<details>
<summary>Dashboard</summary>
<br>

![Dashboard](readme_assets/images/wireframes/dashboard.png)
</details>

<details>
<summary>Documents</summary>
<br>

![Documents](readme_assets/images/wireframes/documents.png)
</details>

<details>
<summary>Add Documents</summary>
<br>

![Documents](readme_assets/images/wireframes/addDocuments.png)
</details>

<details>
<summary>Mobile View</summary>
<br>

![Documents](readme_assets/images/wireframes/mobileview.png)
</details>

Wireframes were created using (Visily.ai).

[Go to Contents](#contents)

---

## Information Architecture

### Database Schema Diagram

Homehub uses a user-owned content model:
- Each user can have many documents, contacts, and expenses.
- Each record belongs to one user.
- Premium state is stored in a subscription model linked to the user.

The diagram below illustrates the database structure and relationships used in Homehub.

![Homehub Database ERD Diagram](readme_assets/images/erd.png)

[Go to Contents](#contents)

---

## Technologies Used

### Languages and Frameworks

- [![HTML](https://img.shields.io/badge/HTML-5-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML5)
- [![CSS](https://img.shields.io/badge/Tailwind_CSS-grey?logo=tailwindcss&logoColor=38B2AC)](https://tailwindcss.com/)
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com)
- [![Python](https://img.shields.io/badge/Python-3.x-grey?logo=python&logoColor=3776AB)](https://www.python.org)
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com/)

### Databases

- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org/) (production)

### Other Tools

- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com)
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com)
- [![Stripe](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=635BFF)](https://stripe.com/)
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io)
- [![W3C HTML Validator](https://img.shields.io/badge/W3C_HTML_Validator-grey?logo=w3c&logoColor=005A9C)](https://validator.w3.org/)
- [![W3C CSS Validator](https://img.shields.io/badge/W3C_CSS_Validator-grey?logo=w3c&logoColor=005A9C)](https://jigsaw.w3.org/css-validator/)
- [![JSHint](https://img.shields.io/badge/JSHint-grey?logo=javascript&logoColor=F7DF1E)](https://jshint.com/)
- [![PEP8 Validator](https://img.shields.io/badge/PEP8_Validator-grey?logo=python&logoColor=A44200)](https://pep8ci.herokuapp.com/)
- [![Am I Responsive](https://img.shields.io/badge/Am_I_Responsive-grey?logo=responsive&logoColor=0078D4)](https://ui.dev/amiresponsive)
- [![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-grey?logo=stackoverflow&logoColor=FE7A16)](https://stackoverflow.com/)

[Go to Contents](#contents)

---

## Agile Methodology

This project was developed using Agile methodology and tracked using GitHub Issues / Projects.

### Kanban Workflow
> Add your board link here:
- Kanban Board: `https://github.com/users/carlssonanton87/projects/<ID>`

### Project Evolution
- Planned epics and user stories first
- Implemented core CRUD functionality
- Added Premium subscription gate (Stripe)
- Iterated UI/UX with Tailwind and responsive improvements
- Deployed to Heroku with auto-deploy from GitHub

[Go to Contents](#contents)

---

## Version Control

For version control, Git was used to track changes through frequent commits:

- `git add .`
- `git commit -m "message"`
- `git push`

[Go to Contents](#contents)

---
## Deployment

Homehub was deployed on Heroku using GitHub integration for automatic deployment.

1. Create a Heroku app
2. Connect the GitHub repository
3. Enable automatic deploys from `main`
4. Add environment variables (Config Vars):
   - `SECRET_KEY`
   - `DATABASE_URL`
   - `DEBUG`
   - `ALLOWED_HOSTS`
   - `CSRF_TRUSTED_ORIGINS`
   - `STRIPE_PUBLIC_KEY`
   - `STRIPE_SECRET_KEY`
   - `STRIPE_PRICE_ID`
5. Add Heroku Postgres add-on
6. Run migrations:
   - `python manage.py migrate`
7. Optional: seed demo user data:
   - `python manage.py seed_demo`

---


### Forking and Local Setup

If you’d like to fork this repository and set it up locally, follow these steps:

1. **Fork the Repository**:  
   - Go to the GitHub repository and click on "Fork" to create a copy in your account.

2. **Clone Your Fork**:  
   - Click "Code" on your forked repository, copy the URL, then open your terminal and run:
     ```
     git clone [URL you copied]
     ```

3. **Set Up Virtual Environment**:  
   - Navigate to the project directory:
     ```
     cd [project directory name]
     ```
   - Create a virtual environment:
     ```
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS and Linux: `source venv/bin/activate`

4. **Install Dependencies**:  
   - With the virtual environment activated, install the required packages:
     ```
     pip install -r requirements.txt
     ```

5. **Set Up Environment Variables**:  
   - Create an `env.py` file in the root directory and add the following environment variables based on `settings.py` requirements:
     ```python
     SECRET_KEY = 'your_secret_key'
     DATABASE_URL = 'your_database_url'
     CLOUDINARY_URL = 'your_cloudinary_url?secure=true'
     DEVELOPMENT = 'True'
     ```
   - Setting `DEVELOPMENT = 'True'` enables `DEBUG=True` in local development, allowing you to test and debug safely.
   - Adding `secure=true` to the `CLOUDINARY_URL` ensures media files are delivered over HTTPS, providing secure access to images and assets.

6. **Apply Migrations**:  
   - Run migrations to set up the database schema:
     ```
     python3 manage.py makemigrations
     python3 manage.py migrate
     ```

7. **Collect Static Files (Optional for Local Testing)**:  
   - If you want to test static files locally in a production-like setup, you can run:
     ```bash
     python3 manage.py collectstatic
     ```
   - This is typically required in production but can be helpful to verify static files locally.

8. **Run the Development Server**:  
   - Start the server locally:
     ```
     python3 manage.py runserver 8001
     ```
   - Note: This project initially used port `8000` but now uses port `8001` to avoid conflicts with other services.
   - Open a browser and go to `http://127.0.0.1:8001/` to view the application locally.

---

This enhanced setup provides a clear process for cloning, setting up environment variables, and preparing the local environment based on your project’s specific configuration requirements.

---

[Go to Contents](#contents)

## Testing

Comprehensive testing has been performed to validate functionality, usability, and reliability.

For detailed test cases, validation screenshots, and device testing, please refer to the  
👉 **[TESTING.md](TESTING.md)** file.

[Go to Contents](#contents)


---

## Known Issues and Future Features

### Future Features
- Expense analytics (categories, charts, trends)
- Optional file uploads for documents (Cloudinary/S3)
- Reminders for renewals and home services
- Export expenses to CSV

### Known Issues
- No recurring expense support yet
- No document file upload (text-only documents)

---

## Credits

### Resources Used
- Django Documentation
- Tailwind CSS Documentation
- Stripe Documentation
- Code Institute course material

### Code Used
- Based on Code Institute Django project patterns
- Stripe integration based on official Stripe documentation

### Acknowledgements
- Code Institute
- Mentor feedback
- ChatGPT for troubleshooting and documentation support

---

## Security
- Authentication is required for all user data features.
- Owner-only permissions are enforced by filtering objects by `owner=request.user`.
- Sensitive configuration (SECRET_KEY, Stripe keys) is stored in environment variables.
- Production settings disable DEBUG and use ALLOWED_HOSTS from the environment.
- POST is used for logout and payments to reduce CSRF risk.



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


