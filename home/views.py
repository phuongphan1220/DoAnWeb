from django.contrib.auth import authenticate, login, logout,forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from home.models import PostForm,HSDLForm,MatHangForm,DonVTForm,QuanForm,LoaiDLForm,CTPhieuXuatHangForm,PhieuXuatHangForm, HoSoDL,PhieuXuatHang,MatHang,Post,RegisterForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return render(request,'pages/home.html')
def DangNhap(request):
    return render(request,'pages/dangNhap.html')
def DangKy(request):
    return  render(request,'pages/dangKy.html')
def QLDL(request):
    return  render(request,'pages/qldl.html')


@login_required(login_url='/dangNhap')
# QUẢN LÍ PHIẾU THU TIỀN
def create_Post(request):
    postForm=PostForm()
    return render(request,'pages/QLPTT.html',{'PostForms':postForm})

@login_required(login_url='/dangNhap')
#execute-thuchien
def Save(request):
   if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            result=form.save()
            if request.method=='POST':
                respone=HttpResponse()
                respone.write('Mã Phiếu Thu Tiền :'+ request.POST['maphieuthutien']+'</br>')
                #respone.write('Mã Hồ Sơ Đại Lý :' + request.POST['mahosodaily'] + '</br>')
                respone.write('Số Tiền Thu :' + request.POST['sotienthu'] + '</br>')
                return respone
            return render(request, 'pages/home.html')
   return render(request, 'pages/home.html',{'form':PostForm})


@login_required(login_url='/dangNhap')
def modify_PTT(request):
    if request.method=='POST':
        form = PostForm(request.POST,instance=Post)
        if form.is_valid():
            Post.maphieuthutien=form['maphieuthutien'].value()
            Post.sotienthu=form['sotienthu'].value()
            Post.save()
            return render(request,'pages/QLPTT.html',{'PTTForms':form})
        return redirect('/phieuThuTien')


@login_required(login_url='/dangNhap')
# XÓA DỮ LIỆU PHIẾU THU TIỀN
def delete_PTT(request, maphieuthutien):
    ptt = get_object_or_404(Post, pk=maphieuthutien)
    ptt.active = False
    ptt.save()
    return redirect('/manage_PhieuThuTien/')


@login_required(login_url='/dangNhap')
#QUẢN LÍ HỒ SƠ ĐẠI LÝ
def create_HSDL(request):
    hsdlForm=HSDLForm()
    return render(request,'pages/HSDL.html',{'HSDLForms':hsdlForm})

@login_required(login_url='/dangNhap')
def SaveHSDL(request):
   if request.method=='POST':
        form=HSDLForm(request.POST)
        if form.is_valid():
            result=form.save()
            if request.method=='POST':
                respone=HttpResponse()
                respone.write('Tên Đại Lý : '+ request.POST['tendaily']+'</br>')
                respone.write('Mã Hồ Sơ Đại Lý : ' + request.POST['mahosodaily'] + '</br>')
                #respone.write('Phiếu Xuất Hàng : ' + request.POST['phieuxuathang'] + '</br>')
                respone.write('Điện Thoại : ' + request.POST['dienthoai'] + '</br>')
                respone.write('Điạ Chỉ : ' + request.POST['diachi'] + '</br>')
                respone.write('Quận : ' + request.POST['quan'] + '</br>')
                respone.write('Loại Đại Lý : ' + request.POST['loaidaily'] + '</br>')
                respone.write('Tiền Nợ : ' + request.POST['tienno'] + '</br>')
                return respone
            return render(request, 'pages/home.html')
   return render(request, 'pages/home.html',{'form':HSDLForm})


@login_required(login_url='/dangNhap')
def modify_HSDL(request):
    if request.method=='POST':
        form = HSDLForm(request.POST,instance=HoSoDL)
        if form.is_valid():
            HoSoDL.tendaily=form['tendaily'].value()
            HoSoDL.mahosodaily=form['mahosodaily'].value()
            HoSoDL.dienthoai=form['dienthoai'].value()
            HoSoDL.diachi=form['diachi'].value()
            HoSoDL.quan=form['loaidaily'].value()
            HoSoDL.save()
            return render(request,'pages/HSDL.html',{'HSDLForms':form})
        return redirect('/hosodl')


@login_required(login_url='/dangNhap')
# XÓA DỮ LIỆU HSDL
def delete_HSDL(request, mahosodaily):
    dl = get_object_or_404(HoSoDL, pk=mahosodaily)
    dl.active = False
    dl.save()
    return redirect('/manage_HoSoDaiLy/')



@login_required(login_url='/dangNhap')
# SHOW DỮ LIỆU
def manage_HoSoDaiLy(request):
    daily=HoSoDL.objects.all()
    for i in daily:
        print(i.active)
    return render(request,'pages/QuanLyCacDaiLy.html',{'daily': daily})



