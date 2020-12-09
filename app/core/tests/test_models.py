from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating user with an email is successful"""
        email = 'test@mail.com'
        password = 'Testpassword321'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@MAIL.cOM'
        user = get_user_model().objects.create_user(email, 'testPass321')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testPass321')

    def test_create_new_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@mail.com',
            'testPass321'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)