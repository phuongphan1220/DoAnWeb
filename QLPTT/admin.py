from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['maphieuthutien','ngaythutien']
    list_filter = ['ngaythutien']
    search_fields = ['maphieuthutien']
admin.site.register(Post, PostAdmin)
