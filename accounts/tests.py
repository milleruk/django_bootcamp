from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
# TDD
User = get_user_model()
class UserTestCase(TestCase):

    def setUp(self):  # Python's builtin unittest case lower to start
        user_a = User(username='testuser', email='dev@dev.com')
        # User.objects.create()
        # User.objects.create_user()
        user_a_pw = 'randompassword@1'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self): # start tests with tests at the start
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1) # ==
        self.assertNotEqual(user_count, 0) # !=

    # def test_user_password(self):
    #     # user_qs = User.objects.filter(username__iexact="testuser")
    #     # user_exists = user_qs.exists() and user_qs.count() == 1
    #     # self.assertTrue(user_exists)  # True/False
    #     # user_a = user_qs.first()
    #     self.assertTrue(
    #         self.user_a.check_password(self.user_a_pw))

    def test_user_password(self):
        user_a = User.objects.get(username="testuser")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )

    def test_login_url(self):
        # login_url = "/login/"
        # self.assertEqual(settings.LOGIN_URL, login_url)
        login_url = settings.LOGIN_URL
        # python requests - manage.py runserver
        # self.clients.get, self.clients.post
        #response = self.clients.post(url, {}, follow=True)
        data = {"username": "testuser", "password": "randompassword@1"}
        response = self.client.post(login_url, data, follow=True)
        #print(dir(response))  # givees you all of response
        #print(response.request)
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(status_code, 200)



        





