from django.contrib import admin
from .models import Produk, Kategori, Status

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_kategori', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('nama_kategori',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_status', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('nama_status',)

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_produk', 'harga', 'kategori', 'status', 'created_at', 'updated_at')
    list_filter = ('kategori', 'status', 'created_at')
    search_fields = ('nama_produk',)
    date_hierarchy = 'created_at'