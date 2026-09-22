# -*- coding: utf-8 -*-
"""
============================================================
  CUTUPLOADER PRO  v4.1  -  MACRO EDITION
  Aplikasi desktop uploader video batch otomatis
  khusus untuk situs CutMotions (Kwai)
------------------------------------------------------------
  Tampilan baru ala Jitbit Macro Recorder:
    - Toolbar Jalankan / Berhenti / Tes Cari / Potong Gambar
    - Tabel langkah makro A-J (klik baris -> edit di panel
      Properti Langkah di bawahnya)
    - JEDA bisa diatur per langkah (jeda sebelum langkah)
      dan jeda antar klik di dalam satu langkah
    - Tema Windows klasik yang ringan dan familiar

  Alur situs yang diikuti aplikasi ini (urutan posisi A-J):
    1. Login manual (email / kata sandi)
    2. Pilih "Versi lama"  ->  "Rilis karya"
    3. Tekan F6, lalu aplikasi mengerjakan:
       A  Klik tombol "Jadwal rilis / publikasi"
       B  Klik dropdown "NEGARA"
       C  Pilih negara - klik biasa ATAU pencarian gambar
          referensi dalam radius (mis. tulisan "Indonesia")
       D  Klik kolom tanggal, lalu ketik tanggal-jam otomatis
          (format: 2026-09-10 02:05:01)
       E  Klik "OKE"
       F  Klik "+ Tambah video" (dialog pilih file terbuka)
       G  Klik bebas berulang (0-500x) dan/atau scroll (0-50x)
       H  Klik video pertama + tahan SHIFT + panah bawah
          (jumlah video - 1)x  -> 5 sampai 20 video terpilih
       H2 Klik bebas (mis. tombol "Buka" pada dialog file)
       I  Caption per video: klik "Edit" -> klik kotak
          caption -> ketik caption -> klik "Konfirmasi";
          posisi klik otomatis bergeser turun per baris
          (5 video = diulang 5x, 20 video = 20x)
       J  Klik "SUBMIT"

  Batas situs: maksimal 20 video / sekali jalan,
  judul video maksimal 250 karakter.

  Hotkey:
    F6         : Mulai
    F7 / ESC   : Berhenti

  Distribusi:
    - Installer Windows : CutUploaderPro-Setup.exe (tanpa Python)
    - EXE portabel      : CutUploaderPro.exe
    - Skrip Python      : butuh Python 3.9+ (lihat PANDUAN.txt)

  Dibuat dengan Python + tkinter + pynput (+ OpenCV/Pillow
  untuk pencarian gambar negara).
  Fokus utama: Windows desktop.
============================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time
import json
import datetime
import os
import sys
import shutil

# Tampilan tajam & koordinat presisi di layar Windows High-DPI.
# Penting supaya posisi klik dan hasil screenshot cocok 1:1
# meski skala Windows 125% / 150%.
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

# ------------------------------------------------------------
# Library pynput: pengendali keyboard & mouse global
# ------------------------------------------------------------
PYNPUT_OK = False
IMPORT_ERROR = ""
try:
    from pynput import keyboard as kb_mod
    from pynput.keyboard import Controller as KeyboardController, Key
    from pynput.mouse import Controller as MouseController, Button
    PYNPUT_OK = True
except Exception as _e:
    IMPORT_ERROR = str(_e)

# ------------------------------------------------------------
# Pencarian gambar di layar (dipakai untuk memilih NEGARA
# lewat gambar referensi - template matching OpenCV).
# ------------------------------------------------------------
CV_OK = False
try:
    import cv2
    import numpy as np
    from PIL import ImageGrab
    CV_OK = True
except Exception:
    CV_OK = False

PIL_OK = False
try:
    from PIL import Image, ImageTk
    PIL_OK = True
except Exception:
    PIL_OK = False

APP_NAME = "CutUploader Pro"
APP_VERSION = "4.1"

VIDEO_EXTS = (".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v",
              ".3gp", ".flv", ".wmv", ".ts")

MAX_BATCH = 20    # batas situs: maks 20 video sekali upload
JUDUL_MAX = 250   # batas karakter judul video di situs


def app_dir():
    """Folder tempat aplikasi berada (aman juga saat sudah jadi .exe)."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


def data_dir():
    """Folder data milik user yang SELALU bisa ditulisi.

    PENTING: saat aplikasi ter-install di C:\\Program Files,
    Windows melarang user biasa menulis file ke folder itu
    (Errno 13 Permission denied). Semua file yang DITULIS
    aplikasi - settings, riwayat, gambar referensi hasil
    potongan - wajib disimpan di folder data ini, BUKAN di
    folder aplikasi.
    """
    base = os.getenv("LOCALAPPDATA") or os.getenv("APPDATA")
    if base:
        d = os.path.join(base, "CutUploaderPro")
    else:
        d = os.path.join(os.path.expanduser("~"), ".cutuploaderpro")
    try:
        os.makedirs(d, exist_ok=True)
        # pastikan benar-benar bisa ditulisi (uji tulis kecil)
        probe = os.path.join(d, ".tes_tulis")
        with open(probe, "w") as f:
            f.write("ok")
        os.remove(probe)
    except Exception:
        d = app_dir()
    return d


def _migrasi_file_lama(nama):
    """Pindahkan settings/riwayat lama dari folder aplikasi
    (mis. Program Files / folder EXE lama) ke folder data user,
    sekali saja - supaya pengguna lama tidak kehilangan setting."""
    try:
        lama = os.path.join(app_dir(), nama)
        baru = os.path.join(data_dir(), nama)
        if os.path.isfile(lama) and not os.path.isfile(baru):
            shutil.copyfile(lama, baru)
    except Exception:
        pass


SETTINGS_FILE = os.path.join(data_dir(), "cutuploader_settings.json")
RIWAYAT_FILE = os.path.join(data_dir(), "cutuploader_riwayat.json")
_migrasi_file_lama("cutuploader_settings.json")
_migrasi_file_lama("cutuploader_riwayat.json")

# ------------------------------------------------------------
# Tema warna: Windows klasik ala Jitbit Macro Recorder
# (terang, rapi, familiar bagi pengguna Windows)
# ------------------------------------------------------------
C_BG      = "#F0F0F0"   # latar jendela
C_PANEL   = "#FFFFFF"   # latar tabel / kotak isian
C_LINE    = "#C9CDD4"   # garis bingkai
C_BLUE    = "#2F6DB5"   # aksen utama (biru Jitbit)
C_BLUE_D  = "#25558F"
C_BLUE_L  = "#E3EDF9"   # sorotan lembut
C_RED     = "#C0392B"
C_RED_D   = "#992D22"
C_GREEN   = "#1E7B34"
C_ORANGE  = "#B26A00"
C_TEXT    = "#1C1C1C"
C_MUTED   = "#6B7078"
C_STRIPE  = "#F3F6FA"   # garis zebra tabel
C_SELROW  = "#D8E6F8"

F_TITLE = ("Segoe UI", 14, "bold")
F_H     = ("Segoe UI", 10, "bold")
F_N     = ("Segoe UI", 10)
F_S     = ("Segoe UI", 9)
F_XS    = ("Segoe UI", 8)
F_MONO  = ("Consolas", 9)

# ------------------------------------------------------------
# Definisi 13 slot posisi klik di situs CutMotions (urutan A-J)
#   (kunci, label pendek, wajib?, nama lengkap)
# ------------------------------------------------------------
POSISI_DEF = [
    ("pos_jadwal",     "A - Jadwal rilis",        True,
     "TOMBOL 'JADWAL RILIS / PUBLIKASI'"),
    ("pos_negara",     "B - Dropdown NEGARA",     True,
     "DROPDOWN / KOTAK 'NEGARA' (sebelum daftar terbuka)"),
    ("pos_pilih_neg",  "C - Pilih negara",        True,
     "ITEM 'INDONESIA' PADA DAFTAR NEGARA (atau titik klik biasa "
     "bila tidak memakai pencarian gambar)"),
    ("pos_tanggal",    "D - Kolom tanggal-jam",   True,
     "KOLOM TANGGAL & JAM RILIS (tanggal-jam diketik otomatis)"),
    ("pos_oke",        "E - Tombol OKE",          True,
     "TOMBOL 'OKE' PADA DIALOG JADWAL"),
    ("pos_tambah",     "F - + Tambah video",      True,
     "TOMBOL '+ TAMBAH VIDEO'"),
    ("pos_bebas1",     "G - Klik bebas 1",        True,
     "TITIK KLIK BEBAS DI DIALOG PILIH FILE (bisa diulang + scroll)"),
    ("pos_video",      "H - Video pertama",       True,
     "VIDEO PERTAMA DI DAFTAR FILE (diklik, lalu Shift+panah bawah)"),
    ("pos_bebas2",     "H2 - Klik bebas 2",       True,
     "TOMBOL 'BUKA/OPEN' / KLIK BEBAS SETELAH VIDEO TERPILIH"),
    ("pos_edit",       "I1 - EDIT baris-1",       True,
     "TOMBOL 'EDIT' PADA BARIS VIDEO TERATAS"),
    ("pos_judul",      "I2 - Kotak caption baris-1", True,
     "KOTAK CAPTION / JUDUL PADA BARIS TERATAS (saat editor terbuka)"),
    ("pos_konfirmasi", "I3 - Konfirmasi (opsional)", False,
     "TOMBOL 'KONFIRMASI' BARIS TERATAS - KOSONGKAN bila letaknya "
     "sama dengan tombol EDIT (I1)"),
    ("pos_submit",     "J - Tombol SUBMIT",       True,
     "TOMBOL 'SUBMIT / KIRIM' (halaman sudah discroll ke bawah)"),
]
POS_KUNCI = [p[0] for p in POSISI_DEF]
POS_WAJIB = [p[0] for p in POSISI_DEF if p[2]]
JUDUL_POSISI = {p[0]: p[3] for p in POSISI_DEF}
LABEL_POSISI = {p[0]: p[1] for p in POSISI_DEF}
SLOT_JADWAL = ("pos_jadwal", "pos_negara", "pos_pilih_neg",
               "pos_tanggal", "pos_oke")
SLOT_KODE = {
    "pos_jadwal": "A", "pos_negara": "B", "pos_pilih_neg": "C",
    "pos_tanggal": "D", "pos_oke": "E", "pos_tambah": "F",
    "pos_bebas1": "G", "pos_video": "H", "pos_bebas2": "H2",
    "pos_edit": "I1", "pos_judul": "I2", "pos_konfirmasi": "I3",
    "pos_submit": "J",
}


def jeda_default_per():
    """Jeda sebelum langkah (detik) untuk tiap slot - bisa diubah user."""
    return {k: 1.0 for k in POS_KUNCI}


def jeda_klik_default_per():
    """Jeda antar klik di dalam satu langkah (detik)."""
    d = {k: 0.30 for k in POS_KUNCI}
    d["pos_video"] = 0.15   # jeda antar tekanan panah bawah (Shift)
    return d


def compose_caption(caption, filename):
    """Gabungkan caption dasar + nama file.

    Contoh: caption '#dangdut', file 'melati.mp4' -> '#dangdut - melati'
    Jika caption kosong, cukup nama file saja.
    """
    name = os.path.splitext(os.path.basename(filename))[0]
    caption = (caption or "").strip()
    if caption:
        return "{} - {}".format(caption, name)
    return name


def daftar_video(folder):
    """Kembalikan daftar file video di folder, urut nama A->Z."""
    if not folder or not os.path.isdir(folder):
        return []
    hasil = []
    try:
        for nama in os.listdir(folder):
            lengkap = os.path.join(folder, nama)
            if os.path.isfile(lengkap) and \
                    nama.lower().endswith(VIDEO_EXTS):
                hasil.append(nama)
    except Exception:
        pass
    hasil.sort(key=lambda s: s.lower())
    return hasil


