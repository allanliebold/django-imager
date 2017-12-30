"""Profile Forms."""
from django import forms
from imager_images.models import Photo


class ProfileForm(forms.ModelForm):
    """Form for photo addition."""

    class Meta:
        """."""

        model = Photo
        fields = ['published']