@login_required(login_url='/dangNhap')
def manage_PhieuXuatHang(request):
    phieuXuatHang=PhieuXuatHang.objects.all()
    for i in phieuXuatHang:
        print(i.active1)
    return render(request,'pages/QuanLyPhieuXuatHang.html',{'phieuXuatHang':phieuXuatHang})


@login_required(login_url='/dangNhap')
def manage_MatHang(request):
    mh=MatHang.objects.all()
    for i in mh:
        print(i.active2)
    return render(request,'pages/QuanLyMatHang.html',{'matHang':mh})


@login_required(login_url='/dangNhap')
def manage_PhieuThuTien(request):
    ptt=Post.objects.all()
    for i in ptt:
        print(i.active3)
    return  render(request,'pages/QuanLyPhieuThuTien.html',{'phieuThuTien':ptt})




@login_required(login_url='/dangNhap')
# MẶT HÀNG
def create_MH(request):
    mhForm=MatHangForm()
    return render(request,'pages/MatHang.html',{'MHForms':mhForm})

@login_required(login_url='/dangNhap')
def SaveMH(request):
    if request.method=='POST':
        form=MatHangForm(request.POST)
        if form.is_valid():
            result=form.save()
            if request.method == 'POST':
                respone = HttpResponse()
                respone.write('Mã Mặt Hàng :' + request.POST['mamathang'] + '</br>')
                respone.write('Tên Mặt Hàng :' + request.POST['tenmathang'] + '</br>')
                respone.write('giá :' + request.POST['gia'] + '</br>')
                respone.write('Mã Đơn Vị Tính :' + request.POST['madonvi'] + '</br>')
                respone.write('Số Lượng :' + request.POST['soluong'] + '</br>')
                return respone
            return render(request, 'pages/home.html')
        return render(request,'pages/home.html',{"MHForm":MatHangForm})


@login_required(login_url='/dangNhap')
def modify_MH(request):
    if request.method=='POST':
        form = MatHangForm(request.POST,instance=MatHang)
        if form.is_valid():
            MatHang.mamathang=form['mamathang'].value()
            MatHang.tenmathang=form['tenmathang'].value()
            MatHang.gia=form['gia'].value()
            MatHang.madonvi=form['madonvi'].value()
            MatHang.soluong=form['soluong'].value()
            MatHang.save()
            return render(request,'pages/MatHang.html',{'MHForms':form})
        return redirect('/matHang')


@login_required(login_url='/dangNhap')
# XÓA DỮ LIỆU MẶT HÀNG
def delete_MH(request,mamathang):
    mh = get_object_or_404(MatHang, pk=mamathang)
    mh.active = False
    mh.save()
    return redirect('/manage_HoSoDaiLy/')



@login_required(login_url='/dangNhap')
# ĐƠN VỊ TÍNH
def create_DVT(request):
    dvtForm = DonVTForm()
    return render(request, 'pages/DonVT.html', {'DVTForm': dvtForm})


@login_required(login_url='/dangNhap')
def SaveDVT(request):
    if request.method=='POST':
        form=DonVTForm(request.POST)
        if form.is_valid():
            result=form.save()
            if request.method == 'POST':
                respone = HttpResponse()
                respone.write('Mã Đơn Vị Tính :' + request.POST['madonvitinh'] + '</br>')
                respone.write('Tên Đơn Vị Tính :' + request.POST['tendonvitinh'] + '</br>')
                return respone
            return render(request, 'pages/home.html')
        return render(request,'pages/home.html',{"DVTForm":DonVTForm})



@login_required(login_url='/dangNhap')
# QUẬN
def create_Quan(request):
    quanForm=QuanForm()
    return  render(request,'pages/Quan.html',{'QuanForm':quanForm})

@login_required(login_url='/dangNhap')
def SaveQuan(request):
    if request.method=='POST':
        form=QuanForm(request.POST)
        if form.is_valid():
            result=form.save()
            if request.method == 'POST':
                respone = HttpResponse()
                respone.write('Mã Quận : ' + request.POST['maquan'] + '</br>')
                respone.write('Tên Quận : ' + request.POST['tenquan'] + '</br>')
                return respone
            return render(request, 'pages/home.html')
        return render(request,'pages/home.html',{"QuanForm":QuanForm})




@login_required(login_url='/dangNhap')
# LOẠI ĐẠI LÝ
def create_LoaiDL(request):
    loaidlForm=LoaiDLForm()
    return  render(request,'pages/LoaiDL.html',{'LoaiDLForm':loaidlForm})

@login_required(login_url='/dangNhap')
def SaveLoaiDL(request):
    if request.method=='POST':
        form=LoaiDLForm(request.POST)
        if form.is_valid():
            result=form.save()
            if request.method == 'POST':
                respone = HttpResponse()
                respone.write('Mã Loại Đại Lý : ' + request.POST['maloaidaily'] + '</br>')
                respone.write('Tên Loại Đại Lý : ' + request.POST['tenloaidaily'] + '</br>')
                return respone
            return render(request, 'pages/home.html')
        return render(request,'pages/home.html',{"LoaiDLForm":LoaiDLForm})




