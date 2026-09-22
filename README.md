# CutUploader Pro

**Uploader Video Batch Otomatis untuk CutMotions (Kwai)** — aplikasi desktop Windows dengan tema dark neon.

Aplikasi ini meng-upload video dari folder kamu ke situs **CutMotions** satu per satu secara otomatis, lengkap dengan **caption otomatis** yang digabung dari caption dasar + nama file.

```
Caption dasar : #dangdut
Nama file     : melati.mp4
Caption jadi  : #dangdut - melati   (otomatis!)
```

## Fitur

- **Multi-browser**: daftarkan banyak browser (Chrome Akun 1, Edge Akun 2, ...) — setiap browser punya **folder video sendiri** dan **posisi klik sendiri** (tersimpan otomatis).
- **Jumlah video sekali jalan**: isi angka bebas — 5, 10, atau sampai 20 video.
- **Caption otomatis**: format `CAPTION - NAMA FILE` (nama file tanpa ekstensi), pratinjau live.
- **Mode Posisi** (kayak Auto Typer Pro): ambil posisi 3 titik di situs dengan tombol **AMBIL POSISI** — tombol pilih video, kolom caption, tombol kirim. Jalan di browser apa pun (Chrome/Edge/Firefox).
- **Riwayat anti-dobel**: video yang sudah terkirim dicatat otomatis, bisa dilewati di upload berikutnya (opsional, bisa dibersihkan).
- **Pengaturan waktu lengkap**: mundur sebelum mulai, jeda buka dialog, jeda antar langkah, tunggu setelah kirim — semua bisa diubah.
- **Hotkey global**: `F6` mulai upload, `F7`/`ESC` berhenti kapan saja.
- **Urut nama A-Z**: file diambil dari folder sesuai urutan abjad.

## Alur kerja (per 1 video)

1. Klik tombol **pilih video** di situs CutMotions
2. Jendela pilih file Windows terbuka → aplikasi mengetik lokasi file → `Enter`
3. Klik **kolom caption** → tulis caption gabungan (`#dangdut - melati`)
4. Klik tombol **kirim**
5. Tunggu sesuai "Tunggu setelah kirim" → lanjut video berikutnya

## Cara pakai cepat

1. Install [Python](https://www.python.org/downloads/) (centang *Add Python to PATH*)
2. Klik dua kali **`JALANKAN.bat`** — otomatis pasang library & buka aplikasi
3. Ikuti langkah setup di **`PANDUAN.txt`** (daftar browser → pilih folder → ambil 3 posisi → isi jumlah & caption → F6)

## Build EXE (opsional)

Klik dua kali **`build_exe.bat`** — hasilnya `dist/CutUploaderPro.exe`, satu file, bisa dipindah bebas.

## Struktur file

| File | Fungsi |
|---|---|
| `cut_uploader.py` | Aplikasi utama (Python + tkinter + pynput) |
| `JALANKAN.bat` | Launcher cepat + auto-install pynput |
| `build_exe.bat` | Membuat `.exe` dengan PyInstaller |
| `PANDUAN.txt` | Panduan lengkap Bahasa Indonesia |
| `requirements.txt` | Daftar library |

`cutuploader_settings.json` (pengaturan) dan `cutuploader_riwayat.json` (riwayat upload) dibuat otomatis di sebelah aplikasi — tidak ikut tersimpan di repo.

## Catatan

- Gunakan sesuai kebijakan platform yang kamu ikuti; kamu bertanggung jawab atas konten yang diupload.
- Kalau tampilan situs berubah, cukup ambil ulang posisi klik — tidak perlu update aplikasi.
- Proyek saudaran: [AutoTyperPro](https://github.com/zacrie85/AutoTyperPro) (auto-typer dengan nomor berurutan).
