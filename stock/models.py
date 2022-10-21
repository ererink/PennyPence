from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.

class Stock(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80},
                                null=True)

    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[Thumbnail(200, 300)],
                                format='JPEG',
                                options={'quality': 80})
