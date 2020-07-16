from django.db import models

# Create your models here.
class Post(models.Model):
    tendaily = models.CharField(max_length=100)
    ngaylapphieu=models.DateTimeField(auto_now_add=True)
    mamathang = models.CharField(max_length=100)
    soluong = models.CharField(max_length=1000)
    tongtien = models.CharField(max_length=1000000)
    maphieuxuathang=models.CharField(max_length=100)
    def __str__(self):
            return self.maphieuxuathang