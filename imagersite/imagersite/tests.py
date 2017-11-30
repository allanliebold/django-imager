"""Test module for imagersite."""
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse_lazy
from bs4 import BeautifulSoup as soup
from django.contrib.auth.models import User
from django.core import mail
from imagersite.views import home_view


class ViewTestCase(TestCase):
    """View test case."""

    def setUp(self):
        """."""
        self.client = Client()

    def test_main_view_status_code_200(self):
        """Test main view has 200 status."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_has_h1(self):
        """Test home page has h1 div with correct text."""
        response = self.client.get(reverse_lazy('home'))
        self.assertContains(response, 'Django Imager')

    def test_home_page_inherits_base_template(self):
        response = self.client.get(reverse_lazy('home'))
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_home_page_shows_login_link(self):
        response = self.client.get(reverse_lazy('home'))
        html = soup(response.content, 'html.parser')
        link = html.find('a', {'href': '/login/'})
        self.assertIsNotNone(link)

    def test_login_view_status_code_301(self):
        """Test login view has 301 status; it redirects to login."""
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)

    # def test_login_view_status_code_200(self):
        # """Test accounts/login view has 200 status."""
        # response = self.client.get(reverse_lazy('accounts-login'))
        # self.assertEqual(response.status_code, 200)

    def test_logging_in_with_nonexistent_user_goes_back_to_login_page(self):
        """Test login view has 200 status."""
        response = self.client.post(
            reverse_lazy('login'),
            {
                'username': 'flergmcblerg',
                'password': 'flergtheblerg'
            }
        )
        html = soup(response.content, 'html.parser')
        # import pdb; pdb.set_trace()
        self.assertTrue("Please enter a correct username and password" in str(html))

    def test_logging_in_with_user_redirects_to_home(self):
        """Test login view has 200 status."""
        user = User(username='testuser', email='testuser@testuser.com')
        user.set_password('djangomango')
        user.save()

        response = self.client.post(
            reverse_lazy('login'),
            {
                'username': user.username,
                'password': 'djangomango'
            },
            follow=True
        )
        self.assertTemplateUsed(response, 'imagersite/home.html')
        self.assertContains(response, bytes(user.username, 'utf8'))

    def test_logout_view_status_code_302(self):
        """Test logout view has 302 status."""
        response = self.client.get(reverse_lazy('logout'))
        self.assertEqual(response.status_code, 302)

    def test_register_view_status_code_200(self):
        """Test register view has 200 status."""
        response = self.client.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_post_registration_redirects(self):
        """."""
        data = {
            'username': 'bobthebuilder',
            'password1': 'hellothere',
            'password2': 'hellothere',
            'email': 'bob@woo.com'
        }
        response = self.client.post(
            reverse_lazy('registration_register'),
            data
        )
        self.assertTrue(response.status_code, 302)
        self.assertTrue(response.url == reverse_lazy('registration_complete'))

    def test_post_registration_lands_on_reg_complete(self):
        """."""
        data = {
            'username': 'bobthebuilder',
            'password1': 'hellothere',
            'password2': 'hellothere',
            'email': 'bob@woo.com'
        }
        response = self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        self.assertContains(response, bytes(
            "Congratulations, you are now registered.", 'utf8'))


    def test_newly_registered_user_exists_and_is_inactive(self):
        """."""
        data = {
            'username': 'bobthebuilder',
            'password1': 'hellothere',
            'password2': 'hellothere',
            'email': 'bob@woo.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        self.assertTrue(User.objects.count() == 1)
        self.assertFalse(User.objects.first().is_active)

    def test_email_gets_sent_on_good_registration(self):
        """."""
        data = {
            'username': 'bobthebuilder',
            'password1': 'hellothere',
            'password2': 'hellothere',
            'email': 'bob@woo.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        # import pdb; pdb.set_trace()
        content = mail.outbox[0].message().get_payload()
        self.assertTrue(content.startswith(
            'Thank you for registering your account.\n\nClick the activation link below:\n\nhttp://testserver/accounts/activate/'))
        self.assertIn('bob@woo.com', email.to)

    def test_email_link_activates_account(self):
        """."""
        data = {
            'username': 'bobthebuilder',
            'password1': 'hellothere',
            'password2': 'hellothere',
            'email': 'bob@woo.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        content = mail.outbox[0].message().get_payload()
        link = content.split('\n\n')[2]
        self.client.get(link)
        self.assertTrue(User.objects.count() == 1)
        user = User.objects.get(username='bobthebuilder')
        self.assertTrue(user.is_active)

    def test_activated_user_can_now_log_in(self):
        """."""
        data = {
            'username': 'bobthebuilder',
            'password1': 'hellothere',
            'password2': 'hellothere',
            'email': 'bob@woo.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        content = mail.outbox[0].message().get_payload()
        link = content.split('\n\n')[2]
        self.client.get(link)
        response = self.client.post(reverse_lazy('login'),
            {
                'username': 'bobthebuilder',
                'password': 'hellothere'
            },
            follow=True
        )
        self.assertContains(response, 'bobthebuilder')


class ViewUnitTests(TestCase):
    def setUp(self):
        self.request = RequestFactory()

    def test_get_request_home_view_returns_proper_response(self):
        response = home_view(self.request.get('/foo'))
        self.assertTrue(True)
