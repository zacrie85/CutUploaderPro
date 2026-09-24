# -*- coding: utf-8 -*-
"""
============================================================
  CUTUPLOADER PRO  v5.9  -  MACRO STUDIO EDITION
  Aplikasi desktop otomasi klik + uploader video batch
  khusus untuk situs CutMotions (Kwai)
------------------------------------------------------------
  DUA MODE DALAM SATU APLIKASI (pilih lewat tab di atas):

  1. STUDIO MAKRO  (BARU v5.0)
     Editor alur kerja bebas ala Jitbit Macro Recorder:
     - Bagian ATAS: semua jenis aksi jadi MENU tersendiri
       (+ Klik Titik, + Jeda, + Cari Gambar, + Ketik Teks,
        + Tekan Tombol, + Scroll, + Catatan, + Ulangi)
     - Bagian BAWAH: tabel ALUR KERJA kosong - susun urutan
       klik-per-klik sendiri satu per satu
     - Setiap langkah punya panel PROPERTI sendiri (posisi,
       jumlah klik, teks, jeda, gambar referensi, dll)
     - Langkah bisa DISALIN / DITEMPEL / DIHAPUS / DIURUTKAN
     - CARI GAMBAR: hasil pencarian bisa LANGSUNG DIKLIK atau
       hanya DIPINDAH kursor tanpa klik
     - Blok ULANGI-MULAI ... ULANGI-AKHIR untuk mengulang
       sepotong alur (mis. caption per baris video)
     - Placeholder teks: {caption} {video} {no} {jumlah}
     - Makro disimpan/muat ke file JSON + auto-save
     - v5.1: POTONG GAMBAR kini LANGSUNG DI LAYAR - layar
       dibekukan fullscreen, tinggal SERET kotak di area yang
       diinginkan (hanya area itu yang disimpan). Setiap
       potongan jadi file BARU, jadi CARI GAMBAR bisa dipakai
       berkali-kali dengan referensi berbeda-beda
     - v5.2: 2 MENU BARU - ISI TANGGAL-JAM (mengisi kolom
       tanggal-jam rilis, nilainya dari tab CutMotions atau
       ketik sendiri) dan ISI VIDEO & CAPTION (mengisi jumlah
       video, atau caption dasar + nama video yang diambil)
     - v5.3: CARI GAMBAR TANPA X,Y - gambar referensi dicari
       lalu LANGSUNG DIKLIK; daerah pencariannya diatur lewat
       AREA FOKUS yang dipilih dengan MENYERET kotak di layar
       (opsional - kosong = seluruh layar). Makro lama dengan
       titik acuan X,Y tetap jalan (otomatis jadi area)
     - v5.4: REKAM AKSI - rekam klik/ketikan/scroll LANGSUNG
       jadi langkah makro. Klik ● REKAM AKSI, jendela aplikasi
       tersembunyi, kerjakan aksimu di aplikasi lain (browser,
       form, dll) - SEMUA klik (klik dobel dikenali), huruf/
       angka yang diketik, tombol Enter/Tab/panah, dan gulungan
       mouse terekam otomatis jadi langkah + jeda antar langkah.
       Tekan F8 (atau ESC) untuk berhenti - hasil DITAMBAH di
       akhir alur kerja, tinggal disunting lalu JALANKAN (F6)
     - v5.6: TAMPILAN MODERN "DARK GLASS" - tema navy pekat
       dengan aksen neon dan tombol yang dirapi: MAKSIMAL 7
       TOMBOL per baris, sisanya berurutan di baris bawahnya
     - v5.7: PILIH BANYAK LANGKAH SEKALIGUS - tahan CTRL atau
       SHIFT saat mengklik baris di tabel (Ctrl+Klik = pilih
       tambah/kurang, Shift+Klik = pilih rentang, Ctrl+A = semua)
       lalu SALIN / TEMPEL / HAPUS / AKTIF-MATI berlaku untuk
       SEMUA langkah terpilih sekaligus. Desain makin modern:
       tombol KAPSUL membulat mengkilat, panel bersudut
       membulat, dan header gradien baru
     - v5.8: CARI GAMBAR BEBAS di ALUR CUTMOTIONS (A-J) - bisa
       ditambahkan BERAPAPUN kalinya (dulu sempat terasa
       "mentok 2x" karena nomor internal langkah menabrak
       setelah hapus langkah lalu aplikasi dibuka ulang;
       profil lama yang sudah rusak otomatis DISEMBUHKAN)
     - v5.9: ERROR "JUMLAH VIDEO dan WAKTU harus diisi angka"
       DIPERBAIKI - validasi kini PER KOLOM (pesan menunjuk
       kolom yang salah), koma diterima sebagai desimal
       (mis. 1,5), kolom kosong otomatis dipakai nilai
       standarnya. PLUS: langkah bawaan A-J kini BISA
       DIHAPUS (hilang dari tabel & dilewati saat jalan)
       dan bisa DIKEMBALIKAN lewat klik kanan tabel

  2. ALUR CUTMOTIONS (A-J)  -  seperti versi sebelumnya
     Alur otomatis uploader batch CutMotions:
       A  Klik tombol "Jadwal rilis / publikasi"
       B  Klik dropdown "NEGARA"
       C  Pilih negara - klik biasa ATAU pencarian gambar
       D  Klik kolom tanggal, lalu ketik tanggal-jam otomatis
       E  Klik "OKE"
       F  Klik "+ Tambah video" (dialog pilih file terbuka)
       G  Klik bebas berulang (0-500x) dan/atau scroll (0-50x)
       H  Klik video pertama + tahan SHIFT + panah bawah
       H2 Klik bebas (mis. tombol "Buka" pada dialog file)
       I  Caption per video: klik "Edit" -> ketik caption ->
          klik "Konfirmasi" (bergeser turun per baris)
       J  Klik "SUBMIT"
     Klik kanan langkah A-J = SALIN/TEMPEL jadi titik klik
     tambahan; cari gambar bisa diaktifkan di semua langkah.
     - v5.5: SEMUA MENU STUDIO MAKRO kini bisa dimasukkan ke
       alur CUTMOTIONS (A-J)! Tombol "+ TAMBAH LANGKAH" di
       toolbar tab ini (atau klik kanan tabel > Tambah langkah
       STUDIO) menyisipkan KLIK TITIK, JEDA, CARI GAMBAR, KETIK
       TEKS, ISI TANGGAL-JAM, ISI VIDEO & CAPTION, TEKAN TOMBOL,
       SCROLL, CATATAN, dan blok ULANGI-MULAI/AKHIR di posisi
       mana pun di antara langkah A-J. Langkah baru berkode "S"
       di tabel, disunting di panel PROPERTI (posisi, teks,
       gambar referensi, AREA FOKUS, dll), ikut tersimpan di
       profil, dan dijalankan TEPAT di posisinya dalam alur -
       termasuk di dalam fase caption per baris video (geser
       otomatis + placeholder {caption}/{video}/{no}/{jumlah}).
     - v5.6: REKAM AKSI kini juga ada di tab ini! Tombol
       '● REKAM AKSI' merekam klik/ketikan/scrollmu langsung
       jadi langkah di ALUR CUTMOTIONS (A-J) - hasil rekaman
       disisipkan TEPAT SETELAH langkah yang kamu pilih, bisa
       disunting di panel PROPERTI, dan ikut tersimpan di
       profil. Tampilan aplikasi juga kini pakai tema modern
       'DARK GLASS' dengan tombol rapi maksimal 7 per baris.
     - v5.7: PILIH BANYAK LANGKAH (Ctrl/Shift+Klik, Ctrl+A)
       untuk SALIN / TEMPEL / HAPUS massal; tombol kapsul
       membulat + panel bersudut membulat + header gradien.
     - v5.8: CARI GAMBAR bisa ditambah BERAPAPUN kalinya di
       alur ini (perbaikan langkah hilang setelah hapus +
       buka ulang aplikasi; profil lama otomatis disembuhkan).
     - v5.9: SEMUA langkah - termasuk bawaan A-J - bisa
       DIHAPUS manual (dilewati saat alur jalan) dan
       dikembalikan lagi lewat klik kanan tabel.

  Batas situs: maksimal 20 video / sekali jalan,
  judul video maksimal 250 karakter.

  Hotkey:
    F6         : Mulai (tab yang sedang aktif)
    F7 / ESC   : Berhenti
    F8 / ESC   : Berhenti MEREKAM (saat mode REKAM AKSI)

  Distribusi:
    - Installer Windows : CutUploaderPro-Setup.exe (tanpa Python)
    - EXE portabel      : CutUploaderPro.exe
    - Skrip Python      : butuh Python 3.9+ (lihat PANDUAN.txt)

  Dibuat dengan Python + tkinter + pynput (+ OpenCV/Pillow
  untuk pencarian gambar).
  Fokus utama: Windows desktop.
============================================================
"""

import tkinter as tk
import tkinter.font as tkfont
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
    from pynput import mouse as mouse_mod
    from pynput.keyboard import Controller as KeyboardController, Key
    from pynput.mouse import Controller as MouseController, Button
    PYNPUT_OK = True
except Exception as _e:
    IMPORT_ERROR = str(_e)

# Stub minimal: supaya kode yang memakai Button/Key tetap aman
# (dan bisa diuji otomatis) meski pynput tidak terpasang.
if not PYNPUT_OK:
    class _NamaPalsu:
        def __init__(self, nama):
            self.nama = nama

        def __str__(self):
            return self.nama

    class Button:  # pengganti pynput.mouse.Button
        left = _NamaPalsu("Button.left")
        right = _NamaPalsu("Button.right")
        middle = _NamaPalsu("Button.middle")

    class Key:  # pengganti pynput.keyboard.Key
        ctrl = _NamaPalsu("Key.ctrl")
        shift = _NamaPalsu("Key.shift")
        alt = _NamaPalsu("Key.alt")
        alt_gr = _NamaPalsu("Key.alt_gr")
        enter = _NamaPalsu("Key.enter")
        esc = _NamaPalsu("Key.esc")
        f8 = _NamaPalsu("Key.f8")
        space = _NamaPalsu("Key.space")
        tab = _NamaPalsu("Key.tab")
        backspace = _NamaPalsu("Key.backspace")
        delete = _NamaPalsu("Key.delete")
        home = _NamaPalsu("Key.home")
        end = _NamaPalsu("Key.end")
        page_down = _NamaPalsu("Key.page_down")
        page_up = _NamaPalsu("Key.page_up")
        down = _NamaPalsu("Key.down")
        up = _NamaPalsu("Key.up")
        left = _NamaPalsu("Key.left")
        right = _NamaPalsu("Key.right")
        f2 = _NamaPalsu("Key.f2")
        f4 = _NamaPalsu("Key.f4")
        f5 = _NamaPalsu("Key.f5")

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
    from PIL import Image, ImageTk, ImageEnhance
    PIL_OK = True
except Exception:
    PIL_OK = False

APP_NAME = "CutUploader Pro"
APP_VERSION = "5.9"

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
# v5.1: gambar referensi CARI GAMBAR
#   - folder khusus "referensi" di dalam folder data (v4.1:
#     selalu bisa ditulisi, aman walau di C:\Program Files)
#   - setiap potongan disimpan sebagai FILE BARU unik
#     (ref_tanggal_jam.png) sehingga menu CARI GAMBAR bisa
#     dipakai berkali-kali dengan referensi berbeda-beda
#   - thumbnail kecil ditampilkan di panel properti langkah
# ------------------------------------------------------------
OVERLAY_POTONG_AKTIF = []   # daftar layar potong yang sedang terbuka


def folder_referensi():
    """Folder khusus gambar referensi di dalam folder data."""
    d = os.path.join(data_dir(), "referensi")
    try:
        os.makedirs(d, exist_ok=True)
    except Exception:
        d = data_dir()
    return d


def nama_referensi_unik(prefiks="ref"):
    """Nama file PNG unik: ref_YYYYMMDD_HHMMSS.png (anti-timpa).

    Setiap kali POTONG GAMBAR dipakai, hasilnya jadi file BARU -
    gambar referensi langkah yang lain TIDAK ikut tertimpa.
    """
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dasar = "{}_{}".format(prefiks, stamp)
    nama = dasar + ".png"
    n = 1
    while (os.path.isfile(os.path.join(folder_referensi(), nama))
           and n < 1000):
        nama = "{}_{}.png".format(dasar, n)
        n += 1
    return nama


def muat_thumbnail(path, maks_w=190, maks_h=54):
    """Muat gambar referensi sebagai PhotoImage kecil (atau None)."""
    if not PIL_OK or not path or not os.path.isfile(path):
        return None
    try:
        with Image.open(path) as im:
            w, h = im.size
            if w < 1 or h < 1:
                return None
            s = min(1.0, float(maks_w) / w, float(maks_h) / h)
            im2 = im.convert("RGB").resize(
                (max(1, int(w * s)), max(1, int(h * s))))
            return ImageTk.PhotoImage(im2)
    except Exception:
        return None


# ------------------------------------------------------------
# v5.6 - Tema warna MODERN "DARK GLASS": navy pekat, panel
# kaca (permukaan sedikit lebih terang + garis bingkai tipis),
# dan aksen neon. Semua widget memakai konstanta di bawah,
# jadi tema bisa diubah dari satu tempat.
# ------------------------------------------------------------
C_BG      = "#0B1020"   # latar jendela (navy pekat)
C_PANEL   = "#131A2E"   # permukaan kaca (tabel / kotak isian)
C_PANEL2  = "#1B2440"   # kaca lebih terang (heading, tombol netral)
C_LINE    = "#2B3860"   # garis bingkai kaca
C_BLUE    = "#3B82F6"   # aksen utama (biru elektrik)
C_BLUE_D  = "#60A5FA"   # versi terang (teks aksen / tombol ditekan)
C_BLUE_L  = "#16294D"   # sorotan lembut (tombol sekunder)
C_RED     = "#EF4444"   # merah neon (BERHENTI)
C_RED_D   = "#B91C1C"
C_GREEN   = "#34D399"   # hijau neon (teks status)
C_GREEN_D = "#059669"   # hijau tombol (+ TAMBAH LANGKAH)
C_ORANGE  = "#FBBF24"   # aksen jeda / peringatan
C_TEXT    = "#E9EEFB"   # teks utama (hampir putih)
C_MUTED   = "#8E9BC0"   # teks redup
C_STRIPE  = "#0F1628"   # garis zebra tabel
C_SELROW  = "#1D3557"   # baris / sorotan terpilih
C_UNGU    = "#A78BFA"   # langkah TEKAN TOMBOL / ULANGI / langkah "S"
C_TEAL    = "#2DD4BF"   # langkah SCROLL

# v5.6: bungkus tk.Entry & tk.Checkbutton supaya tema gelap
# otomatis (kursor Entry putih, kotak centang gelap) tanpa
# harus mengubah satu per satu tempat widget dibuat.
# Class asli disimpan dulu supaya tidak rekursif.
_EntryAsli = tk.Entry
_CheckbuttonAsli = tk.Checkbutton
_KW_ENTRY_GELAP = dict(insertbackground=C_TEXT, disabledbackground=C_PANEL,
                       selectbackground=C_SELROW,
                       selectforeground=C_TEXT)
_KW_CHECK_GELAP = dict(selectcolor=C_PANEL2, activebackground=C_BG,
                       activeforeground=C_TEXT)

class _EntryTemaGelap(_EntryAsli):
    def __init__(self, *a, **kw):
        for k, v in _KW_ENTRY_GELAP.items():
            kw.setdefault(k, v)
        _EntryAsli.__init__(self, *a, **kw)

class _CheckbuttonTemaGelap(_CheckbuttonAsli):
    def __init__(self, *a, **kw):
        for k, v in _KW_CHECK_GELAP.items():
            kw.setdefault(k, v)
        _CheckbuttonAsli.__init__(self, *a, **kw)

tk.Entry = _EntryTemaGelap
tk.Checkbutton = _CheckbuttonTemaGelap

F_TITLE = ("Segoe UI", 14, "bold")
F_H     = ("Segoe UI", 10, "bold")
F_N     = ("Segoe UI", 10)
F_S     = ("Segoe UI", 9)
F_XS    = ("Segoe UI", 8)
F_MONO  = ("Consolas", 9)

# ------------------------------------------------------------
# v5.7 - Perangkat desain MODERN & ELEGAN: sudut membulat,
# tombol kapsul mengkilat, kartu kaca bersudut membulat,
# header gradien. Semuanya digambar sendiri di Canvas supaya
# tampil sama di Windows maupun Linux.
# ------------------------------------------------------------
def _campur(w1, w2, t):
    """Campur dua warna #rrggbb (t=0 -> w1, t=1 -> w2)."""
    try:
        r1, g1, b1 = int(w1[1:3], 16), int(w1[3:5], 16), int(w1[5:7], 16)
        r2, g2, b2 = int(w2[1:3], 16), int(w2[3:5], 16), int(w2[5:7], 16)
        return "#{:02x}{:02x}{:02x}".format(
            int(round(r1 + (r2 - r1) * t)),
            int(round(g1 + (g2 - g1) * t)),
            int(round(b1 + (b2 - b1) * t)))
    except Exception:
        return w1


def _cerahkan(warna, f=1.2):
    """Versi lebih terang (f=1.2 -> 20% menuju putih)."""
    return _campur(warna, "#FFFFFF", min(max(f - 1.0, 0.0), 1.0))


def _gelapkan(warna, f=0.25):
    """Versi lebih gelap (f=0.25 -> 25% menuju hitam)."""
    return _campur(warna, "#000000", min(max(f, 0.0), 1.0))


