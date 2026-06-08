from faker import Faker
from django.core.management.base import BaseCommand
from Accounts.models import User, Profile
import random
import os
from core.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = 'create user and its profils'
    cover_images = ['pic1.png', 'pic2.png']

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker('fa_IR')


    def handle(self, *args, **options):
        for i in range(10):
            user_fake=User.objects.create_user(
                email=self.fake.email(),
                username=self.fake.user_name(),
                password="qw1234QW@"                
            )
            selected_image = random.choice(self.cover_images)
            image_path = os.path.join(MEDIA_ROOT, selected_image)
            profile_fake = Profile.objects.get(user=user_fake)
            profile_fake.first_name=self.fake.first_name()      
            profile_fake.last_name=self.fake.last_name()
            profile_fake.image=image_path
            profile_fake.bio=self.fake.paragraph(nb_sentences=random.randint(4, 8))
            profile_fake.save()                  