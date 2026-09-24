# CutUploader Pro — Macro Studio Edition (v6.2)

Otomasi klik **bebas ala Jitbit Macro Recorder** + uploader video **batch otomatis** untuk situs **CutMotions (Kwai)** — dalam satu aplikasi. Dibundel jadi **installer Windows** (tanpa Python), **REKAM AKSI — klik/ketikan/scrollmu direkam otomatis jadi langkah makro (di kedua tab!)**, **PILIH BANYAK LANGKAH (Ctrl/Shift+Klik) untuk salin/tempel/hapus massal**, pencarian gambar **tanpa X,Y — langsung diklik begitu ketemu** dengan **AREA FOKUS** opsional (seret kotak di layar), salin-tempel langkah, **editor alur kerja kosong** untuk menyusun klik-per-klik sendiri, **potong gambar referensi langsung di layar**, menu pintar **ISI TANGGAL-JAM** + **ISI VIDEO & CAPTION**, semua menu Studio bisa disisipkan ke alur CutMotions (A-J), **v6.1: TANPA PILIH FOLDER — cukup PILIH VIDEO; nama tersimpan otomatis, dipakai di caption, hilang sendiri setelah selesai**, dan **baru v6.2: KARTU VIDEO & CAPTION kini juga di tab STUDIO MAKRO — pilih video, caption dasar, dan tanggal-jam rilis untuk langkah ISI TANGGAL-JAM & ISI VIDEO & CAPTION di alur bebas (sumber data: Otomatis / Studio / CutMotions)**.

## Unduh (tanpa install Python)

Dari halaman [Releases](../../releases) rilis **v6.2**:

| File | Untuk apa |
|---|---|
| `CutUploaderPro-Setup.exe` | **Installer** — Next-Next-Install, shortcut otomatis, bisa di-uninstall |
| `CutUploaderPro.exe` | EXE portabel, tinggal double-click |
| `CutUploaderPro-v6.2.zip` | Source + skrip build (untuk pengguna Python) |

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
- **Placeholder teks**: `{caption}` = caption dasar + nama video ke-i, `{video}` = nama video ke-i, `{no}` = nomor putaran, `{jumlah}` = jumlah video — mengikuti daftar video terpilih/jumlah/riwayat di tab CutMotions (atau pakai menu `+ VIDEO+CAPTION` yang lebih praktis).
- **GESER PER PUTARAN ULANGI** — klik di dalam blok ULANGI otomatis turun N px per putaran (untuk caption per baris video).
- **SIMPAN/BUKA MAKRO** (.json) + **auto-save** makro aktif; **TEMPLATE CUTMOTIONS** mengisi alur A-J versi bebas sekali klik, lalu bebas disunting.

### 2. ALUR CUTMOTIONS (A–J)

Alur otomatis uploader batch CutMotions seperti versi sebelumnya:

```
F6 (setelah login manual → Versi lama → Rilis karya)

A  Klik "Jadwal rilis"          F  Klik "+ Tambah video"
B  Klik dropdown NEGARA         G  Klik bebas 0-500x / scroll
C  Pilih negara (gambar/Klik)   H  Ketik "nama1.mp4" "nama2.mp4"...
D  Ketik tanggal-jam otomatis   H2 Klik bebas ("Buka")
E  Klik "OKE"                   I  Edit → caption → Konfirmasi
                                  (ulang per video, baris bergeser)
                               J  Klik "SUBMIT"
```

Maksimal **20 video** sekali jalan (aturan situs). Caption = `#dangdut - namafile` (atur sendiri awalannya). Klik kanan langkah = salin/tempel jadi titik klik tambahan; pencarian gambar bisa diaktifkan di semua langkah.

### Baru v6.2: kartu VIDEO & CAPTION kini juga ada di tab STUDIO MAKRO (alur bebas)

**Permintaan**: fitur **ISI TANGGAL-JAM**, **ISI VIDEO CAPTION**, dan **BOX VIDEO & CAPTION** seperti yang ada di alur CutMotions (a-j) — ingin ada juga di tab **STUDIO MAKRO**. Sekarang sudah ada:

