from django.contrib import admin
from .models import Post
# Register your models here.
# Hiện time.
class PostAdmin(admin.ModelAdmin):
    list_display = ['tendaily','ngaytiepnhan']
    list_filter = ['ngaytiepnhan']
    search_fields = ['tendaily']
admin.site.register(Post, PostAdmin)