from django.shortcuts import render
from django.shortcuts import render
from .models import BarangWishlist

def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Alya Azhar Agharid'
    }
    return render(request, "wishlist.html", context)