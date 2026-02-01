# Aplikasi Django - Tes Programmer Junior

## Deskripsi Singkat
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
- SQLite (database)
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
7. Lakukan migrasi database:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
8. Jalankan server pengembangan:
   ```
   python manage.py runserver
   ```

## Penggunaan

### Sinkronisasi Data dari API
1. Kunjungi halaman utama aplikasi di http://127.0.0.1:8000/
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

## Catatan
- Aplikasi ini dikonfigurasi untuk menggunakan MySQL sebagai database
- Pastikan server MySQL berjalan sebelum menjalankan aplikasi
- Gunakan skrip `create_tables.sql` untuk membuat database dan tabel yang diperlukan
- Pastikan database 'django_fastprint' telah dibuat sebelum menjalankan migrasi