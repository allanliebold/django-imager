"""."""
from django.test import TestCase
from imager_profile.models import ImagerProfile, User

import factory
import random


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for fake User."""

    class Meta:
        """."""

        model = User

    username = factory.Sequence(lambda n:
                                '{}{}'.format(factory.Faker('first_name'), n))
    email = factory.Faker('email')


class ProfileFactory(factory.django.DjangoModelFactory):
    """Factory for fake ImagerProfile."""

    class Meta:
        """."""

        model = ImagerProfile

    website = factory.Faker('url')
    location = factory.Faker('address')
    fee = random.uniform(0, 100)
    phone = factory.Faker('phone_number')


class ProfileTests(TestCase):
    """Tests for the imager_profile module."""

    def setUp(self):
        """Add one minimal user to the database."""
        user = User(username='fred', email='fred@thestair.net')
        user.set_password('password')
        user.save()
        user.profile.website = 'www.website.com'
        user.profile.location = 'Planet Earth'
        user.profile.fee = 200.00
        user.profile.phone = '888-888-8888'
        user.profile.camera = 'BW'
        user.profile.services = 'SP'
        user.profile.save()

    def test_profile_has_website(self):
        """Test that a profile has a website."""
        active_user = User.objects.get(username='fred')
        user_website = active_user.profile.website
        self.assertEquals(user_website, 'www.website.com')

    def test_profile_has_location(self):
        """Test that a profile has a location."""
        active_user = User.objects.get(username='fred')
        user_location = active_user.profile.location
        self.assertEquals(user_location, 'Planet Earth')

    def test_profile_has_fee(self):
        """Test that a profile has a fee."""
        active_user = User.objects.get(username='fred')
        user_fee = active_user.profile.fee
        self.assertEquals(user_fee, 200.00)

    def test_profile_has_phone_number(self):
        """Test that a profile has a phone number."""
        active_user = User.objects.get(username='fred')
        user_phone = active_user.profile.phone
        self.assertEquals(user_phone, '888-888-8888')

    def test_profile_has_camera(self):
        """Test that a profile has a camera."""
        active_user = User.objects.get(username='fred')
        user_camera = active_user.profile.camera
        self.assertEquals(user_camera, 'BW')

    def test_profile_has_services(self):
        """Test that profile has service."""
        active_user = User.objects.get(username='fred')
        user_services = active_user.profile.services
        self.assertEquals(user_services, 'SP')

    def test_profile_has_photo_styles(self):
        """Test that profile has default photo_styles."""
        active_user = User.objects.get(username='fred')
        user_photo_styles = active_user.profile.photo_styles
        self.assertEquals(user_photo_styles, 'CL')

    def test_profile_is_active(self):
        """Test that profile has default photo_styles."""
        active_user = User.objects.get(username='fred')
        the_user = ImagerProfile.objects.get(user=active_user)
        self.assertTrue(the_user.is_active)
