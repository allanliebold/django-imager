"""Test for the imager_profile app."""
from django.test import TestCase
import factory
from imager_profile.models import ImagerProfile, User


class UserFactory(factory.django.DjangoModelFactory):
    """Factory to create users."""
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f'bob{n}')
    email = factory.Sequence(lambda n: f'bob{n}@thestair.com')


class ProfileTest(TestCase):
    """Profile tests."""

    def setUp(self):
        """Set up 50 users in test database."""
        profile = ImagerProfile(location='Seattle')
        for i in range(50):
            user = UserFactory.create()
            user.set_password('kajfd;lk')
            user.save()

        profile.user = user
        profile.save()

    def test_user_defaults(self):
        """Test user exists and 50 are made and all their defaults."""
        one_user = User.objects.get(id=50)
        all_users = User.objects.all()
        website = one_user.profile.website
        location = one_user.profile.location
        fee = one_user.profile.fee
        phone = one_user.profile.phone
        camera = one_user.profile.camera
        services = one_user.profile.services
        photo_styles = one_user.profile.photo_styles
        # import pdb;pdb.set_trace()
        self.assertIsNotNone(one_user.profile)
        self.assertEqual(len(all_users), 50)
        self.assertEqual(str(one_user), "bob49")
        self.assertEqual(one_user.email, "bob49@thestair.com")
        self.assertEqual(website, "example.com")
        self.assertEqual(location, "Seattle")
        self.assertEqual(fee, 0.0)
        self.assertEqual(phone, None)
        self.assertEqual(camera, 'NK')
        self.assertEqual(services, 'WD')
        self.assertEqual(photo_styles, 'CL')