1. **Kartu "VIDEO & CAPTION STUDIO"** di tab Studio: **PILIH VIDEO... / TAMBAH VIDEO... / HAPUS TERPILIH / KOSONGKAN** + daftar nama video bernomor (urutan pilihan), **TANGGAL & JAM RILIS** (format `2026-09-10 02:05:01`), **JUMLAH VIDEO** terisi otomatis, **CAPTION DASAR** + pratinjau caption.
2. **Langkah ISI TANGGAL-JAM kini punya 3 sumber nilai**: *"Studio Makro (tab ini)"* (= kolom tanggal di kartu Studio — **bawaan langkah baru di Studio**), *"Tab CutMotions"*, atau *"Tetap (isi sendiri)"*. Langkah tambahan ISI TANGGAL-JAM di alur CutMotions juga bisa memilih sumber kartu Studio.
3. **Langkah ISI VIDEO & CAPTION** memakai daftar video + caption sesuai pilihan **AMBIL DATA DARI** di kartu Studio.
4. **AMBIL DATA DARI** (berlaku saat F6 di tab Studio): **Otomatis** (bawaan — kartu Studio dipakai lebih dulu, kolom kosong diambil dari tab CutMotions sehingga makro lama tetap jalan), **Studio Makro (tab ini)**, atau **Tab CutMotions** (cara lama).
5. **Isi kartu ikut tersimpan** di makro (auto-save + SIMPAN/BUKA MAKRO). Catatan: daftar video kartu Studio **tidak dihapus otomatis** setelah makro jalan (makro memang untuk dijalankan berulang) — pakai HAPUS TERPILIH / KOSONGKAN.

Selftest baru **`--selftest-kartu`** (15 cek: daftar & jumlah otomatis, status, pratinjau, mode Otomatis-Studio, mode Otomatis-CutMotions, mode Studio saja, mode CutMotions saja, langkah baru default sumber Studio/CutMotions, teks detail, mesin tanggal kedua sumber, simpan-muat kartu, auto-save).

### Baru v6.1: TANPA pilih folder — pilih videonya langsung, namanya tersimpan otomatis, hilang sendiri setelah selesai

**Keluhan**: sebelumnya harus **memilih FOLDER video** dulu supaya nama file bisa disamakan dengan caption — ribet, dan dialog pilih file di browser harus kebetulan terbuka di folder yang tepat.

**Kini folder tidak diperlukan lagi**:

1. Klik **PILIH VIDEO...** di kartu VIDEO & CAPTION, lalu pilih satu / beberapa / banyak file video sekaligus (tahan `Ctrl`/`Shift` di dialog Windows). **Boleh campur folder.**
2. **Nama setiap video yang dipilih LANGSUNG TERSIMPAN** di daftar kartu (bernomor sesuai urutan pilihan) — urutan pilih = urutan upload = urutan caption.
3. **JUMLAH VIDEO terisi otomatis** sesuai banyaknya video dipilih (boleh diubah manual).
4. Saat alur jalan, aplikasi mengetik **path lengkap** video-video itu di kotak *Nama file* dialog → video yang masuk **PERSIS daftar**, tidak tergantung folder yang sedang terbuka di dialog. Nama di caption PASTI sama dengan videonya.
5. Setelah caption selesai diproses (alur tuntas), **daftar video terpilih OTOMATIS DIHAPUS** — data tidak menumpuk; batch berikutnya tinggal PILIH VIDEO lagi. Bila alur dihentikan di tengah, daftar dipertahankan supaya bisa dilanjutkan.

Tombol pendukung: **PILIH VIDEO...** (ganti daftar), **TAMBAH VIDEO...** (menambah tanpa menghapus; anti-duplikat), **HAPUS TERPILIH** (buang baris tersorot), **KOSONGKAN** (kosongkan semua). Daftar ikut tersimpan di profil.

> Ini sekaligus mengangkat catatan v6.0: dialog kini **boleh terbuka di folder mana pun** karena yang diketik adalah path lengkap. Aturan lama tetap berlaku: jangan sentuh keyboard/mouse selama alur berjalan.

### Baru v6.0: nama video yang diupload PASTI sama dengan caption

**Keluhan**: video yang terupload dan nama yang masuk di caption **BEDA** — caption sudah benar, tapi video yang terupload tidak sesuai nama itu.