@login_required(login_url='/dangNhap')
# CHI TIẾT PHIẾU XUẤT HÀNG
def create_CTPXH(request):
    ctpxhForm=CTPhieuXuatHangForm()
    return  render(request,'pages/CTPXH.html',{'CTPXHForm':CTPhieuXuatHangForm})

@login_required(login_url='/dangNhap')
def SaveCTPXH(request):
    if request.method=='POST':
        form=CTPhieuXuatHangForm(request.POST)
        if form.is_valid():
            result=form.save()
            if request.method == 'POST':
                respone = HttpResponse()
                respone.write('Mã Chi Tiết Phiếu Xuất Hàng : ' + request.POST['machitietphieuxuathang'] + '</br>')
                respone.write('Mã Hồ Sơ Đại Lý : ' + request.POST['mahosodaily'] + '</br>')
                respone.write('Mã Mặt Hàng : ' + request.POST['mamathang'] + '</br>')
                respone.write('Mã Đơn Vị Tính : ' + request.POST['madonvitinh'] + '</br>')
                respone.write('Số Lượng : ' + request.POST['soluong'] + '</br>')
                respone.write('Đơn Gía : ' + request.POST['dongia'] + '</br>')
                respone.write('Thành Tiền : ' + request.POST['thanhtien'] + '</br>')
                return respone
            return render(request, 'pages/home.html')
        return render(request,'pages/home.html',{"CTPXHForm":CTPhieuXuatHangForm})




@login_required(login_url='/dangNhap')
# PHIẾU XUẤT HÀNG
def create_PXH(request):
    pxhForm=PhieuXuatHangForm()
    return  render(request,'pages/PhieuXuatHang.html',{'PXHForm':PhieuXuatHangForm})


@login_required(login_url='/dangNhap')
def SavePXH(request):
    if request.method=='POST':
        form=PhieuXuatHangForm(request.POST)
        if form.is_valid():
            result=form.save()
            if request.method == 'POST':
                respone = HttpResponse()
                respone.write('Mã Phiếu Xuất Hàng : '+ request.POST['maphieuxuathang'] + '</br>')
                #respone.write('Mã Chi Tiết Phiếu Xuất Hàng : ' + request.POST['machitietphieuxuathang'] + '</br>')
                respone.write('Tổng Tiền : ' + request.POST['tongtien'] + '</br>')
                respone.write('Số Tiền Trả : ' + request.POST['sotientra'] + '</br>')
                respone.write('Mã Đại Lý : ' + request.POST['madaily'] + '</br>')
                return respone
            return render(request, 'pages/home.html')
        return render(request,'pages/home.html',{"PXHForm":PhieuXuatHangForm})



@login_required(login_url='/dangNhap')
def modify_PXH(request):
    if request.method=='POST':
        form = PhieuXuatHangForm(request.POST,instance=PhieuXuatHang)
        if form.is_valid():
            PhieuXuatHang.maphieuxuathang=form['maphieuxuathang'].value()
            #PhieuXuatHang.machitietphieuxuathang=form['machitietphieuxuathang'].value()
            #PhieuXuatHang.maphieuthutien=form['maphieuthutien'].value()
            PhieuXuatHang.tongtien=form['tongtien'].value()
            PhieuXuatHang.sotientra=form['sotientra'].value()
            PhieuXuatHang.madaily=form['madaily'].value()
            PhieuXuatHang.save()
            return render(request,'pages/PhieuXuatHang.html',{'PXHForms':form})
        return redirect('/phieuXuatHang')


@login_required(login_url='/dangNhap')
# XÓA DỮ LIỆU PHIẾU XUẤT HÀNG
def delete_PXH(request, maphieuxuathang):
    pxh = get_object_or_404(PhieuXuatHang, pk=maphieuxuathang)
    pxh.active = False
    pxh.save()
    return redirect('/manage_MatHang/')



def sigin(request):
    if request.method=='POST':
        form =AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            # if user is not None and user.is_superuser is False:
            #     login(request,user)
            #     return redirect('/home')
            # elif user and user.is_staff and user.is_superuser is False:
            login(request,user)
            return redirect('/home')
    form=AuthenticationForm()
    return render(request=request,template_name='pages/dangNhap.html',context={'form':form})


def sigout(request):
    logout(request)
    return  redirect('/')


class UserAddress(object):
    pass


class UserProfile(object):
    pass


def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.saveData()
            username=form.cleaned_data.get('username')
            user=User.objects.get(username=username)
            raw_password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=raw_password)
            return redirect('/home')
        return redirect('/dangKy')
    else:
        form=RegisterForm()
        return  render(request,'pages/dangKy.html',{'form':form})

