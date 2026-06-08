from faker import Faker
from django.core.management.base import BaseCommand
from Accounts.models import User, Profile
from Blog.models import Post, Category
import random
import os
from core.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = 'create user and its profils'
    all_prof = Profile.objects.all()
    all_cate = Category.objects.all()
    titles = [
        "۱۰ ترفند طلایی برای افزایش سرعت سایت",
        "معرفی بهترین کتاب‌های علمی تخیلی تاریخ",
        "چگونه با پایتون یک ربات تلگرام بسازیم؟",
        "۵ عادت روزانه افراد موفق و ثروتمند",
        "راهنمای جامع سفر به استانبول در ۷ روز",
        "بهترین تمرینات ورزشی برای کاهش وزن سریع",
        "آشنایی با مفاهیم پایه هوش مصنوعی",
        "رازهای طراحی لوگوی حرفه‌ای با حداقل ابزار",
        "چگونه رمزهای قوی و به یاد ماندنی بسازیم؟",
        "معرفی ۱۰ فیلم برتر تاریخ سینما",
        "راهنمای شروع سرمایه‌گذاری در بورس برای مبتدیان",
        "تاثیر تغذیه بر سلامت روان و خلق و خو",
        "چگونه یک کسب‌وکار آنلاین موفق راه‌اندازی کنیم؟",
        "تکنیک‌های پیشرفته دیباگ کردن در جنگو",
        "بهترین روش‌های یادگیری سریع زبان انگلیسی",
        "چگونه استرس و اضطراب روزمره را کنترل کنیم؟",
        "معرفی جدیدترین تکنولوژی‌های خانه هوشمند",
        "۷ اشتباه رایج در بازاریابی محتوا",
        "چگونه یک عادت خوب را در ۲۱ روز نهادینه کنیم؟",
        "بررسی بهترین گوشی‌های میان‌رده بازار ۲۰۲۵",
        "راهنمای کامل شروع ورزش بدنسازی در خانه",
        "چگونه یک مقاله علمی-پژوهشی بنویسیم؟",
        "معرفی بهترین مکان‌های دیدنی ایران",
        "آشنایی با الگوهای طراحی در برنامه‌نویسی",
        "چگونه از امنیت وای فای خانگی خود مطمئن شویم؟",
        "معرفی ۵ پادکست انگیزشی که باید گوش کنید",
        "چگونه یک توسعه‌دهنده فول استک شویم؟",
        "راهنمای خرید تلویزیون هوشمند (۲۰۲۶)",
        "تاثیر بازی‌های ویدیویی بر مهارت‌های شناختی",
        "چگونه اولین کتاب خود را منتشر کنیم؟",
    ]

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker('fa_IR')


    def handle(self, *args, **options):
        for i in self.all_prof:
            for x in range(4):
                Post.objects.create(
                    author=i,
                    title=self.fake.sentence(nb_words=(random.randint(5, 12))),
                    content=self.fake.paragraph(nb_sentences=random.randint(5, 12)),
                    category=random.choice(self.all_cate)
                )