**Penyebabnya**: dulu aplikasi hanya **mengklik video pertama** di dialog pilih file lalu menahan `SHIFT` + panah bawah. Urutan hasilnya tergantung tampilan dialog (bisa terurut **tanggal**, bukan nama) dan tergantung riwayat *"lewati yang sudah terupload"* (antrean = video yang belum terupload, tapi yang diklik justru video TERATAS dialog = yang sudah terupload) — sehingga video yang terpilih bisa BEDA dari daftar nama yang dipakai untuk caption.

**Solusi — KETIK NAMA FILE (bawaan AKTIF)**, centang di kartu VIDEO & CAPTION:

1. Saat dialog pilih file terbuka, aplikasi menekan `Alt+N` (fokus ke kotak *Nama file*), lalu **mengetik nama-nama file secara PERSIS**: `"lagu_a.mp4" "lagu_b.mp4" ...` — sesuai daftar caption, dalam urutan yang sama.
2. Tombol *Buka* (langkah H2) tetap diklik seperti biasa; kalau H2 dihapus atau jumlah kliknya 0, aplikasi menekan **Enter** sendiri sebagai konfirmasi.
3. Video yang terpilih = **PERSIS daftar caption** — tidak terpengaruh urutan tampil dialog (nama/tanggal/ukuran) maupun riwayat upload.
4. Posisi langkah H (video pertama) **tidak perlu diatur lagi** saat mode ini aktif.
5. Mau kembali ke cara lama (klik + Shift+panah)? Cukup hilangkan centangnya.

> Catatan (v6.0): pastikan dialog terbuka di FOLDER yang benar (sama seperti cara lama). **Sejak v6.1 catatan ini tidak berlaku lagi** — nama diketik path lengkap, dialog boleh terbuka di folder mana pun. Yang tetap: jangan sentuh keyboard/mouse selama alur berjalan.

### Baru v5.9: error angka diperbaiki + semua langkah bisa dihapus

1. **Error "JUMLAH VIDEO dan WAKTU harus diisi dengan angka" DIPERBAIKI** — dulu cukup satu kolom salah/kosong (mis. MUNDUR yang kosong) dan pesannya menyalahkan "JUMLAH VIDEO dan WAKTU" walau kolom itu sudah diisi. Kini validasi **per kolom**: pesan error menunjuk kolom yang tepat beserta isinya. **Koma diterima** sebagai desimal di semua kolom angka (`1,5` → 1.5), dan kolom yang **dibiarkan kosong otomatis dipakai nilai standarnya** (MUNDUR 5, JEDA DIALOG 2, JEDA LANGKAH 1, TUNGGU 60) — tidak lagi menggagalkan alur. Profil lama berisi nilai rusak otomatis dibersihkan saat dibuka.
2. **SEMUA langkah di ALUR CUTMOTIONS (A-J) bisa DIHAPUS manual** — termasuk langkah bawaan A-J yang dulu menolak dihapus. Pilih barisnya (bisa banyak dengan CTRL/SHIFT) lalu tekan **Del** atau klik kanan → Hapus. Langkah bawaan yang dihapus hilang dari tabel dan **dilewati** saat alur jalan (langkah tambahan yang menempel di belakangnya tetap jalan di posisinya). **Bisa dikembalikan** kapan saja: klik kanan tabel → *"Kembalikan langkah bawaan yang dihapus"* → pilih langkahnya. Penghapusan ikut tersimpan di profil.

### Baru v5.8: CARI GAMBAR bebas ditambah di alur CutMotions (A-J)

CARI GAMBAR (dan semua langkah tambahan lain) di tab **ALUR CUTMOTIONS (A-J)** kini bisa **ditambahkan BERAPAPUN kalinya** — tidak ada lagi batas "mentok 2x". Penyebabnya bukan batas fitur, melainkan kutu kecil: setelah menghapus langkah (apalagi hapus massal v5.7) lalu aplikasi dibuka ulang, nomor internal langkah baru bisa **menabrak** nomor langkah lama sehingga langkah baru tidak muncul di tabel — kelihatan seperti tidak bisa ditambah lagi. Kini nomor yang sudah dipakai selalu dilewati, dan **profil lama yang sudah terlanjur rusak otomatis DIPERBAIKI** saat dibuka di v5.8 (tanpa perlu mengatur ulang apa pun). Berlaku juga untuk hasil TEMPEL (Ctrl+V) dan hasil REKAM AKSI di tab CutMotions. Diuji dengan selftest baru `--selftest-uid` (7 cek: unik, jumlah, langkah lama utuh, tampil di tabel, penyembuhan profil, nomor lanjut benar, tambah setelah muat tetap unik).

