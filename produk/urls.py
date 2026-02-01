from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('sync-from-api/', views.sync_produk_from_api, name='sync_produk_from_api'),
    path('create/', views.produk_create_get, name='produk_create_get'),      # GET: Tampilkan form create
    path('store/', views.produk_create_post, name='produk_store'),          # POST: Simpan produk baru
    path('edit/<int:pk>/', views.produk_edit_get, name='produk_edit_get'),  # GET: Tampilkan form edit
    path('update/<int:pk>/', views.produk_update_post, name='produk_update_post'),  # POST: Update produk
    path('delete/<int:pk>/', views.produk_delete, name='produk_delete'),
]