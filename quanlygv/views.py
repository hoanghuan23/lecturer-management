from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
from django.db.models import Q
from django.http import HttpResponseNotAllowed
import os
from django.conf import settings

def set_session_variables(request, user, user_type):
    if user_type == 'admin':
        request.session['admin_id'] = user.id
        request.session['tai_khoan'] = user.tai_khoan
        request.session['mat_khau'] = user.mat_khau
        request.session['ho_va_ten'] = user.ho_va_ten
        request.session['dia_chi'] = user.dia_chi
        request.session['sdt'] = user.sdt
        request.session['anh'] = user.anh
    elif user_type == 'taikhoangv':
        request.session['taikhoangv_id'] = user.id
        request.session['taikhoangv_tai_khoan'] = user.tai_khoan
        request.session['taikhoangv_mat_khau'] = user.mat_khau
        request.session['taikhoangv_giangvien_id'] = user.giangvien.id
        request.session['taikhoangv_giangvien_ho_ten_gv'] = user.giangvien.ho_ten_gv
        request.session['taikhoangv_giangvien_hoc_vi'] = user.giangvien.hoc_vi
        request.session['taikhoangv_giangvien_chuyen_mon'] = user.giangvien.chuyen_mon
        request.session['taikhoangv_giangvien_chuc_vu'] = user.giangvien.chuc_vu
        request.session['taikhoangv_giangvien_ngay_sinh'] = user.giangvien.ngay_sinh
        request.session['taikhoangv_giangvien_gioi_tinh'] = user.giangvien.gioi_tinh
        request.session['taikhoangv_giangvien_sdt'] = user.giangvien.sdt
        request.session['taikhoangv_giangvien_anh'] = user.giangvien.anh
        request.session['taikhoangv_giangvien_khoa_ten_khoa'] = user.giangvien.khoa.ten_khoa

# Đăng nhập
def dang_nhap(request):
    mess = True
    if request.method == 'POST':
        tai_khoan = request.POST.get('tai_khoan')
        mat_khau = request.POST.get('mat_khau')
        try:
            admin = Admin.objects.get(tai_khoan=tai_khoan, mat_khau=mat_khau)
            set_session_variables(request, admin, 'admin')
            return redirect('trangchu')
        except Admin.DoesNotExist:
            mess = False
            try:
                taikhoangv = Taikhoangv.objects.get(tai_khoan=tai_khoan, mat_khau=mat_khau)
                set_session_variables(request, taikhoangv, 'taikhoangv')
                return redirect('trangchugiangvien')
            except Taikhoangv.DoesNotExist:
                mess = False

    return render(request, 'login.html', {'mess': mess})

def dang_xuat(request):
    if 'admin_id' in request.session:
        del request.session['admin_id']
    if 'tai_khoan' in request.session:
        del request.session['tai_khoan']
    if 'ho_va_ten' in request.session:
        del request.session['ho_va_ten']
    if 'dia_chi' in request.session:
        del request.session['dia_chi']
    if 'sdt' in request.session:
        del request.session['sdt']
    if 'anh' in request.session:
        del request.session['anh']

    if 'taikhoangv_id' in request.session:
        del request.session['taikhoangv_id']
    if 'taikhoangv_tai_khoan' in request.session:
        del request.session['taikhoangv_tai_khoan']
    if 'taikhoangv_mat_khau' in request.session:
        del request.session['taikhoangv_mat_khau']
    if 'taikhoangv_giangvien_id' in request.session:
        del request.session['taikhoangv_giangvien_id']
    if 'taikhoangv_giangvien_ho_ten_gv' in request.session:
        del request.session['taikhoangv_giangvien_ho_ten_gv']
    if 'taikhoangv_giangvien_hoc_vi' in request.session:
        del request.session['taikhoangv_giangvien_hoc_vi']
    if 'taikhoangv_giangvien_chuyen_mon' in request.session:
        del request.session['taikhoangv_giangvien_chuyen_mon']
    if 'taikhoangv_giangvien_chuc_vu' in request.session:
        del request.session['taikhoangv_giangvien_chuc_vu']
    if 'taikhoangv_giangvien_ngay_sinh' in request.session:
        del request.session['taikhoangv_giangvien_ngay_sinh']
    if 'taikhoangv_giangvien_gioi_tinh' in request.session:
        del request.session['taikhoangv_giangvien_gioi_tinh']
    if 'taikhoangv_giangvien_sdt' in request.session:
        del request.session['taikhoangv_giangvien_sdt']
    if 'taikhoangv_giangvien_anh' in request.session:
        del request.session['taikhoangv_giangvien_anh']
    if 'taikhoangv_giangvien_khoa_ten_khoa' in request.session:
        del request.session['taikhoangv_giangvien_khoa_ten_khoa']
    return redirect('login')

