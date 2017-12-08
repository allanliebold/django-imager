from django.test import TestCase
from imager_images.models import Photo, Album
import factory

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
        roberto = User(username='Roberto',
                     password='p@ssw0rd')
        roberto.save()
        r_profile = roberto.profile
        r_profile.location = "Buffalo"
        r_profile.save()
        album = Album(user=User.objects.get(username='Roberto'), title='The Album')
        album.save()
        for i in range(30):
            photo = PhotoFactory.build()
            photo.user = User.objects.get(username='Roberto')
            photo.save()
            album.photo.add(photo)
        self.album = album


    def test_user_has_30_photos(self):
        """Test that user Roberto has 30 photo."""
        one_user = User.objects.get(username='Roberto')
        self.assertEqual(one_user.photo.count(), 30)


    def test_first_photo_title_startswith_Photo(self):
        """Test that user Roberto has 30 photo."""
        one_user = User.objects.get(username='Roberto')
        pic = one_user.photo.first()
        self.assertTrue(pic.title.startswith('Photo'))

    def test_album_created(self):
        """Test that the album is created."""
        one_album = Album.objects.get()
        self.assertIsNotNone(one_album)


    def test_album_title_is_the_album(self):
        """Test that the album title is The Album."""
        one_album = Album.objects.get()
        self.assertEqual(one_album.title, 'The Album')


    def test_album_has_photos(self):
        """Check album contains the 30 photos that were created."""
        self.assertTrue(self.album.photo.count() == 30)

    def test_photo_with_album_points_to_album(self):
        """Test photo created actually point to the album it was linked to."""
        a_photo = Photo.objects.order_by('?').first()
        self.assertTrue(self.album in a_photo.album.all())

