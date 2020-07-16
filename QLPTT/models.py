from django.db import models

# Create your models here.
class Post(models.Model):
    maphieuthutien=models.CharField(max_length=100)
    mahosodaily=models.CharField(max_length=100)
    ngaythutien=models.DateTimeField(auto_now_add=True)
    sotienthu=models.CharField(max_length=1000000)
    def __str__(self):
            return self.maphieuthutien
