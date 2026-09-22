@echo off
chcp 65001 >nul
title CutUploader Pro - Build EXE
cd /d "%~dp0"

echo ============================================
echo   CUTUPLOADER PRO - Membuat file .EXE
echo ============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python belum terinstall.
    echo Install Python dulu dan centang "Add Python to PATH".
    pause
    exit /b 1
)

echo Memasang / memperbarui pyinstaller + pynput + pillow + opencv...
echo (opencv-python ukurannya besar, tunggu sebentar)
python -m pip install --upgrade pyinstaller pynput pillow opencv-python
if errorlevel 1 (
    echo [ERROR] Gagal memasang library.
    pause
    exit /b 1
)

echo.
echo Mulai membangun EXE (tunggu 3-8 menit)...
echo PENTING: pillow + opencv IKUT dibungkus supaya fitur
echo "Pencarian Gambar" (langkah C) jalan di dalam EXE.
python -m PyInstaller --onefile --windowed --name CutUploaderPro ^
    --icon icon.ico ^
    --collect-all cv2 ^
    --hidden-import pynput.keyboard --hidden-import pynput.mouse ^
    cut_uploader.py

if errorlevel 1 (
    echo.
    echo [ERROR] Build gagal. Baca pesan error di atas.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   SELESAI!
echo   File EXE ada di: dist\CutUploaderPro.exe
echo   EXE ini sudah menyatukan semua library -
echo   bisa dipakai di PC lain TANPA install Python.
echo.
echo   Mau jadi INSTALLER (Setup.exe)? Jalankan
echo   BANGUN-INSTALLER.bat setelah ini.
echo ============================================
pause
