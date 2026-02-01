from django.db import models
from django.utils import timezone

class BaseTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Kategori(BaseTimestampModel):
    nama_kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kategori

class Status(BaseTimestampModel):
    nama_status = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_status

class Produk(BaseTimestampModel):
    nama_produk = models.CharField(max_length=255)  # Increased max_length to accommodate longer product names
    harga = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_produk