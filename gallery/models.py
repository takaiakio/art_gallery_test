# gallery/models.py

from django.db import models

class Art(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='art_images/')

    def __str__(self):
        return self.title
