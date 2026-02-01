# Panduan Penggunaan MySQL untuk Aplikasi Django

## Persiapan Database MySQL

Sebelum menjalankan aplikasi Django dengan MySQL, Anda perlu melakukan beberapa persiapan:

### 1. Pastikan MySQL Server Berjalan
Pastikan layanan MySQL server sedang berjalan di sistem Anda.

### 2. Buat Database
Anda dapat membuat database secara otomatis menggunakan skrip `setup_mysql.bat` yang tersedia di root direktori proyek, atau secara manual:

```sql
CREATE DATABASE django_fastprint CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Konfigurasi Database
Pastikan konfigurasi database di `settings.py` sudah benar:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'django_fastprint',
        'USER': 'root',
        'PASSWORD': '',  # Sesuaikan dengan password MySQL Anda
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

### 4. Jalankan Migrasi
Setelah database dibuat, jalankan perintah migrasi:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Jalankan Aplikasi
Setelah migrasi berhasil, Anda dapat menjalankan aplikasi:

```bash
python manage.py runserver
```

## Solusi Masalah Umum

### Error Koneksi ke MySQL
- Pastikan MySQL server sedang berjalan
- Periksa kredensial (username, password) di `settings.py`
- Pastikan host dan port benar

### Error mysqlclient
Jika mengalami error saat instalasi mysqlclient, coba:
```bash
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org mysqlclient
```

### Tabel Sudah Ada
Jika Anda mendapatkan error bahwa tabel sudah ada, Anda bisa menggunakan skrip `create_tables.sql` untuk memastikan struktur tabel sesuai dengan model Django.