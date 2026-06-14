from django.contrib import admin
from Blog.models import Post, Category

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "slug"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "slug", "name"]
