from django.contrib.auth.models import User
from django.test import TestCase

from payments.models import Subscription


class SubscriptionTests(TestCase):
    def test_subscription_created_for_new_user(self):
        user = User.objects.create_user(username="subuser", password="pass12345")
        subscription = Subscription.objects.get(owner=user)
        self.assertFalse(subscription.is_premium)
