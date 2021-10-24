from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Profile


class EditProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)