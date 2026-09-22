# CutUploader Pro — Macro Edition (v4.0)

Uploader video **batch otomatis** untuk situs **CutMotions (Kwai)** — tampilan editor makro ala **Jitbit Macro Recorder**, jadi **installer Windows** (tanpa Python), **jeda antar klik bisa diatur per langkah**, dan **pencarian gambar negara** yang diperbaiki total.

## Unduh (tanpa install Python)

Dari [halaman Releases](../../releases) rilis **v4.0**:

| File | Untuk apa |
|---|---|
| `CutUploaderPro-Setup.exe` | **Installer** — Next-Next-Install, shortcut otomatis, bisa di-uninstall |
| `CutUploaderPro.exe` | EXE portabel, tinggal double-click |
| `CutUploaderPro-v4.0.zip` | Source + skrip build (untuk pengguna Python) |

> Catatan: Windows SmartScreen bisa tampil karena aplikasi tanpa tanda tangan digital — klik *More info → Run anyway*.

Dibangun **otomatis oleh GitHub Actions** (Windows runner: PyInstaller + Inno Setup) setiap kali tag `v*` di-push — lihat `.github/workflows/build-windows.yml`.

## Alur otomatis (urutan posisi A–J)

```
F6 (setelah login manual → Versi lama → Rilis karya)

A  Klik "Jadwal rilis"          F  Klik "+ Tambah video"
B  Klik dropdown NEGARA         G  Klik bebas 0-500x / scroll
C  Pilih negara (gambar/Klik)   H  Klik video + SHIFT + ↓ (5-20)
D  Ketik tanggal-jam otomatis   H2 Klik bebas ("Buka")
E  Klik "OKE"                   I  Edit → caption → Konfirmasi
                                  (ulang per video, baris bergeser)
                               J  Klik "SUBMIT"
```

Maksimal **20 video** sekali jalan (aturan situs). Caption = `#dangdut - namafile` (atur sendiri awalannya).

## Fitur utama v4.0

- **UI ala Jitbit Macro Recorder** — toolbar Jalankan/Berhenti, tabel langkah A–J (kolom DETAIL, JEDA, ULANGI), panel *Properti Langkah* untuk baris terpilih, tema Windows klasik.
- **Jeda bisa diatur**: `JEDA SEBELUM LANGKAH` per langkah (kolom JEDA), `JEDA ANTAR KLIK` per langkah (klik berulang G/H2/J, panah Shift di H), tombol *Terapkan ke semua langkah*, plus MUNDUR / JEDA DIALOG / TUNGGU UPLOAD global.
- **Pencarian gambar diperbaiki**: multi-skala (tahan beda zoom 70–125%), pesan error yang jelas (skor kemiripan terbaik dilaporkan), dan alat **POTONG GAMBAR** (screenshot layar hidup → seret kotak → PNG 1:1) — menghilangkan penyebab error paling umum. OpenCV **ikut terbungkus** di EXE/Setup.
- **Tanggal & jam otomatis** langkah D, format `2026-09-10 02:05:01` (detik opsional).
- **Pilih video batch** langkah H: klik video pertama + tahan SHIFT + panah bawah otomatis.
- **Caption per baris** langkah I: Edit → kotak caption → ketik → Konfirmasi, bergeser `JARAK ANTAR BARIS` px per baris, diulang sebanyak jumlah video.
- **Profil makro**: simpan/muat posisi+jeda per browser/akun (`.json`).
- **Riwayat + lewati yang sudah terupload**, lanjut-fase-caption otomatis setelah stop.
- Hotkey global: **F6 mulai, F7/ESC berhenti**, failsafe pojok kiri-atas.

## Menjalankan dari source (opsional)

```bat
JALANKAN.bat          :: auto-install pynput + pillow + opencv lalu jalan
build_exe.bat         :: bangun dist\CutUploaderPro.exe (OpenCV ikut dibungkus)
BANGUN-INSTALLER.bat  :: bangun dist\CutUploaderPro-Setup.exe (butuh Inno Setup 6)
```

`requirements.txt`: `pynput`, `pillow`, `opencv-python`, `pyinstaller` (dev).

## Perubahan v4.0

- UI ditulis ulang ala Jitbit Macro Recorder (tabel makro + panel properti).
- Jeda antar klik & jeda per langkah yang dapat disetel sendiri.
- Perbaikan besar fitur cari gambar (multi-skala + alat potong gambar + pesan error + OpenCV terbungkus di EXE; `build_exe.bat` lama mengecualikan PIL/numpy sehingga fitur mati diam-diam di EXE buatan sendiri).
- Distribusi Windows: Setup.exe (Inno Setup) + EXE portabel, dibangun otomatis GitHub Actions.
- Profil makro menggantikan daftar browser; posisi v3.0 dimigrasi otomatis.

## Keamanan

Login dilakukan **manual** oleh pengguna — aplikasi tidak pernah meminta, menampilkan, atau menyimpan email/password/cookie. Data lokal (profil, riwayat) berupa JSON di folder aplikasi.
