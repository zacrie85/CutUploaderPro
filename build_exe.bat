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

echo Memasang / memperbarui pyinstaller dan pynput...
python -m pip install --upgrade pyinstaller pynput
if errorlevel 1 (
    echo [ERROR] Gagal memasang pyinstaller.
    pause
    exit /b 1
)

echo.
echo Mulai membangun EXE (tunggu 1-3 menit)...
python -m PyInstaller --onefile --windowed --name CutUploaderPro ^
    --exclude-module matplotlib --exclude-module numpy ^
    --exclude-module PyQt5 --exclude-module PIL ^
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
echo   File EXE ada di folder: dist\CutUploaderPro.exe
echo   Boleh dipindah ke mana saja.
echo   Simpan bersama file ini agar mudah dicari.
echo ============================================
echo.
echo Catatan: ikon jendela hitam build boleh ditutup.
pause
