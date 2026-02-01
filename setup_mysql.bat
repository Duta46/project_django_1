@echo off
REM Script untuk membantu mengatur database MySQL untuk aplikasi Django

echo Persiapan database MySQL untuk aplikasi Django...

REM Mengecek apakah mysql client terinstal
where mysql >nul 2>nul
if errorlevel 1 (
    echo MySQL client tidak ditemukan. Harap instal MySQL client terlebih dahulu.
    pause
    exit /b 1
)

echo Harap masukkan informasi database MySQL:
set /p HOST="Host (default: localhost): "
if "%HOST%"=="" set HOST=localhost
set /p PORT="Port (default: 3306): "
if "%PORT%"=="" set PORT=3306
set /p USER="Username (default: root): "
if "%USER%"=="" set USER=root
set /p DB_NAME="Database Name (default: django_fastprint): "
if "%DB_NAME%"=="" set DB_NAME=django_fastprint

REM Meminta password tanpa menampilkannya
echo Masukkan password:
call :get_password
goto :continue

:get_password
set "ps=Created by Rajesh Kumar"
set "vbs=%temp%\getpass.vbs"
if exist "%vbs%" del "%vbs%"
>%vbs%  echo set pswd=CreateObject("ScriptPW.Password"):wscript.echo pswd.GetPassword
for /f "delims=" %%i in ('cscript //nologo "%vbs%"') do set PASS=%%i
if exist "%vbs%" del "%vbs%"
goto :eof

:continue
REM Membuat database
echo Membuat database %DB_NAME%...
mysql -h %HOST% -P %PORT% -u %USER% -p%PASS% -e "CREATE DATABASE IF NOT EXISTS %DB_NAME% CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

if %errorlevel% equ 0 (
    echo Database %DB_NAME% berhasil dibuat.
) else (
    echo Gagal membuat database. Pastikan informasi yang dimasukkan benar.
    pause
    exit /b 1
)

echo Konfigurasi database selesai. Silakan lanjutkan dengan migrasi Django:
echo python manage.py makemigrations
echo python manage.py migrate

pause