def kotak_bulat(cv, x1, y1, x2, y2, r, **kw):
    """Persegi bersudut MEMBULAT (poligon smooth) untuk Canvas."""
    r = max(1, min(int(r), int(x2 - x1) // 2, int(y2 - y1) // 2))
    titik = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r,
             x2, y2 - r, x2, y2, x2 - r, y2, x1 + r, y2,
             x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
    return cv.create_polygon(titik, smooth=True, **kw)


def menu_gelap(m):
    """v5.7: menu popup ikut tema gelap glass."""
    try:
        m.config(bg=C_PANEL2, fg=C_TEXT, activebackground=C_SELROW,
                 activeforeground=C_TEXT, bd=1, relief="flat", font=F_N)
    except Exception:
        pass


class TombolKapsul(tk.Canvas):
    """v5.7: tombol KAPSUL MEMBULAT & MENGKILAT (digambar Canvas).

    Pengganti modern tk.Button di toolbar: sudut membulat, kilau
    gradien lembut di badan tombol, efek sorot saat kursor di
    atas, efek tekan, dan keadaan nonaktif. API tk.Button yang
    dipakai aplikasi tetap didukung: config(state=, text=, bg=,
    fg=, command=, disabledforeground=, font=).
    """

    def __init__(self, parent, teks="", perintah=None, bg=None,
                 fg=None, font=None, radius=11, padx=13, tinggi=32,
                 garis=None, lebar_min=0):
        try:
            latar = parent.cget("bg")
        except Exception:
            latar = C_BG
        self._font = font or ("Segoe UI", 9, "bold")
        self._teks = teks
        self._perintah = perintah
        self._bg = bg or C_PANEL2
        self._fg = fg or C_TEXT
        self._dfg = None
        self._garis = garis
        self._radius = radius
        self._padx = padx
        self._lebar_min = lebar_min
        self._state = "normal"
        self._di_atas = False
        self._tekan = False
        super().__init__(parent, bg=latar, highlightthickness=0, bd=0,
                         height=tinggi, cursor="hand2")
        self.bind("<Configure>", lambda _e: self._gambar())
        self.bind("<Enter>", self._masuk)
        self.bind("<Leave>", self._keluar)
        self.bind("<ButtonPress-1>", self._tekan_mulai)
        self.bind("<ButtonRelease-1>", self._tekan_lepas)
        self._atur_lebar()

    # ---------- ukuran ----------
    def _atur_lebar(self):
        try:
            f = tkfont.Font(font=self._font)
            tw = max(f.measure(x) for x in
                     (self._teks.split("\n") or [""]))
        except Exception:
            tw = len(self._teks) * 7
        tk.Canvas.configure(self, width=max(self._lebar_min,
                                            int(tw) + self._padx * 2))

    # ---------- gambar ----------
    def _gambar(self, _e=None):
        self.delete("all")
        w = int(self.winfo_width())
        h = int(self.winfo_height())
        if w < 6 or h < 6:
            return
        r = max(2, min(self._radius, h // 2 - 1))
        if self._state == "disabled":
            isi = _campur(self._bg, C_BG, 0.55)
            teks = self._dfg or C_MUTED
            garis = C_LINE
            kilau = None
        elif self._tekan:
            isi = _gelapkan(self._bg, 0.18)
            teks = self._fg
            garis = _gelapkan(self._bg, 0.32)
            kilau = None
        elif self._di_atas:
            isi = _cerahkan(self._bg, 1.10)
            teks = self._fg
            garis = _cerahkan(self._bg, 1.5)
            kilau = _cerahkan(self._bg, 1.30)
        else:
            isi = self._bg
            teks = self._fg
            garis = self._garis or _gelapkan(self._bg, 0.30)
            kilau = _cerahkan(self._bg, 1.22)
        kotak_bulat(self, 1, 1, w - 2, h - 2, r, fill=isi, outline=garis)
        if kilau:
            # kilau: gradien vertikal halus mengikuti bentuk kapsul
            for y in range(2, h - 2):
                t = (y - 2) / float(max(1, h - 4))
                warna = _campur(kilau, isi, min(1.0, t * 1.55))
                dalam = 0
                if y < 1 + r:
                    dy = (1 + r) - y
                    if 0 <= dy < r:
                        dalam = r - int((r * r - dy * dy) ** 0.5)
                elif y > h - 2 - r:
                    dy = y - (h - 2 - r)
                    if 0 <= dy < r:
                        dalam = r - int((r * r - dy * dy) ** 0.5)
                self.create_line(2 + dalam, y, w - 2 - dalam, y,
                                 fill=warna)
        self.create_text(w / 2.0, h / 2.0, text=self._teks, fill=teks,
                         font=self._font)

    # ---------- interaksi ----------
    def _masuk(self, _e=None):
        if self._state == "normal":
            self._di_atas = True
            self._gambar()

    def _keluar(self, _e=None):
        self._di_atas = False
        self._tekan = False
        self._gambar()

    def _tekan_mulai(self, _e=None):
        if self._state == "normal":
            self._tekan = True
            self._gambar()

    def _tekan_lepas(self, e=None):
        if self._state != "normal":
            return
        tekan = self._tekan
        self._tekan = False
        self._gambar()
        if (tekan and e is not None
                and 0 <= e.x <= int(self.winfo_width())
                and 0 <= e.y <= int(self.winfo_height())
                and self._perintah):
            try:
                self._perintah()
            except Exception:
                pass

    # ---------- API ala tk.Button ----------
    def config(self, **kw):
        state = kw.pop("state", None)
        if state is not None:
            self._state = state
            self._di_atas = False
            tk.Canvas.configure(self, cursor="hand2"
                                if state == "normal" else "arrow")
        if "text" in kw:
            self._teks = kw.pop("text")
            self._atur_lebar()
        if "bg" in kw:
            self._bg = kw.pop("bg") or C_PANEL2
        if "fg" in kw:
            self._fg = kw.pop("fg") or C_TEXT
        if "disabledforeground" in kw:
            self._dfg = kw.pop("disabledforeground")
        if "command" in kw:
            self._perintah = kw.pop("command")
        if "font" in kw:
            self._font = kw.pop("font")
            self._atur_lebar()
        if kw:
            tk.Canvas.configure(self, **kw)
        self._gambar()

    configure = config


class TombolMenu(TombolKapsul):
    """v5.7: tombol kapsul yang membuka MENU saat diklik
    (pengganti modern tk.Menubutton)."""

    def __init__(self, parent, teks, menu=None, **kw):
        TombolKapsul.__init__(self, parent, teks=teks,
                              perintah=self._buka_menu, **kw)
        self._menu = menu

    def _buka_menu(self):
        m = self._menu
        if not m:
            return
        try:
            m.tk_popup(self.winfo_rootx(),
                       self.winfo_rooty() + self.winfo_height())
        finally:
            try:
                m.grab_release()
            except Exception:
                pass


class KartuBulat(tk.Frame):
    """v5.7: panel kaca bersudut MEMBULAT (bingkai digambar Canvas).

    Pengganti modern tk.LabelFrame: judul kecil di dalam kartu dan
    garis bingkai yang membulat di keempat sudutnya. Isi kartu
    ditaruh di .badan (frame di dalam kartu).
    """

    def __init__(self, parent, judul=None, radius=13, bg=C_BG,
                 garis=C_LINE, warna_judul=C_BLUE,
                 padding=(12, 7, 12, 9)):
        try:
            latar = parent.cget("bg")
        except Exception:
            latar = C_BG
        self._radius = radius
        self._bg = bg
        self._garis = garis
        super().__init__(parent, bg=latar)
        self.cv = tk.Canvas(self, bg=latar, highlightthickness=0, bd=0)
        self.cv.place(relwidth=1.0, relheight=1.0)
        # catatan: canvas dibuat lebih dulu dari judul/badan, jadi
        # otomatis berada di bawahnya (tidak perlu .lower() - nama
        # method itu milik item Canvas, bukan widget)
        kiri, atas, kanan, bawah = padding
        if judul:
            tk.Label(self, text=judul, bg=bg, fg=warna_judul,
                     font=F_H).pack(side="top", anchor="w",
                                    padx=kiri + 2, pady=(atas, 1))
            self.badan = tk.Frame(self, bg=bg)
            self.badan.pack(side="top", fill="both", expand=True,
                            padx=kiri, pady=(1, bawah))
        else:
            self.badan = tk.Frame(self, bg=bg)
            self.badan.pack(side="top", fill="both", expand=True,
                            padx=kiri, pady=(atas, bawah))
        self.bind("<Configure>", self._gambar)

    def _gambar(self, _e=None):
        w = int(self.winfo_width())
        h = int(self.winfo_height())
        if w < 8 or h < 8:
            return
        self.cv.delete("all")
        kotak_bulat(self.cv, 1, 1, w - 2, h - 2, self._radius,
                    fill=self._bg, outline=self._garis)


class HeaderKilau(tk.Canvas):
    """v5.7: header gradien mengkilat di atas tab
    (judul aplikasi + chip versi + hint hotkey)."""

    def __init__(self, parent, tinggi=64):
        super().__init__(parent, height=tinggi, bg=C_BG,
                         highlightthickness=0, bd=0)
        self.bind("<Configure>", lambda _e: self._gambar())

    def _gambar(self, _e=None):
        self.delete("all")
        w = int(self.winfo_width())
        h = int(self.winfo_height())
        if w < 40 or h < 20:
            return
        atas = _cerahkan(C_BLUE_L, 1.35)
        for y in range(h):
            t = y / float(max(1, h - 1))
            self.create_line(0, y, w, y, fill=_campur(atas, C_BG, t))
        self.create_line(0, h - 1, w, h - 1, fill=C_LINE)
        tengah = h / 2.0
        self.create_oval(18, tengah - 5, 28, tengah + 5, fill=C_BLUE,
                         outline="")
        self.create_text(38, tengah - 10, text=APP_NAME, anchor="w",
                         fill=C_TEXT, font=F_TITLE)
        self.create_text(39, tengah + 13, text="MACRO STUDIO EDITION",
                         anchor="w", fill=C_MUTED, font=F_XS)
        teks_v = "v{}".format(APP_VERSION)
        try:
            vw = tkfont.Font(font=F_H).measure(teks_v)
        except Exception:
            vw = 30
        kotak_bulat(self, w - vw - 34, tengah - 13, w - 16, tengah + 13,
                    12, fill=C_BLUE_L, outline=C_BLUE)
        self.create_text(w - 25 - vw / 2.0, tengah, text=teks_v,
                         fill=C_BLUE_D, font=F_H)
        self.create_text(w - vw - 48, tengah,
                         text="F6 Mulai   |   F7 / ESC Berhenti",
                         anchor="e", fill=C_MUTED, font=F_S)


def render_properti_multi(tab, pilihan, catatan=""):
    """v5.7: isi panel PROPERTI saat BANYAK baris terpilih."""
    tab._loading_prop = True
    for wdg in tab.prop_body.winfo_children():
        wdg.destroy()
    tab.lbl_ambil = None
    kotak = tk.Frame(tab.prop_body, bg=C_BG)
    kotak.pack(fill="both", expand=True)
    tk.Label(kotak, text="{} LANGKAH DIPILIH".format(len(pilihan)),
             bg=C_BG, fg=C_BLUE, font=F_TITLE).pack(pady=(4, 4))
    pesan = ("Aksi massal untuk semua langkah terpilih:\n\n"
             "  -  Ctrl+C / SALIN   = salin semua langkah terpilih\n"
             "  -  Ctrl+V / TEMPEL  = tempel berurutan setelah acuan\n"
             "  -  Del / HAPUS      = hapus semua langkah terpilih\n"
             + catatan +
             "\n  -  Klik SATU baris (tanpa Ctrl/Shift) untuk "
             "menyunting propertinya di panel ini.")
    tk.Label(kotak, text=pesan, bg=C_BG, fg=C_MUTED, font=F_N,
             justify="left").pack()
    tab._loading_prop = False

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

# ---- v4.2: pencarian gambar opsional pada SEMUA langkah ----
GAMBAR_AKSI_OPSI = ("Klik di gambar", "Pindah saja")
GAMBAR_GAGAL_OPSI = ("Klik titik X,Y", "Lewati langkah", "Stop alur")

# v5.3 (Studio): tidak ada lagi titik X,Y - fallback tanpa posisi
GAMBAR_GAGAL_OPSI_STUDIO = ("Lewati langkah", "Klik tengah area",
                            "Stop alur")


def gambar_langkah_default():
    """Config pencarian gambar untuk SATU langkah (bawaan/salinan)."""
    return {"aktif": False, "path": "", "aksi": "Klik di gambar",
            "gagal": "Klik titik X,Y", "radius": "", "mirip": ""}


# Parameter tambahan yang dimiliki SALINAN tiap jenis langkah
# (nama, label tampilan, lebar entry)
PARAM_DEF = {
    "pos_jadwal": [], "pos_negara": [], "pos_pilih_neg": [],
    "pos_oke": [], "pos_tambah": [], "pos_video": [],
    "pos_edit": [], "pos_judul": [], "pos_konfirmasi": [],
    "pos_tanggal": [("teks", "TANGGAL & JAM RILIS", 22)],
    "pos_bebas1": [("klik", "JUMLAH KLIK (0-500)", 6),
                   ("scroll", "JUMLAH SCROLL (0-50)", 6)],
    "pos_bebas2": [("klik", "JUMLAH KLIK (0-20)", 6)],
    "pos_submit": [("klik", "JUMLAH KLIK (1-10)", 6)],
}
PARAM_BAWAAN = {"teks": "", "klik": "1", "scroll": "0"}


# ============================================================
# v5.0 STUDIO MAKRO - langkah generik bebas (ala Jitbit)
# Semua jenis aksi jadi "menu" tersendiri; alur kerja disusun
# sendiri satu per satu pada tabel kosong di tab STUDIO MAKRO.
# ============================================================
JENIS_STUDIO = ("KLIK", "JEDA", "GAMBAR", "KETIK", "TANGGAL_JAM",
                "VIDEO_CAPTION", "TOMBOL", "SCROLL", "CATATAN",
                "LOOP_MULAI", "LOOP_AKHIR")

LABEL_JENIS = {
    "KLIK": "KLIK TITIK",
    "JEDA": "JEDA / TUNGGU",
    "GAMBAR": "CARI GAMBAR",
    "KETIK": "KETIK TEKS",
    "TANGGAL_JAM": "ISI TANGGAL-JAM",
    "VIDEO_CAPTION": "ISI VIDEO & CAPTION",
    "TOMBOL": "TEKAN TOMBOL",
    "SCROLL": "SCROLL",
    "CATATAN": "CATATAN",
    "LOOP_MULAI": "ULANGI - MULAI",
    "LOOP_AKHIR": "ULANGI - AKHIR",
}

# v5.2: sumber nilai langkah ISI TANGGAL-JAM
SUMBER_TANGGAL_OPSI = ("Tab CutMotions", "Tetap (isi sendiri)")

# v5.2: pilihan isi langkah ISI VIDEO & CAPTION
ISI_VIDEO_OPSI = ("Jumlah video",
                  "Caption dasar + nama video",
                  "Nama video saja",
                  "Teks sendiri + placeholder")

MOUSE_OPSI = ("Klik kiri", "Klik kanan", "Klik dobel")

# label pendek khusus tombol toolbar (menyesuaikan lebar jendela)
LABEL_TB = {
    "KLIK": "+ KLIK",
    "JEDA": "+ JEDA",
    "GAMBAR": "+ CARI GAMBAR",
    "KETIK": "+ KETIK",
    "TANGGAL_JAM": "+ TANGGAL-JAM",
    "VIDEO_CAPTION": "+ VIDEO+CAPTION",
    "TOMBOL": "+ TOMBOL",
    "SCROLL": "+ SCROLL",
    "CATATAN": "+ CATATAN",
}

TOMBOL_KB_OPSI = (
    "Enter", "Tab", "Esc", "Spasi",
    "Panah Bawah", "Panah Atas", "Panah Kiri", "Panah Kanan",
    "Backspace", "Delete", "Home", "End", "Page Down", "Page Up",
    "Shift+Tab", "Shift+Panah Bawah", "Shift+Panah Atas",
    "Ctrl+A", "Ctrl+C", "Ctrl+V", "Ctrl+S", "Ctrl+Z",
    "F2", "F4", "F5",
)

# nama tombol -> (modifikasi, kunci pynput); kunci tanpa "Key."
TOMBOL_MAP = {
    "Enter": ("", "enter"), "Tab": ("", "tab"), "Esc": ("", "esc"),
    "Spasi": ("", "space"),
    "Panah Bawah": ("", "down"), "Panah Atas": ("", "up"),
    "Panah Kiri": ("", "left"), "Panah Kanan": ("", "right"),
    "Backspace": ("", "backspace"), "Delete": ("", "delete"),
    "Home": ("", "home"), "End": ("", "end"),
    "Page Down": ("", "page_down"), "Page Up": ("", "page_up"),
    "Shift+Tab": ("shift", "tab"),
    "Shift+Panah Bawah": ("shift", "down"),
    "Shift+Panah Atas": ("shift", "up"),
    "Ctrl+A": ("ctrl", "a"), "Ctrl+C": ("ctrl", "c"),
    "Ctrl+V": ("ctrl", "v"), "Ctrl+S": ("ctrl", "s"),
    "Ctrl+Z": ("ctrl", "z"),
    "F2": ("", "f2"), "F4": ("", "f4"), "F5": ("", "f5"),
}

# v5.4: tombol khusus yang DIREKAM saat REKAM AKSI
# (kunci = objek Key pynput/stub, nilai = nama di TOMBOL_KB_OPSI)
TOMBOL_REKAM_MAP = {
    Key.enter: "Enter", Key.tab: "Tab",
    Key.backspace: "Backspace", Key.delete: "Delete",
    Key.home: "Home", Key.end: "End",
    Key.page_up: "Page Up", Key.page_down: "Page Down",
    Key.up: "Panah Atas", Key.down: "Panah Bawah",
    Key.left: "Panah Kiri", Key.right: "Panah Kanan",
    Key.f2: "F2", Key.f4: "F4", Key.f5: "F5",
}

# v5.4: kombinasi Shift+Panah yang dikenali saat merekam
TOMBOL_REKAM_SHIFT = {
    "Panah Atas": "Shift+Panah Atas",
    "Panah Bawah": "Shift+Panah Bawah",
}


def studio_langkah_baru(jenis, uid, **isi):
    """Satu langkah generik Studio Makro dengan nilai bawaan aman."""
    l = {
        "uid": "s{}".format(uid),
        "jenis": jenis if jenis in JENIS_STUDIO else "KLIK",
        "nama": "",
        "aktif": True,
        "posisi": None,        # [x, y] - KLIK / titik acuan GAMBAR
        "jeda": 0.5,           # jeda sebelum langkah (detik)
        "jeda_klik": 0.30,     # jeda antar klik / tekan (detik)
        # KLIK
        "klik": 1,             # jumlah klik
        "tombol_mouse": "Klik kiri",
        "geser": 0,            # geser Y per putaran loop (piksel)
        # JEDA
        "detik": 1.0,
        # KETIK
        "teks": "",
        "ctrl_a": False,
        "enter": False,
        # TOMBOL
        "tombol_kb": "Enter",
        "jumlah_kb": 1,
        # SCROLL
        "arah": "Turun",
        "jumlah_scroll": 3,
        # CATATAN
        "catatan": "",
        # TANGGAL_JAM (v5.2)
        "sumber": "Tab CutMotions",
        # VIDEO_CAPTION (v5.2)
        "isi": "Caption dasar + nama video",
        # LOOP_MULAI
        "jumlah_loop": 2,
        "ikut_video": False,   # ikut jumlah video tab CutMotions
        # GAMBAR
        "gambar": {"path": "", "aksi": "Klik di gambar",
                   "gagal": "Lewati langkah", "radius": "300",
                   "mirip": "0.80", "fokus": None},
    }
    # nilai bawaan khusus per jenis (sebelum isi menimpa)
    if jenis == "TANGGAL_JAM":
        l["ctrl_a"] = True
        l["teks"] = "2026-09-10 02:05:01"
    elif jenis == "VIDEO_CAPTION":
        l["ctrl_a"] = True
    for k, v in isi.items():
        if k in l and v is not None:
            l[k] = v
    return l


def studio_bersihkan(daftar):
    """Sanitasi daftar langkah Studio dari file JSON (buang rusak)."""
    hasil = []
    if not isinstance(daftar, list):
        return hasil
    for e in daftar:
        if not isinstance(e, dict):
            continue
        jenis = str(e.get("jenis") or "")
        if jenis not in JENIS_STUDIO:
            continue
        l = studio_langkah_baru(jenis, 0)
        for k in l:
            if k == "uid":
                l["uid"] = str(e.get("uid") or "s0")
            elif k == "posisi":
                p = e.get("posisi")
                try:
                    l["posisi"] = [int(p[0]), int(p[1])] if p else None
                except Exception:
                    l["posisi"] = None
            elif k == "gambar":
                g = e.get("gambar")
                if isinstance(g, dict):
                    l["gambar"]["path"] = str(g.get("path") or "")
                    aksi = str(g.get("aksi") or "")
                    l["gambar"]["aksi"] = (aksi
                                           if aksi in GAMBAR_AKSI_OPSI
                                           else "Klik di gambar")
                    gagal = str(g.get("gagal") or "")
                    if gagal in GAMBAR_GAGAL_OPSI_STUDIO:
                        l["gambar"]["gagal"] = gagal
                    elif gagal == "Klik titik X,Y":
                        # makro lama v5.2: titik acuan jadi area
                        l["gambar"]["gagal"] = "Klik tengah area"
                    else:
                        l["gambar"]["gagal"] = "Lewati langkah"
                    l["gambar"]["radius"] = str(g.get("radius") or "300")
                    l["gambar"]["mirip"] = str(g.get("mirip") or "0.80")
                    # v5.3: AREA FOKUS [x1,y1,x2,y2] atau None
                    f = g.get("fokus")
                    if isinstance(f, (list, tuple)) and len(f) == 4:
                        try:
                            fx = [int(float(v)) for v in f]
                            l["gambar"]["fokus"] = [
                                min(fx[0], fx[2]), min(fx[1], fx[3]),
                                max(fx[0], fx[2]), max(fx[1], fx[3])]
                        except (ValueError, TypeError):
                            l["gambar"]["fokus"] = None
                    else:
                        l["gambar"]["fokus"] = None
            elif k == "aktif":
                # langkah tanpa kunci "aktif" dianggap AKTIF
                l[k] = bool(e.get(k, True))
            elif k in ("ctrl_a", "enter", "ikut_video"):
                l[k] = bool(e.get(k))
            elif k in ("jeda", "jeda_klik", "detik"):
                lo = 0.05 if k == "jeda_klik" else 0.0
                l[k] = _angka(e.get(k), l[k], lo, 86400)
            elif k in ("klik", "jumlah_kb", "jumlah_scroll", "geser",
                       "jumlah_loop"):
                l[k] = int(_angka(e.get(k), l[k], 0, 100000))
            elif k == "tombol_mouse":
                v = str(e.get(k) or "")
                l[k] = v if v in MOUSE_OPSI else "Klik kiri"
            elif k == "arah":
                v = str(e.get(k) or "")
                l[k] = v if v in ("Turun", "Naik") else "Turun"
            elif k == "sumber":
                v = str(e.get(k) or "")
                l[k] = (v if v in SUMBER_TANGGAL_OPSI
                        else "Tab CutMotions")
            elif k == "isi":
                v = str(e.get(k) or "")
                l[k] = (v if v in ISI_VIDEO_OPSI
                        else "Caption dasar + nama video")
            elif k in ("teks", "catatan", "tombol_kb", "nama"):
                l[k] = str(e.get(k) if e.get(k) is not None else l[k])
        hasil.append(l)
    return hasil


# ------------------------------------------------------------
# v5.4 REKAM AKSI - ubah kejadian mentah hasil rekaman menjadi
# langkah Studio Makro. Dipisah dari GUI supaya bisa diuji
# otomatis tanpa layar / pynput.
# ------------------------------------------------------------
def perekam_bangun_langkah(kejadian, mulai_uid=0, jeda_maks=10.0):
    """Ubah urutan kejadian rekaman menjadi langkah Studio Makro.

    kejadian = list dict hasil rekaman (urut waktu):
      {"tipe": "klik", "x": .., "y": .., "tombol": "kiri"/"kanan",
       "waktu": waktu_unix}
      {"tipe": "char", "teks": "a", "waktu": ..}   (karakter tercetak)
      {"tipe": "tombol", "nama": "Enter", "waktu": ..}
      {"tipe": "scroll", "arah": "Turun"/"Naik", "waktu": ..}

    Aturan penggabungan:
      - Huruf/angka berurutan digabung jadi SATU langkah KETIK.
      - 2 klik kiri < 0,45 detik di posisi hampir sama = Klik dobel.
      - Gulungan mouse searah berurutan (< 1,5 detik) jadi SATU
        langkah SCROLL dengan jumlah gulungan digabung.
      - Jeda antar langkah = jarak waktu kejadian asli, dibatasi
        0,1 - jeda_maks detik (biarkan user menyunting).

    Mengembalikan (daftar_langkah, uid_terakhir_dipakai).
    """
    langkah = []
    uid = int(mulai_uid)
    terakhir = [None]     # waktu kejadian sebelumnya (list = mutable)

    def jeda_dari(waktu):
        if terakhir[0] is None:
            return 0.2
        return round(_angka(waktu - terakhir[0], 0.1, 0.1, jeda_maks), 1)

    def tambah(jenis, waktu, **isi):
        nonlocal uid
        uid += 1
        l = studio_langkah_baru(jenis, uid, **isi)
        l["jeda"] = jeda_dari(waktu)
        langkah.append(l)
        return l

    teks_buf = []                      # huruf berurutan belum dilucutkan
    teks_mulai = [None]
    teks_akhir = [None]
    scroll_buf = [None]                # gulungan berurutan belum dilucutkan
    klik_terakhir = [None]             # utk deteksi klik dobel

    def flush_teks():
        """Lucutkan huruf terkumpul jadi satu langkah KETIK."""
        if not teks_buf:
            return None
        l = tambah("KETIK", teks_mulai[0], teks="".join(teks_buf))
        terakhir[0] = teks_akhir[0]
        teks_buf.clear()
        teks_mulai[0] = teks_akhir[0] = None
        return l

    def flush_scroll():
        """Lucutkan gulungan terkumpul jadi satu langkah SCROLL."""
        if scroll_buf[0] is None:
            return None
        s = scroll_buf[0]
        l = tambah("SCROLL", s["waktu"], arah=s["arah"],
                   jumlah_scroll=s["jumlah"])
        terakhir[0] = s["waktu_akhir"]
        scroll_buf[0] = None
        return l

    for ev in kejadian:
        if not isinstance(ev, dict):
            continue
        tipe = ev.get("tipe")
        waktu = _angka(ev.get("waktu"), 0.0, 0, 1e18)
        if tipe == "klik":
            flush_teks()
            flush_scroll()
            x = int(_angka(ev.get("x"), 0, 0, 100000))
            y = int(_angka(ev.get("y"), 0, 0, 100000))
            kanan = (ev.get("tombol") == "kanan")
            # deteksi klik dobel: klik kiri berikutnya < 0,45 dtk dan
            # posisinya hampir sama (<= 6 px) -> ubah langkah sebelumnya
            kt = klik_terakhir[0]
            if (not kanan and kt is not None
                    and abs(waktu - kt["waktu"]) <= 0.45
                    and abs(x - kt["x"]) <= 6
                    and abs(y - kt["y"]) <= 6):
                kt["langkah"]["tombol_mouse"] = "Klik dobel"
                klik_terakhir[0] = None
                terakhir[0] = waktu
                continue
            l = tambah("KLIK", waktu, posisi=[x, y],
                       tombol_mouse="Klik kanan" if kanan
                       else "Klik kiri")
            klik_terakhir[0] = None if kanan else {
                "langkah": l, "x": x, "y": y, "waktu": waktu}
            terakhir[0] = waktu
        elif tipe == "char":
            ch = str(ev.get("teks") or "")
            if not ch:
                continue
            if not teks_buf:
                flush_scroll()
                teks_mulai[0] = waktu
            teks_buf.append(ch)
            teks_akhir[0] = waktu
            klik_terakhir[0] = None
        elif tipe == "tombol":
            flush_teks()
            flush_scroll()
            nama = str(ev.get("nama") or "")
            if nama:
                tambah("TOMBOL", waktu, tombol_kb=nama)
            terakhir[0] = waktu
        elif tipe == "scroll":
            flush_teks()
            arah = "Naik" if ev.get("arah") == "Naik" else "Turun"
            s = scroll_buf[0]
            if (s is not None and s["arah"] == arah
                    and abs(waktu - s["waktu_akhir"]) <= 1.5):
                s["jumlah"] += 1
                s["waktu_akhir"] = waktu
            else:
                flush_scroll()
                scroll_buf[0] = {"arah": arah, "jumlah": 1,
                                 "waktu": waktu, "waktu_akhir": waktu}
            klik_terakhir[0] = None
    flush_teks()
    flush_scroll()
    return langkah, uid


def area_dari_langkah(l):
    """v5.3: hitung AREA FOKUS pencarian gambar dari sebuah langkah.

    Urutan prioritas:
      1. l["gambar"]["fokus"]  - kotak [x1,y1,x2,y2] pilihan user.
      2. l["posisi"] + radius  - makro lama v5.2 (titik acuan)
         dikonversi jadi kotak persegi, supaya makro lama tetap
         berjalan tanpa diubah.
      3. None                  - cari di seluruh layar.
    """
    g = l.get("gambar") or {}
    f = g.get("fokus")
    if isinstance(f, (list, tuple)) and len(f) == 4:
        try:
            fx = [int(v) for v in f]
            return [min(fx[0], fx[2]), min(fx[1], fx[3]),
                    max(fx[0], fx[2]), max(fx[1], fx[3])]
        except (ValueError, TypeError):
            pass
    titik = l.get("posisi")
    if titik:
        try:
            px, py = int(titik[0]), int(titik[1])
        except (ValueError, TypeError, IndexError):
            return None
        r = int(_angka(g.get("radius"), 300, 10, 4000))
        return [max(0, px - r), max(0, py - r), px + r, py + r]
    return None


def isi_placeholder(teks, idx, caption, videos, jumlah=None):
    """Ganti {caption} {video} {no} {jumlah} pada teks langkah.

    idx    = nomor putaran loop dalam (0-based);
    videos = daftar nama file video (baris ke-idx dipakai);
    jumlah = jumlah video total (bawaan: sepanjang daftar videos).
    """
    teks = str(teks or "")
    if "{" not in teks:
        return teks
    if videos:
        nama = videos[idx] if 0 <= idx < len(videos) else videos[0]
        nama = os.path.splitext(os.path.basename(nama))[0]
        caption_val = compose_caption(caption, nama)
    else:
        # tidak ada video: caption dasar saja, {video} kosong
        nama = ""
        caption_val = (caption or "").strip()
    if jumlah is None:
        jumlah = len(videos) if videos else 0
    teks = teks.replace("{caption}", caption_val)
    teks = teks.replace("{video}", nama)
    teks = teks.replace("{no}", str(idx + 1))
    teks = teks.replace("{jumlah}", str(jumlah))
    return teks


def cari_akhir_loop(langkah, i):
    """Dari LOOP_MULAI di indeks i, cari indeks LOOP_AKHIR pasangannya.

    Tahan blok bersarang (loop dalam loop). Bila tidak ada pasangan,
    kembalikan -1.
    """
    dalam = 0
    for j in range(i + 1, len(langkah)):
        t = langkah[j].get("jenis")
        if t == "LOOP_MULAI":
            dalam += 1
        elif t == "LOOP_AKHIR":
            if dalam == 0:
                return j
            dalam -= 1
    return -1


# ------------------------------------------------------------
# v5.5: Tampilan & mesin eksekusi langkah Studio Makro sebagai
# FUNGSI MODUL - dipakai BERSAMA oleh tab STUDIO MAKRO dan
# tab ALUR CUTMOTIONS (A-J). Dengan begini SEMUA menu Studio
# (klik, jeda, cari gambar, ketik, tanggal-jam, video+caption,
# tombol, scroll, catatan, blok ULANGI) bisa dimasukkan ke
# dalam alur CutMotions dan dijalankan tepat di posisinya.
# ------------------------------------------------------------


def studio_detail_teks(l):
    """Teks kolom DETAIL untuk satu langkah Studio (semua jenis)."""
    jenis = l["jenis"]
    pos = l.get("posisi")
    pos_t = "({},{})".format(pos[0], pos[1]) if pos else "belum diatur"
    if jenis == "KLIK":
        mode = str(l.get("tombol_mouse") or "Klik kiri").lower()
        n = int(_angka(l.get("klik"), 1, 0, 500))
        geser = int(_angka(l.get("geser"), 0, 0, 100000))
        teks = "{} | {}x".format(pos_t, mode)
        if n != 1:
            teks += " x{}".format(n)
        if geser:
            teks += " | geser +{} px/putaran".format(geser)
        return teks
    if jenis == "JEDA":
        return "tunggu {:.1f} detik".format(
            _angka(l.get("detik"), 1.0, 0, 86400))
    if jenis == "GAMBAR":
        g = l.get("gambar") or {}
        gm = os.path.basename(str(g.get("path") or "")) \
            if g.get("path") else "(gambar belum dipilih)"
        aksi_t = ("pindah saja"
                  if g.get("aksi") == "Pindah saja" else "klik gambar")
        f = g.get("fokus")
        if isinstance(f, (list, tuple)) and len(f) == 4:
            fokus_t = "fokus ({},{})-({},{})".format(
                f[0], f[1], f[2], f[3])
        else:
            fokus_t = "cari di seluruh layar"
        return "{} | {} | {}".format(fokus_t, gm, aksi_t)
    if jenis == "KETIK":
        t = str(l.get("teks") or "")
        if len(t) > 42:
            t = t[:42] + "..."
        extra = " | Ctrl+A dulu" if l.get("ctrl_a") else ""
        if l.get("enter"):
            extra += " | Enter"
        return '"{}"{}'.format(t, extra)
    if jenis == "TANGGAL_JAM":
        sumber = str(l.get("sumber") or "Tab CutMotions")
        if sumber == "Tetap (isi sendiri)":
            val = str(l.get("teks") or "(kosong)")
            if len(val) > 22:
                val = val[:22] + "..."
            return "{} | tetap: {}".format(pos_t, val)
        return "{} | dari setelan tab CutMotions".format(pos_t)
    if jenis == "VIDEO_CAPTION":
        isi = str(l.get("isi") or "Caption dasar + nama video")
        if isi == "Teks sendiri + placeholder":
            t = str(l.get("teks") or "")
            if len(t) > 26:
                t = t[:26] + "..."
            return "{} | teks: {}".format(pos_t, t or "(kosong)")
        return "{} | {}".format(pos_t, isi.lower())
    if jenis == "TOMBOL":
        return "tekan {} x{}".format(
            l.get("tombol_kb"),
            int(_angka(l.get("jumlah_kb"), 1, 1, 500)))
    if jenis == "SCROLL":
        return "{} x{}".format(
            l.get("arah"),
            int(_angka(l.get("jumlah_scroll"), 3, 0, 1000)))
    if jenis == "CATATAN":
        t = str(l.get("catatan") or l.get("nama") or l.get("label") or "")
        if len(t) > 60:
            t = t[:60] + "..."
        return t
    if jenis == "LOOP_MULAI":
        if l.get("ikut_video"):
            return "ulangi sebanyak jumlah video (tab CutMotions)"
        return "ulangi {}x".format(int(_angka(l.get("jumlah_loop"),
                                              2, 0, 100000)))
    return "kembali ke ULANGI-MULAI di atas"


def studio_ulang_teks(l):
    """Teks kolom ULANGI untuk satu langkah Studio (semua jenis)."""
    jenis = l["jenis"]
    if jenis == "KLIK":
        n = int(_angka(l.get("klik"), 1, 0, 500))
        return "pindah saja" if n == 0 else "{} klik".format(n)
    if jenis == "JEDA":
        return "-"
    if jenis == "GAMBAR":
        return "cari gambar"
    if jenis == "KETIK":
        return "1 ketikan"
    if jenis in ("TANGGAL_JAM", "VIDEO_CAPTION"):
        return "1 ketikan (isi otomatis)"
    if jenis == "TOMBOL":
        return "{} tekanan".format(int(_angka(l.get("jumlah_kb"), 1,
                                              1, 500)))
    if jenis == "SCROLL":
        return "{}x gulungan".format(int(_angka(
            l.get("jumlah_scroll"), 3, 0, 1000)))
    if jenis == "LOOP_MULAI":
        if l.get("ikut_video"):
            return "x jumlah video"
        return "{}x".format(int(_angka(l.get("jumlah_loop"), 2, 0,
                                       100000)))
    if jenis == "LOOP_AKHIR":
        return "akhir blok"
    return "-"


def studio_klik_titik(mesin, titik):
    """Pindahkan mouse lalu klik kiri satu titik."""
    try:
        mesin.mouse.position = (int(titik[0]), int(titik[1]))
        time.sleep(0.15)
        mesin.mouse.click(Button.left, 1)
    except Exception:
        pass


def studio_ketik(mesin, teks, ctrl_a=False, enter=False):
    """Ketik teks di posisi kursor (pilihan Ctrl+A / Enter)."""
    if not teks and not enter:
        return
    try:
        if ctrl_a:
            time.sleep(0.2)
            with mesin.kb.pressed(Key.ctrl):
                mesin.kb.press("a")
                mesin.kb.release("a")
            time.sleep(0.15)
        if teks:
            mesin.kb.type(teks)
        if enter:
            time.sleep(0.1)
            mesin.kb.press(Key.enter)
            mesin.kb.release(Key.enter)
    except Exception as e:
        mesin._set_status("Gagal mengetik: {}".format(e), C_ORANGE)


def studio_gambar_cari(mesin, l):
    """v5.3: cari gambar referensi lalu LANGSUNG DIKLIK / dipindah.

    v5.5: kini fungsi modul bersama - bisa dipakai langkah CARI
    GAMBAR di Studio MaKRO maupun di dalam alur CutMotions.
    TANPA titik acuan X,Y - gambar dicari di AREA FOKUS (atau
    seluruh layar). Kembalikan "stop" bila alur harus berhenti.
    """
    g = l.get("gambar") or {}
    path = str(g.get("path") or "").strip()
    nama = str(l.get("nama") or l.get("label") or "") \
        or LABEL_JENIS["GAMBAR"]
    if not path or not os.path.isfile(path):
        mesin._set_status(
            "Gambar referensi '{}' belum ada - langkah dilewati "
            "(klik POTONG GAMBAR di panel properti).".format(nama),
            C_ORANGE)
        return None
    if not CV_OK:
        mesin._set_status(
            "opencv-python belum terpasang - langkah CARI GAMBAR "
            "'{}' dilewati.".format(nama), C_ORANGE)
        return None
    mirip = _angka(g.get("mirip"), 0.8, 0.5, 0.99)
    area = area_dari_langkah(l)
    if area:
        desk = "area fokus ({},{})-({},{})".format(area[0], area[1],
                                                   area[2], area[3])
    else:
        desk = "seluruh layar"
    hasil = None
    pesan = ""
    for percobaan in range(1, 4):
        mesin._set_status(
            "Cari gambar '{}' di {} (percobaan {}/3, "
            "multi-skala)...".format(os.path.basename(path), desk,
                                     percobaan), C_GREEN)
        hasil, pesan = cari_di_layar_area(path, area, mirip)
        if hasil:
            break
        mesin._sleep(1.0)
    if hasil:
        x, y, skor = hasil
        if str(g.get("aksi")) == "Pindah saja":
            try:
                mesin.mouse.position = (x, y)
            except Exception:
                pass
            mesin._set_status(
                "Gambar '{}' KETEMU di ({}, {}) - kemiripan {:.0%} - "
                "mouse DIPINDAH tanpa klik.".format(nama, x, y, skor),
                C_GREEN)
            return None
        mesin._set_status(
            "Gambar '{}' KETEMU di ({}, {}) - kemiripan {:.0%} - "
            "diklik.".format(nama, x, y, skor), C_GREEN)
        studio_klik_titik(mesin, (x, y))
        return None
    pilihan = str(g.get("gagal") or "Lewati langkah")
    if pilihan == "Stop alur":
        mesin._finish("Dihentikan: gambar '{}' tidak ketemu 3x. {}"
                      .format(os.path.basename(path), pesan), warn=True)
        return "stop"
    if pilihan == "Klik tengah area" and area:
        tengah = ((area[0] + area[2]) // 2, (area[1] + area[3]) // 2)
        mesin._set_status(
            "Gambar '{}' tidak ketemu - klik tengah area fokus {}. "
            "{}".format(nama, tengah, pesan), C_ORANGE)
        studio_klik_titik(mesin, tengah)
        return None
    mesin._set_status("Gambar '{}' tidak ketemu - langkah dilewati. "
                      "{}".format(nama, pesan), C_ORANGE)
    return None


def studio_jalankan_langkah(mesin, l, idx=0, videos=None, caption="",
                            jumlah=None, tanggal="", geser_baris=0):
    """Jalankan SATU langkah Studio (semua jenis kecuali blok ULANGI).

    mesin       : objek dengan mouse, kb, stop_event, _sleep,
                  _set_status, _finish (kedua tab memenuhinya).
    idx         : nomor putaran ULANGI (0-based) / baris caption.
    videos      : daftar nama file video (untuk placeholder).
    caption     : caption dasar.
    jumlah      : jumlah video total (bila None: panjang videos).
    tanggal     : tanggal-jam rilis dari tab CutMotions.
    geser_baris : geser Y tambahan (px) - posisi baris video pada
                  fase caption alur CutMotions (i x JARAK ANTAR BARIS).

    Kembalikan "stop" bila alur harus dihentikan, selain itu None.
    """
    jenis = str(l.get("jenis") or "")
    if jenis == "CATATAN":
        teks = str(l.get("catatan") or l.get("nama") or l.get("label")
                   or "")
        if teks:
            mesin._set_status("CATATAN: {}".format(teks), C_BLUE)
        return None
    if jenis == "JEDA":
        d = _angka(l.get("detik"), 1.0, 0, 86400)
        mesin._set_status("Tunggu {:.1f} detik...".format(d), C_GREEN)
        mesin._sleep(d)
        return None
    if jenis == "KLIK":
        titik = l.get("posisi")
        if not titik:
            mesin._set_status("Posisi klik belum diatur - langkah "
                              "dilewati.", C_ORANGE)
            return None
        geser = int(_angka(l.get("geser"), 0, 0, 100000)) * idx \
            + int(geser_baris or 0)
        tujuan = (int(titik[0]), int(titik[1]) + geser)
        n = int(_angka(l.get("klik"), 1, 0, 500))
        jk = max(0.05, _angka(l.get("jeda_klik"), 0.3, 0.05, 60))
        mode = l.get("tombol_mouse") if l.get("tombol_mouse") \
            in MOUSE_OPSI else "Klik kiri"
        try:
            mesin.mouse.position = tujuan
            time.sleep(0.12)
        except Exception:
            pass
        for k in range(n):
            if mesin.stop_event.is_set():
                break
            try:
                if mode == "Klik kanan":
                    mesin.mouse.click(Button.right, 1)
                elif mode == "Klik dobel":
                    mesin.mouse.click(Button.left, 2)
                else:
                    mesin.mouse.click(Button.left, 1)
            except Exception:
                pass
            if k < n - 1:
                time.sleep(jk)
        return None
    if jenis == "GAMBAR":
        return studio_gambar_cari(mesin, l)
    videos = list(videos or [])
    jumlah_total = int(jumlah) if jumlah else len(videos)
    if jenis == "KETIK":
        teks = isi_placeholder(l.get("teks", ""), idx, caption, videos,
                               jumlah_total)
        studio_ketik(mesin, teks, bool(l.get("ctrl_a")),
                     bool(l.get("enter")))
        return None
    if jenis == "TANGGAL_JAM":
        sumber = str(l.get("sumber") or "Tab CutMotions")
        if sumber == "Tetap (isi sendiri)":
            teks = str(l.get("teks") or "").strip()
        else:
            teks = str(tanggal or "").strip()
        if not teks:
            mesin._set_status(
                "Tanggal-jam masih KOSONG - langkah dilewati. Isi kolom "
                "TANGGAL & JAM RILIS, atau ganti sumber nilai di "
                "properti langkah.", C_ORANGE)
            return None
        rapikan = parse_tanggal(teks)
        if rapikan:
            teks = rapikan
        else:
            mesin._set_status(
                "Format tanggal '{}' tidak dikenal - diketik apa adanya "
                "(format benar: 2026-09-10 02:05:01).".format(teks),
                C_ORANGE)
        if l.get("posisi"):
            studio_klik_titik(mesin, l["posisi"])
            mesin._sleep(0.4)
        mesin._set_status("Isi tanggal-jam rilis: {}".format(teks),
                          C_GREEN)
        studio_ketik(mesin, teks, bool(l.get("ctrl_a", True)),
                     bool(l.get("enter")))
        return None
    if jenis == "VIDEO_CAPTION":
        isi = str(l.get("isi") or "Caption dasar + nama video")
        if isi == "Jumlah video":
            teks = str(jumlah_total)
        elif isi == "Nama video saja":
            teks = isi_placeholder("{video}", idx, caption, videos,
                                   jumlah_total)
        elif isi == "Teks sendiri + placeholder":
            teks = isi_placeholder(str(l.get("teks") or ""), idx, caption,
                                   videos, jumlah_total)
        else:
            teks = isi_placeholder("{caption}", idx, caption, videos,
                                   jumlah_total)
        if not teks:
            mesin._set_status(
                "Tidak ada teks untuk diketik (folder video / jumlah "
                "kosong) - langkah dilewati.", C_ORANGE)
            return None
        if l.get("posisi"):
            studio_klik_titik(mesin, l["posisi"])
            mesin._sleep(0.4)
        mesin._set_status("Isi {}: {}".format(isi.lower(), teks), C_GREEN)
        studio_ketik(mesin, teks, bool(l.get("ctrl_a", True)),
                     bool(l.get("enter")))
        return None
    if jenis == "TOMBOL":
        nama = str(l.get("tombol_kb") or "Enter").strip() or "Enter"
        n = int(_angka(l.get("jumlah_kb"), 1, 1, 500))
        jk = max(0.05, _angka(l.get("jeda_klik"), 0.3, 0.05, 60))
        mod, kunci = TOMBOL_MAP.get(nama, ("", None))
        try:
            if kunci is None:
                if len(nama) == 1:
                    for k in range(n):
                        if mesin.stop_event.is_set():
                            break
                        mesin.kb.type(nama)
                        if k < n - 1:
                            time.sleep(jk)
                else:
                    mesin._set_status("Tombol '{}' tidak dikenal - "
                                      "dilewati.".format(nama), C_ORANGE)
                return None
            obj = getattr(Key, kunci, None)
            if obj is None:
                mesin._set_status("Tombol '{}' tidak dikenal - dilewati."
                                  .format(nama), C_ORANGE)
                return None

            def tekan():
                mesin.kb.press(obj)
                mesin.kb.release(obj)

            if mod == "shift":
                with mesin.kb.pressed(Key.shift):
                    for k in range(n):
                        if mesin.stop_event.is_set():
                            break
                        tekan()
                        if k < n - 1:
                            time.sleep(jk)
            elif mod == "ctrl":
                with mesin.kb.pressed(Key.ctrl):
                    for k in range(n):
                        if mesin.stop_event.is_set():
                            break
                        tekan()
                        if k < n - 1:
                            time.sleep(jk)
            else:
                for k in range(n):
                    if mesin.stop_event.is_set():
                        break
                    tekan()
                    if k < n - 1:
                        time.sleep(jk)
        except Exception as e:
            mesin._set_status("Gagal menekan tombol: {}".format(e),
                              C_ORANGE)
        return None
    if jenis == "SCROLL":
        n = int(_angka(l.get("jumlah_scroll"), 3, 0, 1000))
        arah = -3 if l.get("arah") == "Turun" else 3
        jk = max(0.05, _angka(l.get("jeda_klik"), 0.3, 0.05, 60))
        for k in range(n):
            if mesin.stop_event.is_set():
                break
            try:
                mesin.mouse.scroll(0, arah)
            except Exception:
                pass
            if k < n - 1:
                time.sleep(jk)
        return None
    return None


def template_cutmotions_steps(cfg, mulai_uid=0):
    """Bangun langkah Studio versi bebas dari setelan tab CutMotions.

    cfg = dict berisi posisi A-J + nilai vars tab CutMotions
    (lihat StudioMakroTab._template_cutmotions).
    Kembalikan list langkah generik siap edit/jalankan.
    """
    steps = []
    ctr = [int(mulai_uid)]

    def add(jenis, **kw):
        ctr[0] += 1
        steps.append(studio_langkah_baru(jenis, ctr[0], **kw))

    pos = cfg.get("posisi") or {}

    def P(k):
        p = pos.get(k)
        return list(p) if p else None

    if not cfg.get("skip_jadwal"):
        add("KLIK", nama="A - Klik 'Jadwal rilis'", posisi=P("pos_jadwal"))
        add("KLIK", nama="B - Klik dropdown 'NEGARA'",
            posisi=P("pos_negara"))
        g = cfg.get("gambar_c")
        if g and g.get("aktif") and g.get("path"):
            gagal_c = str(g.get("gagal") or "")
            if gagal_c not in GAMBAR_GAGAL_OPSI_STUDIO:
                gagal_c = ("Klik tengah area"
                           if gagal_c == "Klik titik X,Y"
                           else "Lewati langkah")
            add("GAMBAR", nama="C - Pilih negara (cari gambar)",
                posisi=P("pos_pilih_neg"),
                gambar={"path": str(g.get("path") or ""),
                        "aksi": g.get("aksi") or "Klik di gambar",
                        "gagal": gagal_c,
                        "radius": str(g.get("radius") or "300"),
                        "mirip": str(g.get("mirip") or "0.80"),
                        "fokus": None})
        else:
            add("KLIK", nama="C - Pilih negara", posisi=P("pos_pilih_neg"))
        add("KLIK", nama="D - Klik kolom tanggal", posisi=P("pos_tanggal"))
        add("TANGGAL_JAM", nama="D - Isi tanggal-jam rilis",
            teks=cfg.get("tanggal", ""), sumber="Tetap (isi sendiri)")
        add("KLIK", nama="E - Klik 'OKE'", posisi=P("pos_oke"))
    add("KLIK", nama="F - Klik '+ Tambah video'", posisi=P("pos_tambah"))
    nk = int(_angka(cfg.get("klik_bebas1"), 2, 0, 500))
    ns = int(_angka(cfg.get("scroll_bebas1"), 0, 0, 50))
    if nk:
        add("KLIK", nama="G - Klik dialog pilih file",
            posisi=P("pos_bebas1"), klik=nk)
    if ns:
        add("SCROLL", nama="G - Scroll dialog pilih file",
            arah=cfg.get("arah_scroll") or "Turun", jumlah_scroll=ns)
    add("KLIK", nama="H - Klik video pertama", posisi=P("pos_video"))
    jumlah = max(1, int(_angka(cfg.get("jumlah"), 5, 1, MAX_BATCH)))
    if jumlah > 1:
        add("TOMBOL", nama="H - Shift+panah bawah (pilih batch)",
            tombol_kb="Shift+Panah Bawah", jumlah_kb=jumlah - 1,
            jeda_klik=0.15)
    nk2 = int(_angka(cfg.get("klik_bebas2"), 1, 0, 20))
    if nk2:
        add("KLIK", nama="H2 - Klik tombol 'Buka'", posisi=P("pos_bebas2"),
            klik=nk2)
    tunggu = _angka(cfg.get("tunggu"), 60, 0, 86400)
    add("CATATAN", nama="Menunggu {} video selesai terupload...".format(
        jumlah))
    add("JEDA", nama="Tunggu upload selesai", detik=tunggu * jumlah)
    jarak = int(_angka(cfg.get("jarak_baris"), 85, 1, 2000))
    add("LOOP_MULAI", nama="Ulangi caption per baris video",
        jumlah_loop=jumlah, ikut_video=True)
    add("KLIK", nama="I1 - Klik tombol 'Edit'", posisi=P("pos_edit"),
        geser=jarak)
    add("KLIK", nama="I2 - Klik kotak caption", posisi=P("pos_judul"),
        geser=jarak)
    add("VIDEO_CAPTION", nama="I2 - Isi caption video ini",
        isi="Caption dasar + nama video", ctrl_a=True)
    add("KLIK", nama="I3 - Klik 'Konfirmasi'",
        posisi=P("pos_konfirmasi") or P("pos_edit"), geser=jarak)
    add("LOOP_AKHIR", nama="Selesai ulangi caption")
    add("SCROLL", nama="Scroll ke bawah (menuju tombol Submit)",
        arah="Turun", jumlah_scroll=10)
    if cfg.get("auto_kirim", True):
        nsub = int(_angka(cfg.get("klik_submit"), 1, 1, 10))
        add("KLIK", nama="J - Klik 'SUBMIT'", posisi=P("pos_submit"),
            klik=nsub)
    return steps


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


def _baca_angka(nama, teks, bawaan=None, bulat=False):
    """v5.9: baca angka isian untuk validasi F6 (jelas per kolom).

    - Kosong  -> kembalikan `bawaan` (kolom opsional tidak menggagalkan
      alur lagi; dulu jadi penyebab "JUMLAH VIDEO dan WAKTU harus diisi
      angka" walau kolom lain sudah diisi).
    - Koma diterima sebagai desimal (mis. "1,5" -> 1.5; "2,0" -> 2).
    - Isi tapi bukan angka -> raise ValueError((nama, teks)) supaya
      pesan error MENUNJUK kolom yang salah, bukan menyalahkan semua.
    """
    teks = str(teks if teks is not None else "").strip()
    if not teks:
        return bawaan
    try:
        v = float(teks.replace(",", "."))
    except ValueError:
        raise ValueError((nama, teks))
    return int(v) if bulat else v


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


def cari_di_layar_area(gambar_path, area, kemiripan=0.8):
    """v5.3: cari gambar referensi di dalam AREA FOKUS persegi.

    area = [x1, y1, x2, y2] koordinat layar (boleh terbalik,
    dinormalkan di sini), atau None = cari di SELURUH LAYAR.
    Tidak butuh titik acuan X,Y lagi - gambar referensi bisa
    langsung diklik begitu ketemu.

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
        if float(tpl.std(axis=(0, 1)).max()) < 2.0:
            # warna rata membuat matchTemplate tidak valid (false 100%)
            return None, ("Gambar referensi polos (warna rata tanpa "
                          "tulisan/gambar) - potong ulang bagian yang "
                          "berisi tulisan atau tombol.")
        x1 = y1 = 0
        bbox = None
        if area:
            try:
                ax = [int(v) for v in area]
                x1, y1 = max(0, min(ax[0], ax[2])), max(0, min(ax[1],
                                                               ax[3]))
                x2, y2 = max(0, max(ax[0], ax[2])), max(0,
                                                        max(ax[1], ax[3]))
                bbox = (x1, y1, max(x1 + 1, x2), max(y1 + 1, y2))
            except (ValueError, TypeError, IndexError):
                bbox = None
        grab = ImageGrab.grab(bbox=bbox) if bbox else ImageGrab.grab()
        layar = np.array(grab)[:, :, ::-1].copy()   # RGB -> BGR
        if layar.shape[0] < th or layar.shape[1] < tw:
            return None, ("Area fokus lebih kecil dari gambar referensi - "
                          "perbesar AREA FOKUS.")
        terbaik = None
        # Multi-skala: zoom browser saat memotong gambar bisa berbeda
        # dengan zoom saat pencarian (penyebab error paling umum).
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
            kandidat = (x1 + lok[0] + ww // 2,
                        y1 + lok[1] + hh // 2, skor)
            if terbaik is None or skor > terbaik[2]:
                terbaik = kandidat
            if skor >= kemiripan:
                return kandidat, ""
        skor_b = terbaik[2] if terbaik else 0.0
        return None, ("Gambar tidak ditemukan (kemiripan terbaik "
                      "{:.0%}, ambang {:.0%}). Coba: potong ulang gambar "
                      "lewat POTONG GAMBAR, perbesar AREA FOKUS, atau "
                      "turunkan KEMIRIPAN ke 0.70.".format(
                          skor_b, kemiripan))
    except Exception as e:
        return None, "Error pencarian gambar: {}".format(e)


# ============================================================
# v5.6 - MESIN REKAM AKSI BERSAMA (mixin untuk 2 tab)
# Sebelumnya hanya ada di tab STUDIO MAKRO. Kini mesinnya jadi
# mixin yang dipakai tab STUDIO MAKRO dan tab ALUR CUTMOTIONS
# (A-J): merekam klik/ketikan/scroll lewat listener pynput,
# mengubah kejadian jadi langkah (perekam_bangun_langkah), lalu
# menyisipkan hasilnya ke alur masing-masing tab lewat hook
# perekam_sisipkan() yang diisi tiap tab.
# ============================================================
class PerekamAksiMixin:
    def perekam_init_state(self):
        """State perekam - dipanggil dari __init__ tiap tab."""
        self.merekam = False
        self._rekam_kejadian = []
        self._rekam_listener_mouse = None
        self._rekam_listener_kb = None
        self._rekam_banner = None
        self._rekam_mod = set()

    # ---- hook yang diisi tiap tab ----
    def perekam_uid_mulai(self):
        """Nomor uid awal untuk langkah hasil rekaman."""
        return 0

    def perekam_sisipkan(self, baru, uid_akhir):
        """Masukkan langkah hasil rekaman ke alur tab ini."""
        raise NotImplementedError

    # ================== MULAI / BERHENTI REKAM ==================
    def _rekam_mulai(self):
        """Klik tombol ● REKAM AKSI (atau menu > Rekam Aksi)."""
        if self.merekam:
            self._rekam_berhenti()
            return
        if self.running:
            messagebox.showwarning(
                APP_NAME,
                "Alur di tab ini sedang BERJALAN.\n\nTunggu sampai "
                "selesai atau tekan F7 dulu, baru merekam.")
            return
        if not PYNPUT_OK:
            messagebox.showerror(
                APP_NAME,
                "Library pynput belum terpasang.\n\n"
                "Buka CMD lalu jalankan:\n  pip install pynput")
            return
        lain = self.shell.tab_lain(self) if self.shell is not self \
            else None
        if lain is not None and lain.running:
            messagebox.showwarning(
                APP_NAME,
                "Alur di tab lain sedang berjalan.\n\nTunggu sampai "
                "selesai atau tekan F7 dulu.")
            return
        # v5.6: perekam hanya boleh jalan di SATU tab
        if lain is not None and getattr(lain, "merekam", False):
            messagebox.showwarning(
                APP_NAME,
                "Perekam sedang berjalan di tab lain.\n\nTekan F8 "
                "(atau ESC) dulu untuk menghentikan rekaman di "
                "sana.")
            return
        if not messagebox.askyesno(
                APP_NAME,
                "MULAI MEREKAM AKSI?\n\n"
                "Setelah jendela ini tersembunyi, SEMUA klik, ketikan, "
                "dan gulungan mouse kamu terekam otomatis menjadi "
                "langkah:\n"
                "  - Klik  -> langkah KLIK TITIK (klik dobel dikenali)\n"
                "  - Huruf / angka  -> langkah KETIK TEKS\n"
                "  - Enter / Tab / panah / Ctrl+A dll  -> langkah "
                "TEKAN TOMBOL\n"
                "  - Gulungan mouse  -> langkah SCROLL\n\n"
                "Tekan F8 (atau ESC) untuk BERHENTI merekam. Hasilnya "
                "DITAMBAH ke alur kerja di tab ini - tidak menimpa "
                "langkah lama.\n\n"
                "Catatan: selagi merekam, jangan menekan F8/ESC di "
                "aplikasi lain kecuali memang mau berhenti merekam.\n\n"
                "Lanjutkan?"):
            return
        self._set_status("Rekam mulai dalam 3 detik - siapkan aplikasi "
                         "yang aksinya mau direkam...", C_ORANGE)
        threading.Thread(target=self._rekam_hitung_mundur,
                         daemon=True).start()

    def _rekam_hitung_mundur(self):
        try:
            for s in range(3, 0, -1):
                self.root.after(0, lambda s=s: self._set_status(
                    "Rekam mulai dalam {} detik...".format(s), C_ORANGE))
                time.sleep(1)
            self.root.after(0, self._rekam_mulai_sekarang)
        except Exception:
            pass

    def _rekam_mulai_sekarang(self):
        if self.merekam or self.running or not PYNPUT_OK:
            return
        self._rekam_kejadian = []
        self._rekam_mod = set()
        try:
            self.root.winfo_toplevel().withdraw()
        except Exception:
            pass
        self.root.after(250, self._rekam_mulai_lanjut)

    def _rekam_mulai_lanjut(self):
        if self.merekam or self.running or not PYNPUT_OK:
            return
        try:
            self._rekam_banner = BannerRekam(self.wadah)
        except Exception:
            self._rekam_banner = None
        try:
            self.btn_rekam.config(text="■ STOP REKAM (F8)",
                                  command=self._rekam_berhenti,
                                  bg="#991B1B")
        except Exception:
            pass
        self.merekam = True
        try:
            self._rekam_listener_mouse = mouse_mod.Listener(
                on_click=self._rekam_on_klik,
                on_scroll=self._rekam_on_scroll)
            self._rekam_listener_mouse.daemon = True
            self._rekam_listener_mouse.start()
            self._rekam_listener_kb = kb_mod.Listener(
                on_press=self._rekam_on_tekan,
                on_release=self._rekam_on_lepas)
            self._rekam_listener_kb.daemon = True
            self._rekam_listener_kb.start()
        except Exception as e:
            self._rekam_bersihkan()
            messagebox.showerror(APP_NAME,
                                 "Gagal memulai perekaman:\n{}".format(e))
            return
        self._set_status("MEREKAM... semua klik / ketikan / scroll "
                         "terekam. Tekan F8 untuk berhenti.", C_RED)

    def _rekam_bersihkan(self):
        """Matikan listener + banner + pulihkan tombol & jendela."""
        self.merekam = False
        for ls in (self._rekam_listener_mouse, self._rekam_listener_kb):
            try:
                if ls is not None:
                    ls.stop()
            except Exception:
                pass
        self._rekam_listener_mouse = None
        self._rekam_listener_kb = None
        self._rekam_kejadian = []
        if self._rekam_banner is not None:
            try:
                self._rekam_banner.tutup()
            except Exception:
                pass
            self._rekam_banner = None
        try:
            self.btn_rekam.config(text="● REKAM AKSI",
                                  command=self._rekam_mulai,
                                  bg="#DC2626")
        except Exception:
            pass
        try:
            self.root.winfo_toplevel().deiconify()
        except Exception:
            pass

    def _rekam_catat(self, ev):
        """Catat satu kejadian (dipanggil dari thread listener).

        pynput di X11 kadang mengirim kejadian DOBEL untuk satu
        tekanan tombol (jarak < 5 ms, isi sama persis) - buang
        duplikatnya. Tekanan manusia tercepat >= 50 ms, jadi
        ambang 20 ms aman untuk huruf kembar (mis. 'll').
        """
        if ev.get("tipe") in ("tombol", "char") and self._rekam_kejadian:
            ahir = self._rekam_kejadian[-1]
            if (ahir.get("tipe") == ev.get("tipe")
                    and ahir.get("nama") == ev.get("nama")
                    and ahir.get("teks") == ev.get("teks")
                    and abs(ev.get("waktu", 0)
                            - ahir.get("waktu", 0)) < 0.02):
                return
        self._rekam_kejadian.append(ev)
        self.root.after(0, self._rekam_perbarui_banner)

    def _rekam_perbarui_banner(self):
        b = self._rekam_banner
        if b is None:
            return
        n_klik = sum(1 for e in self._rekam_kejadian
                     if e.get("tipe") == "klik")
        n_teks = sum(1 for e in self._rekam_kejadian
                     if e.get("tipe") in ("char", "tombol"))
        n_scroll = sum(1 for e in self._rekam_kejadian
                       if e.get("tipe") == "scroll")
        try:
            b.perbarui(n_klik, n_teks, n_scroll)
        except Exception:
            pass

    def _rekam_di_banner(self, x, y):
        """True bila klik/scroll terjadi di atas banner (abaikan)."""
        b = self._rekam_banner
        if b is None:
            return False
        try:
            bx, by = b.winfo_rootx(), b.winfo_rooty()
            bw = max(1, b.winfo_width())
            bh = max(1, b.winfo_height())
            return bx <= x <= bx + bw and by <= y <= by + bh
        except Exception:
            return False

    def _rekam_on_klik(self, x, y, tombol, pressed):
        if not pressed or self._rekam_di_banner(x, y):
            return
        if tombol == Button.left:
            nama = "kiri"
        elif tombol == Button.right:
            nama = "kanan"
        else:
            return          # klik tengah diabaikan
        self._rekam_catat({"tipe": "klik", "x": int(x), "y": int(y),
                           "tombol": nama, "waktu": time.time()})

    def _rekam_on_scroll(self, x, y, dx, dy):
        if not dy or self._rekam_di_banner(x, y):
            return
        self._rekam_catat({"tipe": "scroll",
                           "arah": "Naik" if dy > 0 else "Turun",
                           "waktu": time.time()})

    def _rekam_on_tekan(self, key):
        try:
            if key in (Key.f8, Key.esc):
                self.root.after(0, self._rekam_berhenti)
                return
        except Exception:
            pass
        if key in (Key.ctrl, Key.ctrl_l, Key.ctrl_r):
            self._rekam_mod.add("ctrl")
            return
        if key in (Key.shift, Key.shift_l, Key.shift_r):
            self._rekam_mod.add("shift")
            return
        if key in (Key.alt, Key.alt_l, Key.alt_r, Key.alt_gr):
            self._rekam_mod.add("alt")
            return
        ch = getattr(key, "char", None)
        if "ctrl" in self._rekam_mod:
            # kombinasi Ctrl+huruf yang dikenal aplikasi -> TOMBOL
            huruf = None
            if ch and len(ch) == 1:
                o = ord(ch.lower())
                if 97 <= o <= 122:
                    huruf = chr(o - 32)
                elif 1 <= o <= 26:
                    huruf = chr(o + 64)
            if huruf and ("Ctrl+" + huruf) in TOMBOL_KB_OPSI:
                self._rekam_catat({"tipe": "tombol",
                                   "nama": "Ctrl+" + huruf,
                                   "waktu": time.time()})
            return          # kombinasi Ctrl lain tidak terekam
        if ch and len(ch) == 1 and ch.isprintable() \
                and ch not in "\r\n\t\x00\x7f":
            self._rekam_catat({"tipe": "char", "teks": ch,
                               "waktu": time.time()})
            return
        nama = TOMBOL_REKAM_MAP.get(key)
        if nama is None:
            return
        if "shift" in self._rekam_mod and nama in TOMBOL_REKAM_SHIFT:
            nama = TOMBOL_REKAM_SHIFT[nama]
        self._rekam_catat({"tipe": "tombol", "nama": nama,
                           "waktu": time.time()})

    def _rekam_on_lepas(self, key):
        for nama_mod, kunci in (
                ("ctrl", (Key.ctrl, Key.ctrl_l, Key.ctrl_r)),
                ("shift", (Key.shift, Key.shift_l, Key.shift_r)),
                ("alt", (Key.alt, Key.alt_l, Key.alt_r, Key.alt_gr))):
            if key in kunci:
                self._rekam_mod.discard(nama_mod)

    def _rekam_berhenti(self):
        """Stop rekaman, ubah kejadian jadi langkah, tampilkan lagi."""
        if not self.merekam:
            return
        kejadian = list(self._rekam_kejadian)
        self._rekam_bersihkan()
        if not kejadian:
            self._set_status("Rekaman dihentikan - tidak ada aksi yang "
                             "terekam.", C_MUTED)
            return
        baru, uid_akhir = perekam_bangun_langkah(
            kejadian, self.perekam_uid_mulai())
        if not baru:
            self._set_status("Rekaman dihentikan - kejadian tidak bisa "
                             "dijadikan langkah.", C_MUTED)
            return
        self.perekam_sisipkan(baru, uid_akhir)


class CutMotionsTab(PerekamAksiMixin):
    """Tab ALUR CUTMOTIONS (A-J) - otomatis uploader batch CutMotions.

    Bila `shell` diberikan, tab ini ditanam di Notebook aplikasi v5.0
    (menubar/statusbar/hotkey milik ShellApp). Bila `shell` kosong,
    tab berjalan sendiri sebagai jendela utama (mode lama).
    """

    # ================== INISIALISASI ==================
    def __init__(self, root, shell=None):
        self.root = root
        self.wadah = root
        self.shell = shell if shell is not None else self
        if shell is None:
            # mode mandiri (jendela utama langsung)
            self.root.title("{} v{} - Alur CutMotions (A-J)".format(
                APP_NAME, APP_VERSION))
            self.root.geometry("1000x880")
            self.root.minsize(920, 760)
            if sys.platform == "win32":
                try:
                    self.root.iconbitmap(os.path.join(app_dir(),
                                                      "icon.ico"))
                except Exception:
                    pass

        self.root.configure(bg=C_BG)
        self.stop_event = threading.Event()
        self.running = False

        # ---- data makro (profil aktif) ----
        self.posisi = {k: None for k in POS_KUNCI}
        self.jeda_per = jeda_default_per()        # jeda sebelum langkah
        self.jeda_klik_per = jeda_klik_default_per()  # jeda antar klik
        # v4.2: config pencarian gambar opsional per langkah bawaan
        self.gambar_langkah = {k: gambar_langkah_default()
                               for k in POS_KUNCI}
        # v4.2: salinan langkah (hasil SALIN/TEMPEL)
        self.langkah_extra = []       # list of dict (lihat _tempel_langkah)
        self.papan_klip = None        # langkah yang sedang disalin
        self._extra_counter = 0
        # v5.9: slot bawaan A-J yang DIHAPUS user (bisa dikembalikan);
        # langkah mati = tak tampil di tabel & dilewati mesin saat F6
        self.slot_mati = set()
        self._potong_target = None    # tujuan POTONG GAMBAR aktif
        # v5.6: state REKAM AKSI (mesin bersama, lihat PerekamAksiMixin)
        self.perekam_init_state()
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
            if shell is None:
                self.kb = KeyboardController()
                self.mouse = MouseController()
                self._listener = kb_mod.Listener(on_press=self._on_key)
                self._listener.daemon = True
                self._listener.start()
            else:
                # satu set controller bersama dari ShellApp
                self.kb = self.shell.kb
                self.mouse = self.shell.mouse
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
        if shell is None:
            self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ================== PEMBANGUNAN TAMPILAN ==================
    def _build_ui(self):
        # ----- Baris menu (hanya saat mode mandiri; v5.0 menubar
        #      milik ShellApp supaya berlaku untuk kedua tab) -----
        if self.shell is not self:
            self.lbl_status = self.shell.lbl_status
        else:
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
            m_alat.add_command(label="Potong Gambar Referensi (seret "
                               "langsung di layar)",
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

            # ----- Statusbar paling bawah (dipack dulu supaya selalu
            #       tampak) - hanya mode mandiri; v5.0 pakai statusbar
            #       bersama dari ShellApp -----
            status = tk.Frame(self.root, bg=C_BG, bd=1, relief="sunken")
            status.pack(side="bottom", fill="x")
            self.lbl_status = tk.Label(status, anchor="w", bg=C_BG,
                                       fg=C_GREEN, font=F_S,
                                       text="Siap - login manual dulu "
                                       "di situs (Versi lama > Rilis "
                                       "karya), lalu tekan F6")
            self.lbl_status.pack(side="left", fill="x", expand=True,
                                 padx=6, pady=3)
            tk.Label(status, anchor="e", bg=C_BG, fg=C_MUTED, font=F_XS,
                     text="v{}  |  F6 = Mulai   F7/ESC = Berhenti".format(
                         APP_VERSION)).pack(side="right", padx=6)

        # ----- Strip WAKTU (kartu membulat, di atas statusbar) -----
        kartu_w = KartuBulat(self.root,
                             judul="WAKTU & UNGGAH (detik)",
                             padding=(10, 6, 10, 8))
        kartu_w.pack(side="bottom", fill="x", padx=8, pady=(0, 4))
        w = kartu_w.badan
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

        # ----- Toolbar v5.7 (kartu MEMBULAT + tombol kapsul
        #      mengkilat; tetap MAKS 7 TOMBOL per baris) -----
        tb = KartuBulat(self.root, radius=14, padding=(10, 7, 10, 8))
        tb.pack(side="top", fill="x", padx=6, pady=(6, 2))
        tb_r1 = tk.Frame(tb.badan, bg=C_BG)
        tb_r1.pack(side="top", fill="x")
        tb_r2 = tk.Frame(tb.badan, bg=C_BG)
        tb_r2.pack(side="top", fill="x")
        self.btn_start = self._tb_btn(tb_r1, "JALANKAN  (F6)", self._start,
                                      bg=C_BLUE, fg="white",
                                      aktif=C_BLUE_D)
        self.btn_stop = self._tb_btn(tb_r1, "BERHENTI  (F7)", self._stop,
                                     bg=C_RED, fg="white",
                                     aktif=C_RED_D)
        self.btn_stop.config(state="disabled", disabledforeground="#FECACA")
        # v5.6: REKAM AKSI kini juga ada di tab ALUR CUTMOTIONS
        self.btn_rekam = self._tb_btn(tb_r1, "● REKAM AKSI",
                                      self._rekam_mulai,
                                      bg="#DC2626", fg="white",
                                      aktif="#EF4444")
        self._tb_pemisah(tb_r1)
        # v5.5: SEMUA menu STUDIO MAKRO bisa dimasukkan ke alur A-J
        m_tambah = tk.Menu(self.root, tearoff=0)
        menu_gelap(m_tambah)
        self._isi_menu_tambah(m_tambah)
        self.mb_tambah = TombolMenu(tb_r1, "+ TAMBAH LANGKAH \u25be",
                                    menu=m_tambah, bg=C_GREEN_D,
                                    fg="white")
        self.mb_tambah.pack(side="left", padx=(2, 2), pady=2)
        self._tb_pemisah(tb_r1)
        self._tb_btn(tb_r1, "TES CARI GAMBAR", self._tes_cari)
        self._tb_btn(tb_r1, "POTONG GAMBAR REFERENSI", self._potong_gambar)
        self._tb_btn(tb_r1, "SALIN LANGKAH", self._salin_langkah)
        self._tb_btn(tb_r2, "TEMPEL LANGKAH", self._tempel_langkah)
        self._tb_btn(tb_r2, "HAPUS SALINAN", self._hapus_langkah)
        self._tb_pemisah(tb_r2)
        self._tb_btn(tb_r2, "SIMPAN PROFIL", self._simpan_profil)
        self._tb_btn(tb_r2, "BUKA PROFIL", self._buka_profil)

        # ----- Strip VIDEO & CAPTION (kartu membulat) -----
        kartu_v = KartuBulat(self.root, judul="VIDEO & CAPTION",
                             padding=(10, 6, 10, 8))
        kartu_v.pack(side="top", fill="x", padx=8, pady=(6, 4))
        v = kartu_v.badan
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

        # ---- tabel langkah makro (v5.7: kartu membulat + MULTI-
        #      PILIH: Ctrl+Klik / Shift+Klik / Ctrl+A) ----
        f_tb = KartuBulat(
            paned,
            judul="LANGKAH MAKRO - klik pilih 1; tahan CTRL/SHIFT "
                  "pilih banyak; Ctrl+C salin; Del hapus",
            padding=(8, 5, 8, 6))
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
                       background=C_PANEL2, foreground=C_TEXT,
                       relief="flat")
        gaya.map("Makro.Treeview",
                 background=[("selected", C_BLUE)],
                 foreground=[("selected", "white")])
        kolom = ("no", "nama", "detail", "jeda", "ulang")
        self.tree = ttk.Treeview(f_tb.badan, columns=kolom,
                                 show="headings",
                                 style="Makro.Treeview",
                                 selectmode="extended")
        for k, t, w_, a in [
            ("no", "#", 44, "center"),
            ("nama", "LANGKAH", 205, "w"),
            ("detail", "DETAIL / KOORDINAT", 330, "w"),
            ("jeda", "JEDA", 62, "center"),
            ("ulang", "ULANGI", 170, "w"),
        ]:
            self.tree.heading(k, text=t)
            self.tree.column(k, width=w_, anchor=a, stretch=(k == "detail"))
        vsb = ttk.Scrollbar(f_tb.badan, orient="vertical",
                            command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="left", fill="y")
        self.tree.tag_configure("genap", background=C_STRIPE)
        self.tree.tag_configure("ganjil", background=C_PANEL)
        self.tree.tag_configure("salinan", foreground=C_BLUE)
        self.tree.tag_configure("studio", foreground=C_UNGU)
        self.tree.bind("<<TreeviewSelect>>", self._on_pilih_baris)
        self.tree.bind("<Control-c>", lambda _e: self._salin_langkah())
        self.tree.bind("<Control-v>", lambda _e: self._tempel_langkah())
        self.tree.bind("<Delete>", lambda _e: self._hapus_langkah())
        self.tree.bind("<Control-a>", self._pilih_semua)
        self.tree.bind("<Button-3>", self._menu_klik_kanan)

        # ---- panel properti (kartu membulat) ----
        self.f_prop = KartuBulat(paned, judul="PROPERTI LANGKAH",
                                 padding=(8, 5, 8, 6))
        paned.add(self.f_prop, minsize=230, height=280, stretch="always")
        self.prop_body = tk.Frame(self.f_prop.badan, bg=C_BG)
        self.prop_body.pack(fill="both", expand=True)

    # ---------- pembantu tampilan ----------
    def _tb_btn(self, parent, teks, cmd, bg=None, fg=None, aktif=None):
        # v5.7: tombol kapsul membulat menggantikan tk.Button datar
        b = TombolKapsul(parent, teks=teks, perintah=cmd,
                         bg=bg or C_PANEL2, fg=fg or C_TEXT)
        b.pack(side="left", padx=3, pady=2)
        return b

    def _pilih_semua(self, _ev=None):
        """v5.7: Ctrl+A - pilih semua baris di tabel."""
        semua = self.tree.get_children()
        if semua:
            self.tree.selection_set(semua)
        return "break"

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
            cfg = self.gambar_langkah.get(kunci) or {}
            if cfg.get("aktif"):
                g = os.path.basename(cfg.get("path")) \
                    if cfg.get("path") else "(gambar belum dipilih)"
                aksi_t = ("pindah saja"
                          if cfg.get("aksi") == "Pindah saja"
                          else "klik gambar")
                return "{} | gambar: {} | {} | radius {} px | mirip {}".format(
                    pos_t, g, aksi_t,
                    cfg.get("radius") or V["radius"].get(),
                    cfg.get("mirip") or V["kemiripan"].get())
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
            cfg = self.gambar_langkah.get(kunci) or {}
            return "cari gambar" if cfg.get("aktif") else "1 klik"
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

    # ---------- v4.2: salinan langkah (copy-paste) ----------
    def _iid_ekstra(self, uid):
        """Ambil dict salinan berdasar uid (atau None)."""
        if not uid:
            return None
        for e in self.langkah_extra:
            if e.get("uid") == uid:
                return e
        return None

    def _uid_ekstra_baru(self):
        """v5.8: uid unik 'x{n}' anti-bentrok untuk langkah tambahan.

        Dulu nomor lanjut dari _extra_counter yang saat memuat profil
        diisi JUMLAH langkah. Setelah menghapus langkah (apalagi hapus
        massal v5.7) lalu aplikasi dibuka ulang, nomor bisa MENABRAK
        uid lama - langkah baru (mis. CARI GAMBAR ke-3) tidak muncul
        di tabel seakan-akan 'hanya bisa ditambah 2x'. Kini nomor yang
        sudah dipakai selalu dilewati, jadi CARI GAMBAR bisa
        ditambahkan BERAPAPUN kalinya.
        """
        while True:
            self._extra_counter += 1
            uid = "x{}".format(self._extra_counter)
            if not self._iid_ekstra(uid):
                return uid

    def _params_dari_global(self, sumber):
        """Nilai awal parameter salinan diambil dari setelan global."""
        V = self.vars
        if sumber == "pos_tanggal":
            return {"teks": V["tanggal"].get()}
        if sumber == "pos_bebas1":
            return {"klik": V["klik_bebas1"].get(),
                    "scroll": V["scroll_bebas1"].get()}
        if sumber == "pos_bebas2":
            return {"klik": V["klik_bebas2"].get()}
        if sumber == "pos_submit":
            return {"klik": V["klik_submit"].get()}
        return {}

    def _urutan_lengkap(self):
        """Semua iid baris tabel (bawaan A-J + salinan) urut tampil."""
        anak = {}
        for e in self.langkah_extra:
            anak.setdefault(e.get("setelah"), []).append(e["uid"])
        hasil = []

        def emit(anchor):
            for uid in anak.get(anchor, ()):  # kedalaman dulu
                if uid not in hasil:        # anti siklus
                    hasil.append(uid)
                    emit(uid)

        for k in POS_KUNCI:
            # v5.9: slot yang DIHAPUS (slot_mati) tak tampil, tetapi
            # langkah tambahan yang menempel padanya tetap tampil &
            # tetap dijalankan di posisinya
            if k not in self.slot_mati:
                hasil.append(k)
            emit(k)
        # salinan yang tak tersambung ke urutan (file profil rusak)
        # tetap ditampilkan supaya tidak hilang
        for e in self.langkah_extra:
            if e["uid"] not in hasil:
                hasil.append(e["uid"])
        return hasil

    def _detail_ekstra(self, e):
        # v5.5: langkah gaya Studio tampil dengan format Studio
        if str(e.get("jenis") or "") in JENIS_STUDIO:
            return "S | " + studio_detail_teks(e)
        pos = e.get("posisi")
        pos_t = "({},{})".format(pos[0], pos[1]) if pos else "belum diatur"
        teks = "SALINAN | " + pos_t
        g = e.get("gambar") or {}
        if g.get("aktif"):
            teks += " | gambar: {}".format(
                os.path.basename(g.get("path") or "(kosong)"))
            if g.get("aksi") == "Pindah saja":
                teks += " (pindah saja)"
        p = e.get("params") or {}
        sumber = e.get("sumber")
        if sumber == "pos_tanggal":
            teks += " | ketik: {}".format(p.get("teks")
                                          or self.vars["tanggal"].get())
        elif sumber == "pos_bebas1":
            teks += " | {} klik + {} scroll {}".format(
                p.get("klik", "1"), p.get("scroll", "0"),
                self.vars["arah_scroll"].get())
        elif sumber in ("pos_bebas2", "pos_submit"):
            teks += " | {} klik".format(p.get("klik", "1"))
        elif sumber == "pos_video":
            teks += " | Shift+turun otomatis"
        return teks

    def _ulang_ekstra(self, e):
        if str(e.get("jenis") or "") in JENIS_STUDIO:
            return studio_ulang_teks(e)
        g = e.get("gambar") or {}
        sumber = e.get("sumber")
        if sumber == "pos_tanggal":
            return "klik + ketik"
        if sumber == "pos_bebas1":
            p = e.get("params") or {}
            return "{} klik + {}x scroll".format(p.get("klik", "1"),
                                                 p.get("scroll", "0"))
        if sumber == "pos_video":
            return "Shift+turun (batch)"
        if sumber in ("pos_bebas2", "pos_submit"):
            return "{} klik".format((e.get("params") or {}).get("klik",
                                                                 "1"))
        return "cari gambar" if g.get("aktif") else "1 klik"

    def _refresh_tabel(self):
        if not hasattr(self, "tree"):
            return
        anak = self.tree.get_children()
        if anak:
            self.tree.delete(*anak)
        for i, iid in enumerate(self._urutan_lengkap()):
            if iid in POS_KUNCI:
                kode = SLOT_KODE.get(iid, iid)
                label = LABEL_POSISI[iid]
                detail = self._detail_slot(iid)
                ulang = self._ulang_slot(iid)
                jeda_t = "{:.1f}s".format(self.jeda_per.get(iid, 1.0))
                tag = "genap" if i % 2 == 0 else "ganjil"
            else:
                e = self._iid_ekstra(iid)
                if not e:
                    continue
                if str(e.get("jenis") or "") in JENIS_STUDIO:
                    kode = "S"      # v5.5: langkah gaya Studio
                    tag = "studio"
                else:
                    kode = "+"
                    tag = "salinan"
                label = str(e.get("label") or iid)
                detail = self._detail_ekstra(e)
                ulang = self._ulang_ekstra(e)
                jeda_t = "{:.1f}s".format(float(e.get("jeda", 1.0)))
            self.tree.insert("", "end", iid=iid, tags=(tag,), values=(
                kode, label, detail, jeda_t, ulang))
        if self.sel and self.tree.exists(self.sel):
            try:
                # hindari selection_set bila seleksi sudah tepat -
                # event <<TreeviewSelect>> akan memicu render ulang
                # panel properti DI TENGAH user mengetik (bug UX)
                if tuple(self.tree.selection()) != (self.sel,):
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
        # v5.7: BANYAK baris terpilih -> panel aksi massal
        pilihan = self.tree.selection()
        if len(pilihan) > 1:
            render_properti_multi(
                self, pilihan,
                "\n  -  (langkah bawaan A-J tidak bisa dihapus)\n")
            return
        iid = self.sel
        ek = None
        if iid not in POS_KUNCI:
            ek = self._iid_ekstra(iid) if iid else None
            if not ek:
                self._loading_prop = False
                return
        V = self.vars
        if ek and str(ek.get("jenis") or "") in JENIS_STUDIO:
            self._render_prop_studio(ek, iid)
            return
        if ek:
            kunci = ek.get("sumber")
            label = ek.get("label") or iid
            ket = ("SALINAN LANGKAH (titik klik tambahan) - "
                   + JUDUL_POSISI.get(kunci, kunci))
            pos = ek.get("posisi")
            jeda_v = float(ek.get("jeda", 1.0))
            jk_v = float(ek.get("jeda_klik", 0.3))
            cfg_g = ek.get("gambar") or gambar_langkah_default()
        else:
            kunci = iid
            label = LABEL_POSISI[kunci]
            ket = JUDUL_POSISI[kunci]
            pos = self.posisi.get(kunci)
            jeda_v = self.jeda_per.get(kunci, 1.0)
            jk_v = self.jeda_klik_per.get(kunci, 0.3)
            cfg_g = self.gambar_langkah.get(kunci) or gambar_langkah_default()

        kepala = tk.Frame(self.prop_body, bg=C_BG)
        kepala.pack(fill="x", pady=(0, 4))
        tk.Label(kepala, text="{}   -   {}".format(label, ket), bg=C_BG,
                 fg=C_TEXT, font=F_H, anchor="w",
                 wraplength=860, justify="left").pack(fill="x")

        # ---- posisi X / Y + AMBIL + LIHAT ----
        self.pv = {
            "x": tk.StringVar(value=str(pos[0]) if pos else ""),
            "y": tk.StringVar(value=str(pos[1]) if pos else ""),
            "jeda": tk.StringVar(value="{:.1f}".format(jeda_v)),
            "jeda_klik": tk.StringVar(value="{:.2f}".format(jk_v)),
        }
        r = self._baris_prop("POSISI X , Y")
        self._ent_prop(r, self.pv["x"], 6)
        tk.Label(r, text=",", bg=C_BG, fg=C_MUTED,
                 font=F_N).pack(side="left", padx=2)
        self._ent_prop(r, self.pv["y"], 6)
        self._btn_prop(r, "AMBIL (5 dtk)",
                       lambda k=iid: self._ambil_posisi(k))
        self._btn_prop(r, "LIHAT",
                       lambda k=iid: self._lihat_posisi(k), bg=C_BG)
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

        # ---- kontrol khusus ----
        if ek:
            # salinan: parameter milik sendiri (bukan variabel global)
            for nama_p, label_p, lebar in PARAM_DEF.get(kunci, []):
                r = self._baris_prop(label_p)
                var_p = tk.StringVar(value=str(
                    (ek.get("params") or {}).get(nama_p, "")))
                self.pv["p_" + nama_p] = var_p
                self._ent_prop(r, var_p, lebar)
                if kunci == "pos_tanggal" and nama_p == "teks":
                    tk.Label(r, text="format: 2026-09-10 02:05:01 "
                                     "(detik boleh dilewat)",
                             bg=C_BG, fg=C_MUTED,
                             font=F_XS).pack(side="left", padx=6)
                if kunci == "pos_bebas1" and nama_p == "scroll":
                    tk.Label(r, text="arah scroll mengikuti setelan "
                                     "langkah G",
                             bg=C_BG, fg=C_MUTED,
                             font=F_XS).pack(side="left", padx=6)
            if kunci in ("pos_edit", "pos_judul", "pos_konfirmasi"):
                tk.Label(self.prop_body,
                         text="Salinan langkah caption mengikuti baris "
                              "video: gesernya otomatis pakai JARAK ANTAR "
                              "BARIS milik langkah I3.",
                         bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                         wraplength=860, justify="left").pack(
                             fill="x", pady=(4, 0))
            if kunci == "pos_submit":
                tk.Label(self.prop_body,
                         text="Salinan SUBMIT dijalankan setelah klik "
                              "SUBMIT utama (J).",
                         bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
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

        # ---- v4.2: PENCARIAN GAMBAR untuk SEMUA langkah ----
        pemisah = tk.Frame(self.prop_body, bg=C_LINE, height=1)
        pemisah.pack(fill="x", pady=(6, 2))
        tk.Label(self.prop_body,
                 text="PENCARIAN GAMBAR (opsional) - gambar ketemu bisa "
                      "DIKLIK langsung, atau mouse hanya DIPINDAH ke sana",
                 bg=C_BG, fg=C_BLUE, font=F_XS, anchor="w",
                 wraplength=860, justify="left").pack(fill="x")
        self.pv["g_aktif"] = tk.BooleanVar(value=bool(cfg_g.get("aktif")))
        self.pv["g_path"] = tk.StringVar(value=str(cfg_g.get("path") or ""))
        self.pv["g_aksi"] = tk.StringVar(value=cfg_g.get("aksi")
                                         if cfg_g.get("aksi")
                                         in GAMBAR_AKSI_OPSI
                                         else "Klik di gambar")
        self.pv["g_gagal"] = tk.StringVar(value=cfg_g.get("gagal")
                                          if cfg_g.get("gagal")
                                          in GAMBAR_GAGAL_OPSI
                                          else "Klik titik X,Y")
        self.pv["g_radius"] = tk.StringVar(
            value=str(cfg_g.get("radius") or ""))
        self.pv["g_mirip"] = tk.StringVar(
            value=str(cfg_g.get("mirip") or ""))
        tk.Checkbutton(self.prop_body,
                       text="Aktifkan CARI GAMBAR pada langkah ini "
                            "(cari potongan layar dalam radius titik "
                            "X,Y di atas)",
                       variable=self.pv["g_aktif"], bg=C_BG, fg=C_TEXT,
                       font=F_XS, anchor="w").pack(fill="x", pady=(2, 0))
        r = self._baris_prop("GAMBAR REFERENSI")
        self._ent_prop(r, self.pv["g_path"], 42, tengah=False)
        self._btn_prop(r, "PILIH GAMBAR...",
                       lambda k=iid: self._pilih_gambar_ref(k))
        self._btn_prop(r, "POTONG GAMBAR...",
                       lambda k=iid: self._potong_gambar(("langkah", k)))
        # v5.1: pratinjau gambar referensi langkah ini
        self.pv["g_thumb"] = tk.Label(self.prop_body, bg=C_PANEL,
                                      relief="solid", bd=1, anchor="w")
        self.pv["g_thumb"].pack(anchor="w", padx=18, pady=(3, 2))
        _thumb = muat_thumbnail(str((cfg_g or {}).get("path") or ""))
        if _thumb is not None:
            self.pv["g_thumb"].configure(image=_thumb)
            self.pv["g_thumb"].image = _thumb
        else:
            self.pv["g_thumb"].configure(
                text="  Belum ada gambar referensi - klik POTONG GAMBAR, "
                     "lalu SERET kotak langsung di layar  ",
                fg=C_MUTED, font=F_XS)
        r = self._baris_prop("SAAT KETEMU:")
        tk.OptionMenu(r, self.pv["g_aksi"],
                      *GAMBAR_AKSI_OPSI).pack(side="left")
        tk.Label(r, text="SAAT TIDAK KETEMU:", bg=C_BG, fg=C_MUTED,
                 font=F_XS).pack(side="left", padx=(12, 4))
        tk.OptionMenu(r, self.pv["g_gagal"],
                      *GAMBAR_GAGAL_OPSI).pack(side="left")
        r = self._baris_prop("RADIUS (px) | KEMIRIPAN:")
        self._ent_prop(r, self.pv["g_radius"], 6)
        self._ent_prop(r, self.pv["g_mirip"], 6)
        tk.Label(r, text="kosongkan = pakai nilai global", bg=C_BG,
                 fg=C_MUTED, font=F_XS).pack(side="left", padx=6)
        self._btn_prop(r, "TES CARI LANGKAH INI", self._tes_cari)
        tk.Label(self.prop_body,
                 text="v5.1: POTONG GAMBAR = layar dibekukan sejenak, lalu "
                      "SERET kotak LANGSUNG di area yang diinginkan "
                      "(hanya area itu yang disimpan; ESC = batal). "
                      "Setiap potongan jadi file BARU di folder "
                      "data\\referensi, jadi bisa dipakai berkali-kali "
                      "dengan referensi berbeda-beda. Zoom browser jangan "
                      "diubah setelah gambar dipotong. Mode 'Pindah saja' "
                      "tidak mengklik - cocok untuk hover atau hanya "
                      "kalibrasi posisi.",
                 bg=C_BG, fg=C_ORANGE, font=F_XS, anchor="w",
                 wraplength=860, justify="left").pack(
                     fill="x", pady=(4, 0))

        self.lbl_ambil = tk.Label(self.prop_body, text="", bg=C_BG,
                                  fg=C_ORANGE, font=F_XS, anchor="w",
                                  wraplength=860, justify="left")
        self.lbl_ambil.pack(fill="x", pady=(4, 0))

        # ---- sambungkan perubahan -> simpan ----
        # (v5.1: lewati widget non-variable seperti pv["g_thumb"])
        for var in self.pv.values():
            if isinstance(var, tk.Variable):
                var.trace_add("write", self._terapkan_prop)
        self._loading_prop = False

    def _render_prop_studio(self, ek, iid):
        """v5.5: panel PROPERTI untuk langkah gaya Studio di alur A-J."""
        l = ek
        jenis = l["jenis"]
        judul = str(l.get("label") or "") or LABEL_JENIS[jenis]
        self.pv = {
            "label": tk.StringVar(value=judul),
            "jeda": tk.StringVar(value="{:.1f}".format(
                _angka(l.get("jeda"), 0.5, 0, 86400))),
        }
        kepala = tk.Frame(self.prop_body, bg=C_BG)
        kepala.pack(fill="x", pady=(0, 4))
        tk.Label(kepala, text="{}   -   LANGKAH STUDIO: {}".format(
                     judul, LABEL_JENIS[jenis]),
                 bg=C_BG, fg=C_TEXT, font=F_H, anchor="w",
                 wraplength=860, justify="left").pack(fill="x")

        r = self._baris_prop("NAMA LANGKAH")
        self._ent_prop(r, self.pv["label"], 30, tengah=False)
        r = self._baris_prop("JEDA SEBELUM LANGKAH (detik)")
        self._ent_prop(r, self.pv["jeda"], 6)

        pos = l.get("posisi")
        if jenis in ("KLIK", "TANGGAL_JAM", "VIDEO_CAPTION"):
            self.pv["x"] = tk.StringVar(value=str(pos[0]) if pos else "")
            self.pv["y"] = tk.StringVar(value=str(pos[1]) if pos else "")
            r = self._baris_prop("POSISI KLIK DULU (opsional) X , Y")
            self._ent_prop(r, self.pv["x"], 6)
            tk.Label(r, text=",", bg=C_BG, fg=C_MUTED,
                     font=F_N).pack(side="left", padx=2)
            self._ent_prop(r, self.pv["y"], 6)
            self._btn_prop(r, "AMBIL (5 dtk)",
                           lambda k=iid: self._ambil_posisi(k))
            self._btn_prop(r, "LIHAT",
                           lambda k=iid: self._lihat_posisi(k), bg=C_BG)
            tk.Label(r, text="dikosongkan = langsung aksi tanpa klik",
                     bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=6)

        if jenis == "KLIK":
            self.pv["tombol_mouse"] = tk.StringVar(
                value=l.get("tombol_mouse")
                if l.get("tombol_mouse") in MOUSE_OPSI else "Klik kiri")
            self.pv["klik"] = tk.StringVar(value=str(
                int(_angka(l.get("klik"), 1, 0, 500))))
            self.pv["jeda_klik"] = tk.StringVar(value="{:.2f}".format(
                _angka(l.get("jeda_klik"), 0.3, 0.05, 60)))
            self.pv["geser"] = tk.StringVar(value=str(
                int(_angka(l.get("geser"), 0, 0, 100000))))
            r = self._baris_prop("JENIS KLIK")
            tk.OptionMenu(r, self.pv["tombol_mouse"],
                          *MOUSE_OPSI).pack(side="left")
            tk.Label(r, text="JUMLAH KLIK:", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=(12, 4))
            self._ent_prop(r, self.pv["klik"], 6)
            tk.Label(r, text="JEDA ANTAR KLIK (detik):", bg=C_BG,
                     fg=C_MUTED, font=F_XS).pack(side="left",
                                                 padx=(12, 4))
            self._ent_prop(r, self.pv["jeda_klik"], 6)
            r = self._baris_prop("GESER PER PUTARAN ULANGI (px)")
            self._ent_prop(r, self.pv["geser"], 7)
            tk.Label(r, text="Untuk klik per baris video dalam blok "
                             "ULANGI / fase caption: klik turun sejauh "
                             "nilai ini x nomor putaran.",
                     bg=C_BG, fg=C_MUTED, font=F_XS, wraplength=520,
                     justify="left").pack(side="left", padx=6)
        elif jenis == "JEDA":
            self.pv["detik"] = tk.StringVar(value="{:.1f}".format(
                _angka(l.get("detik"), 1.0, 0, 86400)))
            r = self._baris_prop("TUNGGU BERAPA DETIK")
            self._ent_prop(r, self.pv["detik"], 8)
            tk.Label(r, text="mis. 2.5 (boleh koma atau titik)",
                     bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=6)
        elif jenis == "GAMBAR":
            g = l.get("gambar") or \
                studio_langkah_baru("GAMBAR", 0)["gambar"]
            self.pv["g_path"] = tk.StringVar(
                value=str(g.get("path") or ""))
            self.pv["g_aksi"] = tk.StringVar(
                value=g.get("aksi") if g.get("aksi") in GAMBAR_AKSI_OPSI
                else "Klik di gambar")
            self.pv["g_gagal"] = tk.StringVar(
                value=g.get("gagal") if g.get("gagal")
                in GAMBAR_GAGAL_OPSI_STUDIO else "Lewati langkah")
            self.pv["g_mirip"] = tk.StringVar(
                value=str(g.get("mirip") or "0.80"))
            f = g.get("fokus")
            if isinstance(f, (list, tuple)) and len(f) == 4:
                fokus_teks = "({},{}) - ({},{})".format(
                    f[0], f[1], f[2], f[3])
            else:
                fokus_teks = "Seluruh layar (tidak dibatasi)"
            self.pv["g_fokus"] = tk.StringVar(value=fokus_teks)
            tk.Label(self.prop_body,
                     text="TANPA perlu mengisi X,Y: gambar referensi "
                          "dicari lalu LANGSUNG DIKLIK (atau hanya "
                          "dipindah). AREA FOKUS opsional membatasi "
                          "daerah pencarian.",
                     bg=C_BG, fg=C_BLUE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            r = self._baris_prop("GAMBAR REFERENSI")
            self._ent_prop(r, self.pv["g_path"], 42, tengah=False)
            self._btn_prop(r, "PILIH GAMBAR...",
                           lambda k=iid: self._pilih_gambar_ref(k))
            self._btn_prop(r, "POTONG GAMBAR...",
                           lambda k=iid: self._potong_gambar(
                               ("langkah", k)))
            self.pv["g_thumb"] = tk.Label(self.prop_body, bg=C_PANEL,
                                          relief="solid", bd=1, anchor="w")
            self.pv["g_thumb"].pack(anchor="w", padx=18, pady=(3, 2))
            _thumb = muat_thumbnail(str(g.get("path") or ""))
            if _thumb is not None:
                self.pv["g_thumb"].configure(image=_thumb)
                self.pv["g_thumb"].image = _thumb
            else:
                self.pv["g_thumb"].configure(
                    text="  Belum ada gambar - klik POTONG GAMBAR, lalu "
                         "SERET kotak langsung di layar  ",
                    fg=C_MUTED, font=F_XS)
            r = self._baris_prop("AREA FOKUS (opsional)")
            self._ent_prop(r, self.pv["g_fokus"], 26, tengah=False)
            self._btn_prop(r, "PILIH AREA FOKUS...",
                           lambda k=iid: self._pilih_area_fokus(k))
            self._btn_prop(r, "KOSONGKAN",
                           lambda k=iid: self._fokus_kosongkan(k),
                           bg=C_BG)
            tk.Label(r, text="diisi dengan MENYERET kotak di layar",
                     bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=6)
            r = self._baris_prop("SAAT KETEMU:")
            tk.OptionMenu(r, self.pv["g_aksi"],
                          *GAMBAR_AKSI_OPSI).pack(side="left")
            tk.Label(r, text="SAAT TIDAK KETEMU:", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=(12, 4))
            tk.OptionMenu(r, self.pv["g_gagal"],
                          *GAMBAR_GAGAL_OPSI_STUDIO).pack(side="left")
            r = self._baris_prop("KEMIRIPAN:")
            self._ent_prop(r, self.pv["g_mirip"], 6)
            self._btn_prop(r, "TES CARI LANGKAH INI", self._tes_cari)
        elif jenis == "KETIK":
            self.pv["teks"] = tk.StringVar(value=str(l.get("teks") or ""))
            self.pv["ctrl_a"] = tk.BooleanVar(
                value=bool(l.get("ctrl_a")))
            self.pv["enter"] = tk.BooleanVar(value=bool(l.get("enter")))
            r = self._baris_prop("TEKS YANG DIKETIK")
            self._ent_prop(r, self.pv["teks"], 46, tengah=False)
            tk.Label(self.prop_body,
                     text="Placeholder: {caption} = caption dasar + nama "
                          "video baris ini  |  {video} = nama video  |  "
                          "{no} = nomor putaran ULANGI / baris  |  "
                          "{jumlah} = jumlah video. Di fase caption alur "
                          "A-J, teks otomatis mengikuti baris video yang "
                          "sedang diproses.",
                     bg=C_BG, fg=C_BLUE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Ctrl+A dulu (timpa isi kotak yang lama)",
                           variable=self.pv["ctrl_a"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Tekan Enter setelah selesai mengetik",
                           variable=self.pv["enter"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
        elif jenis == "TANGGAL_JAM":
            self.pv["sumber"] = tk.StringVar(
                value=l.get("sumber")
                if l.get("sumber") in SUMBER_TANGGAL_OPSI
                else "Tab CutMotions")
            self.pv["teks"] = tk.StringVar(value=str(l.get("teks") or ""))
            self.pv["ctrl_a"] = tk.BooleanVar(
                value=bool(l.get("ctrl_a", True)))
            self.pv["enter"] = tk.BooleanVar(value=bool(l.get("enter")))
            r = self._baris_prop("AMBIL NILAI TANGGAL-JAM DARI:")
            tk.OptionMenu(r, self.pv["sumber"],
                          *SUMBER_TANGGAL_OPSI).pack(side="left")
            tk.Label(self.prop_body,
                     text="'Tab CutMotions' = pakai kolom TANGGAL & JAM "
                          "RILIS di atas (ubah sekali, semua ikut).  "
                          "'Tetap' = pakai nilai di bawah ini.",
                     bg=C_BG, fg=C_BLUE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            r = self._baris_prop("TANGGAL & JAM RILIS")
            self._ent_prop(r, self.pv["teks"], 22, tengah=False)
            tk.Label(r, text="format 2026-09-10 02:05:01",
                     bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=6)
            tk.Checkbutton(self.prop_body,
                           text="Ctrl+A dulu (timpa isi kolom yang lama)",
                           variable=self.pv["ctrl_a"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Tekan Enter setelah selesai mengetik",
                           variable=self.pv["enter"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
        elif jenis == "VIDEO_CAPTION":
            self.pv["isi"] = tk.StringVar(
                value=l.get("isi") if l.get("isi") in ISI_VIDEO_OPSI
                else "Caption dasar + nama video")
            self.pv["teks"] = tk.StringVar(value=str(l.get("teks") or ""))
            self.pv["ctrl_a"] = tk.BooleanVar(
                value=bool(l.get("ctrl_a", True)))
            self.pv["enter"] = tk.BooleanVar(value=bool(l.get("enter")))
            r = self._baris_prop("YANG DIKETIK OTOMATIS:")
            tk.OptionMenu(r, self.pv["isi"],
                          *ISI_VIDEO_OPSI).pack(side="left")
            tk.Label(self.prop_body,
                     text="Jumlah video = angka di kolom JUMLAH VIDEO.  "
                          "Caption dasar + nama video = mis. '#dangdut - "
                          "melati' (nama video baris yang sedang "
                          "diproses di fase caption).  Nama video saja = "
                          "mis. 'melati'.",
                     bg=C_BG, fg=C_BLUE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            r = self._baris_prop("TEKS SENDIRI + PLACEHOLDER")
            self._ent_prop(r, self.pv["teks"], 46, tengah=False)
            tk.Label(self.prop_body,
                     text="Dipakai kalau pilihan di atas = 'Teks "
                          "sendiri'. Placeholder: {caption} | {video} | "
                          "{no} | {jumlah}.",
                     bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Ctrl+A dulu (timpa isi kolom yang lama)",
                           variable=self.pv["ctrl_a"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Tekan Enter setelah selesai mengetik",
                           variable=self.pv["enter"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
        elif jenis == "TOMBOL":
            self.pv["tombol_kb"] = tk.StringVar(
                value=str(l.get("tombol_kb") or "Enter"))
            self.pv["jumlah_kb"] = tk.StringVar(value=str(
                int(_angka(l.get("jumlah_kb"), 1, 1, 500))))
            self.pv["jeda_klik"] = tk.StringVar(value="{:.2f}".format(
                _angka(l.get("jeda_klik"), 0.3, 0.05, 60)))
            r = self._baris_prop("TOMBOL YANG DITEKAN")
            ttk.Combobox(r, textvariable=self.pv["tombol_kb"],
                         values=list(TOMBOL_KB_OPSI), width=20,
                         font=F_N).pack(side="left", ipady=2)
            tk.Label(r, text="  (bisa ketik 1 huruf sendiri, mis. a)",
                     bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=4)
            r = self._baris_prop("JUMLAH TEKAN")
            self._ent_prop(r, self.pv["jumlah_kb"], 6)
            tk.Label(r, text="JEDA ANTAR TEKAN (detik):", bg=C_BG,
                     fg=C_MUTED, font=F_XS).pack(side="left",
                                                 padx=(12, 4))
            self._ent_prop(r, self.pv["jeda_klik"], 6)
        elif jenis == "SCROLL":
            self.pv["arah"] = tk.StringVar(
                value=l.get("arah")
                if l.get("arah") in ("Turun", "Naik") else "Turun")
            self.pv["jumlah_scroll"] = tk.StringVar(value=str(
                int(_angka(l.get("jumlah_scroll"), 3, 0, 1000))))
            r = self._baris_prop("ARAH SCROLL")
            tk.OptionMenu(r, self.pv["arah"], "Turun",
                          "Naik").pack(side="left")
            tk.Label(r, text="JUMLAH GULUNGAN:", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=(12, 4))
            self._ent_prop(r, self.pv["jumlah_scroll"], 6)
        elif jenis == "CATATAN":
            self.pv["catatan"] = tk.StringVar(
                value=str(l.get("catatan") or ""))
            r = self._baris_prop("ISI CATATAN")
            self._ent_prop(r, self.pv["catatan"], 46, tengah=False)
            tk.Label(self.prop_body,
                     text="Catatan hanya penanda di tabel - tidak ada "
                          "aksi yang dijalankan.",
                     bg=C_BG, fg=C_MUTED, font=F_XS,
                     anchor="w").pack(fill="x")
        elif jenis == "LOOP_MULAI":
            self.pv["jumlah_loop"] = tk.StringVar(value=str(
                int(_angka(l.get("jumlah_loop"), 2, 0, 100000))))
            self.pv["ikut_video"] = tk.BooleanVar(
                value=bool(l.get("ikut_video")))
            r = self._baris_prop("JUMLAH ULANGAN")
            self._ent_prop(r, self.pv["jumlah_loop"], 7)
            tk.Checkbutton(self.prop_body,
                           text="Ikut JUMLAH VIDEO di kolom isian atas "
                                "(angka di sini diabaikan)",
                           variable=self.pv["ikut_video"], bg=C_BG,
                           fg=C_TEXT, font=F_XS,
                           anchor="w").pack(fill="x")
            tk.Label(self.prop_body,
                     text="Semua langkah di ANTARA 'ULANGI-MULAI' dan "
                          "'ULANGI-AKHIR' diulang sesuai jumlah di atas. "
                          "Gunakan GESER PER PUTARAN pada langkah KLIK "
                          "di dalamnya agar klik turun ke baris "
                          "berikutnya.",
                     bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(
                         fill="x", pady=(4, 0))
        else:  # LOOP_AKHIR
            tk.Label(self.prop_body,
                     text="Akhir blok ULANGI - langkah di antara "
                          "ULANGI-MULAI dan sini diulang sesuai jumlah "
                          "ulangan.",
                     bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(
                         fill="x", pady=(4, 0))

        # ---- aktif + info ----
        self.pv["aktif"] = tk.BooleanVar(value=bool(l.get("aktif", True)))
        tk.Checkbutton(self.prop_body,
                       text="LANGKAH AKTIF (lepas centang = dilewati "
                            "saat jalan)",
                       variable=self.pv["aktif"], bg=C_BG, fg=C_TEXT,
                       font=F_XS, anchor="w").pack(fill="x", pady=(4, 0))
        self.lbl_ambil = tk.Label(self.prop_body, text="", bg=C_BG,
                                  fg=C_ORANGE, font=F_XS, anchor="w",
                                  wraplength=860, justify="left")
        self.lbl_ambil.pack(fill="x", pady=(4, 0))
        for var in self.pv.values():
            if isinstance(var, tk.Variable):
                var.trace_add("write", self._terapkan_prop)
        self._loading_prop = False

    def _terapkan_prop_studio(self, l):
        """v5.5: simpan panel PROPERTI langkah gaya Studio."""
        try:
            x = int(float(str(self.pv["x"].get()).strip() or "nan"))
            y = int(float(str(self.pv["y"].get()).strip() or "nan"))
            l["posisi"] = [x, y]
        except (KeyError, ValueError, TypeError):
            pass
        try:
            l["jeda"] = max(0.0, float(
                str(self.pv["jeda"].get()).replace(",", ".")))
        except (KeyError, ValueError, TypeError):
            pass
        l["label"] = self.pv["label"].get()
        jenis = l["jenis"]
        if jenis == "KLIK":
            l["tombol_mouse"] = self.pv["tombol_mouse"].get()
            l["klik"] = int(_angka(self.pv["klik"].get(), 1, 0, 500))
            l["jeda_klik"] = _angka(self.pv["jeda_klik"].get(), 0.3,
                                    0.05, 60)
            l["geser"] = int(_angka(self.pv["geser"].get(), 0, 0,
                                    100000))
        elif jenis == "JEDA":
            l["detik"] = _angka(self.pv["detik"].get(), 1.0, 0, 86400)
        elif jenis == "GAMBAR":
            g = l.setdefault("gambar", {})
            g["path"] = self.pv["g_path"].get().strip()
            aksi = self.pv["g_aksi"].get()
            g["aksi"] = (aksi if aksi in GAMBAR_AKSI_OPSI
                         else "Klik di gambar")
            gagal = self.pv["g_gagal"].get()
            g["gagal"] = (gagal if gagal in GAMBAR_GAGAL_OPSI_STUDIO
                          else "Lewati langkah")
            g["mirip"] = self.pv["g_mirip"].get().strip()
            # fokus diatur lewat tombol PILIH AREA FOKUS / KOSONGKAN
        elif jenis == "KETIK":
            l["teks"] = self.pv["teks"].get()
            l["ctrl_a"] = bool(self.pv["ctrl_a"].get())
            l["enter"] = bool(self.pv["enter"].get())
        elif jenis == "TANGGAL_JAM":
            sumber = self.pv["sumber"].get()
            l["sumber"] = (sumber if sumber in SUMBER_TANGGAL_OPSI
                           else "Tab CutMotions")
            l["teks"] = self.pv["teks"].get()
            l["ctrl_a"] = bool(self.pv["ctrl_a"].get())
            l["enter"] = bool(self.pv["enter"].get())
        elif jenis == "VIDEO_CAPTION":
            isi = self.pv["isi"].get()
            l["isi"] = (isi if isi in ISI_VIDEO_OPSI
                        else "Caption dasar + nama video")
            l["teks"] = self.pv["teks"].get()
            l["ctrl_a"] = bool(self.pv["ctrl_a"].get())
            l["enter"] = bool(self.pv["enter"].get())
        elif jenis == "TOMBOL":
            l["tombol_kb"] = (self.pv["tombol_kb"].get().strip()
                              or "Enter")
            l["jumlah_kb"] = int(_angka(self.pv["jumlah_kb"].get(), 1,
                                        1, 500))
            l["jeda_klik"] = _angka(self.pv["jeda_klik"].get(), 0.3,
                                    0.05, 60)
        elif jenis == "SCROLL":
            l["arah"] = self.pv["arah"].get()
            l["jumlah_scroll"] = int(_angka(
                self.pv["jumlah_scroll"].get(), 3, 0, 1000))
        elif jenis == "CATATAN":
            l["catatan"] = self.pv["catatan"].get()
        elif jenis == "LOOP_MULAI":
            l["jumlah_loop"] = int(_angka(
                self.pv["jumlah_loop"].get(), 2, 0, 100000))
            l["ikut_video"] = bool(self.pv["ikut_video"].get())
        l["aktif"] = bool(self.pv["aktif"].get())
        self._refresh_tabel()

    def _terapkan_prop(self, *_):
        if self._loading_prop:
            return
        iid = self.sel
        ek = None
        if iid not in POS_KUNCI:
            ek = self._iid_ekstra(iid) if iid else None
            if not ek:
                return
        if ek and str(ek.get("jenis") or "") in JENIS_STUDIO:
            self._terapkan_prop_studio(ek)
            return
        try:
            x = int(float(str(self.pv["x"].get()).strip() or "nan"))
            y = int(float(str(self.pv["y"].get()).strip() or "nan"))
            pos_baru = [x, y]
        except (ValueError, TypeError):
            pos_baru = None
        try:
            jeda_baru = max(0.0, float(
                str(self.pv["jeda"].get()).replace(",", ".")))
        except ValueError:
            jeda_baru = None
        try:
            jk_baru = max(0.05, float(
                str(self.pv["jeda_klik"].get()).replace(",", ".")))
        except ValueError:
            jk_baru = None
        if ek:
            ek["posisi"] = pos_baru
            if jeda_baru is not None:
                ek["jeda"] = jeda_baru
            if jk_baru is not None:
                ek["jeda_klik"] = jk_baru
            params = ek.setdefault("params", {})
            for nama_p, _l, _w in PARAM_DEF.get(ek.get("sumber"), []):
                if "p_" + nama_p in self.pv:
                    params[nama_p] = self.pv["p_" + nama_p].get()
        else:
            kunci = iid
            self.posisi[kunci] = pos_baru
            if jeda_baru is not None:
                self.jeda_per[kunci] = jeda_baru
            if jk_baru is not None:
                self.jeda_klik_per[kunci] = jk_baru
        if "g_aktif" in self.pv:
            cfg = (ek.get("gambar") if ek else
                   self.gambar_langkah.setdefault(
                       iid, gambar_langkah_default()))
            cfg["aktif"] = bool(self.pv["g_aktif"].get())
            cfg["path"] = self.pv["g_path"].get().strip()
            aksi_g = self.pv["g_aksi"].get()
            cfg["aksi"] = aksi_g if aksi_g in GAMBAR_AKSI_OPSI \
                else "Klik di gambar"
            gagal_g = self.pv["g_gagal"].get()
            cfg["gagal"] = gagal_g if gagal_g in GAMBAR_GAGAL_OPSI \
                else "Klik titik X,Y"
            cfg["radius"] = self.pv["g_radius"].get().strip()
            cfg["mirip"] = self.pv["g_mirip"].get().strip()
        self._refresh_tabel()

    def _terapkan_opts(self, *_):
        """Variabel isian berubah -> segarkan tabel/pratinjau."""
        if self._loading:
            return
        self._refresh_tabel()
        if hasattr(self, "lbl_count"):
            self._update_count()
            self._update_preview()

    def _terapkan_jeda_semua(self):
        v = _angka(self.vars["jeda_langkah"].get(), 1.0, 0.0, 3600)
        for k in POS_KUNCI:
            self.jeda_per[k] = v
        for ek in self.langkah_extra:
            ek["jeda"] = v
        self._refresh_tabel()
        self._render_properti()
        self._set_status("Jeda {:.1f} detik diterapkan ke semua langkah "
                         "(kolom JEDA).".format(v), C_GREEN)

    # ================== AMBIL / LIHAT POSISI ==================
    def _tampilkan_info(self, teks, warna=C_ORANGE):
        if hasattr(self, "lbl_ambil") and self.lbl_ambil.winfo_exists():
            self.lbl_ambil.config(text=teks, fg=warna)

    def _ambil_posisi(self, iid):
        if not PYNPUT_OK:
            messagebox.showerror(
                APP_NAME, "Library pynput belum terpasang.\n\n"
                          "Buka CMD lalu jalankan:\n  pip install pynput")
            return
        ek = self._iid_ekstra(iid) if iid not in POS_KUNCI else None
        if ek:
            judul = ek.get("label") or iid
        else:
            judul = LABEL_POSISI.get(iid, iid)

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
                    if ek:
                        ek["posisi"] = [int(px), int(py)]
                    else:
                        self.posisi[iid] = [int(px), int(py)]
                    self._refresh_tabel()
                    if self.sel == iid:
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

    def _lihat_posisi(self, iid):
        if not PYNPUT_OK:
            return
        if iid in POS_KUNCI:
            pos = self.posisi.get(iid)
        else:
            ek = self._iid_ekstra(iid)
            pos = ek.get("posisi") if ek else None
        if not pos:
            messagebox.showinfo(APP_NAME,
                                "Posisi ini belum diatur. Klik dulu AMBIL "
                                "(atau isi X,Y manual).")
            return
        try:
            self.mouse.position = (pos[0], pos[1])
        except Exception:
            pass

    # ================== GAMBAR REFERENSI (SEMUA LANGKAH) ==================
    def _pasang_gambar_langkah(self, iid, path):
        """Pasang file gambar pada satu langkah (bawaan/salinan)."""
        self.vars["gambar_ref"].set(path)   # ingat gambar terakhir
        nama = iid
        if iid and iid not in POS_KUNCI:
            ek = self._iid_ekstra(iid)
            if ek:
                cfg = ek.setdefault("gambar", gambar_langkah_default())
                cfg["aktif"] = True
                cfg["path"] = path
                nama = ek.get("label") or iid
        elif iid in POS_KUNCI:
            cfg = self.gambar_langkah.setdefault(
                iid, gambar_langkah_default())
            cfg["aktif"] = True
            cfg["path"] = path
            nama = LABEL_POSISI.get(iid, iid)
        else:
            return
        self._save_settings()
        self._refresh_tabel()
        if self.sel == iid:
            self._render_properti()
        self._set_status("Gambar referensi terpasang pada {}: {}".format(
            nama, path), C_GREEN)
        self._tampilkan_info("Gambar dipasang pada {}: {}".format(
            nama, os.path.basename(path)), C_GREEN)

    def _pilih_gambar_ref(self, iid=None):
        iid = iid or self.sel
        f = filedialog.askopenfilename(
            title="Pilih gambar referensi (potongan layar)",
            filetypes=[("Gambar", "*.png *.jpg *.jpeg *.bmp"),
                       ("Semua file", "*.*")])
        if f:
            self._pasang_gambar_langkah(iid, f)

    def _potong_gambar(self, target=None):
        """v5.1: potong gambar referensi LANGSUNG DI LAYAR.

        Aplikasi disembunyikan sejenak, layar dibekukan fullscreen,
        lalu user MENYERET kotak langsung di area yang diinginkan -
        hanya area yang diseret yang disimpan (bukan seluruh layar).
        Hasil selalu file BARU di folder data\\referensi sehingga
        bisa dipakai berkali-kali dengan referensi berbeda-beda.

        Gambar dipasang pada LANGKAH TERPILIH (v4.2).
        """
        if not PIL_OK or not CV_OK:
            messagebox.showwarning(
                APP_NAME,
                "Fitur potong gambar butuh Pillow + OpenCV.\n\n"
                "Buka CMD lalu jalankan:\n"
                "  pip install pillow opencv-python")
            return
        self._potong_target = target if target is not None else (
            ("langkah", self.sel) if self.sel else None)

        def kerja():
            try:
                for s in range(3, 0, -1):
                    self.root.after(0, lambda s=s: self._set_status(
                        "Layar akan DIBEKUKAN dalam {} detik - pastikan "
                        "area yang mau dipotong terlihat...".format(s),
                        C_ORANGE))
                    time.sleep(1)
                # v5.1: sembunyikan jendela aplikasi dulu supaya area
                # di baliknya juga bisa dipotong
                induk = self.root.winfo_toplevel()
                self.root.after(0, induk.withdraw)
                time.sleep(0.4)
                img = ImageGrab.grab()
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    APP_NAME, "Gagal mengambil screenshot:\n{}".format(e)))
                self.root.after(0, self._tampil_lagi)
                return

            def tampil():
                try:
                    OverlayPotong(self.root, img, self._gambar_terpotong)
                except Exception as e:
                    messagebox.showerror(
                        APP_NAME,
                        "Gagal membuka layar potong:\n{}".format(e))
                finally:
                    self._tampil_lagi()

            self.root.after(0, tampil)

        threading.Thread(target=kerja, daemon=True).start()

    def _tampil_lagi(self):
        """Tampilkan kembali jendela utama setelah potong selesai."""
        try:
            self.root.winfo_toplevel().deiconify()
        except Exception:
            pass

    def _gambar_terpotong(self, path):
        target = getattr(self, "_potong_target", None)
        iid = target[1] if (target and target[0] == "langkah" and
                            len(target) > 1) else self.sel
        self._pasang_gambar_langkah(iid, path)
        self._set_status("Gambar referensi tersimpan: {}".format(path),
                         C_GREEN)

    def _tes_cari(self):
        """Tes pencarian gambar pada LANGKAH TERPILIH di tabel."""
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
        iid = self.sel
        if iid in POS_KUNCI:
            cfg = self.gambar_langkah.get(iid) or {}
            pos = self.posisi.get(iid)
            nama = LABEL_POSISI.get(iid, iid)
        else:
            ek = self._iid_ekstra(iid) if iid else None
            if not ek:
                messagebox.showinfo(
                    APP_NAME,
                    "Klik dulu satu baris langkah di tabel yang mau "
                    "dites cari gambarnya.")
                return
            if ek.get("jenis") == "GAMBAR":
                # v5.5: langkah CARI GAMBAR gaya Studio -> uji pakai AREA
                self._tes_cari_studio(ek)
                return
            cfg = ek.get("gambar") or {}
            pos = ek.get("posisi")
            nama = ek.get("label") or iid
        gambar = str(cfg.get("path") or "").strip()
        if not cfg.get("aktif"):
            messagebox.showinfo(
                APP_NAME,
                "Cari gambar belum DIAKTIFKAN pada langkah {}.\n\n"
                "Centang 'Aktifkan CARI GAMBAR pada langkah ini' di panel "
                "properti.".format(nama))
            return
        if not gambar or not os.path.isfile(gambar):
            messagebox.showinfo(
                APP_NAME,
                "Pilih dulu gambar referensi langkah {}.\n\nCara termudah: "
                "klik 'POTONG GAMBAR...' pada langkah itu, lalu seret "
                "kotak di atas tulisan/gambarnya.".format(nama))
            return
        if not pos:
            messagebox.showinfo(
                APP_NAME,
                "Atur dulu posisi langkah {} sebagai titik acuan "
                "pencarian (tombol AMBIL).".format(nama))
            return
        V = self.vars
        radius = int(_angka(cfg.get("radius"),
                            _angka(V["radius"].get(), 300, 50, 2000),
                            50, 2000))
        mirip = _angka(cfg.get("mirip"),
                       _angka(V["kemiripan"].get(), 0.8, 0.5, 0.99),
                       0.5, 0.99)

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
                    mode_t = ("pindah saja"
                              if cfg.get("aksi") == "Pindah saja"
                              else "akan diklik")
                    self._set_status(
                        "TES OK: gambar KETEMU di ({}, {}) - kemiripan "
                        "{:.0%}. Mouse dipindah ke sana (tidak diklik; "
                        "mode langkah ini: {})."
                        .format(x, y, skor, mode_t), C_GREEN)
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

    # ================== v4.2: SALIN / TEMPEL / HAPUS LANGKAH ==========
    def _menu_klik_kanan(self, ev):
        iid = self.tree.identify_row(ev.y)
        # v5.7: klik kanan pada baris yang SUDAH terpilih bersama
        # tidak boleh merusak pilihan banyak
        if iid and iid not in self.tree.selection():
            self.tree.selection_set(iid)
        n = len(self.tree.selection())
        m = tk.Menu(self.root, tearoff=0)
        menu_gelap(m)
        m.add_command(label="Tahan CTRL / SHIFT saat klik = pilih "
                            "banyak langkah",
                      state="disabled")
        m.add_separator()
        sub_st = tk.Menu(m, tearoff=0)
        menu_gelap(sub_st)
        self._isi_menu_tambah(sub_st)
        m.add_cascade(label="Tambah langkah STUDIO di sini",
                      menu=sub_st)
        m.add_separator()
        m.add_command(label="Salin {}  (Ctrl+C)".format(
                          "{} langkah terpilih".format(n) if n > 1
                          else "langkah ini"),
                      command=self._salin_langkah)
        m.add_command(label="Tempel salinan di sini  (Ctrl+V)",
                      command=self._tempel_langkah)
        # v5.9: semua langkah (termasuk bawaan A-J) bisa dihapus;
        # bawaan A-J yang terhapus bisa dikembalikan dari sini
        if self.slot_mati:
            sub_k = tk.Menu(m, tearoff=0)
            menu_gelap(sub_k)
            for k in POS_KUNCI:
                if k not in self.slot_mati:
                    continue

                def kembalikan(k=k):
                    self.slot_mati.discard(k)
                    self._refresh_tabel()
                    self._save_settings()
                    self._set_status(
                        "Langkah bawaan {} dikembalikan ke alur.".format(
                            SLOT_KODE.get(k, k)), C_GREEN)

                sub_k.add_command(
                    label="Kembalikan {}  ({})".format(
                        SLOT_KODE.get(k, k), LABEL_POSISI.get(k, k)),
                    command=kembalikan)
            m.add_cascade(label="Kembalikan langkah bawaan yang "
                                "dihapus", menu=sub_k)
        m.add_command(label="Hapus {}  (Del)".format(
                          "langkah terpilih" if n > 1
                          else "langkah ini"),
                      command=self._hapus_langkah)
        try:
            m.tk_popup(ev.x_root, ev.y_root)
        finally:
            m.grab_release()

    def _salin_langkah(self):
        """v5.7: salin SEMUA langkah terpilih ke papan klip.

        Pilihan banyak didapat dengan menahan CTRL / SHIFT saat
        mengklik baris (atau Ctrl+A untuk semua). Urutan salinan
        mengikuti urutan tampil di tabel.
        """
        pilih = list(self.tree.selection())
        if not pilih and self.sel:
            pilih = [self.sel]
        urut = self._urutan_lengkap()
        pilih = [i for i in urut if i in pilih] + \
            [i for i in pilih if i not in urut]
        klip = []
        for iid in pilih:
            if iid in POS_KUNCI:
                klip.append({
                    "sumber": iid,
                    "params": dict(self._params_dari_global(iid)),
                    "posisi": (list(self.posisi.get(iid))
                               if self.posisi.get(iid) else None),
                    "gambar": dict(self.gambar_langkah.get(iid)
                                   or gambar_langkah_default()),
                    "jeda": self.jeda_per.get(iid, 1.0),
                    "jeda_klik": self.jeda_klik_per.get(iid, 0.3),
                })
                continue
            ek = self._iid_ekstra(iid)
            if not ek:
                continue
            if str(ek.get("jenis") or "") in JENIS_STUDIO:
                # v5.5: langkah gaya Studio disalin utuh
                klip.append({"jenis_step": json.loads(
                    json.dumps(ek))})
            else:
                klip.append({
                    "sumber": ek.get("sumber"),
                    "params": dict(ek.get("params") or {}),
                    "posisi": (list(ek["posisi"])
                               if ek.get("posisi") else None),
                    "gambar": dict(ek.get("gambar")
                                   or gambar_langkah_default()),
                    "jeda": float(ek.get("jeda", 1.0)),
                    "jeda_klik": float(ek.get("jeda_klik", 0.3)),
                })
        if not klip:
            messagebox.showinfo(
                APP_NAME,
                "Klik dulu satu baris langkah di tabel yang mau "
                "disalin.\n\nTahan CTRL atau SHIFT saat mengklik untuk "
                "memilih BANYAK langkah sekaligus (Ctrl+A = semua).")
            return
        self.papan_klip = {"banyak": klip}
        self._set_status(
            "{} langkah disalin. Klik baris acuan lalu TEMPEL "
            "LANGKAH (Ctrl+V).".format(len(klip)), C_GREEN)

    def _tempel_langkah(self):
        """v5.7: tempel 1 ATAU BANYAK salinan berurutan setelah acuan.

        Urutan tempel = urutan saat disalin; langkah kedua dst
        dirantai setelah hasil tempel sebelumnya.
        """
        klip = self.papan_klip
        if not klip:
            messagebox.showinfo(
                APP_NAME,
                "Belum ada langkah yang disalin.\n\nKlik satu baris di "
                "tabel, lalu klik SALIN LANGKAH dulu.\n(Tahan CTRL/SHIFT "
                "saat mengklik untuk menyalin banyak sekaligus.)")
            return
        items = klip.get("banyak") or [klip]
        anchor = self.sel if (
            self.sel and (self.sel in POS_KUNCI
                          or self._iid_ekstra(self.sel))) else POS_KUNCI[-1]
        dipaste = []
        for it in items:
            if it.get("jenis_step"):
                # v5.5: langkah gaya Studio (utuh, parameter ikut)
                self._studio_counter = getattr(self, "_studio_counter",
                                               0) + 1
                baru = json.loads(json.dumps(it["jenis_step"]))
                baru["uid"] = self._uid_ekstra_baru()  # v5.8: anti-bentrok
                baru["setelah"] = anchor
                baru["label"] = "{} #{}".format(
                    LABEL_JENIS.get(baru.get("jenis"), "LANGKAH STUDIO"),
                    self._studio_counter)
                self.langkah_extra.append(baru)
                anchor = baru["uid"]
                dipaste.append(baru["uid"])
            elif it.get("sumber"):
                uid = self._uid_ekstra_baru()      # v5.8: anti-bentrok
                kode = SLOT_KODE.get(it["sumber"], "?")
                ek = {"uid": uid, "sumber": it["sumber"],
                      "setelah": anchor,
                      "label": "{} - salinan {}".format(
                          kode, uid[1:]),
                      "posisi": (list(it["posisi"]) if it.get("posisi")
                                 else None),
                      "jeda": float(it.get("jeda", 1.0)),
                      "jeda_klik": float(it.get("jeda_klik", 0.3)),
                      "params": dict(it.get("params") or {}),
                      "gambar": dict(it.get("gambar")
                                     or gambar_langkah_default())}
                self.langkah_extra.append(ek)
                anchor = uid
                dipaste.append(uid)
        if not dipaste:
            messagebox.showinfo(APP_NAME,
                                "Papan klip kosong / isinya tidak "
                                "dikenal. Salin ulang langkahnya.")
            return
        self._refresh_tabel()
        self.sel = dipaste[-1]
        try:
            self.tree.selection_set(*dipaste)
            self.tree.see(self.sel)
        except Exception:
            pass
        self._render_properti()
        self._save_settings()
        self._set_status(
            "{} langkah ditempel berurutan setelah acuan - atur "
            "posisinya (AMBIL) bila perlu, lalu jalankan F6.".format(
                len(dipaste)), C_GREEN)

    def _hapus_langkah(self):
        """v5.9: hapus SEMUA langkah terpilih - TERMASUK bawaan A-J.

        - Salinan/langkah Studio: benar-benar dibuang dari profil.
        - Langkah bawaan A-J: ditandai MATI (slot_mati) - hilang dari
          tabel & dilewati mesin saat F6, tapi bisa DIKEMBALIKAN
          lewat klik kanan tabel > Kembalikan langkah bawaan.
        Dulu bawaan A-J menolak dihapus - user meminta semua langkah
        bisa dihapus manual.
        """
        pilih = list(self.tree.selection())
        if not pilih and self.sel:
            pilih = [self.sel]
        urut = self._urutan_lengkap()
        pilih = [i for i in urut if i in pilih] + \
            [i for i in pilih if i not in urut]
        terhapus = []
        slot_mati_baru = []
        for iid in pilih:
            if iid in POS_KUNCI:
                if iid not in self.slot_mati:
                    slot_mati_baru.append(iid)
                continue
            ek = self._iid_ekstra(iid)
            if ek:
                terhapus.append(ek)
        if not terhapus and not slot_mati_baru:
            messagebox.showinfo(
                APP_NAME,
                "Pilih dulu baris yang mau dihapus.\n\nTahan CTRL/SHIFT "
                "saat mengklik untuk menghapus banyak langkah "
                "sekaligus.")
            return
        n_slot = len(slot_mati_baru)
        if len(terhapus) == 1 and not n_slot:
            pesan = "Hapus salinan '{}'?".format(
                terhapus[0].get("label") or terhapus[0]["uid"])
        else:
            pesan = ("Hapus {} langkah terpilih sekaligus?".format(
                len(terhapus) + n_slot))
            if n_slot:
                daftar = ", ".join(SLOT_KODE.get(s, s)
                                   for s in slot_mati_baru)
                pesan += ("\n\nTermasuk {} langkah bawaan alur ({}): "
                          "langkah itu DILEWATI saat jalan, dan bisa "
                          "DIKEMBALIKAN lewat klik kanan tabel > "
                          "Kembalikan langkah bawaan.".format(
                              n_slot, daftar))
        if not messagebox.askyesno(APP_NAME, pesan):
            return
        for iid in slot_mati_baru:
            self.slot_mati.add(iid)
        for ek in terhapus:
            iid = ek["uid"]
            # rantai anak-anaknya naik ke acuan si penghapus
            for lain in self.langkah_extra:
                if lain.get("setelah") == iid:
                    lain["setelah"] = ek.get("setelah") or "pos_jadwal"
            # v5.9: buang SEMUA entri ber-uid itu (anti sisa dobel)
            self.langkah_extra[:] = [x for x in self.langkah_extra
                                     if x.get("uid") != iid]
        if terhapus:
            anchor = terhapus[0].get("setelah") or "pos_jadwal"
        elif slot_mati_baru:
            anchor = slot_mati_baru[0]
        else:
            anchor = "pos_jadwal"
        self.sel = anchor
        self._refresh_tabel()
        urut2 = self._urutan_lengkap()
        # bila acuan ikut hilang dari tampilan, pilih baris pertama
        self.sel = anchor if anchor in urut2 else \
            (urut2[0] if urut2 else None)
        try:
            if self.sel and self.tree.exists(self.sel):
                self.tree.selection_set(self.sel)
        except Exception:
            pass
        self._render_properti()
        self._save_settings()
        pesan_h = []
        if terhapus:
            pesan_h.append("{} salinan/langkah tambahan dihapus".format(
                len(terhapus)))
        if slot_mati_baru:
            pesan_h.append("{} langkah bawaan dimatikan ({})".format(
                n_slot, ", ".join(SLOT_KODE.get(s, s)
                                  for s in slot_mati_baru)))
        self._set_status("{}.".format("; ".join(pesan_h)).capitalize(),
                         C_ORANGE)

    # ================== v5.5: LANGKAH STUDIO DI ALUR A-J ==================
    # ================== v5.6: HOOK REKAM AKSI (mixin) ==================
    def perekam_uid_mulai(self):
        return 0        # uid ditimpa jadi "x{n}" di perekam_sisipkan

    def perekam_sisipkan(self, baru, uid_akhir):
        """v5.6: hasil REKAM AKSI masuk ALUR CUTMOTIONS (A-J).

        Langkah hasil rekaman disisipkan SETELAH baris terpilih
        (atau di akhir alur bila tidak ada) - berantai, urutannya
        persis seperti yang terekam - lalu langsung bisa disunting
        di panel PROPERTI seperti langkah Studio lainnya.
        """
        anchor = self.sel if (
            self.sel and (self.sel in POS_KUNCI
                          or self._iid_ekstra(self.sel))) else POS_KUNCI[-1]
        for l in baru:
            self._studio_counter = getattr(self, "_studio_counter", 0) + 1
            l["uid"] = self._uid_ekstra_baru()     # v5.8: anti-bentrok
            l["setelah"] = anchor
            l["label"] = "{} #{}".format(
                LABEL_JENIS.get(l.get("jenis"), "LANGKAH STUDIO"),
                self._studio_counter)
            anchor = l["uid"]
            self.langkah_extra.append(l)
        self._refresh_tabel()
        self.sel = baru[0]["uid"]
        try:
            self.tree.selection_set(self.sel)
            self.tree.see(self.sel)
        except Exception:
            pass
        self._render_properti()
        self._save_settings()
        n_klik = sum(1 for l in baru if l["jenis"] == "KLIK")
        n_ketik = sum(1 for l in baru if l["jenis"] in ("KETIK", "TOMBOL"))
        n_scroll = sum(1 for l in baru if l["jenis"] == "SCROLL")
        self._set_status(
            "REKAMAN SELESAI: {} langkah masuk ALUR CUTMOTIONS "
            "({} klik, {} ketikan/tombol, {} scroll) - posisinya tepat "
            "setelah langkah acuan; sunting bila perlu lalu JALANKAN "
            "(F6).".format(len(baru), n_klik, n_ketik, n_scroll), C_GREEN)

    def _isi_menu_tambah(self, m):
        """Isi menu '+ TAMBAH LANGKAH' - semua menu STUDIO MAKRO."""
        for jenis, label in [
            ("KLIK", "+ KLIK TITIK"),
            ("JEDA", "+ JEDA / TUNGGU"),
            ("GAMBAR", "+ CARI GAMBAR (klik / pindah kursor)"),
            ("KETIK", "+ KETIK TEKS"),
            ("TANGGAL_JAM", "+ ISI TANGGAL-JAM (kolom tanggal rilis)"),
            ("VIDEO_CAPTION",
             "+ ISI VIDEO & CAPTION (jumlah / caption + nama video)"),
            ("TOMBOL", "+ TEKAN TOMBOL"),
            ("SCROLL", "+ SCROLL"),
            ("CATATAN", "+ CATATAN"),
        ]:
            m.add_command(label=label,
                          command=lambda j=jenis: self._tambah_studio(j))
        m.add_separator()
        m.add_command(label="+ ULANGI - MULAI (blok pengulangan)",
                      command=lambda: self._tambah_studio("LOOP_MULAI"))
        m.add_command(label="+ ULANGI - AKHIR",
                      command=lambda: self._tambah_studio("LOOP_AKHIR"))

    def _tambah_studio(self, jenis):
        """v5.5: sisipkan langkah gaya Studio Makro ke alur A-J.

        Langkah disisipkan SETELAH baris terpilih (atau di akhir
        alur bila tidak ada) dan dijalankan TEPAT di posisinya.
        """
        if jenis not in JENIS_STUDIO:
            return
        anchor = self.sel if (
            self.sel and (self.sel in POS_KUNCI
                          or self._iid_ekstra(self.sel))) else POS_KUNCI[-1]
        self._studio_counter = getattr(self, "_studio_counter", 0) + 1
        l = studio_langkah_baru(jenis, 0)
        l["uid"] = self._uid_ekstra_baru()      # v5.8: anti-bentrok
        l["setelah"] = anchor
        l["label"] = "{} #{}".format(LABEL_JENIS[jenis],
                                     self._studio_counter)
        self.langkah_extra.append(l)
        self._refresh_tabel()
        self.sel = l["uid"]
        try:
            self.tree.selection_set(l["uid"])
            self.tree.see(l["uid"])
        except Exception:
            pass
        self._render_properti()
        self._save_settings()
        nama_acuan = (LABEL_POSISI.get(anchor, anchor)
                      if anchor in POS_KUNCI
                      else ((self._iid_ekstra(anchor) or {}).get("label")
                            or "langkah terpilih"))
        self._set_status(
            "{} ditambahkan setelah {} - atur di panel PROPERTI. "
            "Langkah dijalankan tepat di posisinya dalam alur "
            "A-J.".format(LABEL_JENIS[jenis], nama_acuan), C_GREEN)

    def _pilih_area_fokus(self, uid=None):
        """v5.5: pilih AREA FOKUS langkah CARI GAMBAR di alur A-J.

        Teknik sama dengan tab Studio: layar dibekukan fullscreen,
        lalu user MENYERET kotak - hasilnya koordinat area, bukan
        file gambar.
        """
        if not PIL_OK:
            messagebox.showwarning(
                APP_NAME,
                "Fitur area fokus butuh Pillow.\n\nBuka CMD lalu jalankan:\n"
                "  pip install pillow")
            return
        uid = uid or self.sel
        ek = self._iid_ekstra(uid) if (uid and uid not in POS_KUNCI) \
            else None
        if not ek or ek.get("jenis") != "GAMBAR":
            messagebox.showinfo(
                APP_NAME,
                "Pilih dulu baris CARI GAMBAR (langkah STUDIO berkode S) "
                "yang mau diberi AREA FOKUS.")
            return
        self._fokus_uid = uid

        def kerja():
            try:
                for s in range(3, 0, -1):
                    self.root.after(0, lambda s=s: self._set_status(
                        "Layar akan DIBEKUKAN dalam {} detik - siapkan "
                        "halaman tempat gambar biasanya muncul...".format(
                            s), C_ORANGE))
                    time.sleep(1)
                induk = self.root.winfo_toplevel()
                self.root.after(0, induk.withdraw)
                time.sleep(0.4)
                img = ImageGrab.grab()
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    APP_NAME,
                    "Gagal mengambil screenshot:\n{}".format(e)))
                self.root.after(0, self._tampil_lagi)
                return

            def tampil():
                try:
                    OverlayPotong(self.wadah, img, None,
                                  on_batal=self._potong_batal,
                                  mode="area",
                                  on_area=self._area_terpilih)
                except Exception as e:
                    messagebox.showerror(
                        APP_NAME,
                        "Gagal membuka layar pilih area:\n{}".format(e))
                finally:
                    self._tampil_lagi()

            self.root.after(0, tampil)

        threading.Thread(target=kerja, daemon=True).start()

    def _area_terpilih(self, koord):
        ek = self._iid_ekstra(getattr(self, "_fokus_uid", None))
        if not ek:
            return
        ek.setdefault("gambar", {})["fokus"] = list(koord)
        self._save_settings()
        self._refresh_tabel()
        if self.sel == ek["uid"]:
            self._render_properti()
        self._set_status(
            "AREA FOKUS tersimpan: ({},{}) - ({},{})  - gambar dicari "
            "hanya di dalam kotak itu.".format(koord[0], koord[1],
                                               koord[2], koord[3]),
            C_GREEN)

    def _potong_batal(self):
        self._set_status("Potong gambar / area fokus dibatalkan (ESC).",
                         C_MUTED)

    def _fokus_kosongkan(self, uid):
        ek = self._iid_ekstra(uid) if (uid and uid not in POS_KUNCI) \
            else None
        if not ek:
            return
        ek.setdefault("gambar", {})["fokus"] = None
        self._save_settings()
        self._refresh_tabel()
        if self.sel == uid:
            self._render_properti()
        self._set_status("Area fokus dikosongkan - gambar dicari di "
                         "seluruh layar.", C_GREEN)

    def _tes_cari_studio(self, ek):
        """Tes pencarian gambar langkah CARI GAMBAR gaya Studio."""
        if not PYNPUT_OK:
            messagebox.showerror(APP_NAME, "Library pynput belum "
                                           "terpasang.")
            return
        if not CV_OK:
            messagebox.showwarning(
                APP_NAME,
                "opencv-python belum terpasang - pencarian gambar tidak "
                "bisa dipakai.\n\nBuka CMD lalu jalankan:\n"
                "  pip install opencv-python\n\n"
                "Atau pakai CutUploaderPro.exe (OpenCV sudah menyatu).")
            return
        g = ek.get("gambar") or {}
        path = str(g.get("path") or "").strip()
        nama = str(ek.get("label") or "") or LABEL_JENIS["GAMBAR"]
        if not path or not os.path.isfile(path):
            messagebox.showinfo(
                APP_NAME,
                "Pilih dulu gambar referensi langkah {}.\n\nCara "
                "termudah: klik 'POTONG GAMBAR...', lalu seret kotak "
                "di atas tulisan/tombolnya.".format(nama))
            return
        mirip = _angka(g.get("mirip"), 0.8, 0.5, 0.99)
        area = area_dari_langkah(ek)
        if area:
            desk = "area fokus ({},{})-({},{})".format(area[0], area[1],
                                                       area[2], area[3])
        else:
            desk = "seluruh layar"

        def kerja():
            self.root.after(0, lambda: self._set_status(
                "Mencari '{}' di {} (multi-skala)...".format(
                    os.path.basename(path), desk), C_ORANGE))
            hasil, pesan = cari_di_layar_area(path, area, mirip)

            def lapor():
                if hasil:
                    x, y, skor = hasil
                    try:
                        self.mouse.position = (x, y)
                    except Exception:
                        pass
                    mode_t = ("pindah saja"
                              if g.get("aksi") == "Pindah saja"
                              else "akan diklik")
                    self._set_status(
                        "TES OK: gambar KETEMU di ({}, {}) - kemiripan "
                        "{:.0%}. Mouse dipindah ke sana (tidak diklik; "
                        "mode langkah ini: {}).".format(x, y, skor,
                                                        mode_t), C_GREEN)
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
            "Pencarian gambar (bisa diaktifkan pada langkah mana pun) "
            "butuh opencv-python + Pillow.\n"
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
            "{} v{} - Macro Studio Edition\n\n"
            "DUA MODE dalam satu aplikasi:\n\n"
            "1. STUDIO MAKRO (baru v5.0) - editor alur kerja bebas\n"
            "ala Jitbit Macro Recorder: semua jenis aksi jadi menu\n"
            "tersendiri di atas (+ Klik, + Jeda, + Cari Gambar,\n"
            "+ Ketik Teks, + Tekan Tombol, + Scroll, + Ulangi) dan\n"
            "tabel kosong di bawahnya untuk menyusun alur sendiri.\n\n"
            "2. ALUR CUTMOTIONS (A-J) - uploader batch CutMotions:\n"
            "Jadwal (A-E) > Tambah video + Shift+turun (F-H2) >\n"
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
            "slot_mati": set(self.slot_mati),   # v5.9: A-J yang dihapus
            "jeda_per": dict(self.jeda_per),
            "jeda_klik_per": dict(self.jeda_klik_per),
            "gambar_langkah": {k: dict(v)
                               for k, v in self.gambar_langkah.items()},
            "langkah_extra": [
                json.loads(json.dumps(e)) if isinstance(e, dict) else e
                for e in self.langkah_extra],
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
        if self.shell is not self:
            lain = self.shell.tab_lain(self)
            if lain is not None and lain.running:
                messagebox.showwarning(
                    APP_NAME,
                    "STUDIO MAKRO sedang menjalankan alurnya.\n\n"
                    "Tunggu sampai selesai atau tekan F7 dulu.")
                return
        snap = self._snapshot()
        # v5.9: validasi PER KOLOM - pesan error menunjuk kolom yang
        # salah; kolom kosong otomatis dipakai nilai standarnya; koma
        # diterima sebagai desimal. Dulu: 1 kolom salah/kosong (mis.
        # MUNDUR) langsung dilaporkan sebagai "JUMLAH VIDEO dan
        # pengaturan WAKTU harus diisi dengan angka" walau kolom itu
        # sudah diisi - user bingung.
        try:
            jumlah = _baca_angka("JUMLAH VIDEO",
                                 snap["jumlah"], None, bulat=True)
            mundur = _baca_angka("MUNDUR SEBELUM MULAI",
                                 snap["mundur"], 5, bulat=True)
            jeda_dialog = _baca_angka("JEDA BUKA DIALOG/EDITOR",
                                      snap["jeda_dialog"], 2)
            jeda_langkah = _baca_angka("JEDA ANTAR LANGKAH (default)",
                                       snap["jeda_langkah"], 1)
            tunggu = _baca_angka("TUNGGU UPLOAD PER VIDEO",
                                 snap["tunggu"], 60)
        except ValueError as e:
            nama, isian = e.args[0]
            messagebox.showwarning(
                APP_NAME,
                "Kolom {} berisi \"{}\" - bukan angka yang benar.\n\n"
                "Perbaiki kolom itu di kartu WAKTU & UNGGAH (angka "
                "boleh pakai koma, mis. 1,5). Kolom yang dibiarkan "
                "kosong otomatis dipakai nilai standarnya.".format(
                    nama, isian))
            return
        if jumlah is None:
            messagebox.showwarning(
                APP_NAME,
                "JUMLAH VIDEO belum diisi.\n\nIsi angkanya dulu di "
                "kartu VIDEO & CAPTION (mis. 5).")
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
        slot_mati = snap.get("slot_mati") or set()
        for kunci, label, wajib, _ket in POSISI_DEF:
            if not wajib:
                continue
            if lewati_jadwal and kunci in SLOT_JADWAL:
                continue
            if kunci == "pos_submit" and not snap["auto_kirim"]:
                continue
            if kunci in slot_mati:      # v5.9: langkah yang dihapus
                continue                # tidak lagi mewajibkan posisi
            if not snap["posisi"].get(kunci):
                messagebox.showwarning(
                    APP_NAME,
                    "Posisi {} belum diatur.\n\n"
                    "Klik barisnya di tabel LANGKAH MAKRO, lalu klik "
                    "AMBIL (atau isi X,Y manual).".format(label))
                return
        # ---- v4.2: validasi salinan langkah (posisi boleh kosong) ----
        # v5.5: langkah gaya Studio dilewati dengan pesan bila tak lengkap
        kosong = [str(e.get("label") or e.get("uid"))
                  for e in snap["langkah_extra"]
                  if not e.get("jenis") and not e.get("posisi")]
        if kosong:
            if not messagebox.askyesno(
                    APP_NAME,
                    "Ada salinan langkah yang posisinya belum diatur:\n- "
                    + "\n- ".join(kosong)
                    + "\n\nLanjut saja? (salinan itu dilewati saat jalan)"):
                return
        # ---- v4.2: validasi pencarian gambar per langkah ----
        def _aktif_gambar(cfg):
            return bool(cfg and cfg.get("aktif"))
        ada_gambar = any(_aktif_gambar(c)
                         for c in snap["gambar_langkah"].values())
        ada_gambar = ada_gambar or any(
            _aktif_gambar(e.get("gambar"))
            for e in snap["langkah_extra"] if not e.get("jenis"))
        # v5.5: langkah CARI GAMBAR gaya Studio juga butuh opencv
        ada_gambar = ada_gambar or any(
            e.get("jenis") == "GAMBAR"
            for e in snap["langkah_extra"])
        if ada_gambar:
            if not CV_OK:
                if not messagebox.askyesno(
                        APP_NAME,
                        "opencv-python belum terpasang sehingga pencarian "
                        "gambar tidak bisa dipakai.\n\n"
                        "Lanjut dengan KLIK BIASA di semua titik?"):
                    return
                for c in snap["gambar_langkah"].values():
                    c["aktif"] = False
                for e in snap["langkah_extra"]:
                    if e.get("gambar"):
                        e["gambar"]["aktif"] = False
            else:
                rusak = []
                for k, c in snap["gambar_langkah"].items():
                    if _aktif_gambar(c):
                        p = str(c.get("path") or "")
                        if not p or not os.path.isfile(p):
                            rusak.append(LABEL_POSISI.get(k, k))
                for e in snap["langkah_extra"]:
                    if e.get("jenis") == "GAMBAR":
                        p = str((e.get("gambar") or {}).get("path") or "")
                        if not p or not os.path.isfile(p):
                            rusak.append(str(e.get("label")
                                             or e.get("uid")))
                    elif _aktif_gambar(e.get("gambar")):
                        p = str((e.get("gambar") or {}).get("path") or "")
                        if not p or not os.path.isfile(p):
                            rusak.append(str(e.get("label")
                                             or e.get("uid")))
                if rusak:
                    messagebox.showwarning(
                        APP_NAME,
                        "Pencarian gambar aktif tapi file gambarnya tidak "
                        "ditemukan pada langkah:\n- "
                        + "\n- ".join(rusak)
                        + "\n\nPilih ulang gambar (PILIH/POTONG GAMBAR) "
                          "pada langkah itu.")
                    return
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
    def _cari_gambar_langkah(self, snap, cfg, titik, jeda_dialog, nama=""):
        """Dukungan pencarian gambar opsional untuk SATU langkah.

        Kembalikan (aksi, nilai):
          ("klik", titik)  -> klik titik itu (pusat gambar ketemu /
                              fallback titik X,Y langkah)
          ("pindah", None) -> mouse sudah DIPINDAH ke gambar, TANPA klik
          ("skip", None)   -> langkah ini dilewati
          ("stop", pesan)  -> alur harus dihentikan
        """
        if not cfg or not cfg.get("aktif"):
            return "klik", titik
        if not titik:
            self._set_status("Titik acuan {} belum diatur - langkah "
                             "dilewati.".format(nama), C_ORANGE)
            return "skip", None
        path = str(cfg.get("path") or "").strip()
        if not path or not os.path.isfile(path) or not CV_OK:
            self._set_status("Cari gambar {} tidak bisa jalan (file "
                             "gambar/opencv tidak ada) - pakai klik "
                             "titik biasa.".format(nama), C_ORANGE)
            return "klik", titik
        radius = snap["radius"]
        if str(cfg.get("radius") or "").strip():
            radius = int(_angka(cfg.get("radius"), snap["radius"],
                                50, 2000))
        mirip = snap["kemiripan"]
        if str(cfg.get("mirip") or "").strip():
            mirip = _angka(cfg.get("mirip"), snap["kemiripan"], 0.5, 0.99)
        hasil = None
        pesan = ""
        for percobaan in range(1, 4):
            self._set_status(
                "Cari gambar '{}' dalam radius {} px (percobaan {}/3, "
                "multi-skala)...".format(os.path.basename(path), radius,
                                         percobaan), C_GREEN)
            hasil, pesan = cari_di_layar(path, titik[0], titik[1],
                                         radius, mirip)
            if hasil:
                break
            self._sleep(jeda_dialog)
        if hasil:
            x, y, skor = hasil
            if str(cfg.get("aksi")) == "Pindah saja":
                try:
                    self.mouse.position = (x, y)
                except Exception:
                    pass
                self._set_status(
                    "Gambar {} KETEMU di ({}, {}) - kemiripan {:.0%} - "
                    "mouse DIPINDAH tanpa klik.".format(nama, x, y, skor),
                    C_GREEN)
                return "pindah", None
            self._set_status(
                "Gambar {} KETEMU di ({}, {}) - kemiripan {:.0%} - "
                "diklik.".format(nama, x, y, skor), C_GREEN)
            return "klik", (x, y)
        # ---- gambar tidak ketemu ----
        pilihan = str(cfg.get("gagal") or "Klik titik X,Y")
        if pilihan == "Stop alur":
            return "stop", ("Dihentikan: gambar referensi {} tidak ketemu "
                            "3x. {}".format(nama, pesan))
        if pilihan == "Lewati langkah":
            self._set_status("Gambar {} tidak ketemu - langkah dilewati "
                             "({}).".format(nama, pesan), C_ORANGE)
            return "skip", None
        self._set_status("Gambar {} tidak ketemu - pakai klik titik X,Y "
                         "({}).".format(nama, pesan), C_ORANGE)
        return "klik", titik

    def _langkah_klik(self, snap, kunci, titik, jeda_dialog, geser=0,
                      cfg=None, nama=""):
        """Klik satu titik dengan pencarian gambar opsional.

        Kembalikan (aksi, nilai):
          ("klik", titik)  - titik sudah DIKLIK (bila titik valid)
          ("pindah", None) - mouse dipindah, TIDAK diklik
          ("skip", None)   - langkah dilewati
          ("stop", pesan)  - alur dihentikan (status sudah diset)
        """
        # v5.9: langkah bawaan yang DIHAPUS user (slot_mati) dilewati
        # tanpa diklik - aksi lanjutan blok itu (ketik tanggal, Shift+
        # panah, dll) ikut aman karena semuanya menunggu aksi "klik"
        if kunci in (snap.get("slot_mati") or ()):
            self._set_status("Langkah {} DILEWATI (sudah dihapus dari "
                             "alur).".format(nama or kunci), C_ORANGE)
            return "skip", None
        if cfg is None:
            cfg = snap["gambar_langkah"].get(kunci)
        aksi, nilai = self._cari_gambar_langkah(snap, cfg, titik,
                                                jeda_dialog, nama)
        if aksi == "stop":
            self._finish(str(nilai), warn=True)
            return "stop", nilai
        if aksi in ("pindah", "skip"):
            return aksi, None
        if nilai is None:
            return "skip", None
        self._klik_off(nilai, geser)
        return "klik", nilai

    def _ekstra_setelah(self, ekstra_all, anchor):
        """Salinan langkah yang menempel setelah `anchor` (berantai)."""
        hasil = []

        def walk(a):
            for e in ekstra_all:
                if e.get("setelah") == a and e not in hasil:
                    hasil.append(e)
                    walk(e.get("uid"))

        walk(anchor)
        return hasil

    def _jalankan_ekstra(self, snap, daftar, jumlah, jeda_dialog,
                         jeda_langkah, geser=0, caption_final=None,
                         idx_caption=0, daftar_caption=None):
        """Jalankan salinan langkah + LANGKAH STUDIO (v5.5) sesuai jenis.

        v5.5: rantai bisa berisi langkah gaya Studio Makro (KLIK,
        JEDA, CARI GAMBAR, KETIK, TANGGAL-JAM, VIDEO+CAPTION, TOMBOL,
        SCROLL, CATATAN) dan blok ULANGI-MULAI ... ULANGI-AKHIR yang
        mengulang sepotong rantai di antaranya.
        """
        if not daftar:
            return
        ctx = {
            "caption": snap.get("caption", ""),
            "videos": list(daftar_caption or []),
            "jumlah": int(jumlah),
            "tanggal": str(snap.get("tanggal") or ""),
            "caption_final": caption_final,
            "geser": int(geser or 0),
            "idx_caption": int(idx_caption or 0),
        }
        loop_stack = []
        i = 0
        aman = 0
        n = len(daftar)
        while i < n:
            if self.stop_event.is_set():
                return
            aman += 1
            if aman > 200000:
                self.stop_event.set()
                self._finish("Dihentikan: rantai langkah tambahan terlalu "
                             "panjang (kemungkinan ULANGI tanpa akhir).",
                             warn=True)
                return
            ek = daftar[i]
            jenis = str(ek.get("jenis") or "")
            if jenis == "LOOP_MULAI":
                if ek.get("ikut_video"):
                    n_loop = len(ctx["videos"]) or int(ctx["jumlah"])
                else:
                    n_loop = int(_angka(ek.get("jumlah_loop"), 2, 0,
                                        100000))
                if n_loop <= 0:
                    j = cari_akhir_loop(daftar, i)
                    i = (j + 1) if j >= 0 else i + 1
                    continue
                loop_stack.append({"mulai": i, "sisa": n_loop, "idx": 0})
                i += 1
                continue
            if jenis == "LOOP_AKHIR":
                if loop_stack:
                    top = loop_stack[-1]
                    top["sisa"] -= 1
                    top["idx"] += 1
                    if top["sisa"] > 0:
                        i = top["mulai"] + 1
                        continue
                    loop_stack.pop()
                i += 1
                continue
            if jenis in JENIS_STUDIO:
                self._eksekusi_studio(ek, ctx, loop_stack)
                i += 1
                continue
            # ---- salinan lama (posisi + aksi per jenis slot) ----
            nama = str(ek.get("label") or ek.get("uid"))
            kind = str(ek.get("sumber") or "")
            titik = ek.get("posisi")
            if not titik:
                self._set_status("{} dilewati (posisi belum diatur)."
                                 .format(nama), C_ORANGE)
                i += 1
                continue
            self._sleep(max(0.0, float(ek.get("jeda", 1.0))))
            params = ek.get("params") or {}
            aksi, _nil = self._langkah_klik(
                snap, None, titik, jeda_dialog, geser=geser,
                cfg=ek.get("gambar") or {}, nama=nama)
            if aksi == "stop":
                self.stop_event.set()
                return
            if aksi in ("pindah", "skip"):
                i += 1
                continue
            jk_e = max(0.05, float(ek.get("jeda_klik", 0.3)))
            # klik pertama sudah dilakukan -> aksi tambahan per jenis:
            if kind == "pos_tanggal":
                time.sleep(0.3)
                with self.kb.pressed(Key.ctrl):
                    self.kb.press("a")
                    self.kb.release("a")
                time.sleep(0.15)
                self.kb.type(str(params.get("teks") or snap["tanggal"]))
            elif kind == "pos_bebas1":
                sisa = int(_angka(params.get("klik"), 1, 0, 500)) - 1
                for _ in range(max(0, sisa)):
                    if self.stop_event.is_set():
                        break
                    self._klik(titik)
                    time.sleep(jk_e)
                n_scroll = int(_angka(params.get("scroll"), 0, 0, 50))
                arah = -3 if snap["arah_scroll"] == "Naik" else 3
                for _ in range(n_scroll):
                    if self.stop_event.is_set():
                        break
                    try:
                        self.mouse.scroll(0, arah)
                    except Exception:
                        pass
                    time.sleep(jk_e)
            elif kind == "pos_video":
                if jumlah > 1:
                    time.sleep(0.3)
                    jeda_panah = max(0.05, jk_e)
                    with self.kb.pressed(Key.shift):
                        for _ in range(jumlah - 1):
                            self.kb.press(Key.down)
                            self.kb.release(Key.down)
                            time.sleep(jeda_panah)
            elif kind == "pos_bebas2":
                sisa = int(_angka(params.get("klik"), 1, 0, 20)) - 1
                for _ in range(max(0, sisa)):
                    if self.stop_event.is_set():
                        break
                    self._klik(titik)
                    time.sleep(jk_e)
            elif kind == "pos_submit":
                sisa = int(_angka(params.get("klik"), 1, 1, 10)) - 1
                for _ in range(max(0, sisa)):
                    if self.stop_event.is_set():
                        break
                    self._klik(titik)
                    time.sleep(jk_e)
            elif kind == "pos_judul" and caption_final:
                time.sleep(0.3)
                with self.kb.pressed(Key.ctrl):
                    self.kb.press("a")
                    self.kb.release("a")
                time.sleep(0.15)
                self.kb.type(caption_final)
            self._sleep(jeda_langkah)
            i += 1

    def _eksekusi_studio(self, l, ctx, loop_stack):
        """v5.5: jalankan satu langkah gaya Studio dalam alur A-J."""
        if not l.get("aktif", True):
            return
        idx = loop_stack[-1]["idx"] if loop_stack \
            else int(ctx.get("idx_caption") or 0)
        hasil = studio_jalankan_langkah(
            self, l, idx, ctx.get("videos") or [],
            ctx.get("caption") or "", ctx.get("jumlah") or 0,
            ctx.get("tanggal") or "",
            geser_baris=int(ctx.get("geser") or 0))
        if hasil == "stop":
            # pastikan alur utama ikut berhenti (CARI GAMBAR gagal)
            self.stop_event.set()

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
            ekstra_all = [e for e in (snap.get("langkah_extra") or [])
                          if isinstance(e, dict)]

            def ekstra_setelah(anchor):
                return self._ekstra_setelah(ekstra_all, anchor)

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
                    aksi, _nil = self._langkah_klik(
                        snap, "pos_jadwal", pos["pos_jadwal"], jeda_dialog,
                        nama="A (jadwal rilis)")
                    if aksi == "stop":
                        return
                    self._jalankan_ekstra(snap, ekstra_setelah("pos_jadwal"),
                                          jumlah, jeda_dialog, jeda_langkah)
                    self._sleep(jeda_dialog)

                    if self.stop_event.is_set():
                        self._finish("Dihentikan saat fase jadwal.",
                                     warn=True)
                        return
                    self._set_status("Klik dropdown 'NEGARA'...", C_GREEN)
                    aksi, _nil = self._langkah_klik(
                        snap, "pos_negara", pos["pos_negara"], jeda_dialog,
                        nama="B (dropdown negara)")
                    if aksi == "stop":
                        return
                    self._jalankan_ekstra(snap, ekstra_setelah("pos_negara"),
                                          jumlah, jeda_dialog, jeda_langkah)
                    self._sleep(jeda_dialog)

                    # ---- C: pilih negara ----
                    if self.stop_event.is_set():
                        self._finish("Dihentikan sebelum memilih negara.",
                                     warn=True)
                        return
                    aksi, _nil = self._langkah_klik(
                        snap, "pos_pilih_neg", pos["pos_pilih_neg"],
                        jeda_dialog, nama="C (pilih negara)")
                    if aksi == "stop":
                        return
                    self._jalankan_ekstra(
                        snap, ekstra_setelah("pos_pilih_neg"),
                        jumlah, jeda_dialog, jeda_langkah)
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
                    aksi, _nil = self._langkah_klik(
                        snap, "pos_tanggal", pos["pos_tanggal"], jeda_dialog,
                        nama="D (kolom tanggal)")
                    if aksi == "stop":
                        return
                    if aksi == "klik":
                        time.sleep(0.3)
                        with self.kb.pressed(Key.ctrl):
                            self.kb.press("a")
                            self.kb.release("a")
                        time.sleep(0.15)
                        self.kb.type(snap["tanggal"])
                    self._jalankan_ekstra(snap, ekstra_setelah("pos_tanggal"),
                                          jumlah, jeda_dialog, jeda_langkah)
                    self._sleep(max(0.0, jp.get("pos_tanggal",
                                                jeda_langkah)))

                    # ---- E: OKE ----
                    if self.stop_event.is_set():
                        self._finish("Dihentikan sebelum klik OKE.",
                                     warn=True)
                        return
                    self._set_status("Klik 'OKE'...", C_GREEN)
                    aksi, _nil = self._langkah_klik(
                        snap, "pos_oke", pos["pos_oke"], jeda_dialog,
                        nama="E (tombol OKE)")
                    if aksi == "stop":
                        return
                    self._jalankan_ekstra(snap, ekstra_setelah("pos_oke"),
                                          jumlah, jeda_dialog, jeda_langkah)
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
                aksi, _nil = self._langkah_klik(
                    snap, "pos_tambah", pos["pos_tambah"], jeda_dialog,
                    nama="F (tambah video)")
                if aksi == "stop":
                    return
                self._jalankan_ekstra(snap, ekstra_setelah("pos_tambah"),
                                      jumlah, jeda_dialog, jeda_langkah)
                self._sleep(jeda_dialog)

                # ---- G: klik bebas 1 + scroll ----
                if self.stop_event.is_set():
                    self._finish(
                        "Dihentikan setelah 'Tambah video'. Video belum "
                        "masuk - aman diulang dari awal.", warn=True)
                    return
                n_klik1 = snap["klik_bebas1"]
                n_scroll = snap["scroll_bebas1"]
                # v5.9: langkah G dihapus -> klik DAN scroll-nya skip
                if "pos_bebas1" in (snap.get("slot_mati") or ()):
                    n_klik1 = 0
                    n_scroll = 0
                if n_klik1 or n_scroll:
                    self._set_status(
                        "Klik bebas {}x + scroll {}x ({})...".format(
                            n_klik1, n_scroll, snap["arah_scroll"]),
                        C_GREEN)
                    arah = -3 if snap["arah_scroll"] == "Naik" else 3
                    sisa1 = 0
                    if n_klik1:
                        aksi, _nil = self._langkah_klik(
                            snap, "pos_bebas1", pos["pos_bebas1"],
                            jeda_dialog, nama="G (klik bebas 1)")
                        if aksi == "stop":
                            return
                        if aksi == "klik":
                            sisa1 = n_klik1 - 1
                    for _ in range(sisa1):
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
                # v5.5: langkah tambahan setelah G tetap jalan walau
                # jumlah klik/scroll G = 0
                self._jalankan_ekstra(
                    snap, ekstra_setelah("pos_bebas1"), jumlah,
                    jeda_dialog, jeda_langkah)
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
                aksi, _nil = self._langkah_klik(
                    snap, "pos_video", pos["pos_video"], jeda_dialog,
                    nama="H (video pertama)")
                if aksi == "stop":
                    return
                if aksi == "klik" and jumlah > 1:
                    time.sleep(0.3)
                    jeda_panah = max(0.05, jk.get("pos_video", 0.15))
                    with self.kb.pressed(Key.shift):
                        for _ in range(jumlah - 1):
                            self.kb.press(Key.down)
                            self.kb.release(Key.down)
                            time.sleep(jeda_panah)
                self._jalankan_ekstra(snap, ekstra_setelah("pos_video"),
                                      jumlah, jeda_dialog, jeda_langkah)
                self._sleep(max(0.0, jp.get("pos_video", jeda_langkah)))

                # ---- H2: klik bebas 2 (tombol Buka) ----
                if self.stop_event.is_set():
                    self._finish("Dihentikan sebelum klik Buka.",
                                 warn=True)
                    return
                self._set_status(
                    "Klik bebas {}x (tombol 'Buka')...".format(
                        snap["klik_bebas2"]), C_GREEN)
                sisa2 = 0
                if snap["klik_bebas2"]:
                    aksi, _nil = self._langkah_klik(
                        snap, "pos_bebas2", pos["pos_bebas2"], jeda_dialog,
                        nama="H2 (klik bebas 2)")
                    if aksi == "stop":
                        return
                    if aksi == "klik":
                        sisa2 = snap["klik_bebas2"] - 1
                for _ in range(sisa2):
                    if self.stop_event.is_set():
                        break
                    self._klik(pos["pos_bebas2"])
                    time.sleep(max(0.05, jk.get("pos_bebas2", 0.3)))
                self._jalankan_ekstra(snap, ekstra_setelah("pos_bebas2"),
                                      jumlah, jeda_dialog, jeda_langkah)
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
                aksi, _nil = self._langkah_klik(
                    snap, "pos_edit", pos["pos_edit"], jeda_dialog,
                    geser=geser, nama="I1 (Edit)")
                if aksi == "stop":
                    return
                self._jalankan_ekstra(snap, ekstra_setelah("pos_edit"),
                                      jumlah, jeda_dialog, jeda_langkah,
                                      geser=geser,
                                      idx_caption=i,
                                      daftar_caption=daftar_caption)
                self._sleep(jeda_dialog)

                # klik kotak caption baris ke-i + ketik caption
                if self.stop_event.is_set():
                    break
                self._set_status(
                    "[{}/{}] Menulis caption: {}".format(
                        i + 1, n_cap, caption_final), C_GREEN)
                aksi, _nil = self._langkah_klik(
                    snap, "pos_judul", pos["pos_judul"], jeda_dialog,
                    geser=geser, nama="I2 (kotak caption)")
                if aksi == "stop":
                    return
                if aksi == "klik":
                    time.sleep(0.3)
                    with self.kb.pressed(Key.ctrl):
                        self.kb.press("a")
                        self.kb.release("a")
                    time.sleep(0.15)
                    self.kb.type(caption_final)
                self._jalankan_ekstra(snap, ekstra_setelah("pos_judul"),
                                      jumlah, jeda_dialog, jeda_langkah,
                                      geser=geser,
                                      caption_final=caption_final,
                                      idx_caption=i,
                                      daftar_caption=daftar_caption)
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
                aksi, _nil = self._langkah_klik(
                    snap, "pos_konfirmasi", titik_ok, jeda_dialog,
                    geser=geser, nama="I3 (Konfirmasi)")
                if aksi == "stop":
                    return
                self._jalankan_ekstra(snap, ekstra_setelah("pos_konfirmasi"),
                                      jumlah, jeda_dialog, jeda_langkah,
                                      geser=geser,
                                      idx_caption=i,
                                      daftar_caption=daftar_caption)
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
                aksi, titik_j = self._langkah_klik(
                    snap, "pos_submit", pos["pos_submit"], jeda_dialog,
                    nama="J (Submit)")
                if aksi == "stop":
                    return
                if aksi == "klik":
                    for _ in range(snap["klik_submit"] - 1):
                        if self.stop_event.is_set():
                            break
                        self._klik(titik_j)
                        time.sleep(max(0.05, jk.get("pos_submit", 0.3)))
                self._jalankan_ekstra(snap, ekstra_setelah("pos_submit"),
                                      jumlah, jeda_dialog, jeda_langkah)
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
            "slot_mati": sorted(self.slot_mati),   # v5.9: A-J dihapus
            "jeda_per": {k: float(v) for k, v in self.jeda_per.items()},
            "jeda_klik_per": {k: float(v)
                              for k, v in self.jeda_klik_per.items()},
            "gambar_langkah": {k: dict(v)
                               for k, v in self.gambar_langkah.items()},
            "langkah_extra": [
                json.loads(json.dumps(e)) if isinstance(e, dict) else e
                for e in self.langkah_extra],
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
        # ---- v4.2: config pencarian gambar per langkah ----
        gl_baru = {k: gambar_langkah_default() for k in POS_KUNCI}
        simpan_gl = data.get("gambar_langkah")
        for k, v in (simpan_gl or {}).items():
            if k in gl_baru and isinstance(v, dict):
                c = gl_baru[k]
                c["aktif"] = bool(v.get("aktif"))
                c["path"] = str(v.get("path") or "")
                c["aksi"] = (str(v.get("aksi"))
                             if str(v.get("aksi")) in GAMBAR_AKSI_OPSI
                             else "Klik di gambar")
                c["gagal"] = (str(v.get("gagal"))
                              if str(v.get("gagal")) in GAMBAR_GAGAL_OPSI
                              else "Klik titik X,Y")
                c["radius"] = str(v.get("radius") or "")
                c["mirip"] = str(v.get("mirip") or "")
        # migrasi v4.1 -> v4.2: checkbox C global jadi config langkah C
        if data.get("pakai_gambar") and not simpan_gl:
            gl_baru["pos_pilih_neg"].update(
                {"aktif": True,
                 "path": str(data.get("gambar_ref") or "")})
        self.gambar_langkah = gl_baru
        # ---- v4.2: salinan langkah + v5.5: langkah gaya Studio ----
        ekstra_baru = []
        for e in (data.get("langkah_extra") or []):
            if not isinstance(e, dict):
                continue
            jenis_e = str(e.get("jenis") or "")
            if jenis_e in JENIS_STUDIO:
                # v5.5: langkah gaya Studio - sanitasi via studio_bersihkan
                bersih = studio_bersihkan([e])
                if not bersih:
                    continue
                st = bersih[0]
                st["uid"] = str(e.get("uid") or "x{}".format(
                    len(ekstra_baru) + 1))
                st["setelah"] = str(e.get("setelah") or "pos_jadwal")
                st["label"] = str(e.get("label") or st.get("nama")
                                  or LABEL_JENIS[jenis_e])
                ekstra_baru.append(st)
                continue
            sumber = str(e.get("sumber") or "")
            if sumber not in POS_KUNCI:
                continue
            p = e.get("posisi")
            try:
                pos_e = [int(p[0]), int(p[1])] if p else None
            except Exception:
                pos_e = None
            gambar_e = gambar_langkah_default()
            g = e.get("gambar")
            if isinstance(g, dict):
                gambar_e["aktif"] = bool(g.get("aktif"))
                gambar_e["path"] = str(g.get("path") or "")
                gambar_e["aksi"] = (str(g.get("aksi"))
                                    if str(g.get("aksi"))
                                    in GAMBAR_AKSI_OPSI
                                    else "Klik di gambar")
                gambar_e["gagal"] = (str(g.get("gagal"))
                                     if str(g.get("gagal"))
                                     in GAMBAR_GAGAL_OPSI
                                     else "Klik titik X,Y")
                gambar_e["radius"] = str(g.get("radius") or "")
                gambar_e["mirip"] = str(g.get("mirip") or "")
            params_e = {}
            for nama_p, _l, _w in PARAM_DEF.get(sumber, []):
                v_p = (e.get("params") or {}).get(nama_p)
                params_e[nama_p] = (str(v_p) if v_p is not None
                                    else PARAM_BAWAAN.get(nama_p, ""))
            uid = str(e.get("uid") or "x{}".format(len(ekstra_baru) + 1))
            ekstra_baru.append({
                "uid": uid,
                "sumber": sumber,
                "setelah": str(e.get("setelah") or sumber),
                "label": str(e.get("label") or (SLOT_KODE.get(
                    sumber, sumber) + " - salinan")),
                "posisi": pos_e,
                "jeda": _angka(e.get("jeda"), 1.0, 0.0, 3600),
                "jeda_klik": _angka(e.get("jeda_klik"), 0.3, 0.05, 60),
                "params": params_e,
                "gambar": gambar_e,
            })
        self.langkah_extra = ekstra_baru
        # v5.8: sembuhkan profil lama ber-uid DOBEL lalu lanjutkan
        # nomor dari uid TERBESAR. Dulu: _extra_counter = jumlah
        # langkah - setelah hapus langkah (apalagi hapus massal v5.7)
        # lalu buka ulang aplikasi, nomor langkah baru bisa MENABRAK
        # uid lama sehingga CARI GAMBAR / langkah tambahan baru tidak
        # muncul di tabel (kelihatannya "hanya bisa ditambah 2x").
        terlihat = set()
        for x in ekstra_baru:
            u = str(x.get("uid") or "")
            if not u or u in terlihat:
                while True:
                    self._extra_counter += 1
                    u = "x{}".format(self._extra_counter)
                    if not any(str(y.get("uid")) == u
                               for y in ekstra_baru):
                        break
                x["uid"] = u
            terlihat.add(u)
        maks_x = len(ekstra_baru)
        for x in ekstra_baru:
            u = str(x.get("uid") or "")
            if u[:1] == "x" and u[1:].isdigit():
                maks_x = max(maks_x, int(u[1:]))
        self._extra_counter = maks_x
        self._studio_counter = sum(
            1 for x in ekstra_baru if x.get("jenis") in JENIS_STUDIO)
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
        # v5.9: kolom angka disanitasi saat dimuat - nilai rusak dari
        # profil lama dibuang (kembali ke bawaan) sehingga F6 tidak
        # lagi menabrak error "harus diisi angka" tanpa sebab jelas
        ANGKA_VAR = ("jumlah", "mundur", "jeda_dialog", "jeda_langkah",
                     "tunggu", "radius", "kemiripan", "klik_bebas1",
                     "scroll_bebas1", "klik_bebas2", "jarak_baris",
                     "klik_submit")
        for key, var in pasangan:
            val = data.get(key)
            if val is None:
                continue
            val = str(val)
            if key in ANGKA_VAR and val.strip():
                try:
                    float(val.strip().replace(",", "."))
                except ValueError:
                    continue        # nilai rusak -> pakai bawaan saja
            var.set(val)
        # v5.9: langkah bawaan A-J yang sempat dihapus (bisa jalan lagi)
        self.slot_mati = set(
            str(k) for k in (data.get("slot_mati") or ())
            if str(k) in POS_KUNCI)
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
            if self.shell is self:
                if PYNPUT_OK and hasattr(self, "_listener"):
                    self._listener.stop()
                self.root.destroy()
        except Exception:
            pass

    def antrian_video_studio(self):
        """Daftar video (urut A-Z, hormati skip & jumlah) untuk Studio.

        Dipakai placeholder {caption}/{video} pada blok ULANGI di
        STUDIO MAKRO - urutannya sama dengan baris video di situs.
        """
        semua = daftar_video(self.vars["folder"].get().strip())
        if self.vars["skip_uploaded"].get():
            sudah = self._riwayat_folder()
            semua = [f for f in semua if f not in sudah]
        try:
            jumlah = max(1, int(self.vars["jumlah"].get()))
        except ValueError:
            jumlah = len(semua) or 1
        return semua[:jumlah]


# ============================================================
# v5.0 - TAB STUDIO MAKRO (editor alur kerja bebas ala Jitbit)
# ============================================================


# ------------------------------------------------------------
# v5.4: jendela kecil melayang penanda REKAM berlangsung.
# Selalu paling atas di pojok kanan bawah, menampilkan hitungan
# aksi yang sudah terekam, bisa digeser (seretan di jendela ini
# TIDAK direkam sebagai langkah).
# ------------------------------------------------------------
class BannerRekam(tk.Toplevel):
    def __init__(self, induk):
        super().__init__(induk)
        self.overrideredirect(True)
        try:
            self.attributes("-topmost", True)
        except Exception:
            pass
        self.configure(bg="#7F1D1D")
        sw = max(1, self.winfo_screenwidth())
        sh = max(1, self.winfo_screenheight())
        self.w, self.h = 316, 116
        self.geometry("{}x{}+{}+{}".format(
            self.w, self.h, max(0, sw - self.w - 16),
            max(0, sh - self.h - 64)))
        f = tk.Frame(self, bg="#7F1D1D")
        f.pack(fill="both", expand=True, padx=10, pady=6)
        l1 = tk.Label(f, text="●  MEREKAM AKSI...", bg="#7F1D1D",
                      fg="#FCA5A5", font=("Segoe UI", 13, "bold"))
        l1.pack(anchor="w")
        self.lbl_hitung = tk.Label(
            f, text="Klik: 0   Teks/tombol: 0   Scroll: 0",
            bg="#7F1D1D", fg="white", font=("Segoe UI", 10, "bold"))
        self.lbl_hitung.pack(anchor="w", pady=(2, 0))
        l3 = tk.Label(f, text="Tekan F8 (atau ESC) untuk BERHENTI.\n"
                              "Seret jendela ini bila menghalangi.",
                      bg="#7F1D1D", fg="#FECACA", font=("Segoe UI", 8),
                      justify="left", anchor="w")
        l3.pack(anchor="w", pady=(2, 0))
        # seret jendela (seretan di sini tidak dihitung sebagai aksi)
        self._geser_awal = None
        for wdg in (self, f, l1, self.lbl_hitung, l3):
            wdg.bind("<ButtonPress-1>", self._tekan)
            wdg.bind("<B1-Motion>", self._geser)

    def _tekan(self, ev):
        self._geser_awal = (ev.x_root, ev.y_root,
                            self.winfo_x(), self.winfo_y())

    def _geser(self, ev):
        if not self._geser_awal:
            return
        dx = ev.x_root - self._geser_awal[0]
        dy = ev.y_root - self._geser_awal[1]
        self.geometry("+{}+{}".format(self._geser_awal[2] + dx,
                                      self._geser_awal[3] + dy))

    def perbarui(self, n_klik, n_teks, n_scroll):
        self.lbl_hitung.config(
            text="Klik: {}   Teks/tombol: {}   Scroll: {}".format(
                n_klik, n_teks, n_scroll))

    def tutup(self):
        try:
            self.destroy()
        except Exception:
            pass


class StudioMakroTab(PerekamAksiMixin):
    """Tab STUDIO MAKRO - susun alur kerja klik sendiri satu per satu.

    Bagian atas  : toolbar semua jenis langkah (menu aksi).
    Bagian bawah : tabel ALUR KERJA (awalnya kosong) + panel
                   PROPERTI LANGKAH sesuai jenis langkah terpilih.
    """

    def __init__(self, wadah, shell):
        self.wadah = wadah
        self.root = wadah          # untuk .after() & pemilik dialog
        self.shell = shell
        self.stop_event = threading.Event()
        self.running = False
        self.langkah = []          # daftar langkah generik (dict)
        self.papan_klip = None
        self._uid = 0
        self.sel = None
        self.makro_path = os.path.join(data_dir(), "makro_terakhir.json")
        self.pv = {}
        self._loading_prop = False
        self.lbl_ambil = None
        # v5.6: state REKAM AKSI (mesin bersama, lihat PerekamAksiMixin)
        self.perekam_init_state()

        self.vars = {"mundur": tk.StringVar(value="5")}

        if PYNPUT_OK:
            self.kb = shell.kb
            self.mouse = shell.mouse
        else:
            self.kb = None
            self.mouse = None

        self._build_ui()
        self._muat_otomatis()

    # ================== PEMBANGUNAN TAMPILAN ==================
    def _build_ui(self):
        # ----- Toolbar 1 v5.7 (kartu MEMBULAT + tombol kapsul
        #      mengkilat; tetap MAKS 7 TOMBOL per baris) -----
        tb1 = KartuBulat(self.wadah, radius=14, padding=(10, 7, 10, 8))
        tb1.pack(side="top", fill="x", padx=6, pady=(6, 2))
        tb1_r1 = tk.Frame(tb1.badan, bg=C_BG)
        tb1_r1.pack(side="top", fill="x")
        tb1_r2 = tk.Frame(tb1.badan, bg=C_BG)
        tb1_r2.pack(side="top", fill="x")
        self.btn_start = self._tb_btn(tb1_r1, "JALANKAN  (F6)",
                                      self._start,
                                      bg=C_BLUE, fg="white",
                                      aktif=C_BLUE_D)
        self.btn_stop = self._tb_btn(tb1_r1, "BERHENTI  (F7)", self._stop,
                                     bg=C_RED, fg="white",
                                     aktif=C_RED_D)
        self.btn_stop.config(state="disabled",
                             disabledforeground="#FECACA")
        # v5.4: tombol REKAM AKSI (rekam klik/ketik/scroll jadi langkah)
        self.btn_rekam = self._tb_btn(tb1_r1, "● REKAM AKSI",
                                      self._rekam_mulai,
                                      bg="#DC2626", fg="white",
                                      aktif="#EF4444")
        self._tb_pemisah(tb1_r1)
        for jenis in ("KLIK", "JEDA", "GAMBAR", "KETIK"):
            self._tb_btn(tb1_r1, LABEL_TB[jenis],
                         lambda j=jenis: self._tambah(j))
        for jenis in ("TANGGAL_JAM", "VIDEO_CAPTION", "TOMBOL",
                      "SCROLL", "CATATAN"):
            self._tb_btn(tb1_r2, LABEL_TB[jenis],
                         lambda j=jenis: self._tambah(j))
        self._tb_pemisah(tb1_r2)
        self._tb_btn(tb1_r2, "+ ULANGI MULAI",
                     lambda: self._tambah("LOOP_MULAI"))
        self._tb_btn(tb1_r2, "+ ULANGI AKHIR",
                     lambda: self._tambah("LOOP_AKHIR"))

        # ----- Toolbar 2: sunting + file + alat gambar (kartu) -----
        tb2 = KartuBulat(self.wadah, radius=14, padding=(10, 7, 10, 8))
        tb2.pack(side="top", fill="x", padx=6, pady=(2, 2))
        tb2_r1 = tk.Frame(tb2.badan, bg=C_BG)
        tb2_r1.pack(side="top", fill="x")
        tb2_r2 = tk.Frame(tb2.badan, bg=C_BG)
        tb2_r2.pack(side="top", fill="x")
        self._tb_btn(tb2_r1, "SALIN", self._salin)
        self._tb_btn(tb2_r1, "TEMPEL", self._tempel)
        self._tb_btn(tb2_r1, "HAPUS", self._hapus)
        self._tb_btn(tb2_r1, "NAIK", self._naik)
        self._tb_btn(tb2_r1, "TURUN", self._turun)
        self._tb_btn(tb2_r1, "AKTIF / MATI", self._toggle_aktif)
        self._tb_btn(tb2_r1, "SIMPAN MAKRO", self._simpan_makro)
        self._tb_btn(tb2_r2, "BUKA MAKRO", self._buka_makro)
        self._tb_btn(tb2_r2, "MAKRO BARU", self._makro_baru)
        self._tb_btn(tb2_r2, "TEMPLATE CUTMOTIONS",
                     self._template_cutmotions)
        self._tb_pemisah(tb2_r2)
        self._tb_btn(tb2_r2, "POTONG GAMBAR", self._potong_dari_menu)
        self._tb_btn(tb2_r2, "TES CARI", self._tes_cari)

        # ----- Strip mundur -----
        strip = tk.Frame(self.wadah, bg=C_BG)
        strip.pack(side="top", fill="x", padx=8, pady=(4, 0))
        tk.Label(strip, text="MUNDUR SEBELUM MULAI (detik):", bg=C_BG,
                 fg=C_MUTED, font=F_XS).pack(side="left")
        tk.Entry(strip, textvariable=self.vars["mundur"], width=4,
                 bg=C_PANEL, fg=C_TEXT, relief="solid", bd=1, font=F_N,
                 justify="center",
                 highlightthickness=0).pack(side="left", padx=(4, 10),
                                            ipady=2)
        tk.Label(strip, text="Jeda setiap langkah diatur lewat kolom JEDA "
                             "/ panel PROPERTI.  Klik kanan baris = "
                             "salin/tempel/hapus/urutkan.  Tahan "
                             "CTRL/SHIFT saat klik = PILIH BANYAK "
                             "langkah (Ctrl+A = semua).  "
                             "● REKAM AKSI = klik/ketikan/scrollmu "
                             "direkam otomatis jadi langkah (F8 = "
                             "berhenti).",
                 bg=C_BG, fg=C_MUTED, font=F_XS).pack(side="left")

        # ----- Area tengah: tabel alur kerja + panel properti -----
        paned = tk.PanedWindow(self.wadah, orient="vertical",
                               sashwidth=5, bg=C_LINE, bd=0)
        paned.pack(side="top", fill="both", expand=True, padx=8, pady=4)

        # ---- tabel alur kerja (v5.7: kartu membulat + MULTI-PILIH:
        #      Ctrl+Klik / Shift+Klik / Ctrl+A) ----
        f_tb = KartuBulat(
            paned,
            judul="ALUR KERJA MAKRO - tahan CTRL/SHIFT saat klik "
                  "untuk PILIH BANYAK langkah sekaligus",
            padding=(8, 5, 8, 6))
        paned.add(f_tb, minsize=260, height=340, stretch="always")
        kolom = ("no", "nama", "detail", "jeda", "ulang")
        self.tree = ttk.Treeview(f_tb.badan, columns=kolom,
                                 show="headings",
                                 style="Makro.Treeview",
                                 selectmode="extended")
        for k, t, w_, a in [
            ("no", "#", 44, "center"),
            ("nama", "LANGKAH", 215, "w"),
            ("detail", "PARAMETER", 330, "w"),
            ("jeda", "JEDA", 62, "center"),
            ("ulang", "ULANGI", 170, "w"),
        ]:
            self.tree.heading(k, text=t)
            self.tree.column(k, width=w_, anchor=a,
                             stretch=(k == "detail"))
        vsb = ttk.Scrollbar(f_tb.badan, orient="vertical",
                            command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        # warna per jenis langkah
        self.tree.tag_configure("genap", background=C_STRIPE)
        self.tree.tag_configure("ganjil", background=C_PANEL)
        self.tree.tag_configure("tklik", foreground=C_TEXT)
        self.tree.tag_configure("tjeda", foreground=C_ORANGE)
        self.tree.tag_configure("tgambar", foreground=C_BLUE)
        self.tree.tag_configure("tketik", foreground=C_GREEN)
        self.tree.tag_configure("ttombol", foreground=C_UNGU)
        self.tree.tag_configure("tscroll", foreground=C_TEAL)
        self.tree.tag_configure("tcatatan", foreground=C_MUTED)
        self.tree.tag_configure("tloop", foreground=C_UNGU, font=F_H)
        self.tree.tag_configure("off", foreground="#A4A8AE")
        self.tree.bind("<<TreeviewSelect>>", self._on_pilih_baris)
        self.tree.bind("<Control-c>", lambda _e: self._salin())
        self.tree.bind("<Control-v>", lambda _e: self._tempel())
        self.tree.bind("<Delete>", lambda _e: self._hapus())
        self.tree.bind("<Control-a>", self._pilih_semua)
        self.tree.bind("<Button-3>", self._menu_klik_kanan)

        self.f_prop = KartuBulat(paned, judul="PROPERTI LANGKAH",
                                 padding=(8, 5, 8, 6))
        paned.add(self.f_prop, minsize=220, height=250, stretch="always")
        self.prop_body = tk.Frame(self.f_prop.badan, bg=C_BG)
        self.prop_body.pack(fill="both", expand=True)

    # ---------- pembantu tampilan ----------
    def _tb_btn(self, parent, teks, cmd, bg=None, fg=None, aktif=None):
        # v5.7: tombol kapsul membulat menggantikan tk.Button datar
        b = TombolKapsul(parent, teks=teks, perintah=cmd,
                         bg=bg or C_PANEL2, fg=fg or C_TEXT)
        b.pack(side="left", padx=3, pady=2)
        return b

    def _pilih_semua(self, _ev=None):
        """v5.7: Ctrl+A - pilih semua baris di tabel."""
        semua = self.tree.get_children()
        if semua:
            self.tree.selection_set(semua)
        return "break"

    def _tb_pemisah(self, parent):
        tk.Frame(parent, bg=C_LINE, width=2).pack(side="left", fill="y",
                                                  padx=4, pady=4)

    def _baris_prop(self, label, lebar_label=30):
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

    def _tampilkan_info(self, teks, warna=C_ORANGE):
        if self.lbl_ambil is not None and self.lbl_ambil.winfo_exists():
            self.lbl_ambil.config(text=teks, fg=warna)

    # ================== BANTUAN STATUS (thread-safe) ==================
    def _set_status(self, msg, color=C_GREEN):
        def do():
            try:
                self.shell.lbl_status.config(text=msg, fg=color)
            except Exception:
                pass
        self.root.after(0, do)

    def _set_progress(self, msg):
        self._set_status(msg, C_BLUE)

    def _sleep(self, seconds):
        """Tidur yang bisa dibatalkan kapan saja lewat tombol stop."""
        end = time.time() + seconds
        while not self.stop_event.is_set():
            remain = end - time.time()
            if remain <= 0:
                break
            time.sleep(min(0.05, remain))

    # ================== TABEL ALUR KERJA ==================
    def _uid_baru(self):
        self._uid += 1
        return self._uid

    def _get(self, uid):
        if not uid:
            return None
        for l in self.langkah:
            if l.get("uid") == uid:
                return l
        return None

    def _idx_of(self, uid):
        for i, l in enumerate(self.langkah):
            if l.get("uid") == uid:
                return i
        return None

    def _detail_langkah(self, l):
        return studio_detail_teks(l)

    def _ulang_langkah(self, l):
        return studio_ulang_teks(l)

    def _refresh_tabel(self):
        if not hasattr(self, "tree"):
            return
        anak = self.tree.get_children()
        if anak:
            self.tree.delete(*anak)
        for i, l in enumerate(self.langkah):
            jenis = l["jenis"]
            nama = str(l.get("nama") or "") or LABEL_JENIS[jenis]
            if jenis == "CATATAN" and not l.get("nama"):
                nama = "CATATAN"
            aktif = bool(l.get("aktif", True))
            if not aktif:
                nama = "(nonaktif) " + nama
            detail = self._detail_langkah(l)
            jeda_t = "{:.1f}s".format(_angka(l.get("jeda"), 0.5, 0,
                                             86400))
            tag = {"KLIK": "tklik", "GAMBAR": "tgambar", "KETIK": "tketik",
                   "TANGGAL_JAM": "tketik", "VIDEO_CAPTION": "tketik",
                   "TOMBOL": "ttombol", "SCROLL": "tscroll",
                   "CATATAN": "tcatatan", "JEDA": "tjeda",
                   "LOOP_MULAI": "tloop", "LOOP_AKHIR": "tloop"}.get(
                       jenis, "tklik")
            if not aktif:
                tag = "off"
            zebra = "genap" if i % 2 == 0 else "ganjil"
            self.tree.insert("", "end", iid=l["uid"], tags=(tag, zebra),
                             values=(i + 1, nama, detail, jeda_t,
                                     self._ulang_langkah(l)))
        if self.sel and self.tree.exists(self.sel):
            try:
                # hindari selection_set bila seleksi sudah tepat -
                # event <<TreeviewSelect>> akan memicu render ulang
                # panel properti DI TENGAH user mengetik (bug UX)
                if tuple(self.tree.selection()) != (self.sel,):
                    self.tree.selection_set(self.sel)
                self.tree.see(self.sel)
            except Exception:
                pass
        self._simpan_auto()

    def _on_pilih_baris(self, _ev=None):
        sel = self.tree.selection()
        if sel:
            self.sel = sel[0]
            self._render_properti()

    # ================== TAMBAH / SUNTING LANGKAH ==================
    def _tambah(self, jenis):
        l = studio_langkah_baru(jenis, self._uid_baru())
        i = self._idx_of(self.sel)
        if i is None:
            self.langkah.append(l)
        else:
            self.langkah.insert(i + 1, l)
        self.sel = l["uid"]
        self._refresh_tabel()
        try:
            self.tree.selection_set(l["uid"])
            self.tree.see(l["uid"])
        except Exception:
            pass
        self._render_properti()
        self._set_status("Langkah {} ditambahkan - atur di panel "
                         "PROPERTI LANGKAH di bawah.".format(
                             LABEL_JENIS[jenis]), C_GREEN)

    def _salin(self):
        """v5.7: salin SEMUA langkah terpilih (urut tampil)."""
        pilih = [self._get(u) for u in self.tree.selection()]
        pilih = [l for l in pilih if l]
        if not pilih:
            l = self._get(self.sel)
            pilih = [l] if l else []
        if not pilih:
            messagebox.showinfo(
                APP_NAME,
                "Klik dulu satu baris langkah yang mau disalin.\n\n"
                "Tahan CTRL atau SHIFT saat mengklik untuk memilih "
                "BANYAK langkah sekaligus (Ctrl+A = semua).")
            return
        self.papan_klip = {"banyak": [json.loads(json.dumps(l))
                                      for l in pilih]}
        self._set_status("{} langkah disalin - klik baris tujuan lalu "
                         "TEMPEL (Ctrl+V).".format(len(pilih)), C_GREEN)

    def _tempel(self):
        """v5.7: tempel 1 ATAU BANYAK salinan berurutan setelah acuan."""
        klip = self.papan_klip
        if not klip:
            messagebox.showinfo(APP_NAME, "Belum ada langkah yang "
                                          "disalin.\n\nKlik satu baris "
                                          "lalu SALIN (Ctrl+C) dulu.")
            return
        items = klip.get("banyak") or [klip]
        i = self._idx_of(self.sel)
        dipaste = []
        for it in items:
            baru = json.loads(json.dumps(it))
            baru["uid"] = "s{}".format(self._uid_baru())
            if i is None:
                self.langkah.append(baru)
            else:
                self.langkah.insert(i + 1, baru)
                i += 1
            dipaste.append(baru["uid"])
        self.sel = dipaste[-1]
        self._refresh_tabel()
        try:
            self.tree.selection_set(*dipaste)
            self.tree.see(self.sel)
        except Exception:
            pass
        self._render_properti()
        self._set_status("{} langkah ditempel berurutan - semua "
                         "parameternya ikut tersalin, silakan "
                         "disunting.".format(len(dipaste)), C_GREEN)

    def _hapus(self):
        """v5.7: hapus SEMUA langkah terpilih sekaligus."""
        pilih = [self._get(u) for u in self.tree.selection()]
        pilih = [l for l in pilih if l]
        if not pilih:
            l = self._get(self.sel)
            pilih = [l] if l else []
        if not pilih:
            messagebox.showinfo(
                APP_NAME,
                "Pilih dulu baris langkah yang mau dihapus.\n\n"
                "Tahan CTRL/SHIFT saat mengklik untuk menghapus "
                "BANYAK langkah sekaligus.")
            return
        if len(pilih) == 1:
            pesan = "Hapus langkah '{}'?".format(
                pilih[0].get("nama") or LABEL_JENIS[pilih[0]["jenis"]])
        else:
            pesan = ("Hapus {} langkah terpilih sekaligus?".format(
                len(pilih)))
        if not messagebox.askyesno(APP_NAME, pesan):
            return
        i0 = self._idx_of(pilih[0]["uid"])
        for l in pilih:
            try:
                self.langkah.remove(l)
            except ValueError:
                pass
        self.sel = None
        if i0 is not None and 0 <= i0 < len(self.langkah):
            self.sel = self.langkah[i0]["uid"]
        elif self.langkah:
            self.sel = self.langkah[-1]["uid"]
        self._refresh_tabel()
        self._render_properti()
        self._set_status("{} langkah dihapus.".format(len(pilih)),
                         C_ORANGE)

    def _geser_langkah(self, delta):
        i = self._idx_of(self.sel)
        if i is None:
            return
        j = i + delta
        if j < 0 or j >= len(self.langkah):
            return
        self.langkah[i], self.langkah[j] = self.langkah[j], \
            self.langkah[i]
        self._refresh_tabel()
        try:
            self.tree.selection_set(self.sel)
            self.tree.see(self.sel)
        except Exception:
            pass

    def _naik(self):
        self._geser_langkah(-1)

    def _turun(self):
        self._geser_langkah(1)

    def _toggle_aktif(self):
        """v5.7: nyalakan/matikan SEMUA langkah terpilih sekaligus."""
        pilih = [self._get(u) for u in self.tree.selection()]
        pilih = [l for l in pilih if l]
        if not pilih:
            l = self._get(self.sel)
            pilih = [l] if l else []
        if not pilih:
            return
        target = not bool(pilih[0].get("aktif", True))
        for l in pilih:
            l["aktif"] = target
        self._refresh_tabel()
        self._set_status("{} langkah {}.".format(
            len(pilih),
            "DINYALAKAN" if target else "DIMATIKAN (dilewati saat "
                                        "jalan)"),
            C_GREEN if target else C_ORANGE)

    def _menu_klik_kanan(self, ev):
        iid = self.tree.identify_row(ev.y)
        # v5.7: klik kanan pada baris yang SUDAH terpilih bersama
        # tidak boleh merusak pilihan banyak
        if iid and iid not in self.tree.selection():
            self.tree.selection_set(iid)
        n = len(self.tree.selection())
        m = tk.Menu(self.wadah, tearoff=0)
        menu_gelap(m)
        m.add_command(label="Tahan CTRL / SHIFT saat klik = pilih "
                            "banyak langkah",
                      state="disabled")
        m.add_separator()
        m.add_command(label="Salin {}  (Ctrl+C)".format(
                          "{} langkah terpilih".format(n) if n > 1
                          else "langkah ini"),
                      command=self._salin)
        m.add_command(label="Tempel salinan di sini  (Ctrl+V)",
                      command=self._tempel)
        m.add_separator()
        m.add_command(label="Naikkan", command=self._naik)
        m.add_command(label="Turunkan", command=self._turun)
        m.add_command(label="Nyalakan / Matikan (semua yang terpilih)",
                      command=self._toggle_aktif)
        m.add_separator()
        m.add_command(label="Hapus {}  (Del)".format(
                          "langkah terpilih" if n > 1
                          else "langkah ini"),
                      command=self._hapus)
        try:
            m.tk_popup(ev.x_root, ev.y_root)
        finally:
            m.grab_release()

    # ================== PANEL PROPERTI ==================
    def _render_properti(self):
        # v5.7: BANYAK baris terpilih -> panel aksi massal
        pilihan = self.tree.selection()
        if len(pilihan) > 1:
            render_properti_multi(
                self, pilihan,
                "\n  -  AKTIF/MATI menyalakan / mematikan semua yang "
                "terpilih\n")
            return
        self._loading_prop = True
        for wdg in self.prop_body.winfo_children():
            wdg.destroy()
        self.lbl_ambil = None
        l = self._get(self.sel)
        if not l:
            tk.Label(
                self.prop_body,
                text="ALUR KERJA MASIH KOSONG / BELUM ADA BARIS "
                     "TERPILIH.\n\n"
                     "Cara pakai:\n"
                     "1. Klik salah satu tombol + di toolbar atas "
                     "(mis. + KLIK TITIK, + JEDA, + CARI GAMBAR, "
                     "+ KETIK TEKS, + TANGGAL-JAM, + VIDEO+CAPTION).\n"
                     "2. Klik barisnya di tabel ALUR KERJA.\n"
                     "3. Atur propertinya di panel ini (posisi, teks, "
                     "jeda, jumlah klik, gambar referensi, dll).\n"
                     "4. Ulangi sampai alur selesai, lalu JALANKAN "
                     "(F6).\n\n"
                     "CARA LEBIH CEPAT: klik tombol ● REKAM AKSI di "
                     "atas - kerjakan aksimu langsung di layar (klik, "
                     "ketik, scroll) dan semuanya terekam otomatis "
                     "menjadi langkah di tabel ini. Tekan F8 untuk "
                     "berhenti merekam.\n\n"
                     "Contoh alur sederhana:\n"
                     "+ CARI GAMBAR (klik tombol login)  >  + KETIK "
                     "TEKS (email)  >  + TEKAN TOMBOL (Tab)  >  "
                     "+ KETIK TEKS (kata sandi)  >  + TEKAN TOMBOL "
                     "(Enter).",
                bg=C_BG, fg=C_MUTED, font=F_S, anchor="w",
                justify="left", wraplength=880).pack(fill="x",
                                                     pady=(4, 0))
            self._loading_prop = False
            return
        jenis = l["jenis"]
        judul = str(l.get("nama") or "") or LABEL_JENIS[jenis]
        self.pv = {
            "nama": tk.StringVar(value=str(l.get("nama") or "")),
            "jeda": tk.StringVar(value="{:.1f}".format(
                _angka(l.get("jeda"), 0.5, 0, 86400))),
        }
        kepala = tk.Frame(self.prop_body, bg=C_BG)
        kepala.pack(fill="x", pady=(0, 4))
        tk.Label(kepala, text="{}   -   {}".format(judul,
                                                   LABEL_JENIS[jenis]),
                 bg=C_BG, fg=C_TEXT, font=F_H, anchor="w",
                 wraplength=860, justify="left").pack(fill="x")

        # ---- nama + jeda (semua jenis) ----
        r = self._baris_prop("NAMA LANGKAH (opsional)")
        self._ent_prop(r, self.pv["nama"], 30, tengah=False)
        r = self._baris_prop("JEDA SEBELUM LANGKAH (detik)")
        self._ent_prop(r, self.pv["jeda"], 6)

        pos = l.get("posisi")
        if jenis in ("KLIK", "TANGGAL_JAM", "VIDEO_CAPTION"):
            self.pv["x"] = tk.StringVar(value=str(pos[0]) if pos else "")
            self.pv["y"] = tk.StringVar(value=str(pos[1]) if pos else "")
            r = self._baris_prop("POSISI KLIK DULU (opsional) X , Y")
            self._ent_prop(r, self.pv["x"], 6)
            tk.Label(r, text=",", bg=C_BG, fg=C_MUTED,
                     font=F_N).pack(side="left", padx=2)
            self._ent_prop(r, self.pv["y"], 6)
            self._btn_prop(r, "AMBIL (5 dtk)",
                           lambda: self._ambil_posisi(l["uid"]))
            self._btn_prop(r, "LIHAT",
                           lambda: self._lihat_posisi(l["uid"]), bg=C_BG)
            tk.Label(r, text="dikosongkan = ketik di posisi kursor "
                             "sekarang", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=6)

        if jenis == "KLIK":
            self.pv["tombol_mouse"] = tk.StringVar(
                value=l.get("tombol_mouse")
                if l.get("tombol_mouse") in MOUSE_OPSI else "Klik kiri")
            self.pv["klik"] = tk.StringVar(value=str(
                int(_angka(l.get("klik"), 1, 0, 500))))
            self.pv["jeda_klik"] = tk.StringVar(value="{:.2f}".format(
                _angka(l.get("jeda_klik"), 0.3, 0.05, 60)))
            self.pv["geser"] = tk.StringVar(value=str(
                int(_angka(l.get("geser"), 0, 0, 100000))))
            r = self._baris_prop("JENIS KLIK")
            tk.OptionMenu(r, self.pv["tombol_mouse"],
                          *MOUSE_OPSI).pack(side="left")
            tk.Label(r, text="JUMLAH KLIK:", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=(12, 4))
            self._ent_prop(r, self.pv["klik"], 6)
            tk.Label(r, text="JEDA ANTAR KLIK (detik):", bg=C_BG,
                     fg=C_MUTED, font=F_XS).pack(side="left",
                                                 padx=(12, 4))
            self._ent_prop(r, self.pv["jeda_klik"], 6)
            r = self._baris_prop("GESER PER PUTARAN ULANGI (px)")
            self._ent_prop(r, self.pv["geser"], 7)
            tk.Label(r, text="0 = tanpa geser. Untuk klik per baris "
                             "video dalam blok ULANGI: isi jarak antar "
                             "baris (Y turun sejauh nilai ini x nomor "
                             "putaran).",
                     bg=C_BG, fg=C_MUTED, font=F_XS, wraplength=520,
                     justify="left").pack(side="left", padx=6)
        elif jenis == "JEDA":
            self.pv["detik"] = tk.StringVar(value="{:.1f}".format(
                _angka(l.get("detik"), 1.0, 0, 86400)))
            r = self._baris_prop("TUNGGU BERAPA DETIK")
            self._ent_prop(r, self.pv["detik"], 8)
            tk.Label(r, text="mis. 2.5 (boleh koma atau titik)",
                     bg=C_BG, fg=C_MUTED, font=F_XS).pack(side="left",
                                                          padx=6)
        elif jenis == "GAMBAR":
            g = l.get("gambar") or \
                studio_langkah_baru("GAMBAR", 0)["gambar"]
            self.pv["g_path"] = tk.StringVar(
                value=str(g.get("path") or ""))
            self.pv["g_aksi"] = tk.StringVar(
                value=g.get("aksi") if g.get("aksi") in GAMBAR_AKSI_OPSI
                else "Klik di gambar")
            self.pv["g_gagal"] = tk.StringVar(
                value=g.get("gagal") if g.get("gagal")
                in GAMBAR_GAGAL_OPSI_STUDIO else "Lewati langkah")
            self.pv["g_mirip"] = tk.StringVar(
                value=str(g.get("mirip") or "0.80"))
            f = g.get("fokus")
            if isinstance(f, (list, tuple)) and len(f) == 4:
                fokus_teks = "({},{}) - ({},{})".format(
                    f[0], f[1], f[2], f[3])
            else:
                fokus_teks = "Seluruh layar (tidak dibatasi)"
            self.pv["g_fokus"] = tk.StringVar(value=fokus_teks)
            tk.Label(self.prop_body,
                     text="TANPA perlu mengisi X,Y lagi: gambar referensi "
                          "dicari lalu LANGSUNG DIKLIK (atau hanya "
                          "dipindah). AREA FOKUS opsional untuk "
                          "membatasi daerah pencariannya.",
                     bg=C_BG, fg=C_BLUE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            r = self._baris_prop("GAMBAR REFERENSI")
            self._ent_prop(r, self.pv["g_path"], 42, tengah=False)
            self._btn_prop(r, "PILIH GAMBAR...",
                           lambda: self._pilih_gambar(l["uid"]))
            self._btn_prop(r, "POTONG GAMBAR...",
                           lambda: self._potong_gambar(l["uid"]))
            # v5.1: pratinjau gambar referensi langkah ini
            self.pv["g_thumb"] = tk.Label(self.prop_body, bg=C_PANEL,
                                          relief="solid", bd=1, anchor="w")
            self.pv["g_thumb"].pack(anchor="w", padx=18, pady=(3, 2))
            _thumb = muat_thumbnail(str(g.get("path") or ""))
            if _thumb is not None:
                self.pv["g_thumb"].configure(image=_thumb)
                self.pv["g_thumb"].image = _thumb
            else:
                self.pv["g_thumb"].configure(
                    text="  Belum ada gambar - klik POTONG GAMBAR, lalu "
                         "SERET kotak langsung di layar  ",
                    fg=C_MUTED, font=F_XS)
            # v5.3: AREA FOKUS (opsional) - dipilih dengan menyeret
            r = self._baris_prop("AREA FOKUS (opsional)")
            self._ent_prop(r, self.pv["g_fokus"], 26, tengah=False)
            self._btn_prop(r, "PILIH AREA FOKUS...",
                           lambda: self._pilih_area_fokus(l["uid"]))
            self._btn_prop(r, "KOSONGKAN",
                           lambda: self._fokus_kosongkan(l["uid"]),
                           bg=C_BG)
            tk.Label(r, text="diisi dengan MENYERET kotak di layar",
                     bg=C_BG, fg=C_MUTED, font=F_XS).pack(side="left",
                                                          padx=6)
            r = self._baris_prop("SAAT KETEMU:")
            tk.OptionMenu(r, self.pv["g_aksi"],
                          *GAMBAR_AKSI_OPSI).pack(side="left")
            tk.Label(r, text="SAAT TIDAK KETEMU:", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=(12, 4))
            tk.OptionMenu(r, self.pv["g_gagal"],
                          *GAMBAR_GAGAL_OPSI_STUDIO).pack(side="left")
            r = self._baris_prop("KEMIRIPAN:")
            self._ent_prop(r, self.pv["g_mirip"], 6)
            self._btn_prop(r, "TES CARI LANGKAH INI", self._tes_cari)
            tk.Label(self.prop_body,
                     text="v5.3: tidak perlu POSISI X,Y lagi - gambar "
                          "dicari di AREA FOKUS (atau seluruh layar bila "
                          "kosong) lalu diklik tepat di gambarnya. PILIH "
                          "AREA FOKUS = layar dibekukan, SERET kotak di "
                          "daerah tempat gambar biasanya muncul (mis. "
                          "daftar negara saja, bukan seluruh halaman) - "
                          "pencarian lebih cepat & lebih akurat. Potongan "
                          "jadi file BARU di folder data\\referensi; "
                          "zoom browser jangan diubah setelah dipotong.",
                     bg=C_BG, fg=C_ORANGE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(
                         fill="x", pady=(4, 0))
        elif jenis == "KETIK":
            self.pv["teks"] = tk.StringVar(value=str(l.get("teks") or ""))
            self.pv["ctrl_a"] = tk.BooleanVar(
                value=bool(l.get("ctrl_a")))
            self.pv["enter"] = tk.BooleanVar(value=bool(l.get("enter")))
            r = self._baris_prop("TEKS YANG DIKETIK")
            self._ent_prop(r, self.pv["teks"], 46, tengah=False)
            tk.Label(self.prop_body,
                     text="Placeholder: {caption} = caption dasar + nama "
                          "video ke-i  |  {video} = nama video ke-i  |  "
                          "{no} = nomor putaran ULANGI (1, 2, 3, ...)  |  "
                          "{jumlah} = jumlah video. Menu ISI VIDEO & "
                          "CAPTION di atas lebih praktis untuk hal ini.",
                     bg=C_BG, fg=C_BLUE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Ctrl+A dulu (timpa isi kotak yang lama)",
                           variable=self.pv["ctrl_a"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Tekan Enter setelah selesai mengetik",
                           variable=self.pv["enter"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
        elif jenis == "TANGGAL_JAM":
            self.pv["sumber"] = tk.StringVar(
                value=l.get("sumber")
                if l.get("sumber") in SUMBER_TANGGAL_OPSI
                else "Tab CutMotions")
            self.pv["teks"] = tk.StringVar(value=str(l.get("teks") or ""))
            self.pv["ctrl_a"] = tk.BooleanVar(
                value=bool(l.get("ctrl_a", True)))
            self.pv["enter"] = tk.BooleanVar(value=bool(l.get("enter")))
            r = self._baris_prop("AMBIL NILAI TANGGAL-JAM DARI:")
            tk.OptionMenu(r, self.pv["sumber"],
                          *SUMBER_TANGGAL_OPSI).pack(side="left")
            tk.Label(self.prop_body,
                     text="'Tab CutMotions' = pakai isi kolom TANGGAL & JAM "
                          "RILIS di tab Alur CutMotions (ubah sekali, semua "
                          "makro ikut).  'Tetap' = pakai nilai di bawah ini.",
                     bg=C_BG, fg=C_BLUE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            r = self._baris_prop("TANGGAL & JAM RILIS")
            self._ent_prop(r, self.pv["teks"], 22, tengah=False)
            tk.Label(r, text="format 2026-09-10 02:05:01",
                     bg=C_BG, fg=C_MUTED, font=F_XS).pack(side="left",
                                                          padx=6)
            tk.Checkbutton(self.prop_body,
                           text="Ctrl+A dulu (timpa isi kolom yang lama)",
                           variable=self.pv["ctrl_a"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Tekan Enter setelah selesai mengetik",
                           variable=self.pv["enter"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
            tk.Label(self.prop_body,
                     text="Alur tipikal: + KLIK (kolom tanggal) lalu + "
                          "TANGGAL-JAM - ATAU isi POSISI KLIK DULU di atas "
                          "agar langkah ini klik sendiri kolomnya.",
                     bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x",
                                                          pady=(2, 0))
        elif jenis == "VIDEO_CAPTION":
            self.pv["isi"] = tk.StringVar(
                value=l.get("isi") if l.get("isi") in ISI_VIDEO_OPSI
                else "Caption dasar + nama video")
            self.pv["teks"] = tk.StringVar(value=str(l.get("teks") or ""))
            self.pv["ctrl_a"] = tk.BooleanVar(
                value=bool(l.get("ctrl_a", True)))
            self.pv["enter"] = tk.BooleanVar(value=bool(l.get("enter")))
            r = self._baris_prop("YANG DIKETIK OTOMATIS:")
            tk.OptionMenu(r, self.pv["isi"],
                          *ISI_VIDEO_OPSI).pack(side="left")
            tk.Label(self.prop_body,
                     text="Jumlah video = angka di kolom JUMLAH VIDEO tab "
                          "CutMotions.  Caption dasar + nama video = mis. "
                          "'#dangdut - melati' (nama video ke-i kalau di "
                          "dalam blok ULANGI).  Nama video saja = mis. "
                          "'melati'.",
                     bg=C_BG, fg=C_BLUE, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            r = self._baris_prop("TEKS SENDIRI + PLACEHOLDER")
            self._ent_prop(r, self.pv["teks"], 46, tengah=False)
            tk.Label(self.prop_body,
                     text="Dipakai kalau pilihan di atas = 'Teks sendiri'. "
                          "Placeholder: {caption} = caption dasar + nama "
                          "video ke-i  |  {video} = nama video ke-i  |  "
                          "{no} = nomor putaran ULANGI  |  {jumlah} = "
                          "jumlah video total.",
                     bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Ctrl+A dulu (timpa isi kolom yang lama)",
                           variable=self.pv["ctrl_a"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
            tk.Checkbutton(self.prop_body,
                           text="Tekan Enter setelah selesai mengetik",
                           variable=self.pv["enter"], bg=C_BG, fg=C_TEXT,
                           font=F_XS, anchor="w").pack(fill="x")
        elif jenis == "TOMBOL":
            self.pv["tombol_kb"] = tk.StringVar(
                value=str(l.get("tombol_kb") or "Enter"))
            self.pv["jumlah_kb"] = tk.StringVar(value=str(
                int(_angka(l.get("jumlah_kb"), 1, 1, 500))))
            self.pv["jeda_klik"] = tk.StringVar(value="{:.2f}".format(
                _angka(l.get("jeda_klik"), 0.3, 0.05, 60)))
            r = self._baris_prop("TOMBOL YANG DITEKAN")
            ttk.Combobox(r, textvariable=self.pv["tombol_kb"],
                         values=list(TOMBOL_KB_OPSI), width=20,
                         font=F_N).pack(side="left", ipady=2)
            tk.Label(r, text="  (bisa ketik 1 huruf sendiri, mis. a)",
                     bg=C_BG, fg=C_MUTED, font=F_XS).pack(side="left",
                                                          padx=4)
            r = self._baris_prop("JUMLAH TEKAN")
            self._ent_prop(r, self.pv["jumlah_kb"], 6)
            tk.Label(r, text="JEDA ANTAR TEKAN (detik):", bg=C_BG,
                     fg=C_MUTED, font=F_XS).pack(side="left",
                                                 padx=(12, 4))
            self._ent_prop(r, self.pv["jeda_klik"], 6)
        elif jenis == "SCROLL":
            self.pv["arah"] = tk.StringVar(
                value=l.get("arah")
                if l.get("arah") in ("Turun", "Naik") else "Turun")
            self.pv["jumlah_scroll"] = tk.StringVar(value=str(
                int(_angka(l.get("jumlah_scroll"), 3, 0, 1000))))
            r = self._baris_prop("ARAH SCROLL")
            tk.OptionMenu(r, self.pv["arah"], "Turun",
                          "Naik").pack(side="left")
            tk.Label(r, text="JUMLAH GULUNGAN:", bg=C_BG, fg=C_MUTED,
                     font=F_XS).pack(side="left", padx=(12, 4))
            self._ent_prop(r, self.pv["jumlah_scroll"], 6)
        elif jenis == "CATATAN":
            self.pv["catatan"] = tk.StringVar(
                value=str(l.get("catatan") or ""))
            r = self._baris_prop("ISI CATATAN")
            self._ent_prop(r, self.pv["catatan"], 46, tengah=False)
            tk.Label(self.prop_body,
                     text="Catatan hanya penanda di tabel - tidak ada "
                          "aksi yang dijalankan.",
                     bg=C_BG, fg=C_MUTED, font=F_XS,
                     anchor="w").pack(fill="x")
        elif jenis == "LOOP_MULAI":
            self.pv["jumlah_loop"] = tk.StringVar(value=str(
                int(_angka(l.get("jumlah_loop"), 2, 0, 100000))))
            self.pv["ikut_video"] = tk.BooleanVar(
                value=bool(l.get("ikut_video")))
            r = self._baris_prop("JUMLAH ULANGAN")
            self._ent_prop(r, self.pv["jumlah_loop"], 7)
            tk.Checkbutton(self.prop_body,
                           text="Ikut JUMLAH VIDEO di tab Alur CutMotions "
                                "(angka di sini diabaikan) - dipakai "
                                "untuk caption per baris video",
                           variable=self.pv["ikut_video"], bg=C_BG,
                           fg=C_TEXT, font=F_XS,
                           anchor="w").pack(fill="x")
            tk.Label(self.prop_body,
                     text="Semua langkah di ANTARA 'ULANGI-MULAI' dan "
                          "'ULANGI-AKHIR' diulang sesuai jumlah di atas. "
                          "Gunakan GESER TURUN pada langkah KLIK di "
                          "dalamnya agar klik turun ke baris berikutnya.",
                     bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(
                         fill="x", pady=(4, 0))
        else:  # LOOP_AKHIR
            tk.Label(self.prop_body,
                     text="Akhir blok ULANGI - alur kembali ke "
                          "ULANGI-MULAI di atas selama jumlah ulangan "
                          "belum habis.",
                     bg=C_BG, fg=C_MUTED, font=F_XS, anchor="w",
                     wraplength=860, justify="left").pack(
                         fill="x", pady=(4, 0))

        # ---- aktif + info ----
        self.pv["aktif"] = tk.BooleanVar(value=bool(l.get("aktif", True)))
        tk.Checkbutton(self.prop_body,
                       text="LANGKAH AKTIF (lepas centang = dilewati "
                            "saat jalan)",
                       variable=self.pv["aktif"], bg=C_BG, fg=C_TEXT,
                       font=F_XS, anchor="w").pack(fill="x", pady=(4, 0))
        self.lbl_ambil = tk.Label(self.prop_body, text="", bg=C_BG,
                                  fg=C_ORANGE, font=F_XS, anchor="w",
                                  wraplength=860, justify="left")
        self.lbl_ambil.pack(fill="x", pady=(4, 0))
        # (v5.1: lewati widget non-variable seperti pv["g_thumb"])
        for var in self.pv.values():
            if isinstance(var, tk.Variable):
                var.trace_add("write", self._terapkan_prop)
        self._loading_prop = False

    def _terapkan_prop(self, *_):
        if self._loading_prop:
            return
        l = self._get(self.sel)
        if not l:
            return
        try:
            x = int(float(str(self.pv["x"].get()).strip() or "nan"))
            y = int(float(str(self.pv["y"].get()).strip() or "nan"))
            l["posisi"] = [x, y]
        except (KeyError, ValueError, TypeError):
            pass
        try:
            l["jeda"] = max(0.0, float(
                str(self.pv["jeda"].get()).replace(",", ".")))
        except (ValueError, TypeError):
            pass
        l["nama"] = self.pv["nama"].get()
        jenis = l["jenis"]
        if jenis == "KLIK":
            l["tombol_mouse"] = self.pv["tombol_mouse"].get()
            l["klik"] = int(_angka(self.pv["klik"].get(), 1, 0, 500))
            l["jeda_klik"] = _angka(self.pv["jeda_klik"].get(), 0.3,
                                    0.05, 60)
            l["geser"] = int(_angka(self.pv["geser"].get(), 0, 0,
                                    100000))
        elif jenis == "JEDA":
            l["detik"] = _angka(self.pv["detik"].get(), 1.0, 0, 86400)
        elif jenis == "GAMBAR":
            g = l.setdefault("gambar", {})
            g["path"] = self.pv["g_path"].get().strip()
            aksi = self.pv["g_aksi"].get()
            g["aksi"] = (aksi if aksi in GAMBAR_AKSI_OPSI
                         else "Klik di gambar")
            gagal = self.pv["g_gagal"].get()
            g["gagal"] = (gagal if gagal in GAMBAR_GAGAL_OPSI_STUDIO
                          else "Lewati langkah")
            g["mirip"] = self.pv["g_mirip"].get().strip()
            # fokus diatur lewat tombol PILIH AREA FOKUS / KOSONGKAN
        elif jenis == "KETIK":
            l["teks"] = self.pv["teks"].get()
            l["ctrl_a"] = bool(self.pv["ctrl_a"].get())
            l["enter"] = bool(self.pv["enter"].get())
        elif jenis == "TANGGAL_JAM":
            sumber = self.pv["sumber"].get()
            l["sumber"] = (sumber if sumber in SUMBER_TANGGAL_OPSI
                           else "Tab CutMotions")
            l["teks"] = self.pv["teks"].get()
            l["ctrl_a"] = bool(self.pv["ctrl_a"].get())
            l["enter"] = bool(self.pv["enter"].get())
        elif jenis == "VIDEO_CAPTION":
            isi = self.pv["isi"].get()
            l["isi"] = (isi if isi in ISI_VIDEO_OPSI
                        else "Caption dasar + nama video")
            l["teks"] = self.pv["teks"].get()
            l["ctrl_a"] = bool(self.pv["ctrl_a"].get())
            l["enter"] = bool(self.pv["enter"].get())
        elif jenis == "TOMBOL":
            l["tombol_kb"] = (self.pv["tombol_kb"].get().strip()
                              or "Enter")
            l["jumlah_kb"] = int(_angka(self.pv["jumlah_kb"].get(), 1,
                                        1, 500))
            l["jeda_klik"] = _angka(self.pv["jeda_klik"].get(), 0.3,
                                    0.05, 60)
        elif jenis == "SCROLL":
            l["arah"] = self.pv["arah"].get()
            l["jumlah_scroll"] = int(_angka(
                self.pv["jumlah_scroll"].get(), 3, 0, 1000))
        elif jenis == "CATATAN":
            l["catatan"] = self.pv["catatan"].get()
        elif jenis == "LOOP_MULAI":
            l["jumlah_loop"] = int(_angka(
                self.pv["jumlah_loop"].get(), 2, 0, 100000))
            l["ikut_video"] = bool(self.pv["ikut_video"].get())
        l["aktif"] = bool(self.pv["aktif"].get())
        self._refresh_tabel()

    # ================== AMBIL / LIHAT POSISI ==================
    def _ambil_posisi(self, uid):
        if not PYNPUT_OK:
            messagebox.showerror(APP_NAME,
                                 "Library pynput belum terpasang.\n\n"
                                 "Buka CMD lalu jalankan:\n"
                                 "  pip install pynput")
            return
        l = self._get(uid)
        if not l:
            return
        judul = str(l.get("nama") or "") or LABEL_JENIS[l["jenis"]]

        def kerja():
            try:
                for s in range(5, 0, -1):
                    self.root.after(0, lambda s=s: self._tampilkan_info(
                        "Arahkan mouse ke titik '{}' dan diamkan... {}"
                        .format(judul, s)))
                    self.root.after(0, lambda s=s: self._set_status(
                        "Ambil posisi '{}' ... {}".format(judul, s),
                        C_ORANGE))
                    time.sleep(1)
                px, py = self.mouse.position

                def isi():
                    l["posisi"] = [int(px), int(py)]
                    self._refresh_tabel()
                    if self.sel == uid:
                        self._render_properti()
                    self._tampilkan_info(
                        "Posisi tersimpan: X={}, Y={}".format(int(px),
                                                              int(py)),
                        C_GREEN)
                    self._set_status("'{}' = ({}, {}) tersimpan."
                                     .format(judul, int(px), int(py)),
                                     C_GREEN)

                self.root.after(0, isi)
            except Exception:
                self.root.after(0, lambda: self._tampilkan_info(
                    "Gagal mengambil posisi.", C_RED))

        threading.Thread(target=kerja, daemon=True).start()

    def _lihat_posisi(self, uid):
        if not PYNPUT_OK:
            return
        l = self._get(uid)
        if not l or not l.get("posisi"):
            messagebox.showinfo(APP_NAME, "Posisi ini belum diatur. Klik "
                                          "dulu AMBIL (atau isi X,Y "
                                          "manual).")
            return
        try:
            self.mouse.position = (l["posisi"][0], l["posisi"][1])
        except Exception:
            pass

    # ================== GAMBAR REFERENSI ==================
    def _pilih_gambar(self, uid=None):
        uid = uid or self.sel
        l = self._get(uid)
        if not l or l["jenis"] != "GAMBAR":
            messagebox.showinfo(APP_NAME, "Pilih dulu baris CARI GAMBAR "
                                          "di tabel.")
            return
        f = filedialog.askopenfilename(
            title="Pilih gambar referensi (potongan layar)",
            filetypes=[("Gambar", "*.png *.jpg *.jpeg *.bmp"),
                       ("Semua file", "*.*")])
        if f:
            l.setdefault("gambar", {})["path"] = f
            self._refresh_tabel()
            if self.sel == uid:
                self._render_properti()
            self._set_status("Gambar referensi terpasang: {}".format(f),
                             C_GREEN)

    def _potong_dari_menu(self):
        self._potong_gambar(None)

    def _potong_gambar(self, uid=None):
        """v5.1: potong gambar referensi LANGSUNG DI LAYAR.

        Aplikasi disembunyikan sejenak, layar dibekukan fullscreen,
        lalu user MENYERET kotak langsung di area yang diinginkan -
        hanya area yang diseret yang disimpan (bukan seluruh layar).

        - Bila langkah CARI GAMBAR terpilih: gambar dipasang pada
          langkah itu (gambar langkah lain TIDAK tertimpa).
        - Bila TIDAK ada langkah CARI GAMBAR terpilih: ditawarkan
          membuat LANGKAH CARI GAMBAR BARU dari hasil potongan -
          sehingga menu ini bisa dipakai berkali-kali dengan
          referensi berbeda-beda.
        """
        if not PIL_OK or not CV_OK:
            messagebox.showwarning(
                APP_NAME,
                "Fitur potong gambar butuh Pillow + OpenCV.\n\n"
                "Buka CMD lalu jalankan:\n"
                "  pip install pillow opencv-python")
            return
        uid = uid or self.sel
        l = self._get(uid)
        if not l or l["jenis"] != "GAMBAR":
            if not messagebox.askyesno(
                    APP_NAME,
                    "Tidak ada langkah CARI GAMBAR yang terpilih.\n\n"
                    "Setelah kamu MENYERET kotak di layar, buat LANGKAH "
                    "CARI GAMBAR BARU dengan gambar hasil potongan "
                    "itu?\n\nYes = buat langkah baru\nNo = batal"):
                return
            self._potong_uid = None   # mode: buat langkah CARI GAMBAR baru
        else:
            self._potong_uid = uid

        def kerja():
            try:
                for s in range(3, 0, -1):
                    self.root.after(0, lambda s=s: self._set_status(
                        "Layar akan DIBEKUKAN dalam {} detik - pastikan "
                        "area yang mau dipotong terlihat...".format(s),
                        C_ORANGE))
                    time.sleep(1)
                # v5.1: sembunyikan jendela aplikasi dulu supaya area
                # di baliknya juga bisa dipotong
                induk = self.root.winfo_toplevel()
                self.root.after(0, induk.withdraw)
                time.sleep(0.4)
                img = ImageGrab.grab()
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    APP_NAME,
                    "Gagal mengambil screenshot:\n{}".format(e)))
                self.root.after(0, self._tampil_lagi)
                return

            def tampil():
                try:
                    OverlayPotong(self.wadah, img, self._gambar_terpotong,
                                  on_batal=self._potong_batal)
                except Exception as e:
                    messagebox.showerror(
                        APP_NAME,
                        "Gagal membuka layar potong:\n{}".format(e))
                finally:
                    self._tampil_lagi()

            self.root.after(0, tampil)

        threading.Thread(target=kerja, daemon=True).start()

    def _tampil_lagi(self):
        """Tampilkan kembali jendela utama setelah potong selesai."""
        try:
            self.root.winfo_toplevel().deiconify()
        except Exception:
            pass

    def _potong_batal(self):
        self._set_status("Potong gambar dibatalkan (ESC).", C_MUTED)

    def _gambar_terpotong(self, path):
        uid = getattr(self, "_potong_uid", None)
        l = self._get(uid)
        if l:
            # mode: pasang pada langkah CARI GAMBAR terpilih
            l.setdefault("gambar", {})["path"] = path
            self._refresh_tabel()
            if self.sel == l["uid"]:
                self._render_properti()
            self._set_status("Gambar referensi baru tersimpan: {}  (langkah "
                             "lain tidak tertimpa)".format(path), C_GREEN)
            return
        # v5.1: mode tanpa langkah terpilih -> buat langkah CARI
        # GAMBAR baru otomatis dari hasil potongan
        l = studio_langkah_baru("GAMBAR", self._uid_baru())
        l["gambar"]["path"] = path
        self.langkah.append(l)
        self.sel = l["uid"]
        self._refresh_tabel()
        try:
            self.tree.selection_set(l["uid"])
            self.tree.see(l["uid"])
        except Exception:
            pass
        self._render_properti()
        self._set_status("Langkah CARI GAMBAR baru dibuat dengan gambar: "
                         "{}".format(path), C_GREEN)

    # ---------- v5.3: AREA FOKUS pencarian gambar ----------
    def _pilih_area_fokus(self, uid=None):
        """Pilih AREA FOKUS pencarian dengan MENYERET kotak di layar.

        Layar dibekukan fullscreen (teknik sama dengan POTONG GAMBAR),
        tapi hasilnya KOORDINAT [x1,y1,x2,y2] - bukan file gambar.
        """
        if not PIL_OK:
            messagebox.showwarning(
                APP_NAME,
                "Fitur area fokus butuh Pillow.\n\nBuka CMD lalu jalankan:\n"
                "  pip install pillow")
            return
        uid = uid or self.sel
        l = self._get(uid)
        if not l or l["jenis"] != "GAMBAR":
            messagebox.showinfo(
                APP_NAME,
                "Pilih dulu baris CARI GAMBAR yang mau diberi AREA "
                "FOKUS.")
            return
        self._fokus_uid = uid

        def kerja():
            try:
                for s in range(3, 0, -1):
                    self.root.after(0, lambda s=s: self._set_status(
                        "Layar akan DIBEKUKAN dalam {} detik - siapkan "
                        "halaman tempat gambar biasanya muncul...".format(
                            s), C_ORANGE))
                    time.sleep(1)
                induk = self.root.winfo_toplevel()
                self.root.after(0, induk.withdraw)
                time.sleep(0.4)
                img = ImageGrab.grab()
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    APP_NAME,
                    "Gagal mengambil screenshot:\n{}".format(e)))
                self.root.after(0, self._tampil_lagi)
                return

            def tampil():
                try:
                    OverlayPotong(self.wadah, img, None,
                                  on_batal=self._potong_batal,
                                  mode="area",
                                  on_area=self._area_terpilih)
                except Exception as e:
                    messagebox.showerror(
                        APP_NAME,
                        "Gagal membuka layar pilih area:\n{}".format(e))
                finally:
                    self._tampil_lagi()

            self.root.after(0, tampil)

        threading.Thread(target=kerja, daemon=True).start()

    def _area_terpilih(self, koord):
        l = self._get(getattr(self, "_fokus_uid", None))
        if not l:
            return
        l.setdefault("gambar", {})["fokus"] = list(koord)
        self._refresh_tabel()
        if self.sel == l["uid"]:
            self._render_properti()
        self._set_status(
            "AREA FOKUS tersimpan: ({},{}) - ({},{})  - gambar dicari "
            "hanya di dalam kotak itu.".format(koord[0], koord[1],
                                               koord[2], koord[3]),
            C_GREEN)

    def _fokus_kosongkan(self, uid):
        l = self._get(uid)
        if not l:
            return
        l.setdefault("gambar", {})["fokus"] = None
        self._refresh_tabel()
        if self.sel == uid:
            self._render_properti()
        self._set_status("Area fokus dikosongkan - gambar dicari di "
                         "seluruh layar.", C_GREEN)

    def _tes_cari(self):
        if not PYNPUT_OK:
            messagebox.showerror(APP_NAME, "Library pynput belum "
                                           "terpasang.")
            return
        if not CV_OK:
            messagebox.showwarning(
                APP_NAME,
                "opencv-python belum terpasang - pencarian gambar tidak "
                "bisa dipakai.\n\nBuka CMD lalu jalankan:\n"
                "  pip install opencv-python\n\n"
                "Atau pakai CutUploaderPro.exe (OpenCV sudah menyatu).")
            return
        l = self._get(self.sel)
        if not l or l["jenis"] != "GAMBAR":
            messagebox.showinfo(APP_NAME, "Pilih dulu baris CARI GAMBAR "
                                          "yang mau dites.")
            return
        g = l.get("gambar") or {}
        path = str(g.get("path") or "").strip()
        nama = str(l.get("nama") or "") or LABEL_JENIS["GAMBAR"]
        if not path or not os.path.isfile(path):
            messagebox.showinfo(
                APP_NAME,
                "Pilih dulu gambar referensi langkah {}.\n\nCara "
                "termudah: klik 'POTONG GAMBAR...', lalu seret kotak "
                "di atas tulisan/tombolnya.".format(nama))
            return
        mirip = _angka(g.get("mirip"), 0.8, 0.5, 0.99)
        area = area_dari_langkah(l)
        if area:
            desk = "area fokus ({},{})-({},{})".format(area[0], area[1],
                                                       area[2], area[3])
        else:
            desk = "seluruh layar"

        def kerja():
            self.root.after(0, lambda: self._set_status(
                "Mencari '{}' di {} (multi-skala)...".format(
                    os.path.basename(path), desk), C_ORANGE))
            hasil, pesan = cari_di_layar_area(path, area, mirip)

            def lapor():
                if hasil:
                    x, y, skor = hasil
                    try:
                        self.mouse.position = (x, y)
                    except Exception:
                        pass
                    mode_t = ("pindah saja"
                              if g.get("aksi") == "Pindah saja"
                              else "akan diklik")
                    self._set_status(
                        "TES OK: gambar KETEMU di ({}, {}) - kemiripan "
                        "{:.0%}. Mouse dipindah ke sana (tidak diklik; "
                        "mode langkah ini: {}).".format(x, y, skor,
                                                        mode_t), C_GREEN)
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

    # ================== v5.6: hook REKAM AKSI (mixin) ==================
    def perekam_uid_mulai(self):
        return self._uid        # langkah Studio memakai uid angka

    def perekam_sisipkan(self, baru, uid_akhir):
        """Masukkan langkah hasil rekaman ke ALUR KERJA Studio.

        Disisipkan SETELAH baris terpilih (atau di akhir bila
        tidak ada yang terpilih) - sama seperti perilaku v5.4.
        """
        mulai_i = len(self.langkah)
        i_sel = self._idx_of(self.sel)
        if i_sel is not None:
            mulai_i = i_sel + 1
        self._uid = max(self._uid, uid_akhir)
        self.langkah[mulai_i:mulai_i] = baru
        self.sel = baru[0]["uid"]
        self._refresh_tabel()
        try:
            self.tree.selection_set(self.sel)
            self.tree.see(self.sel)
        except Exception:
            pass
        self._render_properti()
        n_klik = sum(1 for l in baru if l["jenis"] == "KLIK")
        n_ketik = sum(1 for l in baru if l["jenis"] in
                      ("KETIK", "TOMBOL"))
        n_scroll = sum(1 for l in baru if l["jenis"] == "SCROLL")
        self._set_status(
            "REKAMAN SELESAI: {} langkah ditambahkan ({} klik, {} "
            "ketikan/tombol, {} scroll) - cek & sunting lalu JALANKAN "
            "(F6).".format(len(baru), n_klik, n_ketik, n_scroll), C_GREEN)
    # ================== SIMPAN / BUKA MAKRO ==================
    def _simpan_auto(self):
        """Auto-save makro aktif ke folder data (diam-diam)."""
        try:
            with open(self.makro_path, "w", encoding="utf-8") as f:
                json.dump({"app": APP_NAME, "versi": APP_VERSION,
                           "jenis": "studio", "langkah": self.langkah},
                          f, indent=2, ensure_ascii=False)
        except Exception:
            pass

    def _muat_otomatis(self):
        if not os.path.exists(self.makro_path):
            return
        try:
            with open(self.makro_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            ls = studio_bersihkan(data.get("langkah"))
            if not ls:
                return
            self.langkah = ls
            maks = 0
            for l in ls:
                try:
                    maks = max(maks, int(str(l["uid"]).lstrip("s")))
                except ValueError:
                    pass
            self._uid = maks
            self.sel = ls[0]["uid"]
            self._refresh_tabel()
            self._render_properti()
        except Exception:
            pass

    def _makro_baru(self):
        if self.langkah and not messagebox.askyesno(
                APP_NAME,
                "Kosongkan alur kerja sekarang?\n\nAlur saat ini akan "
                "hilang - simpan dulu (SIMPAN MAKRO) bila perlu."):
            return
        self.langkah = []
        self.sel = None
        self._refresh_tabel()
        self._render_properti()
        self._set_status("Makro baru dibuat - alur kerja kosong. Pilih "
                         "tombol + untuk menambah langkah.", C_GREEN)

    def _simpan_makro(self):
        f = filedialog.asksaveasfilename(
            title="Simpan makro Studio",
            defaultextension=".json",
            initialfile="makro_{}.json".format(
                datetime.datetime.now().strftime("%Y%m%d")),
            filetypes=[("Makro Studio", "*.json")])
        if not f:
            return
        try:
            with open(f, "w", encoding="utf-8") as d:
                json.dump({"app": APP_NAME, "versi": APP_VERSION,
                           "jenis": "studio", "langkah": self.langkah},
                          d, indent=2, ensure_ascii=False)
            self._set_status("Makro tersimpan: {}".format(f), C_GREEN)
        except Exception as e:
            messagebox.showerror(APP_NAME,
                                 "Gagal menyimpan makro:\n" + str(e))

    def _buka_makro(self):
        f = filedialog.askopenfilename(
            title="Buka makro Studio",
            filetypes=[("Makro Studio", "*.json"),
                       ("Semua file", "*.*")])
        if not f:
            return
        try:
            with open(f, "r", encoding="utf-8") as s:
                data = json.load(s)
        except Exception as e:
            messagebox.showerror(APP_NAME,
                                 "Gagal membaca makro:\n" + str(e))
            return
        ls = studio_bersihkan(data.get("langkah"))
        if not ls:
            messagebox.showwarning(APP_NAME, "File makro tidak berisi "
                                             "langkah yang sah.")
            return
        self.langkah = ls
        maks = 0
        for l in ls:
            try:
                maks = max(maks, int(str(l["uid"]).lstrip("s")))
            except ValueError:
                pass
        self._uid = maks
        self.sel = ls[0]["uid"]
        self._refresh_tabel()
        self._render_properti()
        self._set_status("Makro dimuat: {} langkah dari {}".format(
            len(ls), f), C_GREEN)

    # ================== TEMPLATE CUTMOTIONS ==================
    def _template_cutmotions(self):
        cut = self.shell.tab_cut if self.shell is not self else None
        if cut is None:
            messagebox.showinfo(APP_NAME, "Mode mandiri tidak punya tab "
                                          "CutMotions.")
            return
        if not messagebox.askyesno(
                APP_NAME,
                "Muat TEMPLATE ALUR CUTMOTIONS (A-J) ke Studio?\n\n"
                "Alur kerja Studio saat ini akan DIGANTI dengan versi "
                "bebasnya: A jadwal, C cari gambar negara, D tanggal, "
                "F tambah video, H Shift+turun, I caption per baris "
                "(blok ULANGI), J submit.\n\nSetelah jadi template, "
                "semua langkah bebas disunting, disalin, dihapus, atau "
                "ditambah."):
            return
        V = cut.vars
        cfg = {
            "posisi": cut.posisi,
            "skip_jadwal": bool(V["skip_jadwal"].get()),
            "tanggal": V["tanggal"].get().strip(),
            "klik_bebas1": V["klik_bebas1"].get(),
            "scroll_bebas1": V["scroll_bebas1"].get(),
            "arah_scroll": V["arah_scroll"].get(),
            "klik_bebas2": V["klik_bebas2"].get(),
            "klik_submit": V["klik_submit"].get(),
            "jumlah": V["jumlah"].get(),
            "tunggu": V["tunggu"].get(),
            "jarak_baris": V["jarak_baris"].get(),
            "auto_kirim": bool(V["auto_kirim"].get()),
            "gambar_c": dict(cut.gambar_langkah.get("pos_pilih_neg")
                             or {}),
        }
        self.langkah = template_cutmotions_steps(cfg,
                                                 mulai_uid=self._uid)
        self._uid += len(self.langkah)
        self.sel = self.langkah[0]["uid"] if self.langkah else None
        self._refresh_tabel()
        self._render_properti()
        self._set_status("Template CutMotions dimuat: {} langkah - klik "
                         "barisnya untuk menyunting.".format(
                             len(self.langkah)), C_GREEN)

    # ================== JALANKAN / BERHENTI ==================
    def _start(self):
        if self.running:
            return
        if not PYNPUT_OK:
            messagebox.showerror(
                APP_NAME, "Library pynput belum terpasang.\n\n"
                          "Buka CMD lalu jalankan:\n  pip install pynput")
            return
        lain = self.shell.tab_lain(self) if self.shell is not self \
            else None
        if lain is not None and lain.running:
            messagebox.showwarning(
                APP_NAME,
                "ALUR CUTMOTIONS sedang berjalan.\n\nTunggu sampai "
                "selesai atau tekan F7 dulu.")
            return
        if not self.langkah:
            messagebox.showinfo(
                APP_NAME,
                "Alur kerja masih KOSONG.\n\nKlik salah satu tombol + di "
                "toolbar (mis. + KLIK TITIK, + JEDA, + CARI GAMBAR) "
                "untuk menambah langkah pertama.\n\nAtau klik TEMPLATE "
                "CUTMOTIONS untuk mengisi alur CutMotions otomatis.")
            return
        # ---- validasi blok ULANGI ----
        buka = 0
        for l in self.langkah:
            if not l.get("aktif", True):
                continue
            if l["jenis"] == "LOOP_MULAI":
                buka += 1
            elif l["jenis"] == "LOOP_AKHIR":
                if buka == 0:
                    if not messagebox.askyesno(
                            APP_NAME,
                            "Ada ULANGI-AKHIR tanpa ULANGI-MULAI di "
                            "atasnya. Baris itu akan diabaikan. "
                            "Lanjut?"):
                        return
                    break
                buka -= 1
        if buka > 0:
            if not messagebox.askyesno(
                    APP_NAME,
                    "Ada {} blok ULANGI-MULAI tanpa ULANGI-AKHIR. "
                    "Blok itu dijalankan satu kali saja. Lanjut?".format(
                        buka)):
                return
        # ---- validasi gambar langkah CARI GAMBAR ----
        butuh_cv = False
        for l in self.langkah:
            if l["jenis"] == "GAMBAR" and l.get("aktif", True):
                butuh_cv = True
                p = str((l.get("gambar") or {}).get("path") or "")
                if not p or not os.path.isfile(p):
                    messagebox.showwarning(
                        APP_NAME,
                        "Langkah CARI GAMBAR '{}' belum punya file "
                        "gambar.\n\nKlik barisnya lalu POTONG GAMBAR / "
                        "PILIH GAMBAR.".format(
                            l.get("nama") or LABEL_JENIS["GAMBAR"]))
                    return
        if butuh_cv and not CV_OK:
            if not messagebox.askyesno(
                    APP_NAME,
                    "opencv-python belum terpasang sehingga langkah CARI "
                    "GAMBAR akan DILEWATI (yang lain tetap jalan).\n\n"
                    "Lanjut?"):
                return
        cut = self.shell.tab_cut if self.shell is not self else None
        videos = cut.antrian_video_studio() if cut is not None else []
        caption = cut.vars["caption"].get() if cut is not None else ""
        # v5.2: nilai utk langkah ISI TANGGAL-JAM & ISI VIDEO & CAPTION
        tanggal = cut.vars["tanggal"].get().strip() \
            if cut is not None else ""
        jumlah_set = int(_angka(cut.vars["jumlah"].get(), 0, 0,
                                MAX_BATCH)) if cut is not None else 0
        jumlah_total = len(videos) or jumlah_set
        try:
            mundur = int(_angka(self.vars["mundur"].get(), 5, 0, 60))
        except Exception:
            mundur = 5
        snap = {
            "mundur": mundur,
            "langkah": json.loads(json.dumps(self.langkah)),
            "videos": list(videos),
            "caption": caption,
            "tanggal": tanggal,
            "jumlah": jumlah_total,
        }
        self._simpan_auto()
        self.stop_event.clear()
        self.running = True
        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal")
        threading.Thread(target=self._worker, args=(snap,),
                         daemon=True).start()

    def _stop(self):
        if self.running:
            self.stop_event.set()
            self._set_status("Menghentikan makro...", C_ORANGE)

    def _finish(self, msg, warn=False):
        def do():
            self.running = False
            self.btn_start.config(state="normal")
            self.btn_stop.config(state="disabled")
            try:
                self.shell.lbl_status.config(
                    text=msg, fg=C_RED if warn else C_GREEN)
            except Exception:
                pass
        self.root.after(0, do)

    def _worker(self, snap):
        try:
            langkah = snap["langkah"]
            n = len(langkah)
            if n == 0:
                self._finish("Tidak ada langkah yang dijalankan.",
                             warn=True)
                return
            if snap["mundur"] > 0:
                for s in range(snap["mundur"], 0, -1):
                    if self.stop_event.is_set():
                        self._finish("Dibatalkan sebelum mulai.",
                                     warn=True)
                        return
                    self._set_status(
                        "Makro mulai dalam {} detik - siapkan "
                        "halaman/aplikasi tujuan...".format(s), C_ORANGE)
                    self._sleep(1.0)
            videos = snap.get("videos") or []
            caption = snap.get("caption") or ""
            loop_stack = []
            i = 0
            aman = 0
            while i < n:
                if self.stop_event.is_set():
                    self._finish("Makro dihentikan (F7) di langkah {}/{}."
                                 .format(i + 1, n), warn=True)
                    return
                aman += 1
                if aman > 500000:
                    self._finish("Dihentikan: alur ULANGI terlalu panjang "
                                 "(kemungkinan loop tanpa akhir).",
                                 warn=True)
                    return
                l = langkah[i]
                if not l.get("aktif", True):
                    i += 1
                    continue
                self._set_progress("LANGKAH {}/{} - {}".format(
                    i + 1, n,
                    str(l.get("nama") or "") or LABEL_JENIS[l["jenis"]]))
                self._sleep(max(0.0, _angka(l.get("jeda"), 0.5, 0,
                                            86400)))
                jenis = l["jenis"]
                if jenis == "LOOP_MULAI":
                    if l.get("ikut_video"):
                        jumlah = len(videos)
                    else:
                        jumlah = int(_angka(l.get("jumlah_loop"), 2, 0,
                                            100000))
                    if jumlah <= 0:
                        j = cari_akhir_loop(langkah, i)
                        i = (j + 1) if j >= 0 else i + 1
                        continue
                    loop_stack.append({"mulai": i, "sisa": jumlah,
                                       "idx": 0})
                elif jenis == "LOOP_AKHIR":
                    if loop_stack:
                        top = loop_stack[-1]
                        top["sisa"] -= 1
                        top["idx"] += 1
                        if top["sisa"] > 0:
                            i = top["mulai"] + 1
                            continue
                        loop_stack.pop()
                elif jenis in JENIS_STUDIO:
                    # v5.5: mesin langkah Studio kini fungsi modul
                    # bersama - dipakai juga oleh alur CutMotions
                    idx = loop_stack[-1]["idx"] if loop_stack else 0
                    if studio_jalankan_langkah(
                            self, l, idx, videos, caption,
                            len(videos) or int(_angka(
                                snap.get("jumlah"), 0, 0, 100000)),
                            str(snap.get("tanggal") or "")) == "stop":
                        return
                i += 1
            self._finish("Makro selesai! {} langkah sudah dijalankan."
                         .format(n))
        except Exception as e:
            self._finish("Terjadi error: {}".format(e), warn=True)


# ------------------------------------------------------------
# v5.1: potong gambar referensi LANGSUNG DI LAYAR (fullscreen).
# Layar dibekukan memenuhi seluruh monitor, lalu user MENYERET
# kotak langsung di area yang diinginkan - hanya area yang
# diseret yang disimpan (bukan seluruh layar). ESC / klik kanan
# = batal. Pengganti JendelaPotong lama (screenshot diperkecil
# dalam jendela, lalu harus tekan SIMPAN AREA).
# ------------------------------------------------------------
class OverlayPotong(tk.Toplevel):
    def __init__(self, induk, img, on_simpan, on_batal=None,
                 mode="gambar", on_area=None):
        super().__init__(induk)
        self.img = img
        self.on_simpan = on_simpan
        self.on_batal = on_batal
        self.mode = mode          # "gambar" = simpan PNG;
                                  # "area" = kembalikan koordinat
        self.on_area = on_area
        self.mulai = None
        self.akhir = (0, 0)
        self.kotak_id = None
        self.buka_id = None
        self.info_id = None

        sw = max(1, self.winfo_screenwidth())
        sh = max(1, self.winfo_screenheight())
        # Peta koordinat tampilan -> koordinat gambar asli
        # (mengatasi High-DPI / layar berbeda resolusi)
        self.skala = min(1.0, float(sw) / max(1, img.width),
                         float(sh) / max(1, img.height))
        w = max(1, int(round(img.width * self.skala)))
        h = max(1, int(round(img.height * self.skala)))

        self.overrideredirect(True)
        self.geometry("{}x{}+0+0".format(sw, sh))
        self.attributes("-topmost", True)
        self.configure(bg="black")

        # Layar gelap: seluruh screenshot diredupkan; area yang
        # diseret akan DITAMPILKAN TERANG kembali (efek snipping)
        try:
            gelap = ImageEnhance.Brightness(
                img.convert("RGB")).enhance(0.45)
        except Exception:
            gelap = img.convert("RGB")
        if self.skala != 1.0:
            gelap = gelap.resize((w, h))
        self.ph_gelap = ImageTk.PhotoImage(gelap)

        self.cv = tk.Canvas(self, width=sw, height=sh, bg="black",
                            highlightthickness=0, cursor="crosshair")
        self.cv.pack(fill="both", expand=True)
        self.cv.create_image(0, 0, image=self.ph_gelap, anchor="nw")
        self.cv.create_rectangle(0, 0, sw, 46, fill="#1C1C1C",
                                 outline="#1C1C1C")
        self.banner_id = self.cv.create_text(
            sw // 2, 23,
            text=("SERET kotak = AREA FOKUS pencarian gambar  -  gambar "
                  "referensi dicari DI DALAM kotak ini  |  ESC = batal"
                  if self.mode == "area" else
                  "SERET kotak LANGSUNG di area yang diinginkan  -  "
                  "hanya area yang diseret yang disimpan  |  "
                  "ESC = batal"),
            fill="#FFD34D", font=("Segoe UI", 13, "bold"))

        self.cv.bind("<ButtonPress-1>", self._tekan)
        self.cv.bind("<B1-Motion>", self._geser)
        self.cv.bind("<ButtonRelease-1>", self._lepas)
        self.bind("<Escape>", lambda e: self._batal())
        self.cv.bind("<Button-3>", lambda e: self._batal())

        self.deiconify()
        self.lift()
        try:
            self.focus_force()
            self.grab_set()
        except Exception:
            pass
        OVERLAY_POTONG_AKTIF.append(self)

    # ---------- util ----------
    def _peta(self, a, b):
        """Kotak koordinat tampilan -> kotak koordinat gambar asli."""
        s = self.skala
        x1 = max(0, int(round(min(a[0], b[0]) / s)))
        y1 = max(0, int(round(min(a[1], b[1]) / s)))
        x2 = min(self.img.width, int(round(max(a[0], b[0]) / s)))
        y2 = min(self.img.height, int(round(max(a[1], b[1]) / s)))
        x2 = max(x1 + 1, x2)
        y2 = max(y1 + 1, y2)
        return x1, y1, x2, y2

    def _pulihkan_banner(self):
        try:
            self.cv.itemconfigure(
                self.banner_id,
                text=("SERET kotak = AREA FOKUS pencarian gambar  -  "
                      "gambar referensi dicari DI DALAM kotak ini  |  "
                      "ESC = batal"
                      if self.mode == "area" else
                      "SERET kotak LANGSUNG di area yang diinginkan  -  "
                      "hanya area yang diseret yang disimpan  |  "
                      "ESC = batal"),
                fill="#FFD34D")
        except Exception:
            pass

    def _bersihkan_kotak(self):
        if self.kotak_id:
            self.cv.delete(self.kotak_id)
            self.kotak_id = None
        if self.buka_id:
            self.cv.delete(self.buka_id)
            self.buka_id = None
        if self.info_id:
            self.cv.delete(self.info_id)
            self.info_id = None

    def _tutup(self):
        self.mulai = None
        try:
            self.grab_release()
        except Exception:
            pass
        if self in OVERLAY_POTONG_AKTIF:
            OVERLAY_POTONG_AKTIF.remove(self)
        self.destroy()

    # ---------- event seret ----------
    def _tekan(self, ev):
        self.mulai = (ev.x, ev.y)
        self.akhir = (ev.x, ev.y)
        self._gambar_kotak()

    def _geser(self, ev):
        if not self.mulai:
            return
        self.akhir = (ev.x, ev.y)
        self._gambar_kotak()

    def _gambar_kotak(self):
        if not self.mulai:
            return
        self._bersihkan_kotak()
        d1, d2 = self.mulai, self.akhir
        dx1, dy1 = min(d1[0], d2[0]), min(d1[1], d2[1])
        dx2, dy2 = max(d1[0], d2[0]), max(d1[1], d2[1])
        self.kotak_id = self.cv.create_rectangle(
            dx1, dy1, dx2, dy2, outline="#00E676", width=2)
        # tampilkan kembali area terpilih dalam warna asli (terang)
        try:
            ix1, iy1, ix2, iy2 = self._peta(d1, d2)
            pot = self.img.convert("RGB").crop((ix1, iy1, ix2, iy2))
            if self.skala != 1.0:
                pot = pot.resize((max(1, dx2 - dx1),
                                  max(1, dy2 - dy1)))
            self.ph_buka = ImageTk.PhotoImage(pot)
            self.buka_id = self.cv.create_image(dx1, dy1,
                                                image=self.ph_buka,
                                                anchor="nw")
        except Exception:
            self.buka_id = None
        self.info_id = self.cv.create_text(
            dx1 + 4, max(52, dy1 - 12), anchor="w", fill="#00E676",
            font=("Segoe UI", 10, "bold"),
            text="{} x {} px".format(dx2 - dx1, dy2 - dy1))

    def _lepas(self, ev):
        if not self.mulai:
            return
        a, b = self.mulai, (ev.x, ev.y)
        self.mulai = None
        if abs(b[0] - a[0]) < 6 or abs(b[1] - a[1]) < 6:
            # seretan terlalu kecil - jangan simpan, beri tahu user
            self._bersihkan_kotak()
            try:
                self.cv.itemconfigure(
                    self.banner_id,
                    text="Kotak terlalu kecil - SERET dari satu titik ke "
                         "titik lain, lalu lepas  |  ESC = batal",
                    fill="#FF6B6B")
                self.after(3000, self._pulihkan_banner)
            except Exception:
                pass
            return
        self._simpan_area(a, b)

    # ---------- simpan / batal ----------
    def _simpan_area(self, a, b):
        ix1, iy1, ix2, iy2 = self._peta(a, b)
        if self.mode == "area":
            # v5.3: mode AREA FOKUS - hasil koordinat, bukan file
            koord = [ix1, iy1, ix2, iy2]
            self._tutup()
            if self.on_area:
                self.on_area(koord)
            return
        try:
            pot = self.img.crop((ix1, iy1, ix2, iy2))
        except Exception as e:
            self._tutup()
            messagebox.showerror(APP_NAME,
                                 "Gagal memotong gambar:\n{}".format(e))
            return
        nama = nama_referensi_unik()
        path = os.path.join(folder_referensi(), nama)
        gagal = False
        try:
            pot.save(path)
        except Exception:
            # fallback (warisan v4.1): biarkan user memilih lokasi
            # sendiri (Documents / Desktop, dll)
            path = filedialog.asksaveasfilename(
                title="Simpan gambar referensi",
                initialfile=nama,
                defaultextension=".png",
                filetypes=[("Gambar PNG", "*.png"),
                           ("Semua file", "*.*")])
            if not path:
                self._tutup()
                return
            try:
                pot.save(path)
            except Exception as e:
                gagal = True
                self._tutup()
                messagebox.showerror(
                    APP_NAME,
                    "Gagal menyimpan:\n{}\n\nCoba simpan ke folder lain "
                    "(mis. Documents atau Desktop).".format(e))
        if not gagal:
            self._tutup()
            if self.on_simpan:
                self.on_simpan(path)

    def _batal(self):
        cb = self.on_batal
        self._tutup()
        if cb:
            cb()


# ============================================================
# v5.0 - KERANGKA UTAMA: menubar + 2 tab + statusbar + hotkey
# ============================================================
class ShellApp:
    """Kerangka aplikasi v5.0 Macro Studio Edition.

    - Tab 1: STUDIO MAKRO (editor alur bebas ala Jitbit)
    - Tab 2: ALUR CUTMOTIONS (A-J, seperti versi sebelumnya)
    - Menubar & statusbar bersama, hotkey F6/F7 mengikuti tab aktif.
    """

    def __init__(self, root):
        self.root = root
        root.title("{} v{} - Macro Studio".format(APP_NAME, APP_VERSION))
        root.configure(bg=C_BG)
        root.geometry("1280x880")
        root.minsize(1000, 760)
        if sys.platform == "win32":
            try:
                root.iconbitmap(os.path.join(app_dir(), "icon.ico"))
            except Exception:
                pass

        if PYNPUT_OK:
            self.kb = KeyboardController()
            self.mouse = MouseController()
            self._listener = kb_mod.Listener(on_press=self._on_key)
            self._listener.daemon = True
            self._listener.start()
        else:
            self.kb = None
            self.mouse = None

        # ----- header gradien mengkilat (v5.7) -----
        HeaderKilau(root).pack(side="top", fill="x")

        # ----- statusbar bersama (paling bawah) -----
        status = tk.Frame(root, bg=C_PANEL, bd=0,
                          highlightthickness=1,
                          highlightbackground=C_LINE)
        status.pack(side="bottom", fill="x")
        self.lbl_status = tk.Label(
            status, anchor="w", bg=C_PANEL, fg=C_GREEN, font=F_S,
            text="Tahan CTRL/SHIFT saat klik baris di tabel = PILIH "
                 "BANYAK langkah sekaligus (Ctrl+A = semua)  |  "
                 "STUDIO MAKRO: susun alur bebas  |  ALUR CUTMOTIONS: "
                 "login manual dulu di situs, lalu tekan F6")
        self.lbl_status.pack(side="left", fill="x", expand=True,
                             padx=6, pady=3)
        tk.Label(status, anchor="e", bg=C_PANEL, fg=C_MUTED, font=F_XS,
                 text="v{}  |  F6 = Mulai   F7/ESC = Berhenti".format(
                     APP_VERSION)).pack(side="right", padx=6)

        # ----- notebook 2 tab -----
        gaya = ttk.Style()
        try:
            gaya.theme_use("clam")
        except Exception:
            pass
        gaya.configure("TNotebook", background=C_BG, borderwidth=0)
        gaya.configure("TNotebook.Tab", font=F_H, padding=(16, 8))
        gaya.map("TNotebook.Tab",
                 background=[("selected", C_BLUE),
                             ("!selected", C_PANEL2)],
                 foreground=[("selected", "white"),
                             ("!selected", C_MUTED)])
        # v5.6: widget pelengkap ikut tema gelap
        gaya.configure("Vertical.TScrollbar", background=C_PANEL2,
                       troughcolor=C_BG, bordercolor=C_BG,
                       arrowcolor=C_MUTED)
        gaya.configure("Horizontal.TScrollbar", background=C_PANEL2,
                       troughcolor=C_BG, bordercolor=C_BG,
                       arrowcolor=C_MUTED)
        gaya.configure("TCombobox", fieldbackground=C_PANEL,
                       background=C_PANEL2, foreground=C_TEXT,
                       arrowcolor=C_TEXT)
        self.nb = ttk.Notebook(root)
        self.nb.pack(fill="both", expand=True)
        f_studio = tk.Frame(self.nb, bg=C_BG)
        f_cut = tk.Frame(self.nb, bg=C_BG)
        self.nb.add(f_studio, text="  STUDIO MAKRO (alur bebas)  ")
        self.nb.add(f_cut, text="  ALUR CUTMOTIONS (A-J)  ")

        self.tab_studio = StudioMakroTab(f_studio, self)
        self.tab_cut = CutMotionsTab(f_cut, self)
        self._build_menubar()
        root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ---------- menubar ----------
    def _build_menubar(self):
        menubar = tk.Menu(self.root)

        m_berkas = tk.Menu(menubar, tearoff=0)
        m_berkas.add_command(label="Makro Baru (kosongkan Studio)",
                             command=self.tab_studio._makro_baru)
        m_berkas.add_command(label="Buka Makro Studio...",
                             command=self.tab_studio._buka_makro)
        m_berkas.add_command(label="Simpan Makro Studio...",
                             command=self.tab_studio._simpan_makro)
        m_berkas.add_separator()
        m_berkas.add_command(label="Simpan Profil CutMotions...",
                             command=self.tab_cut._simpan_profil)
        m_berkas.add_command(label="Buka Profil CutMotions...",
                             command=self.tab_cut._buka_profil)
        m_berkas.add_separator()
        m_berkas.add_command(label="Keluar", command=self._on_close)
        menubar.add_cascade(label="Berkas", menu=m_berkas)

        m_lang = tk.Menu(menubar, tearoff=0)
        m_lang.add_command(
            label="● Rekam Aksi di TAB AKTIF - klik/ketik/scroll direkam "
                  "jadi langkah (F8 = berhenti)",
            command=lambda: self.tab_aktif()._rekam_mulai())
        m_lang.add_separator()
        for jenis, label in [
            ("KLIK", "Tambah KLIK TITIK"),
            ("JEDA", "Tambah JEDA / TUNGGU"),
            ("GAMBAR", "Tambah CARI GAMBAR (klik / pindah kursor)"),
            ("KETIK", "Tambah KETIK TEKS"),
            ("TANGGAL_JAM", "Tambah ISI TANGGAL-JAM (kolom tanggal rilis)"),
            ("VIDEO_CAPTION",
             "Tambah ISI VIDEO & CAPTION (jumlah + caption + nama video)"),
            ("TOMBOL", "Tambah TEKAN TOMBOL"),
            ("SCROLL", "Tambah SCROLL"),
            ("CATATAN", "Tambah CATATAN"),
        ]:
            m_lang.add_command(
                label=label,
                command=lambda j=jenis: self.tab_studio._tambah(j))
        m_lang.add_separator()
        m_lang.add_command(label="Tambah ULANGI - MULAI",
                           command=lambda: self.tab_studio._tambah(
                               "LOOP_MULAI"))
        m_lang.add_command(label="Tambah ULANGI - AKHIR",
                           command=lambda: self.tab_studio._tambah(
                               "LOOP_AKHIR"))
        m_lang.add_separator()
        m_lang.add_command(label="Salin Langkah  (Ctrl+C)",
                           command=self.tab_studio._salin)
        m_lang.add_command(label="Tempel Langkah  (Ctrl+V)",
                           command=self.tab_studio._tempel)
        m_lang.add_command(label="Hapus Langkah  (Del)",
                           command=self.tab_studio._hapus)
        menubar.add_cascade(label="Studio", menu=m_lang)

        m_alat = tk.Menu(menubar, tearoff=0)
        m_alat.add_command(label="Potong Gambar - seret langsung di "
                                 "layar (langkah Studio terpilih)",
                           command=self.tab_studio._potong_dari_menu)
        m_alat.add_command(label="Tes Cari Gambar (langkah Studio "
                                 "terpilih)",
                           command=self.tab_studio._tes_cari)
        m_alat.add_separator()
        # v5.5: semua menu Studio Makro juga bisa masuk alur CutMotions
        m_alat.add_command(
            label="Tambah Langkah Studio ke Alur CutMotions "
                  "(pakai tombol '+ TAMBAH LANGKAH' di tab itu)",
            command=lambda: (self.nb.select(self.tab_cut.wadah),
                             self.tab_cut._tambah_studio("KLIK")))
        m_alat.add_command(label="Muat Template Alur CutMotions ke Studio",
                           command=self.tab_studio._template_cutmotions)
        m_alat.add_separator()
        m_alat.add_command(label="Lihat Riwayat Upload...",
                           command=self.tab_cut._lihat_riwayat)
        m_alat.add_command(label="Bersihkan Riwayat Folder Ini",
                           command=self.tab_cut._bersihkan_riwayat)
        m_alat.add_separator()
        m_alat.add_command(label="Reset Semua Posisi CutMotions",
                           command=self.tab_cut._reset_posisi)
        m_alat.add_command(label="Cek Kelengkapan Library",
                           command=self.tab_cut._cek_lengkap)
        menubar.add_cascade(label="Alat", menu=m_alat)

        m_bantu = tk.Menu(menubar, tearoff=0)
        m_bantu.add_command(label="Buka Panduan",
                            command=self.tab_cut._buka_panduan)
        m_bantu.add_command(label="Tentang", command=self._tentang)
        menubar.add_cascade(label="Bantuan", menu=m_bantu)
        self.root.config(menu=menubar)

    # ---------- routing tab & hotkey ----------
    def tab_aktif(self):
        try:
            return (self.tab_studio
                    if self.nb.index(self.nb.select()) == 0
                    else self.tab_cut)
        except Exception:
            return self.tab_studio

    def tab_lain(self, t):
        return self.tab_cut if t is self.tab_studio else self.tab_studio

    def _on_key(self, key):
        try:
            # v5.1: saat layar potong gambar terbuka (fullscreen),
            # abaikan hotkey F6/F7 supaya alur tidak mulai tiba-tiba
            if OVERLAY_POTONG_AKTIF:
                return
            # v5.4: selagi REKAM AKSI berlangsung, F6/F7/ESC diabaikan
            # (F8/ESC ditangani listener perekam sendiri)
            # v5.6: perekam bisa berjalan di tab Studio ATAU tab CutMotions
            if getattr(self.tab_studio, "merekam", False) \
                    or getattr(self.tab_cut, "merekam", False):
                return
            if key == kb_mod.Key.f6:
                self.root.after(0, lambda: self.tab_aktif()._start())
            elif key in (kb_mod.Key.f7, kb_mod.Key.esc):
                self.root.after(0, self._stop_semua)
        except Exception:
            pass

    def _stop_semua(self):
        self.tab_studio._stop()
        self.tab_cut._stop()

    def _tentang(self):
        messagebox.showinfo(
            APP_NAME,
            "{} v{} - Macro Studio Edition\n\n"
            "DUA MODE dalam satu aplikasi:\n\n"
            "1. STUDIO MAKRO (baru v5.0) - editor alur kerja bebas\n"
            "ala Jitbit Macro Recorder: semua jenis aksi jadi menu\n"
            "tersendiri di atas (+ Klik, + Jeda, + Cari Gambar,\n"
            "+ Ketik Teks, + Tekan Tombol, + Scroll, + Ulangi) dan\n"
            "tabel kosong di bawahnya untuk menyusun alur sendiri.\n\n"
            "v5.1: POTONG GAMBAR seret langsung di layar (fullscreen)\n"
            "dan setiap potongan jadi file baru - referensi CARI\n"
            "GAMBAR bisa dipakai berkali-kali, beda-beda gambarnya.\n\n"
            "v5.2: 2 MENU BARU di Studio - ISI TANGGAL-JAM (mengisi\n"
            "kolom tanggal-jam rilis otomatis) dan ISI VIDEO & CAPTION\n"
            "(mengisi jumlah video, atau caption dasar + nama video).\n\n"
            "v5.3: CARI GAMBAR TANPA X,Y - gambar referensi langsung\n"
            "diklik begitu ketemu; daerah pencarian dibatasi AREA\n"
            "FOKUS yang dipilih dengan menyeret kotak di layar.\n\n"
            "v5.4: REKAM AKSI - rekam klik/ketikan/scrollmu LANGSUNG\n"
            "jadi langkah makro: klik ● REKAM AKSI, jendela sembunyi,\n"
            "kerjakan aksimu di aplikasi lain, lalu tekan F8 untuk\n"
            "berhenti - semuanya sudah jadi langkah di tabel Studio.\n\n"
            "v5.5: SEMUA MENU STUDIO MAKRO masuk alur CUTMOTIONS!\n"
            "Di tab Alur CutMotions ada tombol '+ TAMBAH LANGKAH' untuk\n"
            "menyisipkan Klik, Jeda, Cari Gambar, Ketik, Tanggal-Jam,\n"
            "Video+Caption, Tombol, Scroll, Catatan, dan blok ULANGI\n"
            "di posisi mana pun di antara langkah A-J.\n\n"
            "v5.6: TAMPILAN BARU 'DARK GLASS' yang lebih modern &\n"
            "mengkilat - tombol dirapi maksimal 7 per baris, sisanya\n"
            "berurutan di baris bawah. REKAM AKSI kini juga ada di\n"
            "tab ALUR CUTMOTIONS (A-J): hasil rekaman langsung masuk\n"
            "alur A-J tepat setelah langkah yang kamu pilih.\n\n"
            "v5.7: PILIH BANYAK LANGKAH SEKALIGUS - tahan CTRL atau\n"
            "SHIFT saat mengklik baris di tabel (Shift+Klik = rentang,\n"
            "Ctrl+Klik = tambah/kurang, Ctrl+A = semua), lalu SALIN /\n"
            "TEMPEL / HAPUS / AKTIF-MATI berlaku untuk semuanya.\n"
            "Desain makin modern & elegan: tombol kapsul membulat\n"
            "mengkilat, panel bersudut membulat, dan header gradien.\n\n"
            "2. ALUR CUTMOTIONS (A-J) - uploader batch CutMotions.\n\n"
            "Maksimal {} video sekali jalan (aturan situs).\n"
            "Login dilakukan manual - tidak ada data akun yang disimpan."
            .format(APP_NAME, APP_VERSION, MAX_BATCH))

    def _on_close(self):
        try:
            self.tab_studio._rekam_berhenti()
        except Exception:
            pass
        try:
            self.tab_cut._rekam_berhenti()
        except Exception:
            pass
        try:
            self.tab_studio._simpan_auto()
            self.tab_cut._save_settings()
            self.tab_cut._save_riwayat()
            self._stop_semua()
            if PYNPUT_OK and hasattr(self, "_listener"):
                self._listener.stop()
        finally:
            self.root.destroy()


def main():
    root = tk.Tk()
    app = ShellApp(root)
    if "--selftest" in sys.argv:
        def _ok():
            print("SELFTEST_OK")
            root.destroy()
        root.after(1800, _ok)
    if "--selftest-prop" in sys.argv:
        def _pilih():
            app.tab_cut.tree.selection_set("pos_pilih_neg")
            app.tab_cut.tree.event_generate("<<TreeviewSelect>>")
        root.after(800, _pilih)

        def _ok2():
            print("SELFTEST_PROP_OK")
            root.destroy()
        root.after(3000, _ok2)
    if "--selftest-studio" in sys.argv:
        def _isi():
            st = app.tab_studio
            st._tambah("KLIK")
            st._tambah("JEDA")
            st._tambah("KETIK")
            st._tambah("TANGGAL_JAM")
            st._tambah("VIDEO_CAPTION")
            st._tambah("LOOP_MULAI")
            st._tambah("KLIK")
            st._tambah("LOOP_AKHIR")
            st._naik()
            st._turun()
            print("STUDIO_STEPS_OK", len(st.langkah))
        root.after(700, _isi)

        def _ok3():
            print("SELFTEST_STUDIO_OK")
            root.destroy()
        root.after(2800, _ok3)
    if "--selftest-rekam" in sys.argv:
        def _rekam_uji():
            st = app.tab_studio
            ev = [
                {"tipe": "klik", "x": 100, "y": 200, "tombol": "kiri",
                 "waktu": 1000.0},
                {"tipe": "char", "teks": "h", "waktu": 1000.6},
                {"tipe": "char", "teks": "a", "waktu": 1000.7},
                {"tipe": "char", "teks": "l", "waktu": 1000.8},
                {"tipe": "tombol", "nama": "Enter", "waktu": 1001.2},
                {"tipe": "scroll", "arah": "Turun", "waktu": 1001.6},
                {"tipe": "scroll", "arah": "Turun", "waktu": 1001.8},
                {"tipe": "klik", "x": 300, "y": 400, "tombol": "kiri",
                 "waktu": 1002.5},
                {"tipe": "klik", "x": 301, "y": 401, "tombol": "kiri",
                 "waktu": 1002.7},
                {"tipe": "klik", "x": 500, "y": 500, "tombol": "kanan",
                 "waktu": 1003.4},
            ]
            baru, uid_akhir = perekam_bangun_langkah(ev, st._uid)
            st._uid = max(st._uid, uid_akhir)
            st.langkah.extend(baru)
            st.sel = baru[0]["uid"] if baru else None
            st._refresh_tabel()
            print("REKAM_LANGKAH_OK", len(baru))
        root.after(700, _rekam_uji)

        def _ok4():
            print("SELFTEST_REKAM_OK")
            root.destroy()
        root.after(2500, _ok4)
    if "--selftest-cutstudio" in sys.argv:
        def _isi_cut():
            # v5.5: semua menu Studio dimasukkan ke alur CutMotions
            cut = app.tab_cut
            cut.tree.selection_set("pos_oke")
            cut.tree.event_generate("<<TreeviewSelect>>")

            def isi():
                cut._tambah_studio("CATATAN")
                cut._tambah_studio("KETIK")
                cut._tambah_studio("JEDA")
                cut._tambah_studio("LOOP_MULAI")
                cut._tambah_studio("KLIK")
                cut._tambah_studio("TOMBOL")
                cut._tambah_studio("SCROLL")
                cut._tambah_studio("LOOP_AKHIR")
                cut._tambah_studio("GAMBAR")
                cut._tambah_studio("TANGGAL_JAM")
                cut._tambah_studio("VIDEO_CAPTION")
                n_studio = sum(1 for e in cut.langkah_extra
                               if e.get("jenis") in JENIS_STUDIO)
                print("CUT_STUDIO_LANGKAH_OK", n_studio)
                # salin-tempel langkah Studio di alur CutMotions
                cut._salin_langkah()
                cut._tempel_langkah()
                n2 = sum(1 for e in cut.langkah_extra
                         if e.get("jenis") in JENIS_STUDIO)
                print("CUT_STUDIO_TEMPEL_OK", n2 == n_studio + 1)

            root.after(300, isi)
        root.after(700, _isi_cut)

        def _ok5():
            print("SELFTEST_CUTSTUDIO_OK")
            root.destroy()
        root.after(2500, _ok5)
    if "--selftest-rekam-cut" in sys.argv:
        def _rekam_cut():
            # v5.6: hasil rekaman masuk ALUR CUTMOTIONS (A-J)
            cut = app.tab_cut
            cut.tree.selection_set("pos_oke")
            cut.tree.event_generate("<<TreeviewSelect>>")
            n_awal = len(cut.langkah_extra)
            ev = [
                {"tipe": "klik", "x": 120, "y": 240, "tombol": "kiri",
                 "waktu": 2000.0},
                {"tipe": "char", "teks": "d", "waktu": 2000.5},
                {"tipe": "char", "teks": "a", "waktu": 2000.6},
                {"tipe": "char", "teks": "d", "waktu": 2000.7},
                {"tipe": "char", "teks": "a", "waktu": 2000.75},
                {"tipe": "char", "teks": "n", "waktu": 2000.8},
                {"tipe": "tombol", "nama": "Tab", "waktu": 2001.1},
                {"tipe": "scroll", "arah": "Turun", "waktu": 2001.5},
                {"tipe": "scroll", "arah": "Turun", "waktu": 2001.7},
                {"tipe": "klik", "x": 420, "y": 520, "tombol": "kiri",
                 "waktu": 2002.4},
                {"tipe": "klik", "x": 560, "y": 520, "tombol": "kanan",
                 "waktu": 2003.2},
            ]
            baru, uid_akhir = perekam_bangun_langkah(ev, 0)
            cut.perekam_sisipkan(baru, uid_akhir)
            n_baru = len(cut.langkah_extra) - n_awal
            print("CUT_REKAM_LANGKAH_OK", len(baru))
            print("CUT_REKAM_EXTRA_OK", n_baru == len(baru))
            print("CUT_REKAM_SEL_OK", cut.sel == baru[0]["uid"])
            # antrean setelah harus berantai urut seperti hasil rekam
            rantai = all(baru[i + 1]["setelah"] == baru[i]["uid"]
                         for i in range(len(baru) - 1))
            print("CUT_REKAM_RANTAI_OK", rantai)

        root.after(700, _rekam_cut)

        def _ok6():
            print("SELFTEST_REKAMCUT_OK")
            root.destroy()
        root.after(2500, _ok6)
    if "--selftest-multi" in sys.argv:
        def _uji_multi():
            # v5.7: pilih banyak -> salin / tempel / hapus massal
            asli_ask = messagebox.askyesno
            messagebox.askyesno = lambda *a, **k: True
            try:
                # ---- tab STUDIO ----
                st = app.tab_studio
                for j in ("KLIK", "JEDA", "KETIK", "TOMBOL"):
                    st._tambah(j)
                uids = [l["uid"] for l in st.langkah]
                st.tree.selection_set(uids[0], uids[1], uids[2])
                st._salin()
                print("MULTI_SALIN_OK",
                      len(st.papan_klip.get("banyak", ())) == 3)
                st.sel = uids[-1]
                st.tree.selection_set(uids[-1])
                st._tempel()
                print("MULTI_TEMPEL_OK", len(st.langkah) == 7)
                st.tree.selection_set(*[l["uid"] for l in st.langkah[2:5]])
                st._hapus()
                print("MULTI_HAPUS_OK", len(st.langkah) == 4)
                st.tree.selection_set(*[l["uid"] for l in st.langkah])
                st._toggle_aktif()
                print("MULTI_AKTIF_OK",
                      all(not l.get("aktif", True) for l in st.langkah))
                # ---- tab CUTMOTIONS ----
                cut = app.tab_cut
                cut.tree.selection_set("pos_oke")
                cut.tree.event_generate("<<TreeviewSelect>>")
                cut._tambah_studio("KLIK")
                cut._tambah_studio("JEDA")
                n_awal = len(cut.langkah_extra)
                dua = [e["uid"] for e in cut.langkah_extra[-2:]]
                cut.tree.selection_set("pos_tanggal", *dua)
                cut._salin_langkah()
                print("CUT_MULTI_SALIN_OK",
                      len(cut.papan_klip.get("banyak", ())) == 3)
                cut.sel = "pos_oke"
                cut.tree.selection_set("pos_oke")
                cut._tempel_langkah()
                print("CUT_MULTI_TEMPEL_OK",
                      len(cut.langkah_extra) == n_awal + 3)
                tiga = [e["uid"] for e in cut.langkah_extra[-3:]]
                cut.tree.selection_set(*tiga)
                cut._hapus_langkah()
                print("CUT_MULTI_HAPUS_OK",
                      len(cut.langkah_extra) == n_awal)
            finally:
                messagebox.askyesno = asli_ask
            print("MULTI_DONE")
        root.after(700, _uji_multi)

        def _ok7():
            print("SELFTEST_MULTI_OK")
            root.destroy()
        root.after(3200, _ok7)
    if "--selftest-uid" in sys.argv:
        def _uji_uid():
            # v5.8: CARI GAMBAR bisa ditambah BERAPAPUN kalinya -
            # uid langkah baru tidak boleh MENABRAK uid langkah lama
            # (bug lama: setelah hapus langkah + buka ulang aplikasi,
            # nomor lanjut dari JUMLAH langkah lalu menabrak uid lama
            # sehingga langkah baru tak muncul di tabel)
            cut = app.tab_cut
            cut.tree.selection_set("pos_oke")
            cut.tree.event_generate("<<TreeviewSelect>>")
            # ---- replika profil "rusak" deterministik: langkah lama
            #      ber-uid x5 & x9, nomor lanjut = jumlah (kode lama)
            cut.langkah_extra = []
            cut._extra_counter = 0
            lama = []
            for u, nm in (("x5", "LAMA-1"), ("x9", "LAMA-2")):
                e = studio_langkah_baru("GAMBAR", 0)
                e["uid"] = u
                e["setelah"] = "pos_oke" if not lama else lama[-1]["uid"]
                e["label"] = "CARI GAMBAR {}".format(nm)
                lama.append(e)
            cut.langkah_extra.extend(lama)
            cut._extra_counter = len(cut.langkah_extra)  # kode lama
            # ---- tambah 10x CARI GAMBAR: semua harus muncul unik
            for _ in range(10):
                cut._tambah_studio("GAMBAR")
            uids = [e["uid"] for e in cut.langkah_extra]
            print("UID_UNIK_OK", len(uids) == len(set(uids)))
            print("UID_TAMBAH_OK", len(uids) == 12)
            print("UID_LAMA_UTUH_OK",
                  lama[0]["uid"] == "x5" and lama[1]["uid"] == "x9")
            tampil = set(cut._urutan_lengkap())
            print("UID_TAMPIL_OK", all(u in tampil for u in uids))
            # ---- muat ulang profil: uid dobel dipaksa lalu sembuh
            data = json.loads(json.dumps(cut._kumpulkan_data()))
            data["langkah_extra"][-1]["uid"] = \
                data["langkah_extra"][-2]["uid"]
            cut._terapkan_data(data)
            uids2 = [e["uid"] for e in cut.langkah_extra]
            print("UID_SEMBUH_OK", len(uids2) == len(set(uids2)))
            print("UID_LANJUT_OK", cut._extra_counter >= max(
                int(u[1:]) for u in uids2 if u[1:].isdigit()))
            cut._tambah_studio("GAMBAR")
            print("UID_STLH_MUAT_OK",
                  cut.langkah_extra[-1]["uid"] not in uids2)
            print("UID_DONE")
        root.after(700, _uji_uid)

        def _ok8():
            print("SELFTEST_UID_OK")
            root.destroy()
        root.after(3600, _ok8)
    if "--selftest-hapus" in sys.argv:
        def _uji_hapus():
            # v5.9: (1) validasi F6 per kolom - koma & kolom kosong OK;
            # (2) langkah bawaan A-J BISA dihapus & dikembalikan
            print("ANGKA_BULAT_OK",
                  _baca_angka("X", "5", None, bulat=True) == 5)
            print("ANGKA_KOMA_OK", _baca_angka("X", "1,5") == 1.5)
            print("ANGKA_KOMA_BULAT_OK",
                  _baca_angka("X", "2,0", None, bulat=True) == 2)
            print("ANGKA_KOSONG_OK", _baca_angka("X", "", 5) == 5
                  and _baca_angka("X", None, 2.5) == 2.5)
            try:
                _baca_angka("KOLONI UJI", "abc", 1)
                print("ANGKA_JELEK_OK", False)
            except ValueError as e:
                print("ANGKA_JELEK_OK",
                      e.args[0] == ("KOLONI UJI", "abc"))

            cut = app.tab_cut
            asli_ask = messagebox.askyesno
            messagebox.askyesno = lambda *a, **k: True
            try:
                # langkah tambahan menempel di E - harus tetap tampil
                # walau E dihapus
                cut.tree.selection_set("pos_oke")
                cut.tree.event_generate("<<TreeviewSelect>>")
                cut._tambah_studio("GAMBAR")
                uid_ekstra = cut.langkah_extra[-1]["uid"]
                cut.tree.selection_set("pos_oke")
                cut._hapus_langkah()
                print("HAPUS_SLOT_OK", "pos_oke" in cut.slot_mati)
                urut = cut._urutan_lengkap()
                print("HAPUS_TAMPIL_OK", "pos_oke" not in urut)
                print("HAPUS_ANAK_UTUH_OK", uid_ekstra in urut)
                tampil = set(cut.tree.get_children())
                print("HAPUS_BARIS_HILANG_OK", "pos_oke" not in tampil)
                # mesin: langkah mati -> ("skip", None)
                snap = cut._snapshot()
                aksi, nil = cut._langkah_klik(
                    snap, "pos_oke", None, 1.0, nama="E (tombol OKE)")
                print("HAPUS_MESIN_SKIP_OK", aksi == "skip" and nil
                      is None)
                # simpan-muat: slot_mati ikut tersimpan & dipulihkan
                data = json.loads(json.dumps(cut._kumpulkan_data()))
                print("HAPUS_SIMPAN_OK",
                      data.get("slot_mati") == ["pos_oke"])
                cut.slot_mati = set()
                cut._terapkan_data(data)
                print("HAPUS_MUAT_OK", cut.slot_mati == {"pos_oke"})
                # kembalikan langkah bawaan
                cut.slot_mati.discard("pos_oke")
                cut._refresh_tabel()
                print("HAPUS_KEMBALI_OK",
                      "pos_oke" in cut._urutan_lengkap())
            finally:
                messagebox.askyesno = asli_ask
            print("HAPUS_DONE")
        root.after(700, _uji_hapus)

        def _ok9():
            print("SELFTEST_HAPUS_OK")
            root.destroy()
        root.after(3600, _ok9)
    root.mainloop()
    if ("--selftest" in sys.argv) or ("--selftest-prop" in sys.argv) \
            or ("--selftest-studio" in sys.argv) \
            or ("--selftest-rekam" in sys.argv) \
            or ("--selftest-cutstudio" in sys.argv) \
            or ("--selftest-rekam-cut" in sys.argv) \
            or ("--selftest-multi" in sys.argv) \
            or ("--selftest-uid" in sys.argv) \
            or ("--selftest-hapus" in sys.argv):
        print("SELFTEST_DONE")


if __name__ == "__main__":
    main()
