# CutUploader Pro — Macro Studio Edition (v5.4)

Otomasi klik **bebas ala Jitbit Macro Recorder** + uploader video **batch otomatis** untuk situs **CutMotions (Kwai)** — dalam satu aplikasi. Dibundel jadi **installer Windows** (tanpa Python), **REKAM AKSI — klik/ketikan/scrollmu direkam otomatis jadi langkah makro**, pencarian gambar **tanpa X,Y — langsung diklik begitu ketemu** dengan **AREA FOKUS** opsional (seret kotak di layar), salin-tempel langkah, **editor alur kerja kosong** untuk menyusun klik-per-klik sendiri, **potong gambar referensi langsung di layar**, dan menu pintar **ISI TANGGAL-JAM** + **ISI VIDEO & CAPTION**.

## Unduh (tanpa install Python)

Dari halaman [Releases](../../releases) rilis **v5.4**:

| File | Untuk apa |
|---|---|
| `CutUploaderPro-Setup.exe` | **Installer** — Next-Next-Install, shortcut otomatis, bisa di-uninstall |
| `CutUploaderPro.exe` | EXE portabel, tinggal double-click |
| `CutUploaderPro-v5.4.zip` | Source + skrip build (untuk pengguna Python) |

> Catatan: Windows SmartScreen bisa tampil karena aplikasi tanpa tanda tangan digital — klik *More info → Run anyway*.

Dibangun **otomatis oleh GitHub Actions** (Windows runner: PyInstaller + Inno Setup) setiap kali tag `v*` di-push — lihat `.github/workflows/build-windows.yml`.

## Dua mode dalam satu aplikasi (baru v5.0)

Saat dibuka ada **dua tab** di bagian atas:

### 1. STUDIO MAKRO (alur bebas) — baru!

Persis konsep Jitbit Macro Recorder: **semua jenis aksi jadi menu tersendiri di bagian atas**, dan **di bawahnya tabel kosong** untuk menyusun alur kerja klik-per-klik satu per satu:

| Menu | Aksi |
|---|---|
| `● REKAM AKSI` | **Baru v5.4** — MEREKAM: klik/ketikan/scroll Anda di aplikasi mana pun terekam otomatis jadi langkah makro; F8 = berhenti |
| `+ KLIK` | Klik kiri/kanan/dobel di satu titik (jumlah klik + jeda antar klik) |
| `+ JEDA` | Tunggu N detik |
| `+ CARI GAMBAR` | Cari potongan gambar di layar **tanpa perlu X,Y** → diklik langsung begitu ketemu atau hanya dipindah; daerah pencarian dibatasi **AREA FOKUS** opsional (seret kotak di layar); tak ketemu → klik tengah area / lewati / stop |
| `+ KETIK` | Ketik teks (opsional Ctrl+A dulu, Enter setelahnya) |
| `+ TANGGAL-JAM` | **Baru v5.2** — isi kolom tanggal-jam rilis otomatis (dari setelan tab CutMotions atau nilai tetap) |
| `+ VIDEO+CAPTION` | **Baru v5.2** — isi jumlah video, atau caption dasar + nama video ke-i (`#dangdut - melati`), atau nama video saja |
| `+ TOMBOL` | Enter, Tab, panah, Shift+Panah Bawah, Ctrl+A/C/V, F2/F4/F5, atau huruf apa saja × jumlah tekan |
| `+ SCROLL` | Gulung Naik/Turun sejumlah gulungan |
| `+ CATATAN` | Komentar/penanda (tidak dieksekusi) |
| `+ ULANGI MULAI/AKHIR` | Blok pengulangan (bisa bersarang) |

- Panel **PROPERTI LANGKAH** menyesuaikan jenis langkah terpilih (posisi + AMBIL 5 dtk, teks, jeda, gambar referensi, dll).
- **SALIN / TEMPEL / HAPUS / NAIK / TURUN / AKTIF-MATI** — klik kanan baris atau Ctrl+C/V/Del; tempel menyisipkan salinan lengkap setelah baris terpilih (cara gampang bikin titik klik berikutnya).
- **Placeholder teks**: `{caption}` = caption dasar + nama video ke-i, `{video}` = nama video ke-i, `{no}` = nomor putaran, `{jumlah}` = jumlah video — mengikuti folder/jumlah/riwayat di tab CutMotions (atau pakai menu `+ VIDEO+CAPTION` yang lebih praktis).
- **GESER PER PUTARAN ULANGI** — klik di dalam blok ULANGI otomatis turun N px per putaran (untuk caption per baris video).
- **SIMPAN/BUKA MAKRO** (.json) + **auto-save** makro aktif; **TEMPLATE CUTMOTIONS** mengisi alur A-J versi bebas sekali klik, lalu bebas disunting.

