from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),

    # Supplier
    path('supplier/', views.daftar_supplier, name='daftar_supplier'),
    path('supplier/tambah/', views.tambah_supplier, name='tambah_supplier'),
    path('supplier/edit/<int:id>/', views.edit_supplier, name='edit_supplier'),
    path('supplier/hapus/<int:id>/', views.hapus_supplier, name='hapus_supplier'),

    # Kategori
    path('kategori/', views.daftar_kategori, name='daftar_kategori'),
    path('kategori/tambah/', views.tambah_kategori, name='tambah_kategori'),
    path('kategori/edit/<int:id>/', views.edit_kategori, name='edit_kategori'),
    path('kategori/hapus/<int:id>/', views.hapus_kategori, name='hapus_kategori'),
]