# Trang chủ
def trangchu(request):
    all_khoa = Khoa.objects.all()
    khoa_count = all_khoa.count()

    all_lophoc = Lophoc.objects.all()
    lophoc_count = all_lophoc.count()

    all_giangvien = Giangvien.objects.all()
    giangvien_count = all_giangvien.count()

    all_monhoc = Monhoc.objects.all()
    monhoc_count = all_monhoc.count()
    return render(request, 'index.html',{
            'all_lophoc': all_lophoc,
            'all_monhoc': all_monhoc,

            'khoa_count': khoa_count,
            'lophoc_count': lophoc_count,
            'giangvien_count': giangvien_count,
            'monhoc_count': monhoc_count,
        })


# Khoa
def khoa(request):
    return render(request, 'khoa/khoa.html',{
        'all_khoa': Khoa.objects.all()
    })

def them_khoa(request):
  if request.method == 'POST':
    form = KhoaForm(request.POST)
    if form.is_valid():
      new_ma_khoa = form.cleaned_data['ma_khoa']
      new_ten_khoa = form.cleaned_data['ten_khoa']

      new_khoa = Khoa(
        ma_khoa = new_ma_khoa,
        ten_khoa = new_ten_khoa
      )
      new_khoa.save()
      return redirect('khoa')
  else:
    form = KhoaForm()
  return render(request, 'khoa/them_khoa.html', {
    'form': KhoaForm()
  })

def sua_khoa(request, id):
    khoa = get_object_or_404(Khoa, pk=id)
    if request.method == 'POST':
        ma_khoa_moi = request.POST.get('ma_khoa')
        ten_khoa_moi = request.POST.get('ten_khoa')

        khoa.ma_khoa = ma_khoa_moi
        khoa.ten_khoa = ten_khoa_moi
        khoa.save()
        return redirect('khoa')
    else:
        return render(request, 'khoa/sua_khoa.html', {'khoa': khoa})

def xoa_khoa(request):
    if request.method == 'GET':
        ma_khoa = request.GET.get('ma_khoa')
        khoa = get_object_or_404(Khoa, ma_khoa=ma_khoa)
        khoa.delete()
        return redirect('khoa')
    
def timkiem_khoa(request):
    query = request.GET.get('thongtin')
    khoa_list = Khoa.objects.filter(Q(ma_khoa__icontains=query) 
                                    | Q(ten_khoa__icontains=query))
    return render(request, 'khoa/khoa.html', {'all_khoa': khoa_list})


# Môn học
def monhoc(request):
    return render(request, 'monhoc/monhoc.html',{
        'all_monhoc': Monhoc.objects.all()
    })

def them_monhoc(request):
  if request.method == 'POST':
    form = MonhocForm(request.POST)
    if form.is_valid():
      new_ma_mh = form.cleaned_data['ma_mh']
      new_ten_mh = form.cleaned_data['ten_mh']
      new_so_tc = form.cleaned_data['so_tc']

      new_monhoc = Monhoc(
        ma_mh = new_ma_mh,
        ten_mh = new_ten_mh,
        so_tc = new_so_tc
      )
      new_monhoc.save()
      return redirect('monhoc')
  else:
    form = MonhocForm()
  return render(request, 'monhoc/them_monhoc.html', {
    'form': MonhocForm()
  })

