# Petunjuk Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi Django ini:

## 1. Siapkan Lingkungan
Pastikan Anda memiliki Python 3.x terinstal di sistem Anda.

## 2. Buat dan Aktifkan Virtual Environment
```bash
python -m venv venv
# Untuk Windows
venv\Scripts\activate
# Untuk Linux/Mac
source venv/bin/activate
```

## 3. Instal Dependensi
```bash
pip install -r requirements.txt
```

## 4. Siapkan Database MySQL
- Pastikan MySQL server berjalan
- Jalankan skrip setup_mysql.bat untuk membuat database
- Atau buat database secara manual: `CREATE DATABASE django_fastprint;`

## 5. Lakukan Migrasi Database
```bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Jalankan Aplikasi
```bash
python manage.py runserver
```

## 7. Akses Aplikasi
Buka browser dan kunjungi: http://127.0.0.1:8000/

## 8. (Opsional) Buat Superuser untuk Admin
```bash
python manage.py createsuperuser
```

Setelah itu, Anda bisa mengakses halaman admin di http://127.0.0.1:8000/admin/