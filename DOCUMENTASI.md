# Aplikasi Django - Tes Programmer Junior

## Deskripsi
Aplikasi ini dibuat sebagai bagian dari tes programmer junior sesuai dengan spesifikasi yang diberikan. Aplikasi ini mengambil data dari API eksternal, menyimpannya dalam database lokal, dan menyediakan antarmuka untuk menampilkan, menambah, mengedit, dan menghapus data produk.

## Fitur Utama
1. Mengambil data dari API eksternal
2. Menyimpan data produk, kategori, dan status ke database lokal
3. Menampilkan produk dengan status "bisa dijual"
4. Fungsi CRUD (Create, Read, Update, Delete) untuk produk
5. Validasi form pada input nama produk dan harga
6. Konfirmasi sebelum menghapus produk

## Teknologi yang Digunakan
- Python 3.x
- Django 6.0.1
- Django REST Framework
- MySQL (database)
- Bootstrap 5 (frontend)
- Requests (untuk HTTP requests)

## Instalasi dan Konfigurasi

### Prasyarat
- Python 3.x
- MySQL Server
- Virtual Environment (disarankan)

### Langkah-langkah Instalasi

1. Clone atau unduh kode sumber aplikasi
2. Buat virtual environment:
   ```
   python -m venv venv
   ```
3. Aktifkan virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```
     source venv/bin/activate
     ```
4. Install dependensi:
   ```
   pip install djangorestframework requests mysqlclient
   ```
5. Pastikan MySQL server berjalan
6. Buat database dan tabel menggunakan skrip `create_tables.sql`
7. Konfigurasi database di `settings.py` (sudah dikonfigurasi untuk MySQL)
8. Lakukan migrasi database:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
9. Buat superuser (opsional):
   ```
   python manage.py createsuperuser
   ```
10. Jalankan server pengembangan:
   ```
   python manage.py runserver
   ```

## Penggunaan

### Sinkronisasi Data dari API
1. Kunjungi halaman utama aplikasi
2. Klik tombol "Sinkronisasi dari API" untuk mengambil data terbaru dari API eksternal

### Melihat Produk
- Produk yang ditampilkan adalah produk dengan status "bisa dijual"

### Menambah Produk
1. Klik tombol "Tambah Produk"
2. Isi formulir dengan informasi produk
3. Klik tombol "Tambah" untuk menyimpan

### Mengedit Produk
1. Di halaman daftar produk, klik tombol "Edit" pada produk yang ingin diubah
2. Perbarui informasi produk
3. Klik tombol "Edit" untuk menyimpan perubahan

### Menghapus Produk
1. Di halaman daftar produk, klik tombol "Hapus" pada produk yang ingin dihapus
2. Konfirmasi penghapusan pada dialog konfirmasi

## Validasi Form
- Nama produk harus diisi
- Harga harus berupa angka positif

## Struktur Proyek
```
project_django_1/          # Root direktori proyek
├── manage.py              # File manajemen Django
├── project_django_1/      # Direktori konfigurasi proyek utama
│   ├── __init__.py
│   ├── settings.py        # Konfigurasi aplikasi
│   ├── urls.py           # URL utama proyek
│   ├── wsgi.py
│   └── asgi.py
└── produk/               # Aplikasi produk
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py         # Definisi model database
    ├── views.py          # Logika bisnis aplikasi
    ├── forms.py          # Formulir Django
    ├── serializers.py    # Serialisasi data
    ├── urls.py           # URL untuk aplikasi produk
    └── templates/        # Template HTML
        └── produk/
            ├── list.html
            ├── form.html
            └── delete_confirmation.html
```

## API Eksternal
Aplikasi ini mengambil data dari API eksternal:
- URL: https://recruitment.fastprint.co.id/tes/api_tes_programmer
- Username: Dinamis berdasarkan tanggal (tesprogrammerDDMMYYC08)
- Password: MD5 dari "bisacoding-DD-MM-YY"

## Database Schema
Aplikasi ini menggunakan tiga tabel:
1. Produk
   - id_produk (primary key)
   - nama_produk
   - harga
   - kategori_id (foreign key)
   - status_id (foreign key)
2. Kategori
   - id_kategori (primary key)
   - nama_kategori
3. Status
   - id_status (primary key)
   - nama_status

## Catatan Penting
- Pastikan MySQL server berjalan sebelum menjalankan aplikasi
- Waktu server penting untuk pembuatan username dan password API
- Validasi dilakukan baik di sisi server maupun di form
- Konfirmasi diperlukan sebelum menghapus produk
- Gunakan skrip setup_mysql.bat untuk membuat database secara otomatis
- Pastikan database 'django_fastprint' telah dibuat sebelum menjalankan migrasi

## Troubleshooting
Jika mengalami masalah saat instalasi paket karena sertifikat SSL, gunakan perintah:
```
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org djangorestframework requests
```

## Penulis
Aplikasi ini dikembangkan sebagai bagian dari tes programmer junior.