def sua_monhoc(request, id):
    monhoc = get_object_or_404(Monhoc, pk=id)
    if request.method == 'POST':
        ma_mh_moi = request.POST.get('ma_mh')
        ten_mh_moi = request.POST.get('ten_mh')
        so_tc_moi = request.POST.get('so_tc')

        monhoc.ma_mh = ma_mh_moi
        monhoc.ten_mh = ten_mh_moi
        monhoc.so_tc = so_tc_moi
        monhoc.save()
        return redirect('monhoc')
    else:
        return render(request, 'monhoc/sua_monhoc.html', {'monhoc': monhoc})

def xoa_monhoc(request):
    if request.method == 'GET':
        ma_mh = request.GET.get('ma_mh')
        monhoc = get_object_or_404(Monhoc, ma_mh=ma_mh)
        monhoc.delete()
        return redirect('monhoc')

def timkiem_monhoc(request):
    query = request.GET.get('thongtin')
    monhoc_list = Monhoc.objects.filter(Q(ma_mh__icontains=query) 
                                        | Q(ten_mh__icontains=query ) 
                                        | Q(so_tc__icontains=query ))
    return render(request, 'monhoc/monhoc.html', {'all_monhoc': monhoc_list})


# Lớp học
def lophoc(request):
    return render(request, 'lophoc/lophoc.html',{
        'all_lophoc': Lophoc.objects.all()
    })

def them_lophoc(request):
  if request.method == 'POST':
    form = LophocForm(request.POST)
    if form.is_valid():
      new_ma_lop = form.cleaned_data['ma_lop']
      new_ten_lop = form.cleaned_data['ten_lop']
      new_si_so = form.cleaned_data['si_so']
      new_khoa = form.cleaned_data['khoa']

      new_lophoc = Lophoc(
        ma_lop = new_ma_lop,
        ten_lop = new_ten_lop,
        si_so = new_si_so,
        khoa = new_khoa
      )
      new_lophoc.save()
      return redirect('lophoc')
  else:
    form = LophocForm()
  return render(request, 'lophoc/them_lophoc.html', {
    'form': LophocForm(),
    'all_khoa': Khoa.objects.all()
  })

def sua_lophoc(request, id):
    lophoc = get_object_or_404(Lophoc, pk=id)
    if request.method == 'POST':
        ma_lop_moi = request.POST.get('ma_lop')
        ten_lop_moi = request.POST.get('ten_lop')
        si_so_moi = request.POST.get('si_so')
        khoa_moi = request.POST.get('khoa')
        khoa = get_object_or_404(Khoa, pk=khoa_moi)
        lophoc.khoa = khoa
        lophoc.ma_lop = ma_lop_moi
        lophoc.ten_lop = ten_lop_moi
        lophoc.si_so = si_so_moi
        lophoc.save()
        return redirect('lophoc')
    else:
        return render(request, 'lophoc/sua_lophoc.html', {
           'lophoc': lophoc,
           'all_khoa': Khoa.objects.all()
          })

def xoa_lophoc(request):
    ma_lop = request.GET.get('ma_lop')
    if ma_lop:
        lop_hoc = get_object_or_404(Lophoc, ma_lop=ma_lop)
        lop_hoc.delete()
        return redirect('lophoc')

def timkiem_lophoc(request):
    query = request.GET.get('thongtin')
    lophoc_list = Lophoc.objects.filter(Q(ma_lop__icontains=query) | 
                                        Q(ten_lop__icontains=query ) | 
                                        Q(si_so__icontains=query ))
    return render(request, 'lophoc/lophoc.html', {'all_lophoc': lophoc_list})


# Giảng viên
def giangvien(request):
    return render(request, 'giangvien/giangvien.html',{
        'all_giangvien': Giangvien.objects.all()
    })

