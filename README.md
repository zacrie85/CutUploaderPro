# CutUploader Pro

**Uploader Video Batch Otomatis untuk CutMotions (Kwai)** — aplikasi desktop Windows dengan tema dark neon.

Aplikasi ini mengikuti alur asli halaman CutMotions: **Tambah video → Jadwalkan rilis (Negara Indonesia) → Caption via Edit/Konfirmasi → Kirim** — semuanya otomatis setelah kamu menekan F6.

```
Caption dasar : #dangdut
Nama file     : melati.mp4
Judul video   : #dangdut - melati   (otomatis!)
```

## Fitur (v2.0)

- **Alur 4 fase sesuai situs asli**:
  1. **UPLOAD** — klik `+ Tambah video`, ketik path file di dialog Windows, tunggu upload, ulangi (urut nama A-Z)
  2. **JADWAL** — (opsional) klik radio `Jadwalkan rilis` + Negara Indonesia otomatis; Zona waktu & Waktu rilis diatur saat **jeda F8**
  3. **CAPTION** — per video: tombol `Edit` → kotak `Judul video` → ketik caption → `Konfirmasi`
  4. **KIRIM** — scroll ke bawah → klik `Kirim`
- **Trik posisi geser-naik**: setelah Konfirmasi, baris video berikutnya naik ke posisi yang sama — **1 set posisi dipakai untuk semua video** (5, 10, sampai 20).
- **Multi-browser**: banyak browser (Chrome Akun 1, Edge Akun 2, ...) — masing-masing punya **folder video** dan **9 slot posisi klik sendiri** (tersimpan otomatis).
- **Batas situs dijaga**: maksimal **20 video** sekali jalan + peringatan judul melebihi **250 karakter**.
- **Riwayat anti-dobel**: video yang sudah terupload dicatat otomatis & dilewati di eksekusi berikutnya (bisa dibersihkan). Eksekusi ulang setelah stop aman dilanjutkan.
- **Pengaturan waktu lengkap**: mundur, jeda dialog/editor, jeda antar langkah, tunggu upload per video.
- **Hotkey global**: `F6` mulai, `F7`/`ESC` berhenti, `F8` lanjut dari jeda jadwal.
- **Kirim otomatis opsional**: bisa juga dimatikan supaya kamu cek dulu manual.

## Alur manual yang tetap kamu lakukan

1. Login ke CutMotions (email/kata sandi)
2. Pilih **Versi lama** → **Rilis karya**
3. Tekan F6 — sisanya dikerjakan aplikasi (kecuali Zona waktu & Waktu rilis saat jeda F8, karena kalendernya sulit diklik otomatis)

## Cara pakai cepat

1. Install [Python](https://www.python.org/downloads/) (centang *Add Python to PATH*)
2. Klik dua kali **`JALANKAN.bat`** — otomatis pasang library & buka aplikasi
3. Ikuti langkah setup di **`PANDUAN.txt`**: daftar browser → pilih folder → ambil posisi (A–I; wajib A–E) → isi jumlah & caption → F6

> ⚠️ Uji dulu dengan **JUMLAH = 1** sampai lancar, baru naik ke 5/10/20.

## Build EXE (opsional)

Klik dua kali **`build_exe.bat`** — hasilnya `dist/cut_uploader.exe`, satu file, bisa dipindah bebas.

## Struktur file

| File | Fungsi |
|---|---|
| `cut_uploader.py` | Aplikasi utama (Python + tkinter + pynput) |
| `JALANKAN.bat` | Launcher cepat + auto-install pynput |
| `build_exe.bat` | Membuat `.exe` dengan PyInstaller |
| `PANDUAN.txt` | Panduan lengkap Bahasa Indonesia |
| `requirements.txt` | Daftar library |

`cutuploader_settings.json` (pengaturan) dan `cutuploader_riwayat.json` (riwayat upload) dibuat otomatis di sebelah aplikasi — tidak ikut tersimpan di repo.

## Changelog

- **v2.0** — Alur disesuaikan dengan halaman CutMotions yang asli: fase jadwal rilis (Negara Indonesia) + jeda F8, caption lewat tombol `Edit → Judul video → Konfirmasi` per video, 9 slot posisi (dari 3), batas 20 video, batas judul 250 karakter, scroll otomatis sebelum Kirim, trik posisi geser-naik, lanjut-otomatis setelah stop.
- **v1.0** — Versi awal (alur lama: caption + kirim per video).

## Catatan

- Gunakan sesuai kebijakan platform yang kamu ikuti; kamu bertanggung jawab atas konten yang diupload.
- Kalau tampilan situs berubah, cukup ambil ulang posisi klik — tidak perlu update aplikasi.
- Proyek saudaran: [AutoTyperPro](https://github.com/zacrie85/AutoTyperPro) (auto-typer dengan nomor berurutan).
