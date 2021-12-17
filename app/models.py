from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

class Image(models.Model):
    picture = CloudinaryField('images', blank=True, null=True,)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
