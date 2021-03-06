from django.test import TestCase
from evader.serializers import User_registration_serializer
from evader.models import Evader_user
from django.contrib.auth import get_user_model
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase

class UserCreationTestCase(TestCase):

    def test_user_model(self):
        Evader_user.objects.create_user( email="email@example.com",
                                username="bobblack",
                                first_name="bob",
                                last_name="black",
                                password="123456789")
        user = Evader_user.objects.get(email="email@example.com")
        self.assertIsNotNone(user)

    def test_user_model_missing_first_name(self):
        Evader_user.objects.create_user( email="email1@example.com",
                                username="bobblack",
                                first_name="",
                                last_name="black",
                                password="123456789")
        users = get_user_model().objects.filter(email='email1@example.com')
        self.assertEqual(users.count(), 1)
        self.assertEqual(users.first().first_name, '')

    def test_serialize_user_data(self):
        user_json_data = {
            "email": "myemail@email.com",
            "username": "Yakiza" ,
            "first_name": "yakizaza" ,
            "last_name": "yakiza" ,
            "password": "13121312" ,
            "password2": "13121312"}

        user = User_registration_serializer(data=user_json_data)
        if user.is_valid():
            user.save()
            serializer_errors = len(user.errors)
            self.assertEqual(serializer_errors, 0)
            # self.assertTrue(status.is_success(response.status_code))

class UserLogInTestCase(APITestCase):

    def test_user_login(self):
        user = Evader_user.objects.create_user( email="email@example.com",
                                username="bobblack",
                                first_name="bob",
                                last_name="black",
                                password="123456789")
        user.save()
        c = Client()
        response = c.login(username='email@example.com', password='1234567')
        self.assertTrue(response, "Cannot Log in, incorrect credentials")


        # Must ADD MORE TESTS AS PER THE STATUS CODE ETC


        


    