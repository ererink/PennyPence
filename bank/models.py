from django.db import models

# Create your models here.


class Bank(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
