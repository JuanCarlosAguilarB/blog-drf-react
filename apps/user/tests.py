from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersTests(TestCase):
    """Test for user model"""
    
    def setUp(self):
        """initial config for all test"""
        self.payload = {"email":'normal@user.com', "password":'F0001@'}

    def test_create_user_sussecsfull(self):
        User = get_user_model()
        user = User.objects.create_user(**self.payload)
        
        self.assertEqual(user.email, self.payload["email"])
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
        self.assertTrue(user.check_password(self.payload["password"]), self.payload["password"])
        
        # try:
        #     # username is None for the AbstractUser option
        #     # username does not exist for the AbstractBaseUser option
        #     self.assertIsNone(user.username)
        # except AttributeError:
        #     pass
        # with self.assertRaises(TypeError):
        #     User.objects.create_user()
        # with self.assertRaises(TypeError):
        #     User.objects.create_user(email='')
        # with self.assertRaises(ValueError):
        #     User.objects.create_user(email='', password="foo")

    # def test_create_superuser(self):
    #     User = get_user_model()
    #     admin_user = User.objects.create_superuser(email='super@user.com', password='foo', username="admin")
    #     self.assertEqual(admin_user.email, 'super@user.com')
    #     self.assertTrue(admin_user.is_active)
    #     self.assertTrue(admin_user.is_staff)
    #     self.assertTrue(admin_user.is_superuser)
    #     try:
    #         # username is None for the AbstractUser option
    #         # username does not exist for the AbstractBaseUser option
    #         self.assertIsNone(admin_user.username)
    #     except AttributeError:
    #         pass
    #     with self.assertRaises(ValueError):
    #         User.objects.create_superuser(
    #             email='super@user.com', password='foo', is_superuser=False)