### Baru v5.7: pilih banyak langkah + desain makin modern & elegan

1. **Pilih banyak langkah sekaligus** — tahan **`Shift`** lalu klik = pilih rentang baris; tahan **`Ctrl`** lalu klik = tambah/kurang baris satu per satu; **`Ctrl+A`** = pilih semua. Klik biasa kembali memilih satu baris seperti biasa.
2. **Aksi massal** — dengan banyak baris terpilih (tampil biru), panel PROPERTI berubah jadi panel aksi massal: **SALIN (Ctrl+C)** menyalin semua langkah terpilih, **TEMPEL (Ctrl+V)** menempel semuanya **berurutan & berantai** setelah baris acuan (campuran slot A-J + salinan + langkah "S" bisa ikut), **HAPUS (Del)** menghapus semuanya cukup 1× konfirmasi (langkah bawaan A-J selamat otomatis; di tab Studio semua bisa dihapus), dan di Studio **AKTIF/MATI** menyalakan/mematikan semuanya sekaligus. Klik kanan pada baris yang sudah ikut terpilih tidak merusak pilihan banyak — judul menunya menyesuaikan ("Salin 5 langkah terpilih").
3. **Desain makin modern & elegan** — semua tombol toolbar jadi **kapsul membulat dengan kilau lembut** (sorot terang saat kursor di atas, efek tekan, bentuk nonaktif jelas), semua panel jadi **kartu bersudut membulat** (toolbar, tabel, properti, VIDEO & CAPTION, WAKTU & UNGGAH), ada **header gradien** baru (judul + chip versi + hint hotkey), menu popup klik kanan ikut tema gelap, dan statusbar lebih rapi. Tata letak **maksimal 7 tombol per baris** tetap dipertahankan.

### Baru v5.6: tampilan "DARK GLASS" + REKAM AKSI di alur CutMotions

1. **Tampilan modern & mengkilat** — tema gelap navy dengan aksen neon (biru elektrik, hijau, merah) dan panel bergaya kaca (bingkai tipis, permukaan lebih terang). Tabel, heading, scroll bar, kotak isian, kotak centang, dan tab atas semuanya ikut tema gelap dengan teks kontras tinggi.
2. **Tombol dirapi: MAKSIMAL 7 per baris** — semua tombol fitur di kedua tab disusun ulang: maksimal 7 tombol menyamping, sisanya berurutan di baris di bawahnya. Tidak ada lagi toolbar yang memanjang tak teratur.
3. **REKAM AKSI kini juga di tab ALUR CUTMOTIONS (A-J)** — tombol merah **`● REKAM AKSI`** ada di toolbar kedua tab. Hasil rekaman di tab CutMotions **langsung masuk alur A-J, tepat setelah langkah yang dipilih** di tabel (tidak ada baris terpilih → di akhir alur). Berantai rapi sesuai urutan asli, berkode "S", bisa disunting di panel PROPERTI, ikut tersimpan di profil. Menu *Studio > ● Rekam Aksi di TAB AKTIF* mengikuti tab yang sedang dibuka.

### Baru v5.5: semua menu Studio Makro masuk ke alur CutMotions (A-J)

Di toolbar tab **ALUR CUTMOTIONS** ada tombol hijau **`+ TAMBAH LANGKAH ▾`** (dan klik kanan tabel → *Tambah langkah STUDIO di sini*) untuk menyisipkan **semua jenis langkah Studio** di posisi mana pun di antara langkah A–J:

