from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from documents.models import Document
from payments.models import Subscription


class DocumentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="pass12345")
        self.client.login(username="user1", password="pass12345")

    def test_user_can_create_document(self):
        response = self.client.post(
            reverse("documents:create"),
            {"title": "My Doc", "description": "Test"},
        )
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(Document.objects.first().owner, self.user)

    def test_user_cannot_access_other_users_document(self):
        other = User.objects.create_user(username="other", password="pass12345")
        doc = Document.objects.create(owner=other, title="Secret")

        response = self.client.get(reverse("documents:detail", args=[doc.pk]))
        self.assertEqual(response.status_code, 404)

    def test_free_user_is_limited_to_five_documents(self):
        subscription = Subscription.objects.get(owner=self.user)
        subscription.is_premium = False
        subscription.save()

        for i in range(5):
            Document.objects.create(owner=self.user, title=f"Doc {i}")

        response = self.client.post(
            reverse("documents:create"),
            {"title": "Blocked Doc"},
        )
        self.assertEqual(Document.objects.count(), 5)
        self.assertRedirects(response, reverse("documents:list"))
