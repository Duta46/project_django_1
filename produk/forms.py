from django import forms
from .models import Produk, Kategori, Status

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']
        widgets = {
            'nama_produk': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama produk'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan harga'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Pilih Kategori')]),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Pilih Status')])
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate choices for kategori and status from the database
        self.fields['kategori'].choices = [('', 'Pilih Kategori')] + [(kategori.id, kategori.nama_kategori) for kategori in Kategori.objects.all()]
        self.fields['status'].choices = [('', 'Pilih Status')] + [(status.id, status.nama_status) for status in Status.objects.all()]

    def clean_nama_produk(self):
        nama_produk = self.cleaned_data.get('nama_produk')
        if not nama_produk or not nama_produk.strip():
            raise forms.ValidationError("Nama produk harus diisi")
        return nama_produk

    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        if harga is None or harga < 0:
            raise forms.ValidationError("Harga harus berupa angka positif")
        return harga