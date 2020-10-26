from django.test import TestCase
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase
from testGenerator.models import Evader_test

class TestCreationTestCase(APITestCase):

    def test_creation_test(self):
        test = Evader_test.objects.create_test()
        test = Evader_test.objects.get(title="test01")
        self.assertIsNotNone(test)