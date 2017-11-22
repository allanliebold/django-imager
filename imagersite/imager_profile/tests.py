from django.test import TestCase
import factory
from imager_profile.models import ImagerProfile, User


class UserFactory(factory.django.DjangoModelFactory):
    """."""
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f'bob{n}' )
    email = factory.Sequence(lambda n: f'bob{n}@thestair.com')

class ProfileTest(TestCase):
    """."""
    def setUp(self):
        import pdb;pdb.set_trace()
        profile = ImagerProfile(location='Seattle')
        for i in range(50):
            user = UserFactory.create()
            user.set_password('kajfd;lk')
            user.save()

        profile.user = user
        profile.save()


    def test_user_can_point_to_its_profile(self):
        """."""
        import pdb;pdb.set_trace()
        one_user = User.objects.get(id=50)
        self.assertIsNotNone(one_user.profile)

    def test_there_are_50_users(self):
        """."""
        all_users = User.objects.all()
        self.assertEqual(len(all_users), 50)