| Menu | Aksi di dalam alur A-J |
|---|---|
| `+ KLIK TITIK` | Klik kiri/kanan/dobel + jumlah klik + geser per putaran |
| `+ JEDA / TUNGGU` | Tunggu N detik di tengah alur |
| `+ CARI GAMBAR` | Gambar referensi dicari (AREA FOKUS opsional) lalu diklik/dipindah |
| `+ KETIK TEKS` | Ketik teks + placeholder `{caption} {video} {no} {jumlah}` |
| `+ ISI TANGGAL-JAM` | Isi kolom tanggal rilis (dari kolom tab ini atau nilai tetap) |
| `+ ISI VIDEO & CAPTION` | Isi jumlah video / caption dasar + nama video baris ini |
| `+ TEKAN TOMBOL` | Enter/Tab/panah/Ctrl+A/… × jumlah tekan |
| `+ SCROLL` | Gulung Naik/Turun sejumlah gulungan |
| `+ CATATAN` | Penanda saja |
| `+ ULANGI MULAI/AKHIR` | Blok pengulangan sepotong alur (bisa bersarang) |

Langkah sisipan berkode **"S"** (ungu) di tabel, disunting di panel **PROPERTI LANGKAH** yang sama persis dengan Studio (termasuk POTONG GAMBAR & PILIH AREA FOKUS), **ikut tersimpan di profil**, SALIN/TEMPEL/HAPUS seperti biasa, dan **dijalankan tepat di posisinya** — termasuk di dalam fase caption per baris video: geser turun otomatis mengikuti JARAK ANTAR BARIS dan teks placeholder mengikuti baris yang sedang diproses.

## Menjalankan dari source (opsional)

```bat
JALANKAN.bat          :: auto-install pynput + pillow + opencv lalu jalan
build_exe.bat         :: bangun dist\CutUploaderPro.exe (OpenCV ikut dibungkus)
BANGUN-INSTALLER.bat  :: bangun dist\CutUploaderPro-Setup.exe (butuh Inno Setup 6)
```

`requirements.txt`: `pynput`, `pillow`, `opencv-python`, `pyinstaller` (dev).

## Perubahan v6.2

- **Kartu VIDEO & CAPTION STUDIO** baru di tab Studio Makro (`StudioMakroTab`): UI sama seperti kartu CutMotions — PILIH/TAMBAH/HAPUS TERPILIH/KOSONGKAN, listbox bernomor, TANGGAL & JAM RILIS, JUMLAH VIDEO otomatis, CAPTION DASAR + pratinjau, dan pilihan **AMBIL DATA DARI** (`SUMBER_DATA_OPSI`: Otomatis / Studio Makro (tab ini) / Tab CutMotions, bawaan Otomatis).
- **State & persistensi baru**: `video_terpilih`, `video_dir_ingat`, vars `jumlah/caption/tanggal/sumber_data`; `_kartu_data()`/`_pasang_kartu()`; ikut dalam **auto-save makro** (`makro_terakhir.json` kunci `"kartu"` — dipulihkan walau daftar langkah kosong), **SIMPAN MAKRO**, dan **BUKA MAKRO** (file lama tanpa kartu aman).
- **Sumber data F6 Studio**: helper baru `_data_sumber()` — mode Otomatis memilih nilai Studio dulu lalu CutMotions per kolom; mode Studio/CutMotions memakai satu sumber penuh. `_start`/`_worker` kini mengirim `tanggal_studio` ke mesin.
- **Mesin langkah bersama**: `studio_jalankan_langkah()` menerima parameter `tanggal_studio` — langkah ISI TANGGAL-JAM dengan sumber *"Studio Makro (tab ini)"* mengetik tanggal dari kartu Studio (`SUMBER_TANGGAL_OPSI` kini 3 pilihan); alur CutMotions (`_eksekusi_studio`) juga meneruskannya. `_tambah("TANGGAL_JAM")` di tab Studio bawaan ke sumber Studio; di tab CutMotions tetap "Tab CutMotions".
- **Teks & bantuan**: detail langkah TANGGAL-JAM menyebut kartu sumbernya; penjelasan panel PROPERTI (kedua tab), pesan tanggal kosong, dan TENTANG diperbarui.
- Selftest baru **`--selftest-kartu`** (15 cek, semua True) + regresi penuh 12 selftest hijau.

## Perubahan v6.1

