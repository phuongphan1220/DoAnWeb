from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#Class Object

# QUẬN
class Quan(models.Model):
    maquan = models.CharField(max_length=100, primary_key=True)
    tenquan = models.CharField(max_length=100)
    def __str__(self):
        return self.tenquan



# LOẠI ĐẠI LÝ
class LoaiDL(models.Model):
    maloaidaily = models.CharField(max_length=100, primary_key=True)
    tenloaidaily = models.CharField(max_length=100)
    def __str__(self):
        return self.tenloaidaily



# ĐƠN VỊ TÍNH
class DonViTinh(models.Model):
    madonvitinh = models.CharField(max_length=100, primary_key=True)
    tendonvitinh = models.CharField(max_length=100)
    def __str__(self):
        return self.tendonvitinh



#MẶT HÀNG
class MatHang(models.Model):
        mamathang = models.CharField(max_length=100, primary_key=True)
        tenmathang = models.CharField(max_length=100)
        gia=models.CharField(max_length=1000000)
        madonvi=models.ForeignKey(DonViTinh,on_delete=models.CASCADE)
        soluong=models.CharField(max_length=100)
        active2 = models.BooleanField(default=True)
        def __str__(self):
            return self.tenmathang

#QUẢN LÍ HỒ SƠ ĐẠI LÝ
class HoSoDL(models.Model):
    tendaily = models.CharField(max_length=100)
    mahosodaily = models.CharField(max_length=100,primary_key=True)
    #phieuxuathang=models.CharField(max_length=100)
    dienthoai = models.CharField(max_length=100)
    diachi = models.CharField(max_length=100)
    ngaytiepnhan = models.DateTimeField(auto_now_add=True)
    quan = models.ForeignKey(Quan,on_delete=models.CASCADE)
    loaidaily = models.ForeignKey(LoaiDL,on_delete=models.CASCADE)
    tienno=models.CharField(max_length=100, default=0)
    active=models.BooleanField(default=True)
    def __str__(self):
        return  self.tendaily

# PHIẾU XUẤT HÀNG
class PhieuXuatHang(models.Model):
    maphieuxuathang=models.CharField(max_length=100,primary_key=True)
    #machitietphieuxuathang=models.ForeignKey(CTPhieuXuatHang,on_delete=models.CASCADE)
    #maphieuthutien=models.ForeignKey(Post,on_delete=models.CASCADE)
    ngaylapphieu=models.DateTimeField(auto_now_add=True)
    tongtien=models.CharField(max_length=1000000)
    sotientra=models.CharField(max_length=1000000)
    active1 = models.BooleanField(default=True)
    madaily=models.ForeignKey(HoSoDL,on_delete=models.CASCADE)
    def __str__(self):
        return self.maphieuxuathang




# QUẢN LÍ PHIẾU THU TIỀN
class Post(models.Model):
    maphieuthutien=models.CharField(max_length=100,primary_key=True)
    maphieuxuathang=models.ForeignKey(PhieuXuatHang,on_delete=models.CASCADE)
    ngaythutien= models.DateTimeField(auto_now_add=True)
    sotienthu=models.CharField(max_length=1000000)
    active3 = models.BooleanField(default=True)

    def __str__(self):
            return self.maphieuthutien





# CHI TIẾT PHIẾU XUẤT HÀNG
class CTPhieuXuatHang(models.Model):
    machitietphieuxuathang=models.CharField(max_length=100,primary_key=True)
    mamathang=models.ForeignKey(MatHang,on_delete=models.CASCADE)
    madonvitinh=models.ForeignKey(DonViTinh,on_delete=models.CASCADE)
    #maphieuthutien=models.ForeignKey(Post,on_delete=models.CASCADE)
    soluong=models.CharField(max_length=1000)
    dongia=models.CharField(max_length=1000000)
    thanhtien=models.CharField(max_length=1000000)
    maphieuxuathang=models.ForeignKey(PhieuXuatHang,on_delete=models.CASCADE)
    active3 = models.BooleanField(default=True)
    def __str__(self):
        return self.machitietphieuxuathang














# Form Object

class QuanForm(forms.ModelForm):
    class Meta:
        model = Quan
        fields = ('maquan', 'tenquan')


class LoaiDLForm(forms.ModelForm):
    class Meta:
        model = LoaiDL
        fields = ('maloaidaily', 'tenloaidaily')



class HSDLForm(forms.ModelForm):
    class Meta:
        model=HoSoDL
        fields=("tendaily","mahosodaily","dienthoai","diachi","quan","loaidaily",'tienno')



class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("maphieuthutien",'sotienthu', 'maphieuxuathang')


class DonVTForm(forms.ModelForm):
    class Meta:
        model = DonViTinh
        fields = '__all__'


class MatHangForm(forms.ModelForm):
    class Meta:
        model = MatHang
        fields = '__all__'


class PhieuXuatHangForm(forms.ModelForm):
    class Meta:
        model=PhieuXuatHang
        fields=('maphieuxuathang','tongtien','sotientra','madaily')


class CTPhieuXuatHangForm(forms.ModelForm):
    class Meta:
        model=CTPhieuXuatHang
        fields=('machitietphieuxuathang','mamathang','madonvitinh','soluong','dongia','thanhtien', 'maphieuxuathang')






class RegisterForm(UserCreationForm):
    username= forms.CharField(label='Username')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    email=forms.EmailField(label='Email address')
    first_name=forms.CharField(label='First name')
    last_name=forms.CharField(label='Last name')


    class Meta(UserCreationForm.Meta):
        fields=('first_name','last_name','username','email','password1','password2')

    def saveData(self,commit=True):
        customer=super().save(commit=False)
        customer.set_password(self.cleaned_data['password1'])
        if commit:
            customer.save()
        return  customer