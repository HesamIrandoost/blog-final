from faker import Faker
from django.core.management.base import BaseCommand
from Accounts.models import Profile
from Blog.models import Post
from Comment.models import Comment
import random
import os
from core.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = 'create user and its profils'
    all_post=Post.objects.all()
    all_profile=Profile.objects.all()    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker('fa_IR')


    def handle(self, *args, **options):
        for i in self.all_post:
            for x in range(4):
                Comment.objects.create(
                    post=i,
                    user=random.choice(self.all_profile),
                    text=self.fake.sentence(nb_words=random.randint(1, 15))

                )