- **Kartu VIDEO & CAPTION dibangun ulang**: kolom FOLDER VIDEO + PILIH FOLDER diganti **VIDEO TERPILIH + daftar bernomor** dengan tombol **PILIH VIDEO...** (`askopenfilenames`, filter ekstensi video), **TAMBAH VIDEO...** (append anti-duplikat), **HAPUS TERPILIH** (buang baris tersorot), **KOSONGKAN**. `JUMLAH VIDEO` terisi otomatis mengikuti banyak pilihan.
- **State baru** `video_terpilih` (list path lengkap, urutan = urutan pilih) + `video_dir_ingat` (dialog pilih berikutnya terbuka di folder terakhir); ikut tersimpan di profil/settings (`video_terpilih`, `video_dir`).
- **Mesin**: `_start` memvalidasi daftar terpilih (kosong → pesan jelas; file hilang → tawarkan buang & lanjut), antrean = path lengkap sesuai urutan pilihan; langkah H mengetik **path lengkap terkutip** via `nama_file_dialog()` → dialog pilih file **boleh terbuka di folder mana pun**; riwayat kini mencatat **nama file** (kunci tetap tunggal "(video terpilih)", tidak lagi terikat folder); fase caption memakai nama pendek dari antrean/riwayat.
- **Data hilang otomatis**: `_finish` sukses (tidak warn) mengosongkan daftar video terpilih + menegaskan di status bar; bila alur dihentikan di tengah (warn), daftar dipertahankan untuk dilanjutkan.
- `antrian_video_studio()` kini memakai nama video terpilih (placeholder `{caption}/{video}` Studio ikut urutan pilihan); menu **Bersihkan Riwayat Folder Ini** diganti **Bersihkan Riwayat Upload**; teks bantuan & pesan tidak lagi menyebut wajibnya folder.
- Selftest baru **`--selftest-pilih`** (14 cek: daftar & urutan, jumlah otomatis, label status, folder ingatan, snapshot, simpan, muat profil, typing path terkutip, caption dari nama pendek, riwayat per nama lintas folder, antrean Studio, hapus baris, deteksi file hilang, pengosongan otomatis pasca-selesai).

## Perubahan v6.0

- **Akar masalah**: mesin tidak pernah mengetik nama file — langkah H hanya *klik video pertama + Shift+panah bawah*, sementara fase caption memakai daftar antrean urut nama A-Z. Mismatch muncul bila (1) dialog terurut tanggal/ukuran, atau (2) riwayat skip membuat antrean mulai dari video ke-N sementara klik memilih dari TERATAS dialog.
- **Perbaikan**: opsi **KETIK NAMA FILE** (bawaan AKTIF, `V["ketik_nama"]`). Di langkah H mesin kini menekan `Alt+N` → `Ctrl+A` → mengetik `"file1.mp4" "file2.mp4" ...` (helper baru `nama_file_dialog()`) → Enter otomatis HANYA bila klik bebas 2 = 0 atau langkah H2 dihapus (selain itu H2 tetap yang mengklik tombol *Buka*).
- **Validasi F6**: posisi H (video pertama) tidak lagi wajib bila mode ketik aktif; langkah H lama tetap tersedia bila centang dimatikan.
- **Persistensi**: `ketik_nama` disimpan di profil/settings (`_kumpulkan_data`/`_terapkan_data`, bawaan True untuk profil lama); pesan selesai F6 kini menyebut cara pemilihan videonya.
- Selftest baru **`--selftest-ketik`** (10 cek: teks dialog, kosong, spasi, var bawaan, snapshot, simpan, muat tanpa kunci → True, muat False → False, H jadi opsional, caption cocok dengan antrean).

## Perubahan v5.9

- **Validasi F6 per kolom** (`_baca_angka`): kolom kosong → nilai standar; koma diterima; isian bukan angka → pesan menunjuk kolom spesifik + isinya (dulu: satu pesan generik "JUMLAH VIDEO dan pengaturan WAKTU harus diisi dengan angka" untuk 5 kolom sekaligus).
- **Sanitasi saat memuat profil** (`_terapkan_data`): 12 kolom angka diperiksa — nilai rusak dari profil lama dibuang dan kembali ke bawaan.
- **Langkah bawaan A-J bisa dihapus** (`slot_mati`): HAPUS/Del + klik kanan kini menerima slot bawaan; slot mati hilang dari tabel (`_urutan_lengkap` melewati barisnya, langkah tambahan yang menempel tetap tampil & jalan), mesin melewatinya (`_langkah_klik` → "skip"; blok G juga mematikan scroll-nya), validasi posisi wajib mengecualikannya; tersimpan di profil (`slot_mati`) dan **bisa dikembalikan** via menu klik kanan baru "Kembalikan langkah bawaan yang dihapus".
- Hapus salinan kini membuang SEMUA entri ber-uid (anti sisa dobel); pesan status hapus menyebutkan detail (salinan dihapus / bawaan dimatikan).
- Selftest baru **`--selftest-hapus`** (13 cek: parser angka 5×, hapus slot bawaan, tampilan tabel, langkah anak utuh, mesin skip, simpan-muat, kembalikan).

