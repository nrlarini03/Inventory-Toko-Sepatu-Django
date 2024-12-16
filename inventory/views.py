from django.shortcuts import render, redirect
from .models import Product, Supplier, Kategori
from .forms import ProductForm, SupplierForm, KategoriForm

def index(request):
    return render(request, 'index.html')
    
def home(request):
    products = Product.objects.all()
    return render(request, 'inventory/home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def update_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/update_product.html', {'form': form})

def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'inventory/delete_product.html', {'product': product})

# Supplier
def daftar_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/daftar_supplier.html', {'suppliers': suppliers})

def tambah_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_supplier')
    else:
        form = SupplierForm()
    return render(request, 'inventory/tambah_supplier.html', {'form': form})

def edit_supplier(request, id):
    supplier = Supplier.objects.get(id=id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('daftar_supplier')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'inventory/edit_supplier.html', {'form': form})

def hapus_supplier(request, id):
    supplier = Supplier.objects.get(id=id)
    supplier.delete()
    return redirect('daftar_supplier')


# Kategori
def daftar_kategori(request):
    kategoris = Kategori.objects.all()
    return render(request, 'inventory/daftar_kategori.html', {'kategoris': kategoris})

def tambah_kategori(request):
    if request.method == 'POST':
        form = KategoriForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_kategori')  
    else:
        form = KategoriForm()

    return render(request, 'inventory/tambah_kategori.html', {'form': form})

def edit_kategori(request, id):
    kategori = Kategori.objects.get(id=id)
    if request.method == 'POST':
        form = KategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            return redirect('daftar_kategori')
    else:
        form = KategoriForm(instance=kategori)
    return render(request, 'inventory/edit_kategori.html', {'form': form})

def hapus_kategori(request, id):
    kategori = Kategori.objects.get(id=id)
    kategori.delete()
    return redirect('daftar_kategori')