def parse_tanggal(teks):
    """Rapikan '2026-09-10 02:05:01' (detik boleh dilewat).

    Kembalikan string format '%Y-%m-%d %H:%M:%S',
    atau None bila formatnya salah.
    """
    teks = (teks or "").strip()
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            return datetime.datetime.strptime(
                teks, fmt).strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    return None


def _angka(teks, bawaan, lo=None, hi=None):
    """Parse angka dari teks dengan aman (terima koma desimal)."""
    try:
        v = float(str(teks).strip().replace(",", "."))
    except (ValueError, TypeError):
        return bawaan
    if lo is not None:
        v = max(lo, v)
    if hi is not None:
        v = min(hi, v)
    return v


def cari_di_layar(gambar_path, cx, cy, radius, kemiripan=0.8):
    """Cari gambar referensi di layar dalam RADIUS piksel dari titik
    acuan (cx, cy) - dipakai untuk memilih negara lewat gambar.

    v4.0: multi-skala (tahan beda zoom), laporan error jelas,
    dan skor terbaik selalu dilaporkan supaya mudah dikoreksi.

    Kembalikan ((x, y, skor), "") saat ketemu,
    atau (None, pesan_penjelasan) saat gagal.
    """
    if not CV_OK:
        return None, ("opencv-python belum terpasang. Install lewat CMD: "
                      "pip install opencv-python  (atau pakai versi EXE "
                      "yang sudah menyatukannya)")
    try:
        tpl = cv2.imread(gambar_path)
        if tpl is None:
            return None, ("File gambar tidak bisa dibaca: "
                          + str(gambar_path))
        th, tw = tpl.shape[:2]
        if tw < 6 or th < 6:
            return None, "Gambar referensi terlalu kecil (minimal 6x6 px)."
        r = max(int(radius), tw // 2 + 20, th // 2 + 20)
        left = max(0, int(cx) - r)
        top = max(0, int(cy) - r)
        grab = ImageGrab.grab(bbox=(left, top, int(cx) + r, int(cy) + r))
        layar = np.array(grab)[:, :, ::-1].copy()   # RGB -> BGR
        if layar.shape[0] < th or layar.shape[1] < tw:
            return None, ("Area pencarian lebih kecil dari gambar - "
                          "perbesar RADIUS.")
        terbaik = None
        # Beberapa skala: zoom browser saat memotong gambar bisa
        # berbeda dengan zoom saat pencarian (penyebab error paling
        # umum pada template matching).
        for skala in (1.0, 0.9, 1.1, 0.8, 1.25, 0.7):
            if skala == 1.0:
                t = tpl
            else:
                try:
                    t = cv2.resize(tpl, (max(6, int(tw * skala)),
                                         max(6, int(th * skala))))
                except Exception:
                    continue
            hh, ww = t.shape[:2]
            if layar.shape[0] < hh or layar.shape[1] < ww:
                continue
            hasil = cv2.matchTemplate(layar, t, cv2.TM_CCOEFF_NORMED)
            _mn, skor, _mnloc, lok = cv2.minMaxLoc(hasil)
            kandidat = (left + lok[0] + ww // 2,
                        top + lok[1] + hh // 2, skor)
            if terbaik is None or skor > terbaik[2]:
                terbaik = kandidat
            if skor >= kemiripan:
                return kandidat, ""
        skor_b = terbaik[2] if terbaik else 0.0
        return None, ("Gambar tidak ditemukan (kemiripan terbaik "
                      "{:.0%}, ambang {:.0%}). Coba: potong ulang gambar "
                      "lewat tombol POTONG GAMBAR, perbesar RADIUS, atau "
                      "turunkan KEMIRIPAN ke 0.70.".format(
                          skor_b, kemiripan))
    except Exception as e:
        return None, "Error pencarian gambar: {}".format(e)


class CutUploaderApp:
    # ================== INISIALISASI ==================
    def __init__(self, root):
        self.root = root
        self.root.title("{} v{} - Macro Edition".format(APP_NAME,
                                                        APP_VERSION))
        self.root.configure(bg=C_BG)
        self.root.geometry("1000x880")
        self.root.minsize(920, 760)
        if sys.platform == "win32":
            try:
                self.root.iconbitmap(os.path.join(app_dir(), "icon.ico"))
            except Exception:
                pass

        self.stop_event = threading.Event()
        self.running = False

        # ---- data makro (profil aktif) ----
        self.posisi = {k: None for k in POS_KUNCI}
        self.jeda_per = jeda_default_per()        # jeda sebelum langkah
        self.jeda_klik_per = jeda_klik_default_per()  # jeda antar klik
        self.sel = "pos_jadwal"                   # slot terpilih di tabel
        self._loading = True                      # penjaga trace variabel
        self._loading_prop = False

        # ---- riwayat upload: {folder_lower: [nama file, ...]} ----
        # urutan isi riwayat = urutan baris video di situs (atas ke bawah)
        self.riwayat = {}

        # ---- variabel isian (StringVar agar mudah disimpan/muat) ----
        V = self.vars = {}
        for kunci, bawaan in [
            ("folder", ""), ("jumlah", "5"), ("caption", "#dangdut"),
            ("mundur", "5"), ("jeda_dialog", "2"), ("jeda_langkah", "1"),
            ("tunggu", "60"), ("tanggal", "2026-09-10 02:05:01"),
            ("radius", "300"), ("kemiripan", "0.80"),
            ("klik_bebas1", "2"), ("scroll_bebas1", "0"),
            ("arah_scroll", "Turun"), ("klik_bebas2", "1"),
            ("jarak_baris", "85"), ("klik_submit", "1"),
            ("gambar_ref", ""),
        ]:
            V[kunci] = tk.StringVar(value=bawaan)
        V["skip_uploaded"] = tk.BooleanVar(value=True)
        V["skip_jadwal"] = tk.BooleanVar(value=False)
        V["pakai_gambar"] = tk.BooleanVar(value=False)
        V["auto_kirim"] = tk.BooleanVar(value=True)
        for kunci in V:
            V[kunci].trace_add("write", self._terapkan_opts)

        self.pv = {}   # variabel panel properti (dibuat saat render)

        if PYNPUT_OK:
            self.kb = KeyboardController()
            self.mouse = MouseController()
            self._listener = kb_mod.Listener(on_press=self._on_key)
            self._listener.daemon = True
            self._listener.start()
        else:
            self.kb = None
            self.mouse = None

        self._build_ui()
        self._load_settings()
        self._load_riwayat()
        self._loading = False
        self._refresh_tabel()
        self._render_properti()
        self._update_count()
        self._update_preview()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ================== PEMBANGUNAN TAMPILAN ==================
    def _build_ui(self):
        # ----- Baris menu (ala aplikasi Windows) -----
        menubar = tk.Menu(self.root)
        m_berkas = tk.Menu(menubar, tearoff=0)
        m_berkas.add_command(label="Simpan Profil Makro...",
                             command=self._simpan_profil)
        m_berkas.add_command(label="Buka Profil Makro...",
                             command=self._buka_profil)
        m_berkas.add_separator()
        m_berkas.add_command(label="Keluar", command=self._on_close)
        menubar.add_cascade(label="Berkas", menu=m_berkas)

        m_alat = tk.Menu(menubar, tearoff=0)
        m_alat.add_command(label="Tes Cari Gambar (langkah C)",
                           command=self._tes_cari)
        m_alat.add_command(label="Potong Gambar Referensi (screenshot)",
                           command=self._potong_gambar)
        m_alat.add_separator()
        m_alat.add_command(label="Lihat Riwayat Upload...",
                           command=self._lihat_riwayat)
        m_alat.add_command(label="Bersihkan Riwayat Folder Ini",
                           command=self._bersihkan_riwayat)
        m_alat.add_separator()
        m_alat.add_command(label="Reset Semua Posisi",
                           command=self._reset_posisi)
        m_alat.add_command(label="Cek Kelengkapan Library",
                           command=self._cek_lengkap)
        menubar.add_cascade(label="Alat", menu=m_alat)

        m_bantu = tk.Menu(menubar, tearoff=0)
        m_bantu.add_command(label="Buka Panduan",
                            command=self._buka_panduan)
        m_bantu.add_command(label="Tentang", command=self._tentang)
        menubar.add_cascade(label="Bantuan", menu=m_bantu)
        self.root.config(menu=menubar)

        # ----- Statusbar paling bawah (dipack dulu supaya selalu tampak)
        status = tk.Frame(self.root, bg=C_BG, bd=1, relief="sunken")
        status.pack(side="bottom", fill="x")
        self.lbl_status = tk.Label(status, anchor="w", bg=C_BG, fg=C_GREEN,
                                   font=F_S, text="Siap - login manual dulu "
                                   "di situs (Versi lama > Rilis karya), "
                                   "lalu tekan F6")
        self.lbl_status.pack(side="left", fill="x", expand=True,
                             padx=6, pady=3)
        tk.Label(status, anchor="e", bg=C_BG, fg=C_MUTED, font=F_XS,
                 text="v{}  |  F6 = Mulai   F7/ESC = Berhenti".format(
                     APP_VERSION)).pack(side="right", padx=6)

        # ----- Strip WAKTU (di atas statusbar) -----
        w = tk.LabelFrame(self.root, text=" WAKTU & UNGGAH (detik) ",
                          bg=C_BG, fg=C_BLUE, font=F_H, bd=1,
                          relief="groove")
        w.pack(side="bottom", fill="x", padx=8, pady=(0, 4))
        row = tk.Frame(w, bg=C_BG)
        row.pack(fill="x", padx=8, pady=(4, 2))
        for kunci, label, lebar in [
            ("mundur", "MUNDUR SEBELUM MULAI", 5),
            ("jeda_dialog", "JEDA BUKA DIALOG/EDITOR", 5),
            ("jeda_langkah", "JEDA ANTAR LANGKAH (default)", 5),
            ("tunggu", "TUNGGU UPLOAD PER VIDEO", 6),
        ]:
            cell = tk.Frame(row, bg=C_BG)
            cell.pack(side="left", padx=(0, 12))
            tk.Label(cell, text=label, bg=C_BG, fg=C_MUTED,
                     font=F_XS, anchor="w").pack(anchor="w")
            tk.Entry(cell, textvariable=self.vars[kunci], width=lebar,
                     bg=C_PANEL, fg=C_TEXT, relief="solid", bd=1,
                     font=F_N, justify="center",
                     highlightthickness=0).pack(anchor="w", ipady=3)
        tk.Button(row, text="TERAPKAN JEDA ANTAR\nLANGKAH KE SEMUA "
                            "LANGKAH",
                  command=self._terapkan_jeda_semua, bg=C_BLUE_L,
                  fg=C_BLUE_D, font=F_XS, relief="raised", bd=1,
                  cursor="hand2", activebackground=C_SELROW).pack(
                      side="left", padx=(0, 12), pady=2)
        kol = tk.Frame(w, bg=C_BG)
        kol.pack(side="left", padx=(0, 4))
        tk.Checkbutton(kol, text="Lewati video yang sudah pernah "
                                 "terupload (riwayat otomatis)",
                       variable=self.vars["skip_uploaded"],
                       bg=C_BG, fg=C_TEXT, font=F_XS, anchor="w",
                       command=self._update_count).pack(anchor="w")
        tk.Checkbutton(kol, text="Lewati langkah JADWAL (A-E) - langsung "
                                 "ke 'Tambah video'",
                       variable=self.vars["skip_jadwal"],
                       bg=C_BG, fg=C_TEXT, font=F_XS,
                       anchor="w").pack(anchor="w")
        tk.Label(w, text="MUNDUR = persiapan sebelum mulai.  "
                         "JEDA BUKA DIALOG/EDITOR = menunggu dialog pilih "
                         "file / editor / dropdown terbuka.  "
                         "JEDA ANTAR LANGKAH = nilai awal kolom JEDA di "
                         "tabel (bisa dioverride per langkah).  "
                         "TUNGGU UPLOAD PER VIDEO dikali jumlah video.",
                 bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                 justify="left").pack(fill="x", padx=8, pady=(0, 4))

        # ----- Toolbar (ala Jitbit) -----
        tb = tk.Frame(self.root, bg=C_BG, bd=1, relief="raised")
        tb.pack(side="top", fill="x")
        self.btn_start = self._tb_btn(tb, "JALANKAN  (F6)", self._start,
                                      bg=C_BLUE, fg="white",
                                      aktif=C_BLUE_D)
        self.btn_stop = self._tb_btn(tb, "BERHENTI  (F7)", self._stop,
                                     bg=C_RED, fg="white",
                                     aktif=C_RED_D)
        self.btn_stop.config(state="disabled", disabledforeground="#F2C4BE")
        self._tb_pemisah(tb)
        self._tb_btn(tb, "TES CARI GAMBAR", self._tes_cari)
        self._tb_btn(tb, "POTONG GAMBAR REFERENSI", self._potong_gambar)
        self._tb_pemisah(tb)
        self._tb_btn(tb, "SIMPAN PROFIL", self._simpan_profil)
        self._tb_btn(tb, "BUKA PROFIL", self._buka_profil)

        # ----- Strip VIDEO & CAPTION -----
        v = tk.LabelFrame(self.root, text=" VIDEO & CAPTION ",
                          bg=C_BG, fg=C_BLUE, font=F_H, bd=1,
                          relief="groove")
        v.pack(side="top", fill="x", padx=8, pady=(6, 4))
        r1 = tk.Frame(v, bg=C_BG)
        r1.pack(fill="x", padx=8, pady=(4, 2))
        tk.Label(r1, text="FOLDER VIDEO", bg=C_BG, fg=C_MUTED,
                 font=F_XS, anchor="w").pack(side="left")
        tk.Entry(r1, textvariable=self.vars["folder"], bg=C_PANEL,
                 fg=C_TEXT, relief="solid", bd=1, font=F_N,
                 highlightthickness=0).pack(side="left", fill="x",
                                            expand=True, padx=6, ipady=3)
        tk.Button(r1, text="PILIH FOLDER...", command=self._pilih_folder,
                  bg=C_BLUE_L, fg=C_BLUE_D, font=F_XS, relief="raised",
                  bd=1, cursor="hand2",
                  activebackground=C_SELROW).pack(side="left", padx=2,
                                                  ipadx=6, ipady=2)
        r2 = tk.Frame(v, bg=C_BG)
        r2.pack(fill="x", padx=8, pady=(0, 2))
        tk.Label(r2, text="JUMLAH VIDEO (maks {}):".format(MAX_BATCH),
                 bg=C_BG, fg=C_MUTED, font=F_XS).pack(side="left")
        tk.Entry(r2, textvariable=self.vars["jumlah"], width=5,
                 bg=C_PANEL, fg=C_TEXT, relief="solid", bd=1, font=F_N,
                 justify="center",
                 highlightthickness=0).pack(side="left", padx=(4, 12),
                                            ipady=3)
        tk.Label(r2, text="CAPTION DASAR:", bg=C_BG, fg=C_MUTED,
                 font=F_XS).pack(side="left")
        tk.Entry(r2, textvariable=self.vars["caption"], width=28,
                 bg=C_PANEL, fg=C_TEXT, relief="solid", bd=1, font=F_N,
                 highlightthickness=0).pack(side="left", padx=(4, 12),
                                            ipady=3)
        self.lbl_count = tk.Label(r2, text="-", bg=C_BG, fg=C_BLUE,
                                  font=F_XS, anchor="w")
        self.lbl_count.pack(side="left", fill="x", expand=True)
        self.lbl_preview = tk.Label(v, text="-", bg=C_BG, fg=C_GREEN,
                                    font=F_MONO, anchor="w")
        self.lbl_preview.pack(fill="x", padx=8, pady=(0, 4))

        # ----- Area tengah: tabel langkah + panel properti -----
        paned = tk.PanedWindow(self.root, orient="vertical", sashwidth=5,
                               bg=C_LINE, bd=0)
        paned.pack(side="top", fill="both", expand=True, padx=8, pady=4)

        # ---- tabel langkah makro ----
        f_tb = tk.LabelFrame(paned, text=" LANGKAH MAKRO  (klik satu "
                             "baris lalu sunting di panel PROPERTI di "
                             "bawah) ", bg=C_BG, fg=C_BLUE, font=F_H,
                             bd=1, relief="groove")
        paned.add(f_tb, minsize=300, height=380, stretch="always")
        gaya = ttk.Style()
        try:
            gaya.theme_use("clam")
        except Exception:
            pass
        gaya.configure("Makro.Treeview", rowheight=26,
                       background=C_PANEL, fieldbackground=C_PANEL,
                       foreground=C_TEXT, font=F_N, borderwidth=0)
        gaya.configure("Makro.Treeview.Heading", font=F_H,
                       background="#E4E8EE", foreground=C_TEXT,
                       relief="raised")
        gaya.map("Makro.Treeview",
                 background=[("selected", C_BLUE)],
                 foreground=[("selected", "white")])
        kolom = ("no", "nama", "detail", "jeda", "ulang")
        self.tree = ttk.Treeview(f_tb, columns=kolom, show="headings",
                                 style="Makro.Treeview", selectmode="browse")
        for k, t, w_, a in [
            ("no", "#", 44, "center"),
            ("nama", "LANGKAH", 205, "w"),
            ("detail", "DETAIL / KOORDINAT", 330, "w"),
            ("jeda", "JEDA", 62, "center"),
            ("ulang", "ULANGI", 170, "w"),
        ]:
            self.tree.heading(k, text=t)
            self.tree.column(k, width=w_, anchor=a, stretch=(k == "detail"))
        vsb = ttk.Scrollbar(f_tb, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side="left", fill="both", expand=True,
                       padx=(6, 0), pady=(2, 6))
        vsb.pack(side="left", fill="y", pady=(2, 6), padx=(0, 6))
        self.tree.tag_configure("genap", background=C_STRIPE)
        self.tree.tag_configure("ganjil", background=C_PANEL)
        self.tree.bind("<<TreeviewSelect>>", self._on_pilih_baris)

        # ---- panel properti ----
        self.f_prop = tk.LabelFrame(paned, text=" PROPERTI LANGKAH ",
                                    bg=C_BG, fg=C_BLUE, font=F_H, bd=1,
                                    relief="groove")
        paned.add(self.f_prop, minsize=230, height=280, stretch="always")
        self.prop_body = tk.Frame(self.f_prop, bg=C_BG)
        self.prop_body.pack(fill="both", expand=True, padx=8, pady=(2, 6))

    # ---------- pembantu tampilan ----------
    def _tb_btn(self, parent, teks, cmd, bg=None, fg=None, aktif=None):
        b = tk.Button(parent, text=teks, command=cmd,
                      bg=bg or C_BG, fg=fg or C_TEXT,
                      font=("Segoe UI", 9, "bold"), relief="flat", bd=1,
                      padx=12, pady=5, cursor="hand2",
                      activebackground=aktif or C_SELROW,
                      activeforeground=fg or C_TEXT)
        b.pack(side="left", padx=(2, 2), pady=2)
        b.bind("<Enter>", lambda e: b.config(relief="raised"))
        b.bind("<Leave>", lambda e: b.config(relief="flat"))
        return b

    def _tb_pemisah(self, parent):
        tk.Frame(parent, bg=C_LINE, width=2).pack(side="left", fill="y",
                                                  padx=4, pady=4)

    def _baris_prop(self, label, lebar_label=30):
        """Satu baris kontrol di panel properti."""
        row = tk.Frame(self.prop_body, bg=C_BG)
        row.pack(fill="x", pady=1)
        tk.Label(row, text=label, bg=C_BG, fg=C_MUTED, font=F_XS,
                 width=lebar_label, anchor="e").pack(side="left",
                                                     padx=(0, 6))
        return row

    def _ent_prop(self, row, var, lebar=8, tengah=True):
        e = tk.Entry(row, textvariable=var, width=lebar, bg=C_PANEL,
                     fg=C_TEXT, relief="solid", bd=1, font=F_N,
                     justify="center" if tengah else "left",
                     highlightthickness=0)
        e.pack(side="left", ipady=3)
        return e

    def _btn_prop(self, row, teks, cmd, bg=C_BLUE_L, fg=C_BLUE_D):
        b = tk.Button(row, text=teks, command=cmd, bg=bg, fg=fg,
                      font=F_XS, relief="raised", bd=1, cursor="hand2",
                      activebackground=C_SELROW, activeforeground=fg)
        b.pack(side="left", padx=(6, 0), ipadx=6, ipady=2)
        return b

    # ================== TABEL LANGKAH ==================
    def _detail_slot(self, kunci):
        pos = self.posisi.get(kunci)
        pos_t = "({},{})".format(pos[0], pos[1]) if pos else "belum diatur"
        V = self.vars
        if kunci == "pos_pilih_neg":
            if V["pakai_gambar"].get():
                g = os.path.basename(V["gambar_ref"].get()) \
                    if V["gambar_ref"].get() else "(gambar belum dipilih)"
                return "{} | gambar: {} | radius {} px | mirip {}".format(
                    pos_t, g, V["radius"].get(), V["kemiripan"].get())
            return pos_t + " | klik biasa"
        if kunci == "pos_tanggal":
            return "{} | ketik: {}".format(pos_t, V["tanggal"].get())
        if kunci == "pos_bebas1":
            return "{} | {} klik + {} scroll {}".format(
                pos_t, V["klik_bebas1"].get(), V["scroll_bebas1"].get(),
                V["arah_scroll"].get())
        if kunci == "pos_video":
            return "{} | Shift+turun otomatis".format(pos_t)
        if kunci == "pos_bebas2":
            return "{} | {} klik".format(pos_t, V["klik_bebas2"].get())
        if kunci == "pos_konfirmasi":
            return "{} | jarak antar baris {} px".format(
                pos_t, V["jarak_baris"].get())
        if kunci == "pos_submit":
            return "{} | {} klik".format(pos_t, V["klik_submit"].get())
        return pos_t

    def _ulang_slot(self, kunci):
        V = self.vars
        if kunci == "pos_pilih_neg":
            return "cari gambar" if V["pakai_gambar"].get() else "1 klik"
        if kunci == "pos_tanggal":
            return "klik + ketik"
        if kunci == "pos_bebas1":
            return "{} klik + {}x scroll".format(V["klik_bebas1"].get(),
                                                 V["scroll_bebas1"].get())
        if kunci == "pos_video":
            return "Shift+turun (batch)"
        if kunci == "pos_bebas2":
            return "{} klik".format(V["klik_bebas2"].get())
        if kunci == "pos_konfirmasi":
            return "per video (jarak {} px)".format(V["jarak_baris"].get())
        if kunci == "pos_submit":
            return "{} klik".format(V["klik_submit"].get())
        return "1 klik"

    def _refresh_tabel(self):
        if not hasattr(self, "tree"):
            return
        anak = self.tree.get_children()
        if anak:
            self.tree.delete(*anak)
        for i, (kunci, label, _w, _ket) in enumerate(POSISI_DEF):
            self.tree.insert("", "end", iid=kunci, tags=(
                "genap" if i % 2 == 0 else "ganjil",), values=(
                SLOT_KODE.get(kunci, kunci),
                label, self._detail_slot(kunci),
                "{:.1f}s".format(self.jeda_per.get(kunci, 1.0)),
                self._ulang_slot(kunci)))
        if self.sel in POS_KUNCI:
            try:
                self.tree.selection_set(self.sel)
                self.tree.see(self.sel)
            except Exception:
                pass

    def _on_pilih_baris(self, _ev=None):
        sel = self.tree.selection()
        if sel:
            self.sel = sel[0]
            self._render_properti()

    # ================== PANEL PROPERTI ==================
    def _render_properti(self):
        self._loading_prop = True
        for wdg in self.prop_body.winfo_children():
            wdg.destroy()
        kunci = self.sel
        if kunci not in POS_KUNCI:
            self._loading_prop = False
            return
        label = LABEL_POSISI[kunci]
        ket = JUDUL_POSISI[kunci]

        kepala = tk.Frame(self.prop_body, bg=C_BG)
        kepala.pack(fill="x", pady=(0, 4))
        tk.Label(kepala, text="{}   -   {}".format(label, ket), bg=C_BG,
                 fg=C_TEXT, font=F_H, anchor="w",
                 wraplength=860, justify="left").pack(fill="x")

        # ---- posisi X / Y + AMBIL + LIHAT ----
        pos = self.posisi.get(kunci)
        self.pv = {
            "x": tk.StringVar(value=str(pos[0]) if pos else ""),
            "y": tk.StringVar(value=str(pos[1]) if pos else ""),
            "jeda": tk.StringVar(value="{:.1f}".format(
                self.jeda_per.get(kunci, 1.0))),
            "jeda_klik": tk.StringVar(value="{:.2f}".format(
                self.jeda_klik_per.get(kunci, 0.3))),
        }
        r = self._baris_prop("POSISI X , Y")
        self._ent_prop(r, self.pv["x"], 6)
        tk.Label(r, text=",", bg=C_BG, fg=C_MUTED,
                 font=F_N).pack(side="left", padx=2)
        self._ent_prop(r, self.pv["y"], 6)
        self._btn_prop(r, "AMBIL (5 dtk)",
                       lambda k=kunci: self._ambil_posisi(k))
        self._btn_prop(r, "LIHAT",
                       lambda k=kunci: self._lihat_posisi(k), bg=C_BG)
        tk.Label(r, text="bisa juga diketik manual", bg=C_BG, fg=C_MUTED,
                 font=F_XS).pack(side="left", padx=6)

        # ---- jeda per langkah ----
        r = self._baris_prop("JEDA SEBELUM LANGKAH (detik)")
        self._ent_prop(r, self.pv["jeda"], 6)
        tk.Label(r, text="JEDA ANTAR KLIK (detik)", bg=C_BG, fg=C_MUTED,
                 font=F_XS).pack(side="left", padx=(12, 4))
        self._ent_prop(r, self.pv["jeda_klik"], 6)
        tk.Label(r, text="jeda antar klik berulang / panah Shift "
                         "di langkah ini", bg=C_BG, fg=C_MUTED,
                 font=F_XS).pack(side="left", padx=6)

        # ---- kontrol khusus per slot ----
        V = self.vars
        if kunci == "pos_pilih_neg":
            tk.Checkbutton(self.prop_body,
                           text="Pilih negara pakai PENCARIAN GAMBAR - "
                                "cari potongan layar (mis. tulisan "
                                "'Indonesia') dalam radius, lalu diklik",
                           variable=V["pakai_gambar"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x", pady=(4, 0))
            r = self._baris_prop("GAMBAR REFERENSI")
            self._ent_prop(r, V["gambar_ref"], 42, tengah=False)
            self._btn_prop(r, "PILIH GAMBAR...", self._pilih_gambar_ref)
            self._btn_prop(r, "POTONG GAMBAR...", self._potong_gambar)
            r = self._baris_prop("RADIUS (px) | KEMIRIPAN:")
            self._ent_prop(r, V["radius"], 6)
            self._ent_prop(r, V["kemiripan"], 6)
            self._btn_prop(r, "TES CARI SEKARANG", self._tes_cari)
            tk.Label(self.prop_body,
                     text="Tips: pakai POTONG GAMBAR supaya ukuran gambar "
                          "PERSIS seperti tampilan layar. Zoom browser "
                          "jangan diubah setelah gambar dipotong.",
                     bg=C_BG, fg=C_ORANGE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(
                         fill="x", pady=(4, 0))
        elif kunci == "pos_tanggal":
            r = self._baris_prop("TANGGAL & JAM RILIS")
            self._ent_prop(r, V["tanggal"], 22)
            tk.Label(r, text="format: 2026-09-10 02:05:01 "
                             "(detik boleh dilewat)", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=6)
        elif kunci == "pos_bebas1":
            r = self._baris_prop("JUMLAH KLIK (0-500)")
            self._ent_prop(r, V["klik_bebas1"], 6)
            tk.Label(r, text="JUMLAH SCROLL (0-50)", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=(12, 4))
            self._ent_prop(r, V["scroll_bebas1"], 6)
            tk.Label(r, text="ARAH SCROLL", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=(12, 4))
            tk.OptionMenu(r, V["arah_scroll"], "Turun",
                          "Naik").pack(side="left")
            tk.Label(self.prop_body,
                     text="Alternatif sesuai permintaan: klik bebas "
                          "berulang 1-500x, ATAU 1 klik lalu scroll "
                          "beberapa kali (isi klik=1, scroll=jumlah).",
                     bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(
                         fill="x", pady=(4, 0))
        elif kunci == "pos_bebas2":
            r = self._baris_prop("JUMLAH KLIK (0-20)")
            self._ent_prop(r, V["klik_bebas2"], 6)
            tk.Label(r, text="mis. tombol 'Buka' pada dialog file",
                     bg=C_BG, fg=C_MUTED, font=F_XS).pack(side="left",
                                                          padx=6)
        elif kunci == "pos_konfirmasi":
            r = self._baris_prop("JARAK ANTAR BARIS (piksel)")
            self._ent_prop(r, V["jarak_baris"], 6)
            tk.Label(self.prop_body,
                     text="Caption mengalir ke baris berikutnya otomatis: "
                          "5 video = 5x, 20 video = 20x. Bila tombol "
                          "Konfirmasi letaknya sama dengan Edit, kosongkan "
                          "X,Y pada slot ini (otomatis pakai titik Edit).",
                     bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(
                         fill="x", pady=(4, 0))
        elif kunci == "pos_submit":
            r = self._baris_prop("JUMLAH KLIK (1-10)")
            self._ent_prop(r, V["klik_submit"], 6)
            tk.Checkbutton(self.prop_body,
                           text="Klik SUBMIT otomatis di akhir (matikan "
                                "kalau mau cek dulu manual)",
                           variable=V["auto_kirim"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x", pady=(4, 0))

        self.lbl_ambil = tk.Label(self.prop_body, text="", bg=C_BG,
                                  fg=C_ORANGE, font=F_XS, anchor="w",
                                  wraplength=860, justify="left")
        self.lbl_ambil.pack(fill="x", pady=(4, 0))

        # ---- sambungkan perubahan -> simpan ----
        for var in self.pv.values():
            var.trace_add("write", self._terapkan_prop)
        self._loading_prop = False

    def _terapkan_prop(self, *_):
        if self._loading_prop or self.sel not in POS_KUNCI:
            return
        kunci = self.sel
        try:
            x = int(float(str(self.pv["x"].get()).strip() or "nan"))
            y = int(float(str(self.pv["y"].get()).strip() or "nan"))
            self.posisi[kunci] = [x, y]
        except (ValueError, TypeError):
            self.posisi[kunci] = None
        try:
            self.jeda_per[kunci] = max(0.0, float(
                str(self.pv["jeda"].get()).replace(",", ".")))
        except ValueError:
            pass
        try:
            self.jeda_klik_per[kunci] = max(0.05, float(
                str(self.pv["jeda_klik"].get()).replace(",", ".")))
        except ValueError:
            pass
        self._refresh_tabel()

    def _terapkan_opts(self, *_):
        """Variabel isian berubah -> segarkan tabel/pratinjau."""
        if self._loading:
            return
        if self.sel in POS_KUNCI:
            self._refresh_tabel()
        if hasattr(self, "lbl_count"):
            self._update_count()
            self._update_preview()

    def _terapkan_jeda_semua(self):
        v = _angka(self.vars["jeda_langkah"].get(), 1.0, 0.0, 3600)
        for k in POS_KUNCI:
            self.jeda_per[k] = v
        self._refresh_tabel()
        self._render_properti()
        self._set_status("Jeda {:.1f} detik diterapkan ke semua langkah "
                         "(kolom JEDA).".format(v), C_GREEN)

    # ================== AMBIL / LIHAT POSISI ==================
    def _tampilkan_info(self, teks, warna=C_ORANGE):
        if hasattr(self, "lbl_ambil") and self.lbl_ambil.winfo_exists():
            self.lbl_ambil.config(text=teks, fg=warna)

    def _ambil_posisi(self, kunci):
        if not PYNPUT_OK:
            messagebox.showerror(
                APP_NAME, "Library pynput belum terpasang.\n\n"
                          "Buka CMD lalu jalankan:\n  pip install pynput")
            return
        judul = LABEL_POSISI[kunci]

        def kerja():
            try:
                for s in range(5, 0, -1):
                    self.root.after(0, lambda s=s: self._tampilkan_info(
                        "Arahkan mouse ke {} dan diamkan... {}".format(
                            judul, s)))
                    self.root.after(0, lambda s=s: self._set_status(
                        "Ambil posisi {} ... {}".format(judul, s), C_ORANGE))
                    time.sleep(1)
                px, py = self.mouse.position

                def isi():
                    self.posisi[kunci] = [int(px), int(py)]
                    self._refresh_tabel()
                    if self.sel == kunci:
                        self._render_properti()
                    self._tampilkan_info(
                        "{} tersimpan: X={}, Y={}".format(judul, int(px),
                                                          int(py)), C_GREEN)
                    self._set_status(
                        "{} = ({}, {}) tersimpan.".format(judul, int(px),
                                                          int(py)), C_GREEN)
                    self._save_settings()

                self.root.after(0, isi)
            except Exception:
                self.root.after(0, lambda: self._tampilkan_info(
                    "Gagal mengambil posisi.", C_RED))

        threading.Thread(target=kerja, daemon=True).start()

    def _lihat_posisi(self, kunci):
        if not PYNPUT_OK:
            return
        pos = self.posisi.get(kunci)
        if not pos:
            messagebox.showinfo(APP_NAME,
                                "Posisi ini belum diatur. Klik dulu AMBIL "
                                "(atau isi X,Y manual).")
            return
        try:
            self.mouse.position = (pos[0], pos[1])
        except Exception:
            pass

    # ================== GAMBAR REFERENSI (LANGKAH C) ==================
    def _pilih_gambar_ref(self):
        f = filedialog.askopenfilename(
            title="Pilih gambar referensi (potongan layar tulisan "
                  "'Indonesia')",
            filetypes=[("Gambar", "*.png *.jpg *.jpeg *.bmp"),
                       ("Semua file", "*.*")])
        if f:
            self.vars["gambar_ref"].set(f)
            self._save_settings()
            self._tampilkan_info("Gambar referensi: "
                                 + os.path.basename(f), C_GREEN)

    def _potong_gambar(self):
        """Screenshot layar -> user seret kotak -> simpan PNG referensi.

        Ini kunci perbaikan 'cari gambar error': gambar referensi
        dipotong PERSIS dari tampilan layar yang hidup, ukurannya
        cocok 1:1 dengan hasil pencarian.
        """
        if not PIL_OK or not CV_OK:
            messagebox.showwarning(
                APP_NAME,
                "Fitur potong gambar butuh Pillow + OpenCV.\n\n"
                "Buka CMD lalu jalankan:\n"
                "  pip install pillow opencv-python")
            return

        def kerja():
            try:
                for s in range(3, 0, -1):
                    self.root.after(0, lambda s=s: self._set_status(
                        "Screenshot layar dalam {} detik - pastikan daftar "
                        "negara terbuka & terlihat...".format(s), C_ORANGE))
                    time.sleep(1)
                img = ImageGrab.grab()
                self.root.after(0, lambda: JendelaPotong(
                    self.root, img, self._gambar_terpotong))
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    APP_NAME, "Gagal mengambil screenshot:\n{}".format(e)))

        threading.Thread(target=kerja, daemon=True).start()

    def _gambar_terpotong(self, path):
        self.vars["gambar_ref"].set(path)
        self.vars["pakai_gambar"].set(True)
        self._save_settings()
        self._set_status("Gambar referensi tersimpan: {}".format(path),
                         C_GREEN)
        self._tampilkan_info("Gambar referensi baru: "
                             + os.path.basename(path), C_GREEN)

    def _tes_cari(self):
        """Tes pencarian gambar tanpa menjalankan seluruh alur."""
        if not PYNPUT_OK:
            messagebox.showerror(APP_NAME, "Library pynput belum terpasang.")
            return
        if not CV_OK:
            messagebox.showwarning(
                APP_NAME,
                "opencv-python belum terpasang - pencarian gambar tidak "
                "bisa dipakai.\n\nBuka CMD lalu jalankan:\n"
                "  pip install opencv-python\n\n"
                "Atau pakai CutUploaderPro.exe (OpenCV sudah menyatu).")
            return
        gambar = self.vars["gambar_ref"].get().strip()
        if not gambar or not os.path.isfile(gambar):
            messagebox.showinfo(
                APP_NAME,
                "Pilih dulu gambar referensinya.\n\nCara termudah: buka "
                "langkah C di tabel, klik 'POTONG GAMBAR...', lalu seret "
                "kotak di atas tulisan negaranya.")
            return
        pos = self.posisi.get("pos_pilih_neg")
        if not pos:
            messagebox.showinfo(APP_NAME,
                                "Atur dulu posisi C sebagai titik acuan "
                                "pencarian (AMBIL pada langkah C).")
            return
        radius = int(_angka(self.vars["radius"].get(), 300, 50, 2000))
        mirip = _angka(self.vars["kemiripan"].get(), 0.8, 0.5, 0.99)

        def kerja():
            self.root.after(0, lambda: self._set_status(
                "Mencari '{}' dalam radius {} px (multi-skala)...".format(
                    os.path.basename(gambar), radius), C_ORANGE))
            hasil, pesan = cari_di_layar(gambar, pos[0], pos[1],
                                         radius, mirip)

            def lapor():
                if hasil:
                    x, y, skor = hasil
                    try:
                        self.mouse.position = (x, y)
                    except Exception:
                        pass
                    self._set_status(
                        "TES OK: gambar KETEMU di ({}, {}) - kemiripan "
                        "{:.0%}. Mouse dipindah ke sana (tidak diklik)."
                        .format(x, y, skor), C_GREEN)
                    self._tampilkan_info(
                        "TES OK: ketemu di ({}, {}), kemiripan {:.0%}."
                        .format(x, y, skor), C_GREEN)
                else:
                    self._set_status("TES GAGAL: " + pesan, C_RED)
                    self._tampilkan_info("TES GAGAL: " + pesan, C_RED)
                    messagebox.showwarning(APP_NAME,
                                           "Gambar tidak ketemu.\n\n"
                                           + pesan)

            self.root.after(0, lapor)

        threading.Thread(target=kerja, daemon=True).start()

    # ================== FOLDER, JUMLAH, CAPTION ==================
    def _pilih_folder(self):
        folder = filedialog.askdirectory(title="Pilih folder video")
        if folder:
            self.vars["folder"].set(os.path.normpath(folder))
            self._save_settings()

    def _kunci_riwayat(self):
        return (self.vars["folder"].get().strip().lower()
                or "(tanpa folder)")

    def _riwayat_folder(self):
        return set(self.riwayat.get(self._kunci_riwayat(), []))

    def _update_count(self, *_):
        if not hasattr(self, "lbl_count"):
            return
        folder = self.vars["folder"].get().strip()
        semua = daftar_video(folder)
        if not folder:
            self.lbl_count.config(text="Folder belum dipilih.",
                                  fg=C_MUTED)
        elif not semua:
            self.lbl_count.config(
                text="Tidak ada file video di folder ini "
                     "(cari .mp4 .mov .avi dll).", fg=C_ORANGE)
        else:
            if self.vars["skip_uploaded"].get():
                sisa = [f for f in semua if f not in self._riwayat_folder()]
                self.lbl_count.config(
                    text="{} video (urut nama A-Z) - {} belum terupload."
                         .format(len(semua), len(sisa)), fg=C_BLUE)
            else:
                self.lbl_count.config(
                    text="{} video ditemukan (urut nama A-Z).".format(
                        len(semua)), fg=C_BLUE)

    def _update_preview(self, *_):
        if not hasattr(self, "lbl_preview"):
            return
        semua = daftar_video(self.vars["folder"].get().strip())
        if self.vars["skip_uploaded"].get() and semua:
            sudah = self._riwayat_folder()
            belum = [f for f in semua if f not in sudah]
            contoh = belum[0] if belum else semua[0]
        else:
            contoh = semua[0] if semua else "melati"
        teks = compose_caption(self.vars["caption"].get(), contoh)
        n = len(teks)
        self.lbl_preview.config(
            text="Pratinjau caption:  {}   ({}{}/{} kar)".format(
                teks, n, "!" if n > JUDUL_MAX else "", JUDUL_MAX),
            fg=C_RED if n > JUDUL_MAX else C_GREEN)

    # ================== RIWAYAT & ALAT ==================
    def _lihat_riwayat(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("Riwayat Upload")
        dlg.configure(bg=C_BG)
        dlg.geometry("560x420")
        dlg.transient(self.root)
        lb = tk.Listbox(dlg, bg=C_PANEL, fg=C_TEXT, font=F_N,
                        relief="solid", bd=1)
        lb.pack(fill="both", expand=True, padx=10, pady=(10, 4))
        kunci = self._kunci_riwayat()
        isi = self.riwayat.get(kunci, [])
        lb.insert("end", "Folder: {}".format(kunci))
        lb.insert("end", "Total {} video tercatat terupload "
                         "(urut baris situs):".format(len(isi)))
        lb.insert("end", "")
        for i, nama in enumerate(isi, 1):
            lb.insert("end", "{}. {}".format(i, nama))
        tk.Button(dlg, text="TUTUP", command=dlg.destroy, bg=C_BLUE,
                  fg="white", font=F_S, relief="flat", cursor="hand2",
                  activebackground=C_BLUE_D).pack(pady=(0, 10), ipadx=10,
                                                  ipady=4)

    def _bersihkan_riwayat(self):
        kunci = self._kunci_riwayat()
        n = len(self.riwayat.get(kunci, []))
        if n == 0:
            messagebox.showinfo(APP_NAME,
                                "Riwayat folder ini masih kosong.")
            return
        if messagebox.askyesno(
                APP_NAME,
                "Hapus riwayat {} video yang sudah terupload?\n\n"
                "Setelah dihapus, video yang sama bisa diupload ulang "
                "dari awal.".format(n)):
            self.riwayat.pop(kunci, None)
            self._save_riwayat()
            self._update_count()
            self._set_status("Riwayat folder ini dibersihkan.", C_GREEN)

    def _reset_posisi(self):
        if messagebox.askyesno(APP_NAME,
                               "Hapus SEMUA posisi klik (A-J)?\n"
                               "Pengaturan lain tidak ikut terhapus."):
            self.posisi = {k: None for k in POS_KUNCI}
            self._refresh_tabel()
            self._render_properti()
            self._save_settings()
            self._set_status("Semua posisi dikosongkan.", C_ORANGE)

    def _cek_lengkap(self):
        import importlib
        def cek(nama):
            try:
                importlib.import_module(nama)
                return "OK"
            except Exception as e:
                return "BELUM ({})".format(e)
        pesan = (
            "Kondisi library di komputer ini:\n\n"
            "pynput        : {}\n"
            "Pillow (PIL)  : {}\n"
            "opencv-python: {}\n\n"
            "Pencarian gambar (langkah C) butuh opencv-python + Pillow.\n"
            "Catatan: versi EXE/Setup sudah menyatukan semuanya, jadi "
            "tidak perlu install apa pun.".format(
                cek("pynput"), cek("PIL"), cek("cv2")))
        messagebox.showinfo(APP_NAME, pesan)

    def _buka_panduan(self):
        path = os.path.join(app_dir(), "PANDUAN.txt")
        try:
            if sys.platform == "win32":
                os.startfile(path)
            elif sys.platform == "darwin":
                os.system('open "{}"'.format(path))
            else:
                os.system('xdg-open "{}"'.format(path))
        except Exception:
            messagebox.showinfo(APP_NAME,
                                "Buka file ini secara manual:\n" + path)

    def _tentang(self):
        messagebox.showinfo(
            APP_NAME,
            "{} v{} - Macro Edition\n\n"
            "Uploader video batch otomatis untuk CutMotions (Kwai).\n"
            "Tampilan editor makro ala Jitbit Macro Recorder.\n\n"
            "Alur: Jadwal (A-E) > Tambah video + Shift+turun (F-H2) >\n"
            "Caption per baris (I) > Submit (J).\n\n"
            "Maksimal {} video sekali jalan (aturan situs).\n"
            "Login dilakukan manual - tidak ada data akun yang disimpan."
            .format(APP_NAME, APP_VERSION, MAX_BATCH))

    # ================== SIMPAN / BUKA PROFIL ==================
    def _simpan_profil(self):
        self._save_settings()
        f = filedialog.asksaveasfilename(
            title="Simpan profil makro (posisi + pengaturan)",
            defaultextension=".json",
            initialfile="profil_{}.json".format(
                datetime.datetime.now().strftime("%Y%m%d")),
            filetypes=[("Profil makro", "*.json")])
        if f:
            try:
                with open(SETTINGS_FILE, "r", encoding="utf-8") as s:
                    data = json.load(s)
                with open(f, "w", encoding="utf-8") as d:
                    json.dump(data, d, indent=2, ensure_ascii=False)
                self._set_status("Profil tersimpan: {}".format(f), C_GREEN)
            except Exception as e:
                messagebox.showerror(APP_NAME,
                                     "Gagal menyimpan profil:\n" + str(e))

    def _buka_profil(self):
        f = filedialog.askopenfilename(
            title="Buka profil makro",
            filetypes=[("Profil makro", "*.json"), ("Semua file", "*.*")])
        if not f:
            return
        try:
            with open(f, "r", encoding="utf-8") as s:
                data = json.load(s)
        except Exception as e:
            messagebox.showerror(APP_NAME,
                                 "Gagal membaca profil:\n" + str(e))
            return
        self._terapkan_data(data)
        self._save_settings()
        self._set_status("Profil dimuat: {}".format(f), C_GREEN)

    # ================== BANTUAN UI (THREAD-SAFE) ==================
    def _set_status(self, msg, color=C_GREEN):
        def do():
            try:
                self.lbl_status.config(text=msg, fg=color)
            except Exception:
                pass
        self.root.after(0, do)

    def _set_progress(self, msg):
        def do():
            try:
                self.lbl_status.config(text=msg, fg=C_BLUE)
            except Exception:
                pass
        self.root.after(0, do)

    def _sleep(self, seconds):
        """Tidur yang bisa dibatalkan kapan saja lewat tombol stop."""
        end = time.time() + seconds
        while not self.stop_event.is_set():
            remain = end - time.time()
            if remain <= 0:
                break
            time.sleep(min(0.05, remain))

    # ================== MULAI / BERHENTI ==================
    def _snapshot(self):
        """Ambil seluruh pengaturan sekarang untuk dipakai worker."""
        V = self.vars
        return {
            "folder": V["folder"].get().strip(),
            "jumlah": V["jumlah"].get().strip(),
            "caption": V["caption"].get(),
            "mundur": V["mundur"].get().strip(),
            "jeda_dialog": V["jeda_dialog"].get().strip(),
            "jeda_langkah": V["jeda_langkah"].get().strip(),
            "tunggu": V["tunggu"].get().strip(),
            "skip": bool(V["skip_uploaded"].get()),
            "skip_jadwal": bool(V["skip_jadwal"].get()),
            "pakai_gambar": bool(V["pakai_gambar"].get()),
            "gambar": V["gambar_ref"].get().strip(),
            "radius": int(_angka(V["radius"].get(), 300, 50, 2000)),
            "kemiripan": _angka(V["kemiripan"].get(), 0.8, 0.5, 0.99),
            "tanggal": V["tanggal"].get().strip(),
            "klik_bebas1": V["klik_bebas1"].get().strip(),
            "scroll_bebas1": V["scroll_bebas1"].get().strip(),
            "arah_scroll": V["arah_scroll"].get(),
            "klik_bebas2": V["klik_bebas2"].get().strip(),
            "jarak_baris": V["jarak_baris"].get().strip(),
            "klik_submit": V["klik_submit"].get().strip(),
            "auto_kirim": bool(V["auto_kirim"].get()),
            "posisi": {k: (list(v) if v else None)
                       for k, v in self.posisi.items()},
            "jeda_per": dict(self.jeda_per),
            "jeda_klik_per": dict(self.jeda_klik_per),
            "caption_only": False,
        }

    def _start(self):
        if self.running:
            return
        if not PYNPUT_OK:
            messagebox.showerror(
                APP_NAME, "Library pynput belum terpasang.\n\n"
                          "Buka CMD lalu jalankan:\n  pip install pynput")
            return
        snap = self._snapshot()
        try:
            jumlah = int(snap["jumlah"])
            mundur = int(snap["mundur"])
            jeda_dialog = float(snap["jeda_dialog"].replace(",", "."))
            jeda_langkah = float(snap["jeda_langkah"].replace(",", "."))
            tunggu = float(snap["tunggu"].replace(",", "."))
        except ValueError:
            messagebox.showwarning(
                APP_NAME, "JUMLAH VIDEO dan pengaturan WAKTU harus diisi "
                          "dengan angka yang benar.")
            return
        if jumlah < 1:
            messagebox.showwarning(APP_NAME, "Jumlah video minimal 1.")
            return
        if jumlah > MAX_BATCH:
            if not messagebox.askyesno(
                    APP_NAME,
                    "Jumlah {} melebihi batas situs CutMotions "
                    "(maksimal {} video sekali jalan).\n\n"
                    "Lanjut dengan {} video pertama saja?".format(
                        jumlah, MAX_BATCH, MAX_BATCH)):
                return
            jumlah = MAX_BATCH
        folder = snap["folder"]
        if not folder or not os.path.isdir(folder):
            messagebox.showwarning(
                APP_NAME, "Folder video belum dipilih atau tidak ada:\n"
                + (folder or "(kosong)"))
            return
        # ---- posisi wajib sesuai alur A-J ----
        lewati_jadwal = snap["skip_jadwal"]
        for kunci, label, wajib, _ket in POSISI_DEF:
            if not wajib:
                continue
            if lewati_jadwal and kunci in SLOT_JADWAL:
                continue
            if kunci == "pos_submit" and not snap["auto_kirim"]:
                continue
            if not snap["posisi"].get(kunci):
                messagebox.showwarning(
                    APP_NAME,
                    "Posisi {} belum diatur.\n\n"
                    "Klik barisnya di tabel LANGKAH MAKRO, lalu klik "
                    "AMBIL (atau isi X,Y manual).".format(label))
                return
        # ---- pencarian gambar negara (C) ----
        if snap["pakai_gambar"]:
            if not snap["gambar"] or not os.path.isfile(snap["gambar"]):
                messagebox.showwarning(
                    APP_NAME,
                    "Pencarian gambar aktif tapi gambar referensi belum "
                    "dipilih.\n\nKlik POTONG GAMBAR pada langkah C.")
                return
            if not CV_OK:
                if not messagebox.askyesno(
                        APP_NAME,
                        "opencv-python belum terpasang sehingga pencarian "
                        "gambar tidak bisa dipakai.\n\n"
                        "Lanjut dengan KLIK BIASA di titik C?"):
                    return
                snap["pakai_gambar"] = False
        # ---- tanggal-jam rilis (D) ----
        tgl = parse_tanggal(snap["tanggal"])
        if tgl is None:
            messagebox.showwarning(
                APP_NAME, "Format TANGGAL & JAM salah.\n\nContoh yang "
                          "benar:\n  2026-09-10 02:05:01")
            return
        snap["tanggal"] = tgl
        # ---- angka pelengkap alur ----
        klik_b1 = int(_angka(snap["klik_bebas1"], 0, 0, 500))
        scroll_b1 = int(_angka(snap["scroll_bebas1"], 0, 0, 50))
        klik_b2 = int(_angka(snap["klik_bebas2"], 0, 0, 20))
        jarak = int(_angka(snap["jarak_baris"], 85, 10, 2000))
        klik_sub = int(_angka(snap["klik_submit"], 1, 1, 10))
        snap["klik_bebas1"] = klik_b1
        snap["scroll_bebas1"] = scroll_b1
        snap["klik_bebas2"] = klik_b2
        snap["jarak_baris"] = jarak
        snap["klik_submit"] = klik_sub
        if mundur < 0 or mundur > 60:
            messagebox.showwarning(APP_NAME,
                                   "MUNDUR SEBELUM MULAI harus 0-60 detik.")
            return
        if jeda_dialog < 0.5:
            messagebox.showwarning(
                APP_NAME, "JEDA BUKA DIALOG/EDITOR minimal 0.5 detik "
                          "supaya dialog/editor sempat terbuka.")
            return
        if tunggu < 0:
            tunggu = 0
        # ---- susun daftar video yang mau diupload ----
        semua = daftar_video(folder)
        if not semua:
            messagebox.showwarning(
                APP_NAME, "Tidak ada file video (.mp4/.mov/dll) di "
                          "folder ini.")
            return
        if snap["skip"]:
            sudah = self._riwayat_folder()
            semua = [f for f in semua if f not in sudah]
        if not semua:
            riw = self.riwayat.get(self._kunci_riwayat(), [])
            if riw and messagebox.askyesno(
                    APP_NAME,
                    "Semua video di folder ini sudah terupload.\n\n"
                    "Mau lanjut LANGSUNG KE FASE CAPTION untuk {} video "
                    "terakhir? (jadwal & tambah video dilewati)".format(
                        min(jumlah, len(riw)))):
                jumlah = min(jumlah, len(riw))
                snap["caption_only"] = True
            else:
                return
        else:
            snap["antrian"] = semua[:jumlah]
        # ---- cek panjang caption ----
        if snap["caption_only"]:
            riw = self.riwayat.get(self._kunci_riwayat(), [])
            cek_caption = list(riw[-jumlah:])
        else:
            cek_caption = snap.get("antrian", [])
        terpanjang = 0
        for f in cek_caption:
            terpanjang = max(terpanjang,
                             len(compose_caption(snap["caption"], f)))
        if terpanjang > JUDUL_MAX:
            if not messagebox.askyesno(
                    APP_NAME,
                    "Ada caption melebihi {} karakter (batas judul video "
                    "situs).\nTerpanjang: {} karakter.\n\n"
                    "Lanjut saja? (situs bisa memotong / menolak)".format(
                        JUDUL_MAX, terpanjang)):
                return
        self._save_settings()
        self.stop_event.clear()
        self.running = True
        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal")
        threading.Thread(target=self._worker,
                         args=(snap, jumlah, mundur, jeda_dialog,
                               jeda_langkah, tunggu),
                         daemon=True).start()

    # ================== BANTUAN SCROLL & KLIK ==================
    def _scroll_top(self):
        try:
            self.mouse.scroll(0, 40)
        except Exception:
            pass

    def _scroll_bottom(self):
        try:
            self.mouse.scroll(0, -80)
        except Exception:
            pass

    def _klik(self, pos):
        self.mouse.position = (pos[0], pos[1])
        time.sleep(0.2)
        self.mouse.click(Button.left, 1)

    def _klik_off(self, pos, dy=0):
        """Klik pada posisi (x, y + dy) - untuk baris video ke-n."""
        self._klik((int(pos[0]), int(pos[1]) + int(dy)))

    def _jeda_sebelum(self, snap, kunci):
        """Jeda sebelum langkah: per langkah (kolom JEDA) jika diubah,
        kalau tidak pakai JEDA ANTAR LANGKAH global."""
        return max(0.0, float(snap["jeda_per"].get(
            kunci, _angka(snap["jeda_langkah"], 1.0))))

    # ================== MESIN OTOMATIS ==================
    def _worker(self, snap, jumlah, mundur, jeda_dialog, jeda_langkah,
                tunggu):
        try:
            pos = {k: tuple(v) for k, v in snap["posisi"].items() if v}
            caption_dasar = snap["caption"]
            kunci = self._kunci_riwayat()
            caption_only = bool(snap.get("caption_only"))
            antrian = snap.get("antrian", [])
            jk = snap["jeda_klik_per"]      # jeda antar klik per slot
            jp = snap["jeda_per"]           # jeda sebelum langkah per slot

            # ---- hitung mundur sebelum mulai ----
            if mundur > 0:
                for s in range(mundur, 0, -1):
                    if self.stop_event.is_set():
                        self._finish("Dibatalkan sebelum mulai.", warn=True)
                        return
                    if caption_only:
                        pesan = ("Lanjut CAPTION dalam {} detik - buka "
                                 "halaman Rilis karya sekarang...")
                    else:
                        pesan = ("Mulai dalam {} detik - buka halaman "
                                 "Rilis karya CutMotions sekarang...")
                    self._set_status(pesan.format(s), C_ORANGE)
                    self._sleep(1.0)

            # =================================================
            # FASE 1 - JADWAL RILIS (A - E)
            # =================================================
            if not caption_only:
                if snap["skip_jadwal"]:
                    self._set_status("Langkah JADWAL (A-E) dilewati "
                                     "sesuai pengaturan.", C_ORANGE)
                else:
                    self._set_status(
                        "FASE 1/3 JADWAL RILIS - klik tombol 'Jadwal "
                        "rilis'... (jangan sentuh mouse/keyboard!)",
                        C_GREEN)
                    self._sleep(self._jeda_sebelum(snap, "pos_jadwal"))
                    self._klik(pos["pos_jadwal"])
                    self._sleep(jeda_dialog)

                    if self.stop_event.is_set():
                        self._finish("Dihentikan saat fase jadwal.",
                                     warn=True)
                        return
                    self._set_status("Klik dropdown 'NEGARA'...", C_GREEN)
                    self._klik(pos["pos_negara"])
                    self._sleep(jeda_dialog)

                    # ---- C: pilih negara ----
                    if self.stop_event.is_set():
                        self._finish("Dihentikan sebelum memilih negara.",
                                     warn=True)
                        return
                    if snap["pakai_gambar"]:
                        hasil = None
                        for percobaan in range(1, 4):
                            self._set_status(
                                "Cari gambar '{}' dalam radius {} px "
                                "(percobaan {}/3, multi-skala)...".format(
                                    os.path.basename(snap["gambar"]),
                                    snap["radius"], percobaan), C_GREEN)
                            hasil, pesan_gambar = cari_di_layar(
                                snap["gambar"], pos["pos_pilih_neg"][0],
                                pos["pos_pilih_neg"][1], snap["radius"],
                                snap["kemiripan"])
                            if hasil:
                                break
                            self._sleep(jeda_dialog)
                        if hasil:
                            x, y, skor = hasil
                            self._set_status(
                                "Negara KETEMU di ({}, {}) - kemiripan "
                                "{:.0%} - diklik.".format(x, y, skor),
                                C_GREEN)
                            self._klik((x, y))
                        else:
                            self._set_status(
                                "Gambar negara tidak ketemu 3x ({}). Pakai "
                                "klik biasa di titik C.".format(pesan_gambar),
                                C_ORANGE)
                            self._klik(pos["pos_pilih_neg"])
                    else:
                        self._set_status("Klik pilihan negara...", C_GREEN)
                        self._klik(pos["pos_pilih_neg"])
                    self._sleep(max(0.0, jp.get(
                        "pos_pilih_neg", jeda_langkah)))

                    # ---- D: kolom tanggal + ketik tanggal-jam ----
                    if self.stop_event.is_set():
                        self._finish("Dihentikan sebelum mengisi tanggal.",
                                     warn=True)
                        return
                    self._set_status(
                        "Ketik tanggal-jam rilis: {}...".format(
                            snap["tanggal"]), C_GREEN)
                    self._klik(pos["pos_tanggal"])
                    time.sleep(0.3)
                    with self.kb.pressed(Key.ctrl):
                        self.kb.press("a")
                        self.kb.release("a")
                    time.sleep(0.15)
                    self.kb.type(snap["tanggal"])
                    self._sleep(max(0.0, jp.get("pos_tanggal",
                                                jeda_langkah)))

                    # ---- E: OKE ----
                    if self.stop_event.is_set():
                        self._finish("Dihentikan sebelum klik OKE.",
                                     warn=True)
                        return
                    self._set_status("Klik 'OKE'...", C_GREEN)
                    self._klik(pos["pos_oke"])
                    self._sleep(max(0.0, jp.get("pos_oke", jeda_langkah))
                                + 0.5)

            # =================================================
            # FASE 2 - TAMBAH & PILIH VIDEO (F - H2)
            # =================================================
            if not caption_only:
                if self.stop_event.is_set():
                    self._finish("Dihentikan.", warn=True)
                    return
                self._set_status(
                    "FASE 2/3 TAMBAH VIDEO - klik '+ Tambah video'...",
                    C_GREEN)
                self._sleep(self._jeda_sebelum(snap, "pos_tambah"))
                self._klik(pos["pos_tambah"])
                self._sleep(jeda_dialog)

                # ---- G: klik bebas 1 + scroll ----
                if self.stop_event.is_set():
                    self._finish(
                        "Dihentikan setelah 'Tambah video'. Video belum "
                        "masuk - aman diulang dari awal.", warn=True)
                    return
                n_klik1 = snap["klik_bebas1"]
                n_scroll = snap["scroll_bebas1"]
                if n_klik1 or n_scroll:
                    self._set_status(
                        "Klik bebas {}x + scroll {}x ({})...".format(
                            n_klik1, n_scroll, snap["arah_scroll"]),
                        C_GREEN)
                    arah = -3 if snap["arah_scroll"] == "Naik" else 3
                    for _ in range(n_klik1):
                        if self.stop_event.is_set():
                            break
                        self._klik(pos["pos_bebas1"])
                        time.sleep(max(0.05, jk.get("pos_bebas1", 0.3)))
                    for _ in range(n_scroll):
                        if self.stop_event.is_set():
                            break
                        try:
                            self.mouse.scroll(0, arah)
                        except Exception:
                            pass
                        time.sleep(max(0.05, jk.get("pos_bebas1", 0.3)))
                    self._sleep(max(0.0, jp.get("pos_bebas1",
                                                jeda_langkah)))

                # ---- H: klik video pertama + Shift + panah bawah ----
                if self.stop_event.is_set():
                    self._finish("Dihentikan di dialog pilih file.",
                                 warn=True)
                    return
                self._set_status(
                    "Klik video pertama + tahan SHIFT + panah bawah {}x "
                    "(memilih {} video dari atas)...".format(
                        max(0, jumlah - 1), jumlah), C_GREEN)
                self._klik(pos["pos_video"])
                time.sleep(0.3)
                if jumlah > 1:
                    jeda_panah = max(0.05, jk.get("pos_video", 0.15))
                    with self.kb.pressed(Key.shift):
                        for _ in range(jumlah - 1):
                            self.kb.press(Key.down)
                            self.kb.release(Key.down)
                            time.sleep(jeda_panah)
                self._sleep(max(0.0, jp.get("pos_video", jeda_langkah)))

                # ---- H2: klik bebas 2 (tombol Buka) ----
                if self.stop_event.is_set():
                    self._finish("Dihentikan sebelum klik Buka.",
                                 warn=True)
                    return
                self._set_status(
                    "Klik bebas {}x (tombol 'Buka')...".format(
                        snap["klik_bebas2"]), C_GREEN)
                for _ in range(snap["klik_bebas2"]):
                    if self.stop_event.is_set():
                        break
                    self._klik(pos["pos_bebas2"])
                    time.sleep(max(0.05, jk.get("pos_bebas2", 0.3)))
                self._sleep(max(0.0, jp.get("pos_bebas2", jeda_langkah)))

                # ---- tunggu semua video selesai terupload ----
                total_tunggu = max(0.0, tunggu * jumlah)
                akhir = time.time() + total_tunggu
                while not self.stop_event.is_set():
                    sisa = akhir - time.time()
                    if sisa <= 0:
                        break
                    self._set_progress(
                        "FASE 2 UPLOAD {} video   |   menunggu: "
                        "{:.0f} dtk".format(jumlah, sisa))
                    time.sleep(min(0.5, sisa))
                if self.stop_event.is_set():
                    self._finish(
                        "Dihentikan saat menunggu upload. Cek dulu di "
                        "situs: kalau video sudah masuk semua, jalankan "
                        "F6 lagi - aplikasi menawarkan lanjut ke fase "
                        "caption.", warn=True)
                    return

                # ---- catat riwayat (tersimpan instan) ----
                self.riwayat.setdefault(kunci, [])
                for nama_file in antrian:
                    if nama_file not in self.riwayat[kunci]:
                        self.riwayat[kunci].append(nama_file)
                self._save_riwayat()

            # =================================================
            # FASE 3 - CAPTION per baris (I) lalu SUBMIT (J)
            # =================================================
            self._set_status("FASE 3/3 CAPTION - menggulir ke atas...",
                             C_GREEN)
            self._scroll_top()
            self._sleep(jeda_langkah)

            # urutan caption = urutan video di daftar situs (atas-bawah);
            # pakai riwayat supaya aman bila dijalankan ulang setelah stop.
            riw = self.riwayat.get(kunci, [])
            if len(riw) >= jumlah:
                daftar_caption = list(riw[-jumlah:])
            else:
                daftar_caption = list(antrian)
            n_cap = len(daftar_caption)
            jarak = max(1, int(snap["jarak_baris"]))
            i = 0

            for i, nama_file in enumerate(daftar_caption):
                if self.stop_event.is_set():
                    break
                caption_final = compose_caption(caption_dasar, nama_file)
                geser = i * jarak  # baris ke-i turun sejauh i x jarak
                self._set_progress(
                    "FASE 3 CAPTION {}/{} (baris {} | geser {} px)   |   "
                    "{}".format(i + 1, n_cap, i + 1, geser, caption_final))

                # klik tombol Edit pada baris video ke-i
                self._set_status(
                    "[{}/{}] Klik tombol Edit (baris {})...".format(
                        i + 1, n_cap, i + 1), C_GREEN)
                self._sleep(self._jeda_sebelum(snap, "pos_edit"))
                self._klik_off(pos["pos_edit"], geser)
                self._sleep(jeda_dialog)

                # klik kotak caption baris ke-i + ketik caption
                if self.stop_event.is_set():
                    break
                self._set_status(
                    "[{}/{}] Menulis caption: {}".format(
                        i + 1, n_cap, caption_final), C_GREEN)
                self._klik_off(pos["pos_judul"], geser)
                time.sleep(0.3)
                with self.kb.pressed(Key.ctrl):
                    self.kb.press("a")
                    self.kb.release("a")
                time.sleep(0.15)
                self.kb.type(caption_final)
                self._sleep(max(0.0, jp.get("pos_judul", jeda_langkah)))

                # klik tombol Konfirmasi baris ke-i
                # (kalau I3 tidak diatur, klik lagi titik Edit -
                #  letaknya sama persis dengan tombol Konfirmasi)
                if self.stop_event.is_set():
                    break
                titik_ok = pos.get("pos_konfirmasi", pos["pos_edit"])
                self._set_status(
                    "[{}/{}] Klik Konfirmasi...".format(i + 1, n_cap),
                    C_GREEN)
                self._klik_off(titik_ok, geser)
                self._sleep(max(0.0, jp.get("pos_konfirmasi",
                                            jeda_langkah)) + 0.5)

            if self.stop_event.is_set():
                self._finish(
                    "Dihentikan saat FASE CAPTION ({}/{} caption selesai). "
                    "Jalankan F6 lagi dan pilih 'lanjut ke fase caption' "
                    "- caption diulang dari baris atas dan yang sudah "
                    "jadi otomatis ditimpa sama.".format(i + 1, n_cap),
                    warn=True)
                return

            # =================================================
            # J - SUBMIT
            # =================================================
            if snap["auto_kirim"] and "pos_submit" in pos:
                self._set_status(
                    "Klik SUBMIT {}x (halaman digulir ke bawah)...".format(
                        snap["klik_submit"]), C_GREEN)
                self._scroll_bottom()
                self._sleep(jeda_langkah + 0.5)
                for _ in range(snap["klik_submit"]):
                    if self.stop_event.is_set():
                        break
                    self._klik(pos["pos_submit"])
                    time.sleep(max(0.05, jk.get("pos_submit", 0.3)))
                self._finish(
                    "Selesai! {} video: jadwal diatur, video ditambahkan "
                    "(Shift+turun), caption ditulis per baris, dan SUBMIT "
                    "sudah diklik. Cek status rilis di situs.".format(
                        n_cap))
            else:
                self._finish(
                    "Caption {} video selesai! Cek dulu di browser, lalu "
                    "klik tombol 'Submit' secara manual.".format(n_cap))
        except Exception as e:
            self._finish("Terjadi error: {}".format(e), warn=True)

    def _finish(self, msg, warn=False):
        def do():
            self.running = False
            self.btn_start.config(state="normal")
            self.btn_stop.config(state="disabled")
            self.lbl_status.config(text=msg,
                                   fg=C_RED if warn else C_GREEN)
            self._update_count()
        self.root.after(0, do)

    def _stop(self):
        if self.running:
            self.stop_event.set()
            self._set_status("Menghentikan...", C_ORANGE)

    # ================== HOTKEY GLOBAL ==================
    def _on_key(self, key):
        try:
            if key == kb_mod.Key.f6:
                self.root.after(0, self._start)
            elif key in (kb_mod.Key.f7, kb_mod.Key.esc):
                self.root.after(0, self._stop)
        except Exception:
            pass

    # ================== SIMPAN / MUAT ==================
    def _kumpulkan_data(self):
        V = self.vars
        data = {
            "folder": V["folder"].get(),
            "jumlah": V["jumlah"].get(),
            "caption": V["caption"].get(),
            "mundur": V["mundur"].get(),
            "jeda_dialog": V["jeda_dialog"].get(),
            "jeda_langkah": V["jeda_langkah"].get(),
            "tunggu_upload": V["tunggu"].get(),
            "skip_uploaded": bool(V["skip_uploaded"].get()),
            "skip_jadwal": bool(V["skip_jadwal"].get()),
            "pakai_gambar": bool(V["pakai_gambar"].get()),
            "gambar_ref": V["gambar_ref"].get(),
            "radius_cari": V["radius"].get(),
            "kemiripan_cari": V["kemiripan"].get(),
            "tanggal_jam": V["tanggal"].get(),
            "klik_bebas1": V["klik_bebas1"].get(),
            "scroll_bebas1": V["scroll_bebas1"].get(),
            "arah_scroll": V["arah_scroll"].get(),
            "klik_bebas2": V["klik_bebas2"].get(),
            "jarak_baris": V["jarak_baris"].get(),
            "klik_submit": V["klik_submit"].get(),
            "auto_kirim": bool(V["auto_kirim"].get()),
            "posisi": {k: v for k, v in self.posisi.items()},
            "jeda_per": {k: float(v) for k, v in self.jeda_per.items()},
            "jeda_klik_per": {k: float(v)
                              for k, v in self.jeda_klik_per.items()},
            "versi": APP_VERSION,
        }
        return data

    def _save_settings(self):
        try:
            with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(self._kumpulkan_data(), f, indent=2,
                          ensure_ascii=False)
        except Exception:
            pass

    def _terapkan_data(self, data):
        """Isi seluruh UI dari dict profil (dengan sanitasi)."""
        if not isinstance(data, dict):
            return
        V = self.vars
        posisi_baru = {k: None for k in POS_KUNCI}
        for kunci in POS_KUNCI:
            p = data.get("posisi", {}).get(kunci)
            try:
                posisi_baru[kunci] = [int(p[0]), int(p[1])] if p else None
            except Exception:
                posisi_baru[kunci] = None
        # Migrasi otomatis dari v3.0 (browsers[aktif] -> posisi datar)
        if not any(posisi_baru.values()):
            bs = data.get("browsers")
            if isinstance(bs, list) and bs and isinstance(bs[0], dict):
                src = bs[min(max(0, int(data.get("aktif", 0))
                                  if str(data.get("versi", "")).startswith(
                                      "3") else 0), len(bs) - 1)]
                dari_v3 = str(data.get("versi", "")).startswith("3")
                if dari_v3:
                    for kunci in POS_KUNCI:
                        p = src.get(kunci)
                        try:
                            posisi_baru[kunci] = ([int(p[0]), int(p[1])]
                                                  if p else None)
                        except Exception:
                            posisi_baru[kunci] = None
        self.posisi = posisi_baru
        jp_baru = jeda_default_per()
        for k, v in (data.get("jeda_per") or {}).items():
            if k in jp_baru:
                jp_baru[k] = _angka(v, 1.0, 0.0, 3600)
        self.jeda_per = jp_baru
        jk_baru = jeda_klik_default_per()
        for k, v in (data.get("jeda_klik_per") or {}).items():
            if k in jk_baru:
                jk_baru[k] = _angka(v, 0.3, 0.05, 60)
        self.jeda_klik_per = jk_baru
        self._loading = True
        pasangan = [
            ("folder", V["folder"]), ("jumlah", V["jumlah"]),
            ("caption", V["caption"]), ("mundur", V["mundur"]),
            ("jeda_dialog", V["jeda_dialog"]),
            ("jeda_langkah", V["jeda_langkah"]),
            ("tunggu_upload", V["tunggu"]), ("tunggu", V["tunggu"]),
            ("tanggal_jam", V["tanggal"]),
            ("radius_cari", V["radius"]),
            ("kemiripan_cari", V["kemiripan"]),
            ("klik_bebas1", V["klik_bebas1"]),
            ("scroll_bebas1", V["scroll_bebas1"]),
            ("klik_bebas2", V["klik_bebas2"]),
            ("jarak_baris", V["jarak_baris"]),
            ("klik_submit", V["klik_submit"]),
            ("gambar_ref", V["gambar_ref"]),
        ]
        for key, var in pasangan:
            val = data.get(key)
            if val is not None:
                var.set(str(val))
        V["skip_uploaded"].set(bool(data.get("skip_uploaded", True)))
        V["skip_jadwal"].set(bool(data.get("skip_jadwal", False)))
        V["pakai_gambar"].set(bool(data.get("pakai_gambar", False)))
        V["auto_kirim"].set(bool(data.get("auto_kirim", True)))
        arah = str(data.get("arah_scroll") or "Turun")
        V["arah_scroll"].set(arah if arah in ("Turun", "Naik") else "Turun")
        self._loading = False
        self._refresh_tabel()
        self._render_properti()
        self._update_count()
        self._update_preview()

    def _load_settings(self):
        if not os.path.exists(SETTINGS_FILE):
            return
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            return
        self._terapkan_data(data)

    def _load_riwayat(self):
        if not os.path.exists(RIWAYAT_FILE):
            return
        try:
            with open(RIWAYAT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(v, list):
                        self.riwayat[str(k)] = [str(x) for x in v]
                        # migrasi kunci lama "nama||folder" -> "folder"
                        if "||" in k:
                            p = k.split("||", 1)[1]
                            self.riwayat.setdefault(p,
                                                    [str(x) for x in v])
        except Exception:
            pass

    def _save_riwayat(self):
        try:
            with open(RIWAYAT_FILE, "w", encoding="utf-8") as f:
                json.dump(self.riwayat, f, indent=2, ensure_ascii=False)
        except Exception:
            pass

    def _on_close(self):
        try:
            self._save_settings()
            self._save_riwayat()
            if self.running:
                self.stop_event.set()
            if PYNPUT_OK and hasattr(self, "_listener"):
                self._listener.stop()
        finally:
            self.root.destroy()


# ------------------------------------------------------------
# Jendela potong gambar referensi (screenshot -> seret kotak)
# ------------------------------------------------------------
class JendelaPotong(tk.Toplevel):
    def __init__(self, induk, img, on_simpan):
        super().__init__(induk)
        self.title("Potong gambar referensi - seret kotak, lalu SIMPAN")
        self.configure(bg=C_BG)
        self.resizable(False, False)
        self.transient(induk)
        self.grab_set()
        self.img = img
        self.on_simpan = on_simpan
        self.kotak_id = None
        self.mulai = (0, 0)
        self.akhir = (0, 0)
        skala = min(1.0, 1100.0 / max(1, img.width),
                    560.0 / max(1, img.height))
        self.skala = skala
        w, h = int(img.width * skala), int(img.height * skala)
        self.tampil = ImageTk.PhotoImage(img.resize((w, h)))
        self.cv = tk.Canvas(self, width=w, height=h, cursor="crosshair",
                            highlightthickness=1,
                            highlightbackground=C_LINE)
        self.cv.pack(padx=10, pady=(10, 4))
        self.cv.create_image(0, 0, image=self.tampil, anchor="nw")
        self.cv.create_text(10, 12, anchor="w", fill="#FF3333",
                            font=("Segoe UI", 10, "bold"),
                            text="Seret kotak di atas tulisan negara "
                                 "(potong SEMPIT, tanpa ruang kosong)")
        self.cv.bind("<ButtonPress-1>", self._tekan)
        self.cv.bind("<B1-Motion>", self._geser)
        self.cv.bind("<ButtonRelease-1>", self._lepas)
        bar = tk.Frame(self, bg=C_BG)
        bar.pack(fill="x", padx=10, pady=(2, 10))
        tk.Label(bar, text="Nama file:", bg=C_BG, fg=C_MUTED,
                 font=F_XS).pack(side="left")
        self.ent = tk.Entry(bar, bg=C_PANEL, fg=C_TEXT, font=F_XS,
                            relief="solid", bd=1)
        self.ent.insert(0, "referensi_negara.png")
        self.ent.pack(side="left", padx=6, ipady=2)
        tk.Button(bar, text="SIMPAN AREA", command=self._simpan,
                  bg=C_BLUE, fg="white", font=F_XS, relief="flat",
                  cursor="hand2", activebackground=C_BLUE_D).pack(
                      side="left", padx=4, ipadx=8, ipady=3)
        tk.Button(bar, text="BATAL", command=self.destroy, bg=C_BG,
                  fg=C_MUTED, font=F_XS, relief="raised",
                  cursor="hand2").pack(side="left", ipadx=8, ipady=3)
        tk.Label(self, text="Tersimpan otomatis ke folder data: "
                 + data_dir(), bg=C_BG, fg=C_MUTED, font=F_XS,
                 anchor="w").pack(fill="x", padx=10, pady=(0, 8))

    def _tekan(self, ev):
        self.mulai = (ev.x, ev.y)
        self.akhir = (ev.x, ev.y)
        self._gambar_kotak()

    def _geser(self, ev):
        self.akhir = (ev.x, ev.y)
        self._gambar_kotak()

    def _lepas(self, ev):
        self.akhir = (ev.x, ev.y)
        self._gambar_kotak()

    def _gambar_kotak(self):
        if self.kotak_id:
            self.cv.delete(self.kotak_id)
        x1, y1 = self.mulai
        x2, y2 = self.akhir
        self.kotak_id = self.cv.create_rectangle(
            min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2),
            outline="#FF3333", width=2)

    def _simpan(self):
        x1, y1 = self.mulai
        x2, y2 = self.akhir
        if abs(x2 - x1) < 4 or abs(y2 - y1) < 4:
            messagebox.showinfo(APP_NAME,
                                "Seret dulu kotak di atas tulisan "
                                "negaranya.")
            return
        s = self.skala
        kotak = (int(min(x1, x2) / s), int(min(y1, y2) / s),
                 int(max(x1, x2) / s), int(max(y1, y2) / s))
        nama = self.ent.get().strip() or "referensi_negara.png"
        # bersihkan karakter yang tidak sah untuk nama file Windows
        for ch in '\\/:*?"<>|':
            nama = nama.replace(ch, "_")
        if not nama.lower().endswith(".png"):
            nama += ".png"

        # 1) Simpan ke folder data milik user (SELALU bisa ditulisi,
        #    walau aplikasi ter-install di C:\Program Files).
        #    Dulu disimpan ke folder aplikasi -> Errno 13
        #    Permission denied saat aplikasi ter-install.
        path = os.path.join(data_dir(), nama)
        try:
            self.img.crop(kotak).save(path)
        except Exception:
            # 2) Kalau tetap gagal, biarkan user memilih lokasinya
            #    sendiri (Documents / Desktop, dll).
            path = filedialog.asksaveasfilename(
                title="Simpan gambar referensi",
                initialfile=nama,
                defaultextension=".png",
                filetypes=[("Gambar PNG", "*.png"),
                           ("Semua file", "*.*")])
            if not path:
                return
            try:
                self.img.crop(kotak).save(path)
            except Exception as e:
                messagebox.showerror(
                    APP_NAME,
                    "Gagal menyimpan:\n{}\n\nCoba simpan ke folder "
                    "lain (mis. Documents atau Desktop)."
                    .format(e))
                return
        self.grab_release()
        self.destroy()
        self.on_simpan(path)


def main():
    root = tk.Tk()
    app = CutUploaderApp(root)
    if "--selftest" in sys.argv:
        def _ok():
            print("SELFTEST_OK")
            root.destroy()
        root.after(1800, _ok)
    if "--selftest-prop" in sys.argv:
        def _pilih():
            app.tree.selection_set("pos_pilih_neg")
            app.tree.event_generate("<<TreeviewSelect>>")
        root.after(800, _pilih)

        def _ok2():
            print("SELFTEST_PROP_OK")
            root.destroy()
        root.after(3000, _ok2)
    root.mainloop()
    if ("--selftest" in sys.argv) or ("--selftest-prop" in sys.argv):
        print("SELFTEST_DONE")


if __name__ == "__main__":
    main()