def luu_anh(image_name, image_data):
    static_dir = os.path.join(settings.BASE_DIR, 'quanlygv', 'static', 'assets', 'images')
    if not os.path.exists(static_dir):
      os.makedirs(static_dir)
    image_path = os.path.join(static_dir, image_name)
    with open(image_path, 'wb') as f:
      f.write(image_data)
    return image_name 

def xoa_anh(image_name):
    static_dir = os.path.join(settings.BASE_DIR, 'quanlygv', 'static', 'assets', 'images')
    image_path = os.path.join(static_dir, image_name)
    if os.path.exists(image_path):
        os.remove(image_path)
        return f"Đã xóa ảnh {image_name}"
    else:
        return f"Không tìm thấy ảnh {image_name}"

def them_giangvien(request):
  if request.method == 'POST':
    form = GiangvienForm(request.POST, request.FILES)
    if form.is_valid():
      image_data = request.FILES['image'].read()
      new_ho_ten_gv = form.cleaned_data['ho_ten_gv']
      new_hoc_vi = form.cleaned_data['hoc_vi']
      new_chuyen_mon = form.cleaned_data['chuyen_mon']
      new_chuc_vu = form.cleaned_data['chuc_vu']
      new_ngay_sinh = form.cleaned_data['ngay_sinh']
      new_gioi_tinh = form.cleaned_data['gioi_tinh']
      new_sdt = form.cleaned_data['sdt']
      new_anh = form.cleaned_data['anh']
      new_khoa = form.cleaned_data['khoa']
      
      xoa_anh(new_anh)

      image_path = luu_anh(new_anh, image_data)

      new_giangvien = Giangvien(
        ho_ten_gv = new_ho_ten_gv, 
        hoc_vi = new_hoc_vi,
        chuyen_mon = new_chuyen_mon,
        chuc_vu = new_chuc_vu,
        ngay_sinh = new_ngay_sinh,
        gioi_tinh = new_gioi_tinh,
        sdt = new_sdt,
        anh = image_path,
        khoa = new_khoa,
      )
      new_giangvien.save()
      return redirect('giangvien')
  else:
    form = GiangvienForm()
  return render(request, 'giangvien/them_giangvien.html', {
    'form': GiangvienForm(),
    'all_khoa': Khoa.objects.all()
  })

def sua_giangvien(request, id):
    giangvien = get_object_or_404(Giangvien, pk=id)
    if request.method == 'POST':
        image_file = request.FILES.get('image') 
        ho_ten_gv_moi = request.POST.get('ho_ten_gv')
        hoc_vi_moi = request.POST.get('hoc_vi')
        chuyen_mon_moi = request.POST.get('chuyen_mon')
        chuc_vu_moi = request.POST.get('chuc_vu')
        ngay_sinh_moi = request.POST.get('ngay_sinh')
        gioi_tinh_moi = request.POST.get('gioi_tinh')
        sdt_moi = request.POST.get('sdt')
        khoa_moi = request.POST.get('khoa')
        anh_moi = request.POST.get('anh')
        if ngay_sinh_moi:
          parts = ngay_sinh_moi.split('-')
          ngay_sinh_moi = f"{parts[2]}/{parts[1]}/{parts[0]}"

        if anh_moi == giangvien.anh:
            khoa = get_object_or_404(Khoa, pk=khoa_moi)
            giangvien.khoa = khoa
            giangvien.ho_ten_gv = ho_ten_gv_moi
            giangvien.hoc_vi = hoc_vi_moi
            giangvien.chuyen_mon = chuyen_mon_moi
            giangvien.chuc_vu = chuc_vu_moi
            giangvien.ngay_sinh = ngay_sinh_moi
            giangvien.gioi_tinh = gioi_tinh_moi
            giangvien.sdt = sdt_moi
            giangvien.anh = anh_moi
            giangvien.save()
            return redirect('giangvien')
        else:
            if giangvien.anh:
                xoa_anh(giangvien.anh)
            if image_file:
                image_data = image_file.read() 
                image_path = luu_anh(anh_moi, image_data)
                giangvien.anh = image_path
        
            khoa = get_object_or_404(Khoa, pk=khoa_moi)
            giangvien.khoa = khoa
            giangvien.ho_ten_gv = ho_ten_gv_moi
            giangvien.hoc_vi = hoc_vi_moi
            giangvien.chuyen_mon = chuyen_mon_moi
            giangvien.chuc_vu = chuc_vu_moi
            giangvien.ngay_sinh = ngay_sinh_moi
            giangvien.gioi_tinh = gioi_tinh_moi
            giangvien.sdt = sdt_moi
            giangvien.anh = image_path
            giangvien.save()
            return redirect('giangvien')
    else:
        return render(request, 'giangvien/sua_giangvien.html', {
            'giangvien': giangvien,
            'all_khoa': Khoa.objects.all()
        })

