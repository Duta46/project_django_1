-- Skrip SQL untuk membuat database dan tabel untuk aplikasi Django

-- Membuat database
CREATE DATABASE IF NOT EXISTS django_fastprint;

-- Menggunakan database
USE django_fastprint;

-- Membuat tabel kategori
CREATE TABLE IF NOT EXISTS produk_kategori (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_kategori VARCHAR(100) NOT NULL,
    created_at DATETIME NULL,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL
);

-- Membuat tabel status
CREATE TABLE IF NOT EXISTS produk_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_status VARCHAR(100) NOT NULL,
    created_at DATETIME NULL,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL
);

-- Membuat tabel produk
CREATE TABLE IF NOT EXISTS produk_produk (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_produk VARCHAR(100) NOT NULL,
    harga INT NOT NULL,
    kategori_id INT NOT NULL,
    status_id INT NOT NULL,
    created_at DATETIME NULL,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL,
    FOREIGN KEY (kategori_id) REFERENCES produk_kategori(id),
    FOREIGN KEY (status_id) REFERENCES produk_status(id)
);