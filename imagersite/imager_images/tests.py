from django.test import TestCase
from imager_images.models import Photo, Album
import Factory

from imager_profile.models import ImagerProfile, User


class PhotoFactory(factory.django.DjangoModelFactory):
    """Photo factory to make photos."""

    class Meta:
        """Meta class."""

        model = Photo

    title = factory.Sequence(lambda n: f'Photo{n}')


class PhotoTestCase(TestCase):
    """Photo test case."""

    # @classmethod
    # def setUpClass(cls):

    def setUp(self):
        """Setup."""
        jimbo = User(username='Jimbo',
                     password='p@ssw0rd')
        jimbo.save()
        j_profile = jimbo.profile
        j_profile.location = "Buffalo"
        j_profile.save()
        album = Album(user=j_profile, title='The Album')
        album.save()
        for i in range(30):
            photo = PhotoFactory.build()
            photo.user = j_profile
            # photo = Photo(user=j_profile, title=f'Pic{i}')
            photo.save()
            album.photos.add(photo)
        self.album = album


    def test_user_has_30_photos(self):
        """Test that user Jimbo has 30 photo."""
        one_user = User.objects.first()
        self.assertEqual(one_user.profile.photo_set.count(), 30)

