from django.contrib import admin
from .models import Post, UserContact

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'desc']

# admin.site.register(UserContact)
@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'phone', 'desc']
