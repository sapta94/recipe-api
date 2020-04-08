from django.test import TestCase
from django.contrib.auth import  get_user_model


class ModelTests(TestCase):

    def test_create_user_success(self):
        """Test creating a new user with an email is successful"""
        email = 'abc@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email(self):
        """Test User without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        ##Test for creating a super user
        user = get_user_model().objects.create_superuser(
            'dey7.kol@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        