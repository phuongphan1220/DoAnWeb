"""DoAnWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from home.views import sigin, sigout,register,create_Post,Save,create_HSDL,SaveHSDL,create_MH,SaveMH,create_DVT,SaveDVT,create_Quan,SaveQuan,create_LoaiDL,SaveLoaiDL,create_CTPXH,SaveCTPXH,create_PXH,SavePXH,manage_HoSoDaiLy,manage_PhieuXuatHang,manage_MatHang,manage_PhieuThuTien,delete_HSDL,modify_HSDL,modify_PXH,delete_PXH,modify_MH,delete_MH,delete_PTT,modify_PTT
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('home/',views.index),
    path('dangNhap/',sigin,name='sigIn'),
    path('dangKy/',register,name='dangKy'),
    path('thoat/', sigout, name='sigOut'),

    # PHIẾU THU TIỀN
    path('PostForm/',create_Post,name='PostForm'),
    path('Save/',Save,name="luu"),
       # HỒ SƠ ĐẠI LÝ
    path('HSDL/',create_HSDL,name='HSDLForm'),
    path('SaveHSDL/',SaveHSDL,name="luuHSDL"),
        # MẶT HÀNG
    path('MatHang/',create_MH,name='MHForm'),
    path('SaveMH/',SaveMH,name="luuMH"),
        # ĐƠN VỊ TÍNH
    path('DonViTinh/',create_DVT,name='DonViTinhForm'),
    path('SaveDVT/',SaveDVT,name="luuDVT"),
        # QUẬN
    path('Quan/',create_Quan,name='QuanForm'),
    path('SaveQuan/',SaveQuan,name="luuQuan"),
        # LOẠI ĐẠI LÝ
    path('LoaiDL/',create_LoaiDL,name='LoaiDLForm'),
    path('SaveLoaiDL/',SaveLoaiDL,name="luuLoaiDL"),
        # CHI TIẾT PHIẾU XUẤT HÀNG
    path('CTPXH/',create_CTPXH,name='CTPXHForm'),
    path('SaveCTPXH/',SaveCTPXH,name="luuCTPXH"),
        # PHIẾU XUẤT HÀNG
    path('PXH/',create_PXH,name='PXHForm'),
    path('SavePXH/',SavePXH,name="luuPXH"),
        #SHOW DỮ LIỆU
    path("HoSoDL/",manage_HoSoDaiLy,name='hsdl'),
    path("QLPXH/",manage_PhieuXuatHang,name='qlpxh'),
    path('QLMH/',manage_MatHang,name='mh'),
    path('QLPTT/',manage_PhieuThuTien,name="ptt"),


        # QUẢN LÝ HỒ SƠ ĐẠI LÝ
    path('HSDL-modify/<id>',modify_HSDL,name='modify_HSDL'),
    path('HSDL-delete/<mahosodaily>',delete_HSDL,name='delete-HSDL'),


        # QUẢN LÝ PHIẾU XUẤT HÀNG
    path('PXH-modify/<id>',modify_PXH,name='modify_PXH'),
    path('PXH-delete/<maphieuxuathang>',delete_PXH,name='delete-PXH'),


        # QUẢN LÝ MẶT HÀNG
    path('MH-modify/<id>',modify_MH,name='modify_MH'),
    path('MH-delete/<mamathang>',delete_MH,name='delete-MH'),


        # QUẢN LÝ PHIẾU THU TIỀN
    path('PTT-modify/<id>',modify_PTT,name='modify_PTT'),
    path('PTT-delete/<maphieuthutien>',delete_PTT,name='delete-PTT')
]