### 2. ALUR CUTMOTIONS (A–J)

Alur otomatis uploader batch CutMotions seperti versi sebelumnya:

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

Maksimal **20 video** sekali jalan (aturan situs). Caption = `#dangdut - namafile` (atur sendiri awalannya). Klik kanan langkah = salin/tempel jadi titik klik tambahan; pencarian gambar bisa diaktifkan di semua langkah.

## Menjalankan dari source (opsional)

```bat
JALANKAN.bat          :: auto-install pynput + pillow + opencv lalu jalan
build_exe.bat         :: bangun dist\CutUploaderPro.exe (OpenCV ikut dibungkus)
BANGUN-INSTALLER.bat  :: bangun dist\CutUploaderPro-Setup.exe (butuh Inno Setup 6)
```

`requirements.txt`: `pynput`, `pillow`, `opencv-python`, `pyinstaller` (dev).

## Perubahan v5.4

- **● REKAM AKSI (macro recorder)** — sekarang Anda tidak perlu menyusun langkah satu per satu. Klik tombol merah `● REKAM AKSI` (atau menu *Studio → Rekam Aksi*) → konfirmasi → hitung mundur 3 detik → jendela aplikasi tersembunyi, muncul **banner kecil "● MEREKAM AKSI"** di pojok kanan bawah (hitungan aksi live, bisa digeser, klik di atasnya tidak dihitung sebagai aksi). Kerjakan aksimu di aplikasi mana pun, lalu tekan **F8** (atau ESC) — jendela tampil lagi dan **semuanya sudah jadi langkah di tabel Studio**, ditambah di akhir alur tanpa menimpa yang lama.
- **Yang direkam & caranya digabung cerdas**:
  - Klik kiri → langkah **KLIK TITIK** (posisi persis); **klik dobel dikenali otomatis** (2 klik < 0,45 dtk di posisi hampir sama) → mode `Klik dobel`; klik kanan pun terekam.
  - Huruf/angka berurutan digabung jadi **SATU langkah KETIK TEKS** (mis. `#dangdut - melati`).
  - Enter/Tab/Backspace/Delete/panah/Home/End/Page Up/Page Down/F2/F4/F5 → langkah **TEKAN TOMBOL**; kombinasi **Ctrl+A/C/V/S/Z** juga terekam. Shift+↑/↓ dikenali sebagai Shift+Panah.
  - Gulungan mouse searah berurutan (< 1,5 dtk) digabung jadi **SATU langkah SCROLL** dengan jumlah gulungan digabung.
  - **Jeda antar aksi terekam otomatis** jadi kolom JEDA (dibatasi 0,1–10 detik) — ritme aksi asli terjaga, tinggal disunting bila perlu.
- **Aman & rapi**: F6/F7/ESC diabaikan selagi merekam (tidak bisa tak sengaja menjalankan/menghentikan makro); kejadian dobel sisa driver keyboard dibuang otomatis (dedup < 20 ms) tanpa memengaruhi huruf kembar sungguhan seperti `ll`; hasil rekaman ikut tersimpan di file makro (SIMPAN MAKRO + auto-save) dan bebas disalin/diurutkan/dimatikan seperti langkah biasa.
- Hotkey baru: **F8 / ESC = berhenti merekam** (tertera di banner & tombol).

## Perubahan v5.3

- **CARI GAMBAR TANPA X,Y** — isian POSISI X,Y dan RADIUS di langkah CARI GAMBAR Studio **dihapus**. Gambar referensi yang sudah dipotong langsung dicari dan **diklik otomatis** begitu ketemu (atau hanya dipindah, sesuai pilihan SAAT KETEMU) — tidak ada lagi langkah mengisi posisi acuan.
- **AREA FOKUS (opsional)** — pengganti titik acuan: daerah persegi tempat gambar dicari. Klik `PILIH AREA FOKUS...` → layar dibekukan fullscreen → **seret kotak** di daerah tempat gambar biasanya muncul → lepas, tersimpan sebagai koordinat. `KOSONGKAN` = cari di seluruh layar. Pencarian jadi lebih cepat (tidak scan layar penuh), lebih akurat (gambar mirip di luar area tak ikut terdeteksi), dan tetap jalan walau gambar bergeser di dalam area.
- **Makro lama tetap jalan** — langkah CARI GAMBAR versi lama (titik acuan X,Y + radius) otomatis dikonversi jadi area persegi saat dimuat/dijalankan; pilihan lama "Klik titik X,Y" dimapkan ke "Klik tengah area".
- **Penjagaan gambar polos** — referensi yang warnanya rata (tanpa tulisan/gambar) ditolak dengan pesan jelas, karena template matching pada gambar konstan menghasilkan positif-palsu 100%.
- Saat opencv tidak terpasang, langkah CARI GAMBAR kini dilewati dengan pesan (dulu fallback klik titik acuan yang sudah tidak ada).

