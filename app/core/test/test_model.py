from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_model_with_email(self):
        """ Test Creating user model with email """

        email = 'dummy@test.com'
        password = 'dummypass'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized_email(self):

        email = 'test@TEST.COM'

        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())
    
    def test_invalid_email_raise_error(self):
        """ Should raise value error when no email has been passed """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
        
    def test_create_super_user(self):
        """ Super user should get created """
        email = 'test@test.com'
        password = 'test123'

        user = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
