from django.db import models


class ImageModel(models.Model):
    photo = models.ImageField(upload_to='my_images')
    date = models.DateTimeField(auto_now_add=True)
    