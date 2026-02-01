# Proses Migrasi Database untuk Aplikasi Django

## Penjelasan Migrasi

Django menggunakan sistem migrasi untuk membuat dan memperbarui struktur database sesuai dengan model-model yang didefinisikan dalam aplikasi. Proses ini terdiri dari dua tahap utama:

1. `makemigrations` - Membuat file migrasi berdasarkan perubahan pada model
2. `migrate` - Menerapkan file-file migrasi ke database

## Tahapan Migrasi untuk Aplikasi Ini

### 1. Membuat File Migrasi
Perintah ini akan memeriksa model-model dalam aplikasi dan membuat file-file migrasi jika ada perubahan:

```bash
python manage.py makemigrations
```

### 2. Menerapkan Migrasi ke Database
Perintah ini akan menerapkan file-file migrasi ke database yang telah dikonfigurasi:

```bash
python manage.py migrate
```

## Struktur Migrasi dalam Aplikasi Ini

Aplikasi ini memiliki model-model berikut yang akan dibuatkan migrasinya:

1. **Kategori** - Tabel untuk menyimpan kategori produk
2. **Status** - Tabel untuk menyimpan status produk
3. **Produk** - Tabel utama yang menyimpan informasi produk dengan relasi ke Kategori dan Status

## Catatan untuk MySQL

Saat menggunakan MySQL sebagai database, pastikan:

1. MySQL server sedang berjalan
2. Database 'django_fastprint' telah dibuat
3. Kredensial (username/password) di settings.py benar
4. Port dan host MySQL dikonfigurasi dengan benar

## Jika Muncul Error saat Migrasi

Beberapa error umum dan solusinya:

1. **OperationalError: (2002, "Can't connect to server")** - MySQL server tidak berjalan atau konfigurasi host/port salah
2. **Access denied for user** - Username atau password salah
3. **Unknown database** - Database yang dituju belum dibuat

## Verifikasi Migrasi

Setelah migrasi berhasil, Anda dapat memverifikasi bahwa tabel telah dibuat dengan perintah:

```bash
python manage.py dbshell
SHOW TABLES;
```

Ini akan menampilkan semua tabel yang telah dibuat oleh Django.