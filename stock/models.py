from django.db import models

# Create your models here.


class Stock(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
