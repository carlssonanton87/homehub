from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Document


class DocumentTests(TestCase):
    def setUp(self):
        # I create two users so I can verify ownership rules (users should only access their own documents).
        self.user_a = User.objects.create_user(username="user_a", password="pass12345")
        self.user_b = User.objects.create_user(username="user_b", password="pass12345")

    def test_logged_in_user_can_create_document(self):
        # I verify that a logged-in user can create a document and that it is linked to the correct owner.
        self.client.login(username="user_a", password="pass12345")

        response = self.client.post(
            reverse("documents:create"),
            {
                "title": "Home Insurance Policy",
                "description": "Policy details and renewal notes",
            },
        )

        self.assertEqual(Document.objects.count(), 1)
        doc = Document.objects.first()
        self.assertEqual(doc.owner, self.user_a)

        # I expect a redirect after a successful create (usually back to list).
        self.assertEqual(response.status_code, 302)

    def test_document_list_shows_only_own_documents(self):
        # I ensure users only see their own documents in the list view.
        Document.objects.create(owner=self.user_a, title="User A Doc", description="")
        Document.objects.create(owner=self.user_b, title="User B Doc", description="")

        self.client.login(username="user_a", password="pass12345")
        response = self.client.get(reverse("documents:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User A Doc")
        self.assertNotContains(response, "User B Doc")

    def test_owner_can_view_delete_confirm_page(self):
        # I confirm that the owner can open the delete confirmation page.
        doc = Document.objects.create(owner=self.user_a, title="Delete Me", description="")

        self.client.login(username="user_a", password="pass12345")
        response = self.client.get(reverse("documents:delete", args=[doc.id]))

        self.assertEqual(response.status_code, 200)

    def test_owner_can_delete_document_via_post(self):
        # I verify that the owner can delete a document using POST.
        doc = Document.objects.create(owner=self.user_a, title="Delete Me", description="")

        self.client.login(username="user_a", password="pass12345")
        response = self.client.post(reverse("documents:delete", args=[doc.id]))

        # DeleteView redirects on success (usually to success_url).
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Document.objects.filter(id=doc.id).exists())

    def test_user_cannot_view_or_delete_another_users_document(self):
        # I prevent URL tampering by making sure a user cannot delete another user's document.
        doc = Document.objects.create(owner=self.user_b, title="Private Doc", description="")

        self.client.login(username="user_a", password="pass12345")

        # Non-owner should not even be able to view the delete confirm page.
        response_get = self.client.get(reverse("documents:delete", args=[doc.id]))
        self.assertIn(response_get.status_code, (403, 404))

        # Non-owner should not be able to delete via POST either.
        response_post = self.client.post(reverse("documents:delete", args=[doc.id]))
        self.assertIn(response_post.status_code, (403, 404))

        # I confirm the document still exists after the attempted delete.
        self.assertTrue(Document.objects.filter(id=doc.id).exists())
