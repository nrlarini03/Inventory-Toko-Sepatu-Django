from django import forms
from .models import Product, Supplier, Kategori

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brand', 'size', 'color', 'price']

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama_kategori']
        widgets = {
            'nama_kategori': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['nama_supplier', 'alamat', 'nomor_telepon']
        widgets = {
            'nama_supplier': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nomor_telepon': forms.TextInput(attrs={'class': 'form-control'}),
        }