def xoa_giangvien(request):
    id = request.GET.get('id')
    if id:
        giangvien = get_object_or_404(Giangvien, pk=id)
        xoa_anh(giangvien.anh)
        giangvien.delete()
        return redirect('giangvien')
    
def timkiem_giangvien(request):
    query = request.GET.get('thongtin')
    giangvien_list = Giangvien.objects.filter(Q(ho_ten_gv__icontains=query) | Q(hoc_vi__icontains=query ) | Q(chuyen_mon__icontains=query) | Q(chuc_vu__icontains=query) 
                                              | Q(ngay_sinh__icontains=query) | Q(gioi_tinh__icontains=query) | Q(sdt__icontains=query) | Q(khoa__ten_khoa__icontains=query))
    return render(request, 'giangvien/giangvien.html', {'all_giangvien': giangvien_list})


# Thông tin tài khoản và sửa
def thongtintk(request):
    if request.method == 'POST':
        admin_id = request.POST.get('admin_id')
        admin = get_object_or_404(Admin, pk=admin_id)

        image_file = request.FILES.get('image')  # Sử dụng get để tránh MultiValueDictKeyError
        ho_va_ten_moi = request.POST.get('ho_va_ten')
        sdt_moi = request.POST.get('sdt')
        dia_chi_moi = request.POST.get('dia_chi')
        tai_khoan_moi = request.POST.get('tai_khoan')
        mat_khau_moi = request.POST.get('mat_khau')
        anh_moi = request.POST.get('anh')

        if anh_moi == admin.anh:
            admin.ho_va_ten = ho_va_ten_moi
            admin.sdt = sdt_moi
            admin.dia_chi = dia_chi_moi
            admin.tai_khoan = tai_khoan_moi
            admin.mat_khau = mat_khau_moi
            admin.anh = anh_moi
            admin.save()
        else:
            if admin.anh:
                xoa_anh(admin.anh)
            if image_file:
                image_data = image_file.read()  # Đọc dữ liệu từ file dưới dạng bytes
                image_path = luu_anh(anh_moi, image_data)
                admin.anh = image_path

            admin.ho_va_ten = ho_va_ten_moi
            admin.sdt = sdt_moi
            admin.dia_chi = dia_chi_moi
            admin.tai_khoan = tai_khoan_moi
            admin.mat_khau = mat_khau_moi
            admin.save()
        
        request.session['admin_id'] = admin.id
        request.session['tai_khoan'] = admin.tai_khoan
        request.session['mat_khau'] = admin.mat_khau
        request.session['ho_va_ten'] = admin.ho_va_ten
        request.session['dia_chi'] = admin.dia_chi
        request.session['sdt'] = admin.sdt
        request.session['anh'] = admin.anh
        return redirect('trangchu')
    else:
        return render(request, 'thongtintk.html')


# Phân công giảng viên
def phanconggv(request):
  return render(request, 'phanconggv/phanconggv.html',{
      'all_phanconggv': Phanconggv.objects.all()
  })

