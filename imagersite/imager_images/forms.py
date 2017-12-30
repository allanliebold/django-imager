from django import forms
from imager_images.models import Photo, Album


class PhotoForm(forms.ModelForm):
    """Form for photo addition."""

    class Meta:
        """."""

        model = Photo
        fields = ['title', 'description', 'published']
        widgets = {
            'descriptiion': forms.Textarea()
        }


class AlbumForm(forms.ModelForm):
    """Form for photo addition."""

    class Meta:
        """."""

        model = Photo
        exclude = ['user', 'date_published']
        widgets = {
            'descriptiion': forms.Textarea()
        }
