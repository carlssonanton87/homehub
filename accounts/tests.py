from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthTests(TestCase):
    def test_user_can_signup(self):
        response = self.client.post(
            reverse("accounts:signup"),
            {
                "username": "testuser",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, reverse("core:home"))

    def test_login_required_redirect(self):
        response = self.client.get(reverse("documents:list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("accounts:login"), response.url)
