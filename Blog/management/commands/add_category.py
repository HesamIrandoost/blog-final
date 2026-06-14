from faker import Faker
from django.core.management.base import BaseCommand
from Blog.models import Category
import random
import os
from core.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = "create user and its profils"
    category_names = [
        "Technology",
        "Programming",
        "Artificial Intelligence",
        "Data Science",
        "Cybersecurity",
        "Video Games",
        "Lifestyle",
        "Health & Fitness",
        "Nutrition",
        "Psychology",
        "Business",
        "Digital Marketing",
        "Entrepreneurship",
        "Finance & Investment",
        "Travel & Tourism",
        "Books & Reading",
        "Movies & Series",
        "Music",
        "Fashion",
        "Home & Decoration",
        "Family & Parenting",
        "Education & Learning",
        "English Language",
        "Art & Design",
        "Sports",
        "Science & Technology",
        "History",
        "Philosophy",
        "Society & Culture",
        "News & Events",
    ]

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker("fa_IR")

    def handle(self, *args, **options):
        for i in self.category_names:
            Category.objects.create(name=i)
