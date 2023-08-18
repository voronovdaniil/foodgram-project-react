from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Tag(models.Model):
    name = models.CharFiel