## Perubahan v5.8

- **Akar masalah**: saat memuat profil, `_extra_counter` diisi JUMLAH langkah tambahan (bukan nomor terbesar). Setelah langkah dihapus (uid jadi renggang, mis. tinggal x5 & x9) lalu aplikasi dibuka ulang, langkah baru mendapat nomor yang SUDAH DIPAKAI → baris baru tidak muncul di tabel (iid dobel) dan panel PROPERTI menampilkan langkah lama — terasa seperti "CARI GAMBAR hanya bisa ditambah 2x".
- **Perbaikan**: penentu uid baru `_uid_ekstra_baru()` selalu MELEWATI nomor yang sudah dipakai (anti-bentrok), dipakai di semua jalur pembuat langkah tambahan: `+ TAMBAH LANGKAH` / klik kanan (`_tambah_studio`), TEMPEL (`_tempel_langkah`), dan REKAM AKSI (`perekam_sisipkan`).
- **Pemuatan profil diperkuat** (`_terapkan_data`): nomor lanjut diambil dari uid TERBESAR; langkah ber-uid DOBEL (profil korban kutu lama) otomatis diberi nomor baru saat dimuat — penyembuhan tanpa manual.
- Selftest baru **`--selftest-uid`** (replika profil rusak deterministik + 10 tambahan CARI GAMBAR + paksa uid dobel lalu muat ulang).

## Perubahan v5.7

- **Multi-pilih langkah (kedua tab)**: tabel kini `selectmode="extended"` — Shift+Klik (rentang), Ctrl+Klik (toggle), Ctrl+A (semua), Ctrl+C / Ctrl+V / Del berfungsi massal. Panel PROPERTI menampilkan panel aksi massal "N LANGKAH DIPILIH" saat >1 baris terpilih.
- **Papan klip massal**: format baru `{"banyak": [item, ...]}` — urutan salin = urutan tampil di tabel; tempel massal **berantai** (anchor maju per langkah); format lama (1 langkah) tetap didukung penuh. Hapus massal menaut-ulang (re-chain) rantai `setelah` anak-anak langkah yang dihapus.
- **Perangkat desain v5.7**: helper warna `_campur/_cerahkan/_gelapkan`, `kotak_bulat()` (poligon smooth), kelas **`TombolKapsul`** (tombol kapsul Canvas dengan gradien kilau + hover + tekan + disabled, API ala tk.Button: config state/text/bg/fg/command), **`TombolMenu`** (pengganti tk.Menubutton untuk "+ TAMBAH LANGKAH"), **`KartuBulat`** (panel bersudut membulat pengganti LabelFrame), **`HeaderKilau`** (header gradien + chip versi), dan `menu_gelap()` untuk popup menu.
- Semua toolbar/panel di kedua tab dipindah ke kartu membulat; `_tb_btn` kini memakai TombolKapsul; panel properti multi = `render_properti_multi()`; selftest baru `--selftest-multi` (8 cek salin/tempel/hapus/aktif-mati massal di kedua tab).
- Diuji: 36 unit test baru (helper warna, kotak membulat, TombolKapsul state/klik/width, KartuBulat, HeaderKilau, panel massal, selectmode extended), regresi v5.1–v5.6 tetap hijau (26+39+28+46+53+52), 7 selftest Xvfb, uji visual 11/11 + 3 screenshot.

## Perubahan v5.6

