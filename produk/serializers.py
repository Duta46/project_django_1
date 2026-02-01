from rest_framework import serializers
from .models import Produk, Kategori, Status

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

    def validate_nama_produk(self, value):
        if not value.strip():
            raise serializers.ValidationError("Nama produk harus diisi")
        return value

    def validate_harga(self, value):
        if value is None or value < 0:
            raise serializers.ValidationError("Harga harus berupa angka positif")
        return value