def them_phanconggv(request):
    if request.method == 'POST':
        form = PhanconggvForm(request.POST)
        if form.is_valid():
            new_lophoc = form.cleaned_data['lophoc']
            new_giangvien = form.cleaned_data['giangvien']
            new_monhoc = form.cleaned_data['monhoc']
            new_ngay_bd = form.cleaned_data['ngay_bd']
            new_ngay_kt = form.cleaned_data['ngay_kt']
            new_trang_thai = form.cleaned_data['trang_thai']

            new_phanconggv = Phanconggv(
                lophoc=new_lophoc,
                giangvien=new_giangvien,
                monhoc=new_monhoc,
                ngay_bd=new_ngay_bd,
                ngay_kt=new_ngay_kt,
                trang_thai=new_trang_thai
            )
            new_phanconggv.save()
            return redirect('phanconggv')
        else:
            print(form.errors)  # In lỗi của form ra để debug
    else:
        form = PhanconggvForm()

    return render(request, 'phanconggv/them_phanconggv.html', {
        'form': form,
        'all_monhoc': Monhoc.objects.all(),
        'all_lophoc': Lophoc.objects.all(),
        'all_giangvien': Giangvien.objects.all()
    })

def xoa_phanconggv(request):
    id = request.GET.get('id')
    if id:
        phanconggv = get_object_or_404(Phanconggv, pk=id)
        phanconggv.delete()
        return redirect('phanconggv')
    
def sua_phanconggv(request, id):
    phanconggv = get_object_or_404(Phanconggv, pk=id)
    if request.method == 'POST':
        lophoc_moi = request.POST.get('lophoc')
        giangvien_moi = request.POST.get('giangvien')
        monhoc_moi = request.POST.get('monhoc')
        lophoc = get_object_or_404(Lophoc, pk=lophoc_moi)
        giangvien = get_object_or_404(Giangvien, pk=giangvien_moi)
        monhoc = get_object_or_404(Monhoc, pk=monhoc_moi)

        ngay_bd_moi = request.POST.get('ngay_bd')
        ngay_kt_moi = request.POST.get('ngay_kt')
        trang_thai_moi = request.POST.get('trang_thai')

        phanconggv.lophoc = lophoc
        phanconggv.giangvien = giangvien
        phanconggv.monhoc = monhoc
        phanconggv.ngay_bd = ngay_bd_moi
        phanconggv.ngay_kt = ngay_kt_moi
        phanconggv.trang_thai = trang_thai_moi
        phanconggv.save()
        return redirect('phanconggv')
    else:
        return render(request, 'phanconggv/sua_phanconggv.html', {
           'phanconggv': phanconggv,
           'all_monhoc': Monhoc.objects.all(),
           'all_lophoc': Lophoc.objects.all(),
           'all_giangvien': Giangvien.objects.all()
          })

def timkiem_phanconggv(request):
    query = request.GET.get('thongtin')
    phanconggv_list = Phanconggv.objects.filter(Q(trang_thai__icontains=query) | Q(lophoc__ma_lop__icontains=query) | Q(lophoc__ten_lop__icontains=query)
                                                | Q(giangvien__ho_ten_gv__icontains=query) | Q(monhoc__ten_mh__icontains=query) | Q(monhoc__ma_mh__icontains=query))
    return render(request, 'phanconggv/phanconggv.html', {'all_phanconggv': phanconggv_list})

def timkiemtheongay_phanconggv(request):
    query1 = request.GET.get('thongtin1')
    query2 = request.GET.get('thongtin2')
    
    if query1 and query2:
        phanconggv_list = Phanconggv.objects.filter(
            Q(ngay_bd__gte=query1) & Q(ngay_kt__lte=query2)
        )
    elif query1:
        phanconggv_list = Phanconggv.objects.filter(
            Q(ngay_bd__gte=query1)
        )
    elif query2:
        phanconggv_list = Phanconggv.objects.filter(
            Q(ngay_kt__lte=query2)
        )
    else:
        phanconggv_list = Phanconggv.objects.none()
    return render(request, 'phanconggv/phanconggv.html', {'all_phanconggv': phanconggv_list})



# Quản lý tài khoản giảng viên
def taikhoangv(request):
    return render(request, 'taikhoangv/taikhoangv.html',{
        'all_taikhoangv': Taikhoangv.objects.all()
    })

