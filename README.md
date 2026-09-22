# CutUploader Pro

**Uploader Video Batch Otomatis untuk CutMotions (Kwai)** — aplikasi desktop Windows dengan tema dark neon.

Aplikasi ini mengikuti alur asli halaman CutMotions: **Jadwal rilis (Negara + tanggal-jam) → Tambah video batch (Shift+↓) → Caption per baris via Edit/Konfirmasi → Submit** — semuanya otomatis setelah kamu menekan F6.

```
Caption dasar : #dangdut
Nama file     : melati.mp4
Judul video   : #dangdut - melati   (otomatis!)
```

## Fitur (v3.0) — urutan posisi A–J

| Slot | Otomatis |
|---|---|
| **A** | Klik tombol **Jadwal rilis/publikasi** |
| **B** | Klik dropdown **NEGARA** |
| **C** | Pilih negara — klik biasa **ATAU pencarian gambar referensi dalam radius** (mis. tulisan "Indonesia") dengan tombol **TES CARI** |
| **D** | Klik kolom tanggal + **ketik tanggal-jam otomatis** — format bebas diisi, contoh `2026-09-10 02:05:01` |
| **E** | Klik **OKE** |
| **F** | Klik **+ Tambah video** |
| **G** | Klik bebas **0–500x** di satu titik dan/atau **scroll 0–50x** (arah Turun/Naik) |
| **H** | Klik video pertama + **tahan SHIFT + panah bawah** (jumlah−1)x → pilih 5–20 video sekaligus |
| **H2** | Klik bebas (mis. tombol **Buka**) |
| **I** | Caption per video: **Edit → kotak caption → ketik → Konfirmasi**, posisi klik **otomatis bergeser turun per baris** — 5 video = 5x, 20 video = 20x |
| **J** | Klik **SUBMIT** (jumlah klik bisa diatur, bisa dimatikan) |

- **Pencarian gambar negara (C)**: potongan layar dicari di dalam **radius** dari titik acuan pakai OpenCV template matching — ada pengaturan **radius**, **kemiripan (0.50–0.99)**, dan tombol **TES CARI**. Tidak ketemu 3x? Otomatis fallback ke klik biasa, alur tidak berhenti.
- **Tanggal-jam rilis (D)**: format `2026-09-10 02:05:01` (detik boleh dilewat), diketik otomatis ke kolom tanggal setelah diklik.
- **Caption per baris (I)**: cukup atur posisi baris-1 + **JARAK ANTAR BARIS (piksel)** — aplikasi menghitung posisi baris 2, 3, ... sampai 20 sendiri.
- **Multi-browser**: banyak browser — masing-masing punya **folder video** dan **13 slot posisi klik sendiri** (tersimpan otomatis).
- **Batas situs dijaga**: maksimal **20 video** sekali jalan + peringatan judul melebihi **250 karakter**.
- **Riwayat anti-dobel** + **lanjut ke fase caption saja** bila upload kemarin sudah selesai tapi caption belum.
- **Hotkey global**: `F6` mulai, `F7`/`ESC` berhenti.

## Alur manual yang tetap kamu lakukan

1. Login ke CutMotions (email/kata sandi)
2. Pilih **Versi lama** → **Rilis karya**
3. Tekan F6 — sisanya dikerjakan aplikasi (A sampai J)

## Cara pakai cepat

1. Install [Python](https://www.python.org/downloads/) (centang *Add Python to PATH*)
2. Klik dua kali **`JALANKAN.bat`** — otomatis pasang library & buka aplikasi
3. Ikuti langkah setup di **`PANDUAN.txt`**: daftar browser → pilih folder → ambil 13 posisi (A–J) → isi jumlah & caption → F6

> ⚠️ Uji dulu dengan **JUMLAH = 1** sampai lancar, baru naik ke 5/10/20.

## Build EXE (opsional)

Klik dua kali **`build_exe.bat`** — hasilnya `dist/cut_uploader.exe`. Karena membawa OpenCV (untuk pencarian gambar), ukuran exe cukup besar; kalau tidak pakai fitur gambar, hapus `opencv-python` dari requirements dan pakai klik biasa di titik C.

## Struktur file

| File | Fungsi |
|---|---|
| `cut_uploader.py` | Aplikasi utama (Python + tkinter + pynput + OpenCV/Pillow opsional) |
| `JALANKAN.bat` | Launcher cepat + auto-install pynput/pillow/opencv |
| `build_exe.bat` | Membuat `.exe` dengan PyInstaller |
| `PANDUAN.txt` | Panduan lengkap Bahasa Indonesia |
| `requirements.txt` | Daftar library |

`cutuploader_settings.json` (pengaturan) dan `cutuploader_riwayat.json` (riwayat upload) dibuat otomatis di sebelah aplikasi — tidak ikut tersimpan di repo.

## Changelog

- **v3.0** — Urutan posisi baru **A–J** sesuai alur situs terkini: jadwal rilis pindah ke **awal** (A jadwal → B negara → C pilih negara → D tanggal → E OKE), lalu F tambah video → G klik bebas/scroll → H pilih video dengan **Shift+panah bawah** (batch 5–20 sekaligus, bukan ketik path satu-satu) → H2 Buka → I caption **per baris dengan jarak piksel yang bisa diatur** → J Submit. Fitur baru: **pencarian gambar negara** (radius + kemiripan + TES CARI, fallback klik biasa), **input tanggal-jam otomatis** `2026-09-10 02:05:01`, **klik bebas 0–500x / scroll**, **jarak antar baris**, mode lanjut-caption, lewati-jadwal. Posisi lama v2.0 tidak dimigrasi (makna slot berubah) — ambil ulang posisi sekali lagi.
- **v2.0** — Alur halaman asli: fase jadwal + jeda F8, caption per video lewat Edit→Judul→Konfirmasi, 9 slot posisi, batas 20 video.
- **v1.0** — Versi awal (caption + kirim per video).

## Catatan

- Gunakan sesuai kebijakan platform yang kamu ikuti; kamu bertanggung jawab atas konten yang diupload.
- Kalau tampilan situs berubah, cukup ambil ulang posisi klik — tidak perlu update aplikasi.
- Proyek saudaran: [AutoTyperPro](https://github.com/zacrie85/AutoTyperPro) (auto-typer dengan nomor berurutan).
