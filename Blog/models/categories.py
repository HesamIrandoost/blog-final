from django.db import models
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
