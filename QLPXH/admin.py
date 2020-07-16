from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['tendaily','maphieuxuathang','ngaylapphieu']
    list_filter = ['ngaylapphieu']
    search_fields = ['tendaily']
admin.site.register(Post, PostAdmin)