- **Tema baru "DARK GLASS"**: palet navy pekat + neon (`#0B1020` / biru elektrik / hijau / merah), kartu bergaris bingkai tipis, tabel zebra gelap, heading & scroll bar gelap, kursor + seleksi kotak isian putih, tab atas gelap dengan tab aktif biru elektrik.
- **Tata letak tombol baru**: toolbar Studio (2 baris: 7 + 7 dan 7 + 5) dan toolbar CutMotions (2 baris: 7 + 4) — **maksimal 7 tombol per baris**, sisanya berurutan di bawah, persis seperti permintaan.
- **REKAM AKSI di ALUR CUTMOTIONS**: mesin rekam v5.4 dijadikan **mixin bersama `PerekamAksiMixin`** — dipakai Studio Makro DAN tab CutMotions. Di tab CutMotions, hasil rekaman disisipkan ke `langkah_extra` berantai `setelah` (urutan tampil + urutan eksekusi konsisten), otomatis tersimpan di profil, dan bisa disunting di panel PROPERTI langkah Studio.
- Tombol **`● REKAM AKSI`** (merah) di toolbar kedua tab; selagi merekam F6/F7/ESC diabaikan di kedua tab; saat menutup aplikasi perekam kedua tab ikut dihentikan.
- Diuji: 52 unit test baru (palet, mixin, sisip-rekam CutMotions & Studio, dedup, selftest terdaftar), regresi v5.1–v5.5 tetap hijau (26+39+28+46+53), 6 selftest Xvfb, 2 uji E2E input sungguhan pynput (Studio 16/16 + CutMotions 21/21), uji visual 20/20.

## Perubahan v5.5

- **SEMUA MENU STUDIO MAKRO kini bisa dimasukkan ke alur CUTMOTIONS (A-J)** — tombol hijau **`+ TAMBAH LANGKAH ▾`** baru di toolbar tab Alur CutMotions (plus submenu *klik kanan tabel → Tambah langkah STUDIO di sini*, dan menu *Alat*). Pilih salah satu: KLIK TITIK, JEDA/TUNGGU, CARI GAMBAR, KETIK TEKS, ISI TANGGAL-JAM, ISI VIDEO & CAPTION, TEKAN TOMBOL, SCROLL, CATATAN, ULANGI-MULAI, ULANGI-AKHIR — langkahnya disisipkan **SETELAH baris terpilih** dan dijalankan **tepat di posisinya** dalam alur.
- **Langkah berkode "S" (ungu) di tabel** dengan panel PROPERTI lengkap ala Studio: posisi klik-dulu + AMBIL/LIHAT, teks + placeholder, GAMBAR REFERENSI + thumbnail + **POTONG GAMBAR** + **PILIH AREA FOKUS** (seret kotak di layar) + KOSONGKAN + **TES CARI**, jumlah klik/tombol/scroll, jeda, aktif-mati.
- **Blok ULANGI di dalam alur A-J** — ULANGI-MULAI/AKHIR bisa membungkus sepotong langkah sisipan (mis. klik + ketik + scroll) dan diulang N kali atau mengikuti jumlah video; ada penjaga anti loop-tak-berujung.
- **Fase caption per baris ikut pintar**: langkah Studio yang disisipkan setelah I1/I2/I3 otomatis **bergeser mengikuti JARAK ANTAR BARIS** dan placeholder `{caption}/{video}/{no}/{jumlah}` mengikuti baris video yang sedang diproses — sama seperti salinan langkah lama.
- **SALIN/TEMPEL untuk langkah Studio** di tab CutMotions (Ctrl+C/Ctrl+V) — semua parameter ikut tersalin; profil makro (SIMPAN/BUKA PROFIL) menyertakan langkah-langkah ini dan dimuat ulang dengan sanitasi penuh (macro lama tetap kompatibel).
- CARI GAMBAR versi Studio di alur A-J ikut tervalidasi saat JALANKAN (file gambar harus ada; opencv tidak terpasang → langkah dilewati dengan pesan), dan pilihan *Stop alur* kini benar-benar menghentikan seluruh alur A-J (sebelumnya sisa salinan berhenti tapi fase berikutnya masih jalan).
- Mesin eksekusi langkah Studio kini **satu fungsi bersama** untuk kedua tab (perilaku Studio tidak berubah; diuji ulang 53 unit test + 28/39/45 regresi + selftest).

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
