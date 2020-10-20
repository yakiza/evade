from django.test import TestCase
from evader.models import EvaderUser

class AccountsTestCase(TestCase):
    def setUp(self):
        EvaderUser.objects.create_user( email="email@example.com",
                                        username="bobblack",
                                        first_name="bob",
                                        last_name="black",
                                        password="123456789"
                                        )

    def test_account_created(self):
        """User Created exists in database"""
        user = EvaderUser.objects.get(email="email@example.com")
        self.assertIsNotNone(user)