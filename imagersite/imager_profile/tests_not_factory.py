"""Tests for imager_profile app."""
from django.db import models
from django.test import TestCase
from imager_profile.models import ImagerProfile, User

class StandardTest(TestCase):
    """Profile tests."""

    def test_no_profile_created_not_in_database(self):
        """No profiles created should have empty table."""
        self.assertEqual(len(User.objects.all()), 0)

    def test_one_profile_created_creates_one(self):
        """One profile created should have object length 1."""
        profile = ImagerProfile()
        # profile = ImagerProfile.objects.create(name='Apple')
        profile.save()
        import pdb;pdb.set_trace()



    # def test_one_profile_created_creates_one(self):
        # """One profile created should have object length 1."""
        # profile = ImagerProfile()
        # user = models.OneToOneField(User, related_name='profile', null=True)
        # user.set_password('jfaljdfra')
        # user.save()
        # profile.save()
        # self.assertEqual(len(User.objects.all()), 1)
