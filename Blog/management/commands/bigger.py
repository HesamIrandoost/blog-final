from faker import Faker
from django.core.management.base import BaseCommand
from Accounts.models import User, Profile
from Blog.models import Post, Category
import random
import os
from core.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = "بیشتر کردن کانتنت یا متن هر بلاگ"
    all_post = Post.objects.all()

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker("fa_IR")

    def handle(self, *args, **options):
        for s_post in self.all_post:
            s_post.content = self.fake.paragraph(nb_sentences=random.randint(20, 100))
            s_post.save()
