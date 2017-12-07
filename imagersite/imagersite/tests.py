"""Test module for imagersite."""
from bs4 import BeautifulSoup as soup
from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.conf import settings
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from imager_images.models import Photo
import factory
import os


class PhotoFactory(factory.django.DjangoModelFactory):
    """Factory for fake Photo."""

    class Meta:
        """Meta."""

        model = Photo

    image = SimpleUploadedFile(
        name='sample_img.jpg',
        content=open(
            os.path.join(settings.BASE_DIR, 'imagersite/static/test_image.jpg'), 'rb'
        ).read(),
        content_type="image/jpeg"
    )

    title = factory.Faker('word')
    description = factory.Faker('sentence')
    published = 'PUBLIC'


class ViewTestCase(TestCase):
    """View test case."""

    def setUp(self):
        """."""
        self.client = Client()

        user1 = User(username='Frederick',
                     password='hfaldjl')

        user1.save()

        photos = [PhotoFactory.build() for _ in range(10)]
        for photo in photos:
            photo.user = user1
            photo.save()

    def test_main_view_status_code_200(self):
        """Test main view has 200 status."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_has_h1(self):
        """Test home page has h1 div with correct text."""
        # import pdb; pdb.set_trace()
        response = self.client.get(reverse_lazy('home'))
        self.assertContains(response, 'Django Imager')

    def test_home_page_inherits_base_template(self):
        """."""
        response = self.client.get(reverse_lazy('home'))
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_home_page_shows_login_link(self):
        """."""
        response = self.client.get(reverse_lazy('home'))
        html = soup(response.content, 'html.parser')
        link = html.find('a', {'href': '/login/'})
        self.assertIsNotNone(link)

    def test_login_view_status_code_200(self):
        """Test login view has 301 status; it redirects to login."""
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)

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
        self.assertTrue("Your username and password didn't match." in str(html))

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
        self.assertTemplateUsed(response, 'imagersite/index.html')
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
        self.assertTrue(User.objects.count() == 2)
        self.assertFalse(User.objects.all()[1].is_active)

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
        self.assertTrue(User.objects.count() == 2)
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
        response = self.client.post(reverse_lazy('login'), {
            'username': 'bobthebuilder',
            'password': 'hellothere'
        },
            follow=True
        )
        self.assertContains(response, 'bobthebuilder')
