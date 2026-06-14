from django.db import models
from Accounts.models import Profile
import uuid
from slugify import slugify

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    slug = models.SlugField(max_length=60, unique=True, blank=True, editable=False)
    title = models.CharField(max_length=250)
    cover = models.ImageField(upload_to=("upload/cover/"), blank=True, null=True)
    content = models.TextField()
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # base_slug = slugify(self.title[:50], allow_unicode=True)
            # self.slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"
            self.slug = uuid.uuid4().hex

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title[:20]
