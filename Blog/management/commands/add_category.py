from faker import Faker
from django.core.management.base import BaseCommand
from Blog.models import Category
import random
import os
from core.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = 'create user and its profils'
    category_names = [
        "تکنولوژی", "برنامه‌نویسی", "هوش مصنوعی", "علم داده", "امنیت سایبری",
        "بازی‌های ویدیویی", "سبک زندگی", "سلامت و تناسب اندام", "تغذیه", "روانشناسی",
        "کسب‌وکار", "بازاریابی دیجیتال", "کارآفرینی", "مالی و سرمایه‌گذاری", "سفر و گردشگری",
        "کتاب و مطالعه", "فیلم و سریال", "موسیقی", "مد و فشن", "خانه و دکوراسیون",
        "خانواده و فرزندپروری", "آموزش و یادگیری", "زبان انگلیسی", "هنر و طراحی", "ورزش",
        "علم و فناوری", "تاریخ", "فلسفه", "جامعه و فرهنگ", "اخبار و رویدادها"
    ]


    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker('fa_IR')


    def handle(self, *args, **options):
        for i in self.category_names:
            Category.objects.create(
                name=i                
            )