def them_taikhoangv(request):
    if request.method == 'POST':
        form = TaikhoangvForm(request.POST)
        if form.is_valid():
            new_giangvien = form.cleaned_data['giangvien']
            new_tai_khoan = form.cleaned_data['tai_khoan']
            new_mat_khau = form.cleaned_data['mat_khau']

            new_taikhoangv = Taikhoangv(
                giangvien=new_giangvien,
                tai_khoan=new_tai_khoan,
                mat_khau=new_mat_khau
            )
            new_taikhoangv.save()
            return redirect('taikhoangv')
        else:
            print(form.errors) 
    else:
        form = TaikhoangvForm()
    return render(request, 'taikhoangv/them_taikhoangv.html', {
        'form': form,
        'all_giangvien': Giangvien.objects.all()
    })

def sua_taikhoangv(request, id):
    taikhoangv = get_object_or_404(Taikhoangv, pk=id)
    if request.method == 'POST':
        giangvien_moi = request.POST.get('giangvien')
        giangvien = get_object_or_404(Giangvien, pk=giangvien_moi)

        tai_khoan_moi = request.POST.get('tai_khoan')
        mat_khau_moi = request.POST.get('mat_khau')

        taikhoangv.giangvien = giangvien
        taikhoangv.tai_khoan = tai_khoan_moi
        taikhoangv.mat_khau = mat_khau_moi
        taikhoangv.save()
        return redirect('taikhoangv')
    else:
        return render(request, 'taikhoangv/sua_taikhoangv.html', {
           'taikhoangv': taikhoangv,
           'all_giangvien': Giangvien.objects.all()
          })
    
def xoa_taikhoangv(request):
    id = request.GET.get('id')
    if id:
        taikhoangv = get_object_or_404(Taikhoangv, pk=id)
        taikhoangv.delete()
        return redirect('taikhoangv')
    

# Thống kê báo cáo
def thongkebaocao(request):
    all_khoa = Khoa.objects.all()  
    khoa_giangvien_count = []
    for khoa in all_khoa:
        giangvien_count = Giangvien.objects.filter(khoa=khoa).count()
        khoa_giangvien_count.append({
            'khoa': khoa,
            'giangvien_count': giangvien_count
        })
    
    khoa_lophoc_count = []
    for khoa in all_khoa:
        lophoc_count = Lophoc.objects.filter(khoa=khoa).count()
        khoa_lophoc_count.append({
            'khoa': khoa,
            'lophoc_count': lophoc_count
        })
    
    return render(request, 'thongkebaocao/thongkebaocao.html', {
        'khoa_giangvien_count': khoa_giangvien_count,
        'khoa_lophoc_count': khoa_lophoc_count
    })


# Giảng viên đăng nhập
def trangchugiangvien(request):
    all_giangvien = Giangvien.objects.all()
    giangvien_count = all_giangvien.count()

    # Lấy thông tin giảng viên từ session
    giangvien_khoa_ten_khoa = request.session.get('taikhoangv_giangvien_khoa_ten_khoa')
    
    # Khởi tạo giangvien_list_count với giá trị mặc định
    giangvien_list_count = 0
    
    # Kiểm tra xem tên khoa có trong session hay không
    if giangvien_khoa_ten_khoa:
        giangvien_list = Giangvien.objects.filter(khoa__ten_khoa=giangvien_khoa_ten_khoa)
        giangvien_list_count = giangvien_list.count()
    
    return render(request, 'giangvien_dangnhap/index.html', {
        'giangvien_list_count': giangvien_list_count,
        'giangvien_count': giangvien_count,
    })


def giangvienphanconggd(request):
    giangvien_id = request.session.get('taikhoangv_giangvien_id')
    if giangvien_id:
        # Tìm giảng viên theo ID
        giangvien = Giangvien.objects.filter(pk=giangvien_id).first()
        
        # Nếu tìm thấy giảng viên, lấy danh sách các môn học đang giảng dạy
        if giangvien:
            monhoc_list = Phanconggv.objects.filter(giangvien=giangvien)
        else:
            monhoc_list = []
    else:
        monhoc_list = []

    return render(request, 'giangvien_dangnhap/phanconggiangday.html', {
        'monhoc_list': monhoc_list
    })


