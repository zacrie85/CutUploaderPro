@echo off
chcp 65001 >nul
title CutUploader Pro - Launcher
cd /d "%~dp0"

echo ============================================
echo   CUTUPLOADER PRO - Menyiapkan aplikasi...
echo ============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python belum terinstall di PC ini.
    echo.
    echo Silakan install Python dulu:
    echo   1. Buka https://www.python.org/downloads/
    echo   2. Download dan install
    echo   3. PENTING: centang "Add Python to PATH" saat install!
    echo.
    pause
    exit /b 1
)

echo Memeriksa library pynput...
python -c "import pynput" >nul 2>nul
if errorlevel 1 (
    echo Library pynput belum ada. Menginstall otomatis...
    python -m pip install --upgrade pynput
    if errorlevel 1 (
        echo.
        echo [ERROR] Gagal memasang pynput.
        echo Coba manual di CMD:  pip install pynput
        echo.
        pause
        exit /b 1
    )
)

echo Memeriksa library pillow + opencv (untuk pencarian gambar negara)...
python -c "import PIL" >nul 2>nul
if errorlevel 1 (
    python -m pip install --quiet pillow
)
python -c "import cv2" >nul 2>nul
if errorlevel 1 (
    echo Ini butuh unduhan cukup besar, mohon tunggu...
    python -m pip install --quiet opencv-python
    if errorlevel 1 (
        echo.
        echo [PERINGATAN] opencv-python gagal dipasang.
        echo Pencarian gambar negara tidak bisa dipakai - aplikasi
        echo tetap jalan dengan KLIK BIASA di titik C.
        echo Coba manual di CMD:  pip install opencv-python
        echo.
    )
)

echo Memeriksa library pyinstaller (untuk build EXE, opsional)...
python -c "import PyInstaller" >nul 2>nul
if errorlevel 1 (
    python -m pip install --quiet pyinstaller
)

echo.
echo Semua siap! Membuka CutUploader Pro...
echo (Tutup jendela hitam ini untuk mematikan aplikasi)
echo.
python cut_uploader.py
if errorlevel 1 (
    echo.
    echo [ERROR] Aplikasi gagal dibuka. Screenshot pesan error ini
    echo dan laporkan ke yang membuat aplikasi.
    pause
)
