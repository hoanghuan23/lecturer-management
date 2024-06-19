from django.urls import path
from .import views

urlpatterns = [
    path('', views.dang_nhap, name='login'),
    path('', views.dang_xuat, name='logout'),
    path('trangchu/', views.trangchu, name='trangchu'),


    path('trangchugiangvien/', views.trangchugiangvien, name='trangchugiangvien'),
    path('giangvienphanconggd/', views.giangvienphanconggd, name='giangvienphanconggd'),
    path('giangvienthongtintk/', views.sua_ttgiangvien, name='giangvienthongtintk'),
    

    path('thongtintk/', views.thongtintk, name='thongtintk'),
 

    path('khoa/', views.khoa, name='khoa'),
    path('khoa/themkhoa/', views.them_khoa, name='themkhoa'),
    path('khoa/xoakhoa/', views.xoa_khoa, name='xoakhoa'),
    path('khoa/suakhoa/<int:id>/', views.sua_khoa, name='suakhoa'),
    path('khoa/timkiemkhoa/', views.timkiem_khoa, name='timkiemkhoa'),


    path('monhoc/', views.monhoc, name='monhoc'),
    path('monhoc/themmonhoc/', views.them_monhoc, name='themmonhoc'),
    path('monhoc/suamonhoc/<int:id>/', views.sua_monhoc, name='suamonhoc'),
    path('monhoc/xoamonhoc/', views.xoa_monhoc, name='xoamonhoc'),
    path('monhoc/timkiemmonhoc/', views.timkiem_monhoc, name='timkiemmonhoc'),


    path('lophoc/', views.lophoc, name='lophoc'),
    path('lophoc/themlophoc/', views.them_lophoc, name='themlophoc'),
    path('lophoc/sualophoc/<int:id>/', views.sua_lophoc, name='sualophoc'),
    path('lophoc/xoalophoc/', views.xoa_lophoc, name='xoalophoc'),
    path('lophoc/timkiemlophoc/', views.timkiem_lophoc, name='timkiemlophoc'),


    path('giangvien/', views.giangvien, name='giangvien'),
    path('giangvien/themgiangvien/', views.them_giangvien, name='themgiangvien'),
    path('giangvien/suagiangvien/<int:id>/', views.sua_giangvien, name='suagiangvien'),
    path('giangvien/xoagiangvien/', views.xoa_giangvien, name='xoagiangvien'),
    path('giangvien/timkiemgiangvien/', views.timkiem_giangvien, name='timkiemgiangvien'),


    path('phanconggv/', views.phanconggv, name='phanconggv'),
    path('phanconggv/themphanconggv/', views.them_phanconggv, name='themphanconggv'),
    path('phanconggv/xoaphanconggv/', views.xoa_phanconggv, name='xoaphanconggv'),
    path('phanconggv/suaphanconggv/<int:id>/', views.sua_phanconggv, name='suaphanconggv'),
    path('phanconggv/timkiemphanconggv/', views.timkiem_phanconggv, name='timkiemphanconggv'),
    path('phanconggv/timkiemtheongayphanconggv/', views.timkiemtheongay_phanconggv, name='timkiemtheongayphanconggv'),
    

    path('taikhoangv/', views.taikhoangv, name='taikhoangv'),
    path('taikhoangv/themtaikhoangv/', views.them_taikhoangv, name='themtaikhoangv'),
    path('taikhoangv/suataikhoangv/<int:id>/', views.sua_taikhoangv, name='suataikhoangv'),
    path('taikhoangv/xoataikhoangv/', views.xoa_taikhoangv, name='xoataikhoangv'),


    path('thongkebaocao/', views.thongkebaocao, name='thongkebaocao'),
]