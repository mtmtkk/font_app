from django.forms import ModelForm
from django import forms
from .models import Image
from cloudinary.forms import CloudinaryFileField

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture',]
    image = CloudinaryFileField(
            options={'folder': 'media/Model_image', 'tags': 'Model_name'})