"""Profile Forms."""
from django import forms
from imager_profile.models import ImagerProfile


class ProfileForm(forms.ModelForm):
    """Form for profile addition."""

    class Meta:
        """."""

        model = ImagerProfile
        fields = ['location',
                  'fee',
                  'phone',
                  'website',
                  'camera',
                  'services',
                  'photo_styles']
