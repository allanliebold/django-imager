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
        self.profile = ImagerProfile()
        self.user = User(username='fred', email="user@user.com")
        self.user.set_password("jflakd")
        self.user.save()
        self.profile.user = self.user
        self.profile.save()
        import pdb;pdb.set_trace()
        # profile = ImagerProfile.objects.create(name='Apple')



    # def test_one_profile_created_creates_one(self):
        # """One profile created should have object length 1."""
        # profile = ImagerProfile()
        # user = models.OneToOneField(User, related_name='profile', null=True)
        # user.set_password('jfaljdfra')
        # user.save()
        # profile.save()
        # self.assertEqual(len(User.objects.all()), 1)
