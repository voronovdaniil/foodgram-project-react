from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        'Name',
        max_length=200,
        unique=True
    )
    color = models.CharField(
        max_length=200,
        unique=True
    )
    slug = models.CharField(
        maz
    )
