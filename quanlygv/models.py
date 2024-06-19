from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    tai_khoan = models.CharField(max_length=20)
    mat_khau = models.CharField(max_length=20)
    ho_va_ten = models.CharField(max_length=50)
    dia_chi = models.CharField(max_length=128)
    sdt = models.CharField(max_length=10)
    anh = models.CharField(max_length=255)

    def __str__(self):
        return self.ho_va_ten
    

class Khoa(models.Model):
    id = models.AutoField(primary_key=True)
    ma_khoa = models.CharField(max_length=20)
    ten_khoa = models.CharField(max_length=128)

    def __str__(self):
        return self.ten_khoa


class Monhoc(models.Model):
    id = models.AutoField(primary_key=True)
    ma_mh = models.CharField(max_length=20)
    ten_mh = models.CharField(max_length=128)
    so_tc = models.IntegerField()

    def __str__(self):
        return self.ten_mh


class Lophoc(models.Model):
    id = models.AutoField(primary_key=True)
    ma_lop = models.CharField(max_length=20)
    ten_lop = models.CharField(max_length=128)
    si_so = models.PositiveIntegerField()
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten_lop


class Giangvien(models.Model):
    id = models.AutoField(primary_key=True)
    ho_ten_gv = models.CharField(max_length=50)
    hoc_vi = models.CharField(max_length=128)
    chuyen_mon = models.CharField(max_length=128)
    chuc_vu = models.CharField(max_length=128)
    ngay_sinh = models.CharField(max_length=50)
    gioi_tinh = models.CharField(max_length=50)
    sdt = models.CharField(max_length=10)
    anh = models.CharField(max_length=255)
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.ho_ten_gv

class Taikhoangv(models.Model):
    id = models.AutoField(primary_key=True)
    tai_khoan = models.CharField(max_length=20)
    mat_khau = models.CharField(max_length=20)
    giangvien = models.ForeignKey(Giangvien, on_delete=models.CASCADE)
    
    
class Phanconggv(models.Model):
    lophoc = models.ForeignKey(Lophoc, on_delete=models.CASCADE)
    giangvien = models.ForeignKey(Giangvien, on_delete=models.CASCADE)
    monhoc = models.ForeignKey(Monhoc, on_delete=models.CASCADE)
    ngay_bd = models.DateField()
    ngay_kt = models.DateField()
    trang_thai = models.CharField(max_length=50)