## Perubahan v5.2

- **2 MENU BARU di Studio Makro** yang menutup celah "alur bebas tidak punya langkah pengisi kolom tanggal-jam & jumlah video / caption":
  - **`+ TANGGAL-JAM` (ISI TANGGAL-JAM)** — satu langkah untuk mengisi kolom tanggal-jam rilis. Sumber nilai: **Tab CutMotions** (mengikuti kolom TANGGAL & JAM RILIS di tab Alur CutMotions — ubah sekali, semua makro ikut) atau **Tetap (isi sendiri)** (format `2026-09-10 02:05:01`). Bisa klik kolomnya sendiri lewat *POSISI KLIK DULU*; Ctrl+A dulu otomatis menimpa isi lama; format divalidasi (`parse_tanggal`) dan dirapikan sebelum diketik.
  - **`+ VIDEO+CAPTION` (ISI VIDEO & CAPTION)** — satu langkah pengisi data video, pilihannya: **Jumlah video** (angka di kolom JUMLAH VIDEO tab CutMotions), **Caption dasar + nama video** (mis. `#dangdut - melati`; di dalam blok ULANGI nama video berganti otomatis tiap putaran), **Nama video saja**, atau **Teks sendiri + placeholder** (`{caption} {video} {no} {jumlah}`).
- **Placeholder baru `{jumlah}`** di langkah KETIK — jumlah video total.
- **TEMPLATE CUTMOTIONS kini memakai keduanya**: langkah D menjadi ISI TANGGAL-JAM dan langkah I2 menjadi ISI VIDEO & CAPTION (dulu KETIK TEKS biasa) — makro hasil template langsung ikut nilai terbaru dari tab CutMotions.
- Perbaikan kecil: kalau folder video kosong, `{caption}` kini menghasilkan caption dasar saja (bukan `#dangdut - video`); jendela diperlebar ke 1280px agar semua tombol menu muat.

## Perubahan v5.1

- **POTONG GAMBAR LANGSUNG DI LAYAR (fullscreen)** — dulu: seluruh layar di-screenshot lalu ditampilkan dalam jendela kecil, seret, tekan SIMPAN AREA. Kini: aplikasi disembunyikan sejenak → layar dibekukan memenuhi monitor → **tinggal MENYERET kotak langsung di area yang diinginkan** → lepas mouse, **langsung tersimpan**. Hanya area yang diseret yang disimpan (bukan seluruh layar); area sekitar tampil gelap, area terpilih tampil terang, ada label ukuran piksel. `ESC`/klik kanan = batal, seretan terlalu kecil ditolak dengan peringatan.
- **CARI GAMBAR bisa dipakai berkali-kali dengan referensi berbeda-beda** — setiap potongan otomatis menjadi **file baru** `ref_tanggal-jam.png` di `%LOCALAPPDATA%\CutUploaderPro\referensi` (tidak pernah menimpa gambar langkah lain). Tambah langkah CARI GAMBAR sebanyak apa pun, masing-masing dengan referensinya sendiri.
- **Thumbnail referensi** — panel PROPERTI langkah CARI GAMBAR menampilkan pratinjau gambar referensi langkah itu (dua tab).
- **POTONG = bikin langkah baru (Studio)** — kalau belum ada langkah CARI GAMBAR terpilih saat menekan POTONG GAMBAR, aplikasi menawarkan membuat **langkah CARI GAMBAR baru** langsung dengan gambar hasil potongan.
- Hotkey F6/F7 otomatis diabaikan selagi layar potong terbuka (alur tidak mulai tak sengaja).

## Perubahan v5.0