def sua_ttgiangvien(request):
    giangvien_id = request.session.get('taikhoangv_giangvien_id')
    giangvien = get_object_or_404(Giangvien, pk=giangvien_id)
    giangvien_tk = get_object_or_404(Taikhoangv, pk=giangvien_id)
    if request.method == 'POST':

        image_file = request.FILES.get('image')  
        ho_ten_gv_moi = request.POST.get('ho_ten_gv')
        sdt_moi = request.POST.get('sdt')
        gioi_tinh_moi = request.POST.get('gioi_tinh')
        ngay_sinh_moi = request.POST.get('ngay_sinh')
        tai_khoan_moi = request.POST.get('tai_khoan')
        mat_khau_moi = request.POST.get('mat_khau')
        anh_moi = request.POST.get('anh')
        if ngay_sinh_moi:
          parts = ngay_sinh_moi.split('-')
          ngay_sinh_moi = f"{parts[2]}/{parts[1]}/{parts[0]}"

        if anh_moi == giangvien.anh:
            giangvien.ho_ten_gv = ho_ten_gv_moi
            giangvien.sdt = sdt_moi
            giangvien.ngay_sinh = ngay_sinh_moi
            giangvien.gioi_tinh = gioi_tinh_moi
            giangvien.anh = anh_moi
            
            giangvien_tk.tai_khoan = tai_khoan_moi
            giangvien_tk.mat_khau = mat_khau_moi
            giangvien.save()
            giangvien_tk.save()
        else:
            if giangvien.anh:
                xoa_anh(giangvien.anh)
            if image_file:
                image_data = image_file.read() 
                image_path = luu_anh(anh_moi, image_data)
                giangvien.anh = image_path

            giangvien.ho_ten_gv = ho_ten_gv_moi
            giangvien.sdt = sdt_moi
            giangvien.ngay_sinh = ngay_sinh_moi
            giangvien.gioi_tinh = gioi_tinh_moi
            giangvien.anh = anh_moi
            
            giangvien_tk.tai_khoan = tai_khoan_moi
            giangvien_tk.mat_khau = mat_khau_moi
            giangvien.save()
            giangvien_tk.save()
        
        request.session['taikhoangv_id'] = giangvien_tk.id
        request.session['taikhoangv_tai_khoan'] = giangvien_tk.tai_khoan
        request.session['taikhoangv_mat_khau'] = giangvien_tk.mat_khau
        request.session['taikhoangv_giangvien_id'] = giangvien_tk.giangvien.id
        request.session['taikhoangv_giangvien_ho_ten_gv'] = giangvien_tk.giangvien.ho_ten_gv
        request.session['taikhoangv_giangvien_hoc_vi'] = giangvien_tk.giangvien.hoc_vi
        request.session['taikhoangv_giangvien_chuyen_mon'] = giangvien_tk.giangvien.chuyen_mon
        request.session['taikhoangv_giangvien_chuc_vu'] = giangvien_tk.giangvien.chuc_vu
        request.session['taikhoangv_giangvien_ngay_sinh'] = giangvien_tk.giangvien.ngay_sinh
        request.session['taikhoangv_giangvien_gioi_tinh'] = giangvien_tk.giangvien.gioi_tinh
        request.session['taikhoangv_giangvien_sdt'] = giangvien_tk.giangvien.sdt
        request.session['taikhoangv_giangvien_anh'] = giangvien_tk.giangvien.anh
        request.session['taikhoangv_giangvien_khoa_ten_khoa'] = giangvien_tk.giangvien.khoa.ten_khoa
        return redirect('trangchugiangvien')
    else:
        return render(request, 'giangvien_dangnhap/thongtintaikhoan.html', {
            'giangvien': giangvien,
            'giangvientk': giangvien_tk
        })
