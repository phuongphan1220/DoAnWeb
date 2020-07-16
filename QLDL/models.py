from django.db import models

# Create your models here.
class Post(models.Model):
    tendaily=models.CharField(max_length=100)
    mahosodaily=models.CharField(max_length=100)
    dienthoai=models.CharField(max_length=100)
    diachi=models.CharField(max_length=100)
    ngaytiepnhan=models.DateTimeField(auto_now_add=True)
    quan=models.CharField(max_length=100)
    loaidaily=models.CharField(max_length=10)

    def __str__(self):
            return self.tendaily