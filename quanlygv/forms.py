from django import forms
from .models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['tai_khoan', 'mat_khau', 'ho_va_ten', 'dia_chi', 'sdt', 'anh']
        labels = {
            'tai_khoan': 'Tài khoản',
            'mat_khau': 'Mật khẩu',
            'ho_va_ten': 'Họ và tên',
            'dia_chi': 'Địa chỉ',
            'sdt': 'Số điện thoại',
            'anh': 'Ảnh',
        }
        widgets = {
            'tai_khoan': forms.TextInput(attrs={'class': 'form-control'}),
            'mat_khau': forms.TextInput(attrs={'class': 'form-control'}),
            'ho_va_ten': forms.TextInput(attrs={'class': 'form-control'}),
            'dia_chi': forms.TextInput(attrs={'class': 'form-control'}),
            'sdt': forms.TextInput(attrs={'class': 'form-control'}),
            'anh': forms.TextInput(attrs={'class': 'form-control'}),
        }


class KhoaForm(forms.ModelForm):
    class Meta:
        model = Khoa
        fields = ['ma_khoa', 'ten_khoa']
        labels = {
            'ma_khoa': 'Mã khoa',
            'ten_khoa': 'Tên khoa',
        }
        widgets = {
            'ma_khoa': forms.TextInput(attrs={'class': 'form-control'}),
            'ten_khoa': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MonhocForm(forms.ModelForm):
    class Meta:
        model = Monhoc
        fields = ['ma_mh', 'ten_mh', 'so_tc']
        labels = {
            'ma_mh': 'Mã môn học',
            'ten_mh': 'Tên môn học',
            'so_tc': 'Số tín chỉ'
        }
        widgets = {
            'ma_mh': forms.TextInput(attrs={'class': 'form-control'}),
            'ten_mh': forms.TextInput(attrs={'class': 'form-control'}),
            'so_tc': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class LophocForm(forms.ModelForm):
    class Meta:
        model = Lophoc
        fields = ['ma_lop', 'ten_lop', 'si_so', 'khoa']
        labels = {
            'ma_lop': 'Mã lớp học',
            'ten_lop': 'Tên lớp học',
            'si_so': 'Sĩ số',
            'khoa': 'Khoa'
        }
        widgets = {
            'ma_lop': forms.TextInput(attrs={'class': 'form-control'}),
            'ten_lop': forms.TextInput(attrs={'class': 'form-control'}),
            'si_so': forms.NumberInput(attrs={'class': 'form-control'}),
            'khoa': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GiangvienForm(forms.ModelForm):
    class Meta:
        model = Giangvien
        fields = ['ho_ten_gv', 'hoc_vi', 'chuyen_mon', 'chuc_vu', 'ngay_sinh', 'gioi_tinh', 'sdt', 'anh', 'khoa']
        labels = {
            'ho_ten_gv': 'Họ và tên',
            'hoc_vi': 'Học vị',
            'chuyen_mon': 'Chuyên môn',
            'chuc_vu': 'Chức vụ',
            'ngay_sinh': 'Ngày sinh',
            'gioi_tinh': 'Giới tính',
            'sdt': 'Số điện thoại',
            'anh': 'Ảnh',
            'khoa': 'Khoa',
        }
        widgets = {
            'ho_ten_gv': forms.TextInput(attrs={'class': 'form-control'}),
            'hoc_vi': forms.TextInput(attrs={'class': 'form-control'}),
            'chuyen_mon': forms.TextInput(attrs={'class': 'form-control'}),
            'chuc_vu': forms.TextInput(attrs={'class': 'form-control'}),
            'ngay_sinh': forms.TextInput(attrs={'class': 'form-control'}),
            'gioi_tinh': forms.TextInput(attrs={'class': 'form-control'}),
            'sdt': forms.TextInput(attrs={'class': 'form-control'}),
            'anh': forms.TextInput(attrs={'class': 'form-control'}),
            'khoa': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TaikhoangvForm(forms.ModelForm):
    class Meta:
        model = Taikhoangv
        fields = ['tai_khoan', 'mat_khau', 'giangvien']
        labels = {
            'tai_khoan': 'Tài khoản',
            'mat_khau': 'Mật khẩu',
            'giangvien': 'Giảng viên'
        }
        widgets = {
            'tai_khoan': forms.TextInput(attrs={'class': 'form-control'}),
            'mat_khau': forms.TextInput(attrs={'class': 'form-control'}),
            'giangvien': forms.TextInput(attrs={'class': 'form-control'})
        }


class PhanconggvForm(forms.ModelForm):
    class Meta:
        model = Phanconggv
        fields = ['lophoc', 'giangvien', 'monhoc', 'ngay_bd', 'ngay_kt', 'trang_thai']
        labels = {
            'lophoc': 'Lớp học',
            'giangvien': 'Giảng viên',
            'monhoc': 'Môn học',
            'ngay_bd': 'Ngày bắt đầu',
            'ngay_kt': 'Ngày kết thúc',
            'trang_thai': 'Trạng thái',
        }
        widgets = {
            'lophoc': forms.TextInput(attrs={'class': 'form-control'}),
            'giangvien': forms.TextInput(attrs={'class': 'form-control'}),
            'monhoc': forms.TextInput(attrs={'class': 'form-control'}),
            'ngay_bd': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ngay_kt': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trang_thai': forms.TextInput(attrs={'class': 'form-control'}),
        }