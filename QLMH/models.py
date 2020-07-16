from django.db import models

# Create your models here.
class Post(models.Model):
    mamathang=models.CharField(max_length=100)
    tenmathang=models.CharField(max_length=100)
    gia=models.CharField(max_length=1000000)
    madonvitinh=models.CharField(max_length=100)
    soluong=models.CharField(max_length=1000)
    maloaimathang=models.CharField(max_length=100)
    def __str__(self):
            return self.tenmathang