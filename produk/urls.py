from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('sync-from-api/', views.sync_produk_from_api, name='sync_produk_from_api'),
    path('create/', views.produk_create, name='produk_create'),
    path('update/<int:pk>/', views.produk_update, name='produk_update'),
    path('delete/<int:pk>/', views.produk_delete, name='produk_delete'),
]