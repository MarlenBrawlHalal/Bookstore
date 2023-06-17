from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='dias', email='dias@email.com', password='test123test'
        )
        self.assertEqual(user.username, 'dias')
        self.assertEqual(user.email, 'dias@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superdias', email='superdias@email.com', password='test123test'
        )
        self.assertEqual(admin_user.username, 'superdias')
        self.assertEqual(admin_user.email, 'superdias@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)