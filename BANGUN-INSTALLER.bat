@echo off
chcp 65001 >nul
title CutUploader Pro - Build Installer (Setup.exe)
cd /d "%~dp0"

echo ============================================
echo   CUTUPLOADER PRO - Membuat INSTALLER
echo   Hasil akhir: dist\CutUploaderPro-Setup.exe
echo ============================================
echo.

set "ISCC=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"

if not exist "%ISCC%" (
    echo [ERROR] Inno Setup 6 belum terinstall di PC ini.
    echo.
    echo Cara mendapatkan:
    echo   1. Buka https://jrsoftware.org/isdl.php
    echo   2. Download "innosetup-6.x.x.exe" lalu install
    echo   3. Jalankan lagi BANGUN-INSTALLER.bat ini
    echo.
    pause
    exit /b 1
)

if not exist "dist\CutUploaderPro.exe" (
    echo [ERROR] dist\CutUploaderPro.exe belum ada.
    echo Jalankan dulu build_exe.bat supaya EXE-nya jadi,
    echo baru kemudian jalankan BANGUN-INSTALLER.bat ini.
    echo.
    pause
    exit /b 1
)

echo Membangun installer (tunggu 1-2 menit)...
"%ISCC%" installer.iss
if errorlevel 1 (
    echo.
    echo [ERROR] Build installer gagal. Baca pesan error di atas.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   SELESAI!
echo   Installer ada di: dist\CutUploaderPro-Setup.exe
echo.
echo   Cara pakai di PC lain:
echo   - Double-click Setup.exe - Next - Next - Install
echo   - Shortcut muncul di Start Menu + Desktop
echo   - Bisa di-uninstall lewat Control Panel
echo ============================================
pause
