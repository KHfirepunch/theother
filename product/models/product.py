from django.db import models
from tag.models import Tag


class Product(models.Model):
    tags = models.OneToOneField(
        Tag,
        on_delete=models.CASCADE,
    )