- **STUDIO MAKRO** — tab baru: editor alur kerja bebas ala Jitbit Macro Recorder; semua jenis aksi (klik, jeda, cari gambar, ketik, tombol, scroll, catatan, ulangi) jadi menu tersendiri di toolbar atas + menubar "Studio", tabel alur kerja kosong di bawah, panel properti dinamis per jenis langkah.
- **Dua tab** dalam satu jendela: `STUDIO MAKRO (alur bebas)` dan `ALUR CUTMOTIONS (A-J)`; menubar & statusbar bersama; hotkey F6/F7 mengikuti tab aktif; kedua tab saling menahan (tidak bisa jalan bersamaan).
- **Blok ULANGI** dengan penjaga anti loop-tak-berujung, pasangan MULAI/AKHIR divalidasi sebelum jalan, dan opsi "ikut jumlah video CutMotions".
- **Placeholder `{caption} {video} {no}`** untuk langkah ketik di dalam ULANGI — caption per baris video bisa dirangkai di alur bebas.
- **SIMPAN/BUKA MAKRO .json + auto-save** (`%LOCALAPPDATA%\CutUploaderPro\makro_terakhir.json`) dan tombol **TEMPLATE CUTMOTIONS** (alur A-J → langkah bebas siap edit).
- Perbaikan bug: panel properti kini tidak lagi ter-render ulang di tengah pengeditan (sebelumnya setiap perubahan memicu event seleksi tabel); langkah tanpa kunci `aktif` pada file makro kini dianggap aktif.

## Perubahan v4.2

- **CARI GAMBAR di SEMUA langkah** — dulu hanya langkah C; kini setiap langkah A-J (dan salinannya) punya seksi *Pencarian Gambar* opsional: gambar referensi sendiri, radius/kemiripan sendiri, dan tombol *Tes Cari Langkah Ini*.
- **Mode SAAT KETEMU**: `Klik di gambar` (klik langsung pusat gambar yang ditemukan) atau `Pindah saja` (mouse dipindah tanpa klik).
- **Mode SAAT TIDAK KETEMU**: `Klik titik X,Y` (fallback), `Lewati langkah`, atau `Stop alur`.
- **SALIN / TEMPEL / HAPUS LANGKAH** — langkah A-J bisa digandakan (toolbar, klik kanan, Ctrl+C/Ctrl+V/Del) menjadi titik klik tambahan dengan posisi, jeda, jumlah klik, dan pencarian gambar sendiri. Salinan tampil sebagai baris biru `+` dan dieksekusi di fase langkah asalnya (salinan I ikut loop caption per baris).
- Konfigurasi gambar per langkah tersimpan di profil makro; setelan lama v4.1 (checkbox C) dimigrasi otomatis.

## Perubahan v4.1

- **Perbaikan error "Errno 13 Permission denied" saat SIMPAN AREA di jendela POTONG GAMBAR**: sebelumnya potongan disimpan ke folder aplikasi (`C:\Program Files\...`) yang dikunci Windows bila aplikasi ter-install. Kini semua file yang ditulis aplikasi (potongan gambar, settings, riwayat) disimpan ke folder data user `%LOCALAPPDATA%\CutUploaderPro` yang selalu bisa ditulisi.
- Kalau simpan tetap gagal, muncul dialog **pilih lokasi sendiri** (Documents/Desktop) dan pesan error yang lebih jelas.
- Label lokasi tersimpan ditampilkan di bawah jendela potong; nama file otomatis dibersihkan dari karakter terlarang Windows.
- Settings & riwayat versi lama **dimigrasi otomatis** dari folder aplikasi ke folder data user.

## Perubahan v4.0

- UI ditulis ulang ala Jitbit Macro Recorder (tabel makro + panel properti).
- Jeda antar klik & jeda per langkah yang dapat disetel sendiri.
- Perbaikan besar fitur cari gambar (multi-skala + alat potong gambar + pesan error + OpenCV terbungkus di EXE; `build_exe.bat` lama mengecualikan PIL/numpy sehingga fitur mati diam-diam di EXE buatan sendiri).
- Distribusi Windows: Setup.exe (Inno Setup) + EXE portabel, dibangun otomatis GitHub Actions.
- Profil makro menggantikan daftar browser; posisi v3.0 dimigrasi otomatis.

## Keamanan

Login dilakukan **manual** oleh pengguna — aplikasi tidak pernah meminta, menampilkan, atau menyimpan email/password/cookie. Data lokal (profil, makro, riwayat, gambar referensi) berupa file di folder data user `%LOCALAPPDATA%\CutUploaderPro` (bukan folder instalasi Program Files).
