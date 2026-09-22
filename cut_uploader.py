# -*- coding: utf-8 -*-
"""
============================================================
  CUTUPLOADER PRO  v3.0
  Aplikasi desktop uploader video batch otomatis
  khusus untuk situs CutMotions (Kwai)
------------------------------------------------------------
  Alur situs yang diikuti aplikasi ini (urutan posisi A-J):
    1. Login manual (email / kata sandi)
    2. Pilih "Versi lama"  ->  "Rilis karya"
    3. Tekan F6, lalu aplikasi mengerjakan:
       A  Klik tombol "Jadwal rilis / publikasi"
       B  Klik dropdown "NEGARA"
       C  Pilih negara — klik biasa ATAU pencarian gambar
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

  Dibuat dengan Python + tkinter + pynput (+ OpenCV/Pillow
  untuk pencarian gambar negara — opsional).
  Fokus utama: Windows desktop.
============================================================
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import time
import json
import datetime
import os
import sys

# Tampilan tajam di layar Windows beresolusi tinggi (High-DPI)
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
# Pencarian gambar di layar (opsional): dipakai untuk memilih
# NEGARA lewat gambar referensi (template matching OpenCV).
# ------------------------------------------------------------
CV_OK = False
try:
    import cv2
    import numpy as np
    from PIL import ImageGrab
    CV_OK = True
except Exception:
    CV_OK = False

APP_NAME = "CutUploader Pro"
APP_VERSION = "3.0"

VIDEO_EXTS = (".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v",
              ".3gp", ".flv", ".wmv", ".ts")

MAX_BATCH = 20    # batas situs: maks 20 video sekali upload
JUDUL_MAX = 250   # batas karakter judul video di situs


def app_dir():
    """Folder tempat aplikasi berada (aman juga saat sudah jadi .exe)."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


SETTINGS_FILE = os.path.join(app_dir(), "cutuploader_settings.json")
RIWAYAT_FILE = os.path.join(app_dir(), "cutuploader_riwayat.json")

# ------------------------------------------------------------
# Tema warna: dark neon (satu keluarga dengan Auto Typer Pro)
# ------------------------------------------------------------
C_BG       = "#0f1220"
C_CARD     = "#171b30"
C_LINE     = "#2a3054"
C_ACCENT   = "#00e68a"
C_ACCENT_D = "#0f9d63"
C_RED      = "#ff4d6d"
C_RED_D    = "#c7314e"
C_YELLOW   = "#ffd166"
C_BLUE     = "#4da3ff"
C_TEXT     = "#eef0ff"
C_MUTED    = "#9aa0c3"
C_ENTRY    = "#232948"
C_BTN_TXT  = "#052e1d"

F_TITLE = ("Segoe UI", 17, "bold")
F_SUB   = ("Segoe UI", 9)
F_H     = ("Segoe UI", 10, "bold")
F_N     = ("Segoe UI", 10)
F_S     = ("Segoe UI", 9)
F_MONO  = ("Consolas", 10, "bold")

# ------------------------------------------------------------
# Definisi 13 slot posisi klik di situs CutMotions (urutan A-J)
#   (kunci, label pendek, wajib?, nama lengkap)
# ------------------------------------------------------------
POSISI_DEF = [
    ("pos_jadwal",     "A · Jadwal rilis",        True,
     "TOMBOL 'JADWAL RILIS / PUBLIKASI'"),
    ("pos_negara",     "B · Dropdown NEGARA",     True,
     "DROPDOWN / KOTAK 'NEGARA' (sebelum daftar terbuka)"),
    ("pos_pilih_neg",  "C · Pilih negara",        True,
     "ITEM 'INDONESIA' PADA DAFTAR NEGARA (atau titik klik biasa "
     "bila tidak memakai pencarian gambar)"),
    ("pos_tanggal",    "D · Kolom tanggal-jam",   True,
     "KOLOM TANGGAL & JAM RILIS (tanggal-jam diketik otomatis)"),
    ("pos_oke",        "E · Tombol OKE",          True,
     "TOMBOL 'OKE' PADA DIALOG JADWAL"),
    ("pos_tambah",     "F · + Tambah video",      True,
     "TOMBOL '+ TAMBAH VIDEO'"),
    ("pos_bebas1",     "G · Klik bebas 1",        True,
     "TITIK KLIK BEBAS DI DIALOG PILIH FILE (bisa diulang + scroll)"),
    ("pos_video",      "H · Video pertama",       True,
     "VIDEO PERTAMA DI DAFTAR FILE (diklik, lalu Shift+panah bawah)"),
    ("pos_bebas2",     "H2 · Klik bebas 2",       True,
     "TOMBOL 'BUKA/OPEN' / KLIK BEBAS SETELAH VIDEO TERPILIH"),
    ("pos_edit",       "I1 · EDIT baris-1",       True,
     "TOMBOL 'EDIT' PADA BARIS VIDEO TERATAS"),
    ("pos_judul",      "I2 · Kotak caption baris-1", True,
     "KOTAK CAPTION / JUDUL PADA BARIS TERATAS (saat editor terbuka)"),
    ("pos_konfirmasi", "I3 · Konfirmasi (opsional)", False,
     "TOMBOL 'KONFIRMASI' BARIS TERATAS — KOSONGKAN bila letaknya "
     "sama dengan tombol EDIT (I1)"),
    ("pos_submit",     "J · Tombol SUBMIT",       True,
     "TOMBOL 'SUBMIT / KIRIM' (halaman sudah discroll ke bawah)"),
]
POS_KUNCI = [p[0] for p in POSISI_DEF]
POS_WAJIB = [p[0] for p in POSISI_DEF if p[2]]
JUDUL_POSISI = {p[0]: p[3] for p in POSISI_DEF}


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


def cari_di_layar(gambar_path, cx, cy, radius, kemiripan=0.8):
    """Cari gambar referensi di layar dalam RADIUS piksel dari titik
    acuan (cx, cy) — dipakai untuk memilih negara lewat gambar.

    Kembalikan (x, y, skor) titik tengah kecocokan terbaik,
    atau None bila tidak ketemu / OpenCV tidak tersedia.
    """
    if not CV_OK:
        return None
    try:
        tpl = cv2.imread(gambar_path)
        if tpl is None:
            return None
        th, tw = tpl.shape[:2]
        r = max(int(radius), tw // 2 + 20, th // 2 + 20)
        left = max(0, int(cx) - r)
        top = max(0, int(cy) - r)
        grab = ImageGrab.grab(bbox=(left, top, int(cx) + r, int(cy) + r))
        layar = np.array(grab)[:, :, ::-1].copy()   # RGB -> BGR
        if layar.shape[0] < th or layar.shape[1] < tw:
            return None
        hasil = cv2.matchTemplate(layar, tpl, cv2.TM_CCOEFF_NORMED)
        _mn, skor, _mnloc, lok = cv2.minMaxLoc(hasil)
        if skor >= kemiripan:
            return (left + lok[0] + tw // 2,
                    top + lok[1] + th // 2, skor)
    except Exception:
        return None
    return None


class CutUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("{} v{}".format(APP_NAME, APP_VERSION))
        self.root.configure(bg=C_BG)
        self.root.geometry("640x960")
        self.root.minsize(540, 640)

        self.stop_event = threading.Event()
        self.running = False
        self.gambar_ref = ""  # path gambar referensi negara (pencarian C)

        # ---- data browser: satu entri per browser ----
        # {"nama": str, "folder": str,
        #  "pos_tambah": [x,y]|None, ... 9 slot posisi}
        self.browsers = []
        self.aktif = 0
        self._loading = False  # penjaga event listbox saat refresh

        # ---- riwayat upload: {"nama||folder": [nama file, ...]} ----
        # urutan isi riwayat = urutan baris video di situs (atas ke bawah)
        self.riwayat = {}

        if PYNPUT_OK:
            self.kb = KeyboardController()
            self.mouse = MouseController()
            self._listener = kb_mod.Listener(on_press=self._on_key)
            self._listener.daemon = True
            self._listener.start()

        self._build_ui()
        self._load_settings()
        self._load_riwayat()
        self._refresh_browser_list(keep=self.aktif)
        self._update_count()
        self._update_preview()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ================== PEMBANGUNAN TAMPILAN ==================
    def _card(self, title):
        outer = tk.Frame(self.body, bg=C_CARD,
                         highlightbackground=C_LINE, highlightthickness=1)
        outer.pack(fill="x", padx=14, pady=(8, 0))
        tk.Label(outer, text=title, bg=C_CARD, fg=C_ACCENT,
                 font=F_H, anchor="w").pack(fill="x", padx=14, pady=(10, 2))
        inner = tk.Frame(outer, bg=C_CARD)
        inner.pack(fill="both", expand=True, padx=14, pady=(0, 12))
        return inner

    def _field(self, parent, label, initial=""):
        tk.Label(parent, text=label, bg=C_CARD, fg=C_MUTED,
                 font=F_S, anchor="w").pack(fill="x", pady=(6, 1))
        ent = tk.Entry(parent, bg=C_ENTRY, fg=C_TEXT, insertbackground=C_TEXT,
                       relief="flat", font=F_N, highlightthickness=1,
                       highlightbackground=C_LINE, highlightcolor=C_ACCENT)
        ent.pack(fill="x", ipady=6)
        if initial:
            ent.insert(0, initial)
        return ent

    def _field_mini(self, parent, label, initial="", width=7):
        """Entry kecil sebaris (untuk angka: radius, jumlah klik, dll)."""
        tk.Label(parent, text=label, bg=C_CARD, fg=C_MUTED,
                 font=F_S).pack(side="left")
        ent = tk.Entry(parent, bg=C_ENTRY, fg=C_TEXT,
                       insertbackground=C_TEXT, relief="flat",
                       font=F_N, width=width, justify="center",
                       highlightthickness=1, highlightbackground=C_LINE,
                       highlightcolor=C_ACCENT)
        ent.pack(side="left", ipady=4, padx=(4, 10))
        if initial:
            ent.insert(0, initial)
        return ent

    def _btn(self, parent, text, cmd, bg=C_ENTRY, fg=C_TEXT,
             font=("Segoe UI", 9, "bold"), padx=0):
        b = tk.Button(parent, text=text, command=cmd, bg=bg, fg=fg,
                      font=font, relief="flat", bd=0, cursor="hand2",
                      activebackground=C_LINE, activeforeground=fg)
        if padx:
            b.pack(side="left", ipady=5, padx=(padx, 0))
        else:
            b.pack(side="left", ipady=5)
        return b

    def _check(self, parent, text, var, cmd=None):
        cb = tk.Checkbutton(parent, text=text, variable=var,
                            bg=C_CARD, fg=C_TEXT, activebackground=C_CARD,
                            activeforeground=C_TEXT, selectcolor=C_ENTRY,
                            font=F_S, bd=0, highlightthickness=0,
                            command=cmd, cursor="hand2", anchor="w")
        cb.pack(fill="x", pady=(8, 0))
        return cb

    def _on_wheel(self, e):
        try:
            if getattr(e, "delta", 0) > 0:
                self.canvas.yview_scroll(-1, "units")
            elif getattr(e, "delta", 0) < 0:
                self.canvas.yview_scroll(1, "units")
        except Exception:
            pass

    def _build_ui(self):
        # ----- Judul -----
        head = tk.Frame(self.root, bg=C_BG)
        head.pack(fill="x", padx=18, pady=(12, 4))
        tk.Label(head, text="CUTUPLOADER PRO", bg=C_BG, fg=C_ACCENT,
                 font=F_TITLE).pack(anchor="w")
        tk.Label(head, text="Uploader batch otomatis CutMotions (Kwai) — "
                            "Jadwal → Tambah video (Shift+↓) → Caption → "
                            "Submit",
                 bg=C_BG, fg=C_MUTED, font=F_SUB).pack(anchor="w")

        # ----- Area isi yang bisa digulir (scroll) -----
        container = tk.Frame(self.root, bg=C_BG)
        container.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(container, bg=C_BG, highlightthickness=0,
                                bd=0)
        vsb = tk.Scrollbar(container, orient="vertical",
                           command=self.canvas.yview, width=10, bd=0,
                           elementborderwidth=0, troughcolor=C_BG)
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.body = tk.Frame(self.canvas, bg=C_BG)
        self._win = self.canvas.create_window((0, 0), window=self.body,
                                              anchor="nw")
        self.body.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")))
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(self._win, width=e.width))
        self.canvas.bind_all("<MouseWheel>", self._on_wheel)
        self.canvas.bind_all("<Button-4>",
                             lambda e: self.canvas.yview_scroll(-2, "units"))
        self.canvas.bind_all("<Button-5>",
                             lambda e: self.canvas.yview_scroll(2, "units"))

        # ----- Peringatan bila pynput belum terpasang -----
        if not PYNPUT_OK:
            warn = tk.Frame(self.body, bg="#3a1220",
                            highlightbackground=C_RED, highlightthickness=1)
            warn.pack(fill="x", padx=14, pady=(8, 0))
            tk.Label(warn, text="Library pynput belum terpasang!\n"
                                "Buka CMD lalu jalankan:  pip install pynput",
                     bg="#3a1220", fg=C_RED, font=F_S, wraplength=560,
                     justify="left").pack(padx=10, pady=8, anchor="w")

        # ============ 1. DAFTAR BROWSER & FOLDER ============
        c1 = self._card("1. DAFTAR BROWSER & FOLDER VIDEO")
        self.lb_browser = tk.Listbox(
            c1, bg=C_ENTRY, fg=C_TEXT, selectbackground=C_ACCENT,
            selectforeground=C_BTN_TXT, relief="flat", font=F_N,
            height=3, highlightthickness=1, highlightbackground=C_LINE,
            activestyle="none", exportselection=False)
        self.lb_browser.pack(fill="x")
        self.lb_browser.bind("<<ListboxSelect>>", self._on_browser_select)
        rowb = tk.Frame(c1, bg=C_CARD)
        rowb.pack(fill="x", pady=(8, 0))
        self._btn(rowb, "+ TAMBAH BROWSER", self._tambah_browser,
                  bg=C_ACCENT, fg=C_BTN_TXT)
        self._btn(rowb, "HAPUS", self._hapus_browser, padx=6, fg=C_RED)

        tk.Label(c1, text="FOLDER VIDEO UNTUK BROWSER INI",
                 bg=C_CARD, fg=C_MUTED, font=F_S,
                 anchor="w").pack(fill="x", pady=(10, 1))
        rowf = tk.Frame(c1, bg=C_CARD)
        rowf.pack(fill="x")
        self.ent_folder = tk.Entry(rowf, bg=C_ENTRY, fg=C_TEXT,
                                   insertbackground=C_TEXT, relief="flat",
                                   font=F_N, highlightthickness=1,
                                   highlightbackground=C_LINE,
                                   highlightcolor=C_ACCENT)
        self.ent_folder.pack(side="left", fill="x", expand=True, ipady=6)
        self.ent_folder.bind("<KeyRelease>", lambda e: self._update_count())
        self._btn(rowf, "PILIH\nFOLDER", self._pilih_folder, padx=6)

        self.lbl_count = tk.Label(c1, text="Ditemukan: -",
                                  bg=C_CARD, fg=C_BLUE, font=F_S, anchor="w")
        self.lbl_count.pack(fill="x", pady=(6, 0))

        self.skip_var = tk.BooleanVar(value=True)
        self._check(c1, "Lewati video yang sudah pernah terupload "
                        "(riwayat tersimpan otomatis)",
                    self.skip_var, cmd=self._update_count)
        self._btn(c1, "Bersihkan riwayat browser ini",
                  self._bersihkan_riwayat,
                  font=("Segoe UI", 8, "underline"), fg=C_MUTED)

        # ============ 2. JUMLAH & CAPTION ============
        c2 = self._card("2. JUMLAH VIDEO & CAPTION (JUDUL VIDEO)")
        row2 = tk.Frame(c2, bg=C_CARD)
        row2.pack(fill="x")
        kiri = tk.Frame(row2, bg=C_CARD)
        kiri.pack(side="left", fill="x", expand=True, padx=(0, 6))
        kanan = tk.Frame(row2, bg=C_CARD)
        kanan.pack(side="left", fill="x", expand=True, padx=(6, 0))
        self.ent_jumlah = self._field(
            kiri, "JUMLAH VIDEO SEKALI JALAN (MAKS {})".format(MAX_BATCH),
            "5")
        self.ent_caption = self._field(
            kanan, "CAPTION DASAR (contoh: #dangdut)", "#dangdut")
        self.lbl_preview = tk.Label(c2, text="Pratinjau caption :  -",
                                    bg=C_CARD, fg=C_ACCENT, font=F_MONO,
                                    anchor="w")
        self.lbl_preview.pack(fill="x", pady=(8, 0))
        self.ent_caption.bind("<KeyRelease>",
                              lambda e: self._update_preview())
        self.ent_jumlah.bind("<KeyRelease>",
                             lambda e: self._update_preview())
        tk.Label(c2, text="Caption otomatis digabung dengan nama video "
                          "(tanpa .mp4) lalu diketik ke kotak 'Judul video' "
                          "lewat tombol Edit → Konfirmasi. Batas situs: "
                          "{} karakter.".format(JUDUL_MAX),
                 bg=C_CARD, fg=C_MUTED, font=F_S, wraplength=560,
                 justify="left").pack(fill="x", pady=(4, 0))

        # ============ 3. POSISI KLIK DI SITUS ============
        c3 = self._card("3. POSISI KLIK DI SITUS (khusus browser ini)")
        self.var_skip_jadwal = tk.BooleanVar(value=False)
        self._check(c3, "Lewati langkah JADWAL (A-E) — langsung ke "
                        "'Tambah video' (kalau rilisnya tidak dijadwalkan)",
                    self.var_skip_jadwal)
        self.lbl_pos = {}
        self.btn_pos = {}
        for kunci, label, wajib, _ket in POSISI_DEF:
            row = tk.Frame(c3, bg=C_CARD)
            row.pack(fill="x", pady=(3, 0))
            tk.Label(row, text=label, bg=C_CARD,
                     fg=C_TEXT if wajib else C_MUTED,
                     font=("Segoe UI", 9), width=26,
                     anchor="w").pack(side="left")
            self.btn_pos[kunci] = tk.Button(
                row, text="AMBIL", command=lambda k=kunci:
                    self._ambil_posisi(k),
                bg=C_ENTRY, fg=C_ACCENT, font=("Segoe UI", 8, "bold"),
                relief="flat", bd=0, cursor="hand2",
                activebackground=C_LINE, activeforeground=C_ACCENT)
            self.btn_pos[kunci].pack(side="left", ipady=3, padx=(0, 3))
            lihat = tk.Button(
                row, text="LIHAT", command=lambda k=kunci:
                    self._lihat_posisi(k),
                bg=C_ENTRY, fg=C_MUTED, font=("Segoe UI", 8, "bold"),
                relief="flat", bd=0, cursor="hand2",
                activebackground=C_LINE, activeforeground=C_MUTED)
            lihat.pack(side="left", ipady=3, padx=(0, 6))
            self.lbl_pos[kunci] = tk.Label(row, text="belum diatur",
                                           bg=C_CARD, fg=C_YELLOW,
                                           font=("Segoe UI", 8),
                                           width=13, anchor="w")
            self.lbl_pos[kunci].pack(side="left")

            # ---- kontrol tambahan di bawah slot tertentu ----
            if kunci == "pos_pilih_neg":
                # C: pilih negara — klik biasa atau pencarian gambar
                sub = tk.Frame(c3, bg=C_CARD)
                sub.pack(fill="x", padx=(26, 0))
                self.var_gambar = tk.BooleanVar(value=False)
                self._check(sub, "Pilih negara pakai PENCARIAN GAMBAR — "
                                 "cari potongan layar (mis. tulisan "
                                 "'Indonesia') dalam radius, lalu diklik",
                            self.var_gambar)
                sub2 = tk.Frame(sub, bg=C_CARD)
                sub2.pack(fill="x", pady=(2, 0))
                self._btn(sub2, "PILIH GAMBAR...", self._pilih_gambar_ref)
                self.lbl_gambar = tk.Label(sub2, text="(belum ada gambar)",
                                           bg=C_CARD, fg=C_YELLOW,
                                           font=F_S, anchor="w")
                self.lbl_gambar.pack(side="left", padx=(6, 0))
                sub3 = tk.Frame(sub, bg=C_CARD)
                sub3.pack(fill="x", pady=(2, 0))
                self.ent_radius = self._field_mini(
                    sub3, "RADIUS CARI (piksel):", "300", width=7)
                self.ent_kemiripan = self._field_mini(
                    sub3, "KEMIRIPAN (0.50-0.99):", "0.80", width=7)
                self._btn(sub3, "TES CARI", self._tes_cari, fg=C_BLUE)
            elif kunci == "pos_tanggal":
                # D: tanggal & jam rilis diketik otomatis
                sub = tk.Frame(c3, bg=C_CARD)
                sub.pack(fill="x", padx=(26, 0))
                self.ent_tanggal = self._field(
                    sub, "TANGGAL & JAM UPLOAD — FORMAT: "
                         "2026-09-10 02:05:01",
                    "2026-09-10 02:05:01")
            elif kunci == "pos_bebas1":
                # G: klik bebas berulang + scroll
                sub = tk.Frame(c3, bg=C_CARD)
                sub.pack(fill="x", padx=(26, 0))
                self.ent_klik_bebas1 = self._field_mini(
                    sub, "JUMLAH KLIK (0-500):", "2", width=7)
                self.ent_scroll_bebas1 = self._field_mini(
                    sub, "JUMLAH SCROLL (0-50):", "0", width=7)
                tk.Label(sub, text="ARAH:", bg=C_CARD, fg=C_MUTED,
                         font=F_S).pack(side="left")
                self.arah_scroll = tk.StringVar(value="Turun")
                om = tk.OptionMenu(sub, self.arah_scroll,
                                   "Turun", "Naik")
                om.configure(bg=C_ENTRY, fg=C_TEXT, font=F_S,
                             relief="flat", bd=0, highlightthickness=0,
                             activebackground=C_LINE,
                             activeforeground=C_TEXT, cursor="hand2")
                om["menu"].configure(bg=C_ENTRY, fg=C_TEXT)
                om.pack(side="left")
            elif kunci == "pos_bebas2":
                # H2: jumlah klik bebas kedua
                sub = tk.Frame(c3, bg=C_CARD)
                sub.pack(fill="x", padx=(26, 0))
                self.ent_klik_bebas2 = self._field_mini(
                    sub, "JUMLAH KLIK (0-20):", "1", width=7)
                tk.Label(sub, text="mis. tombol 'Buka' pada dialog file",
                         bg=C_CARD, fg=C_MUTED,
                         font=F_S).pack(side="left")
            elif kunci == "pos_konfirmasi":
                # I: jarak antar baris video
                sub = tk.Frame(c3, bg=C_CARD)
                sub.pack(fill="x", padx=(26, 0))
                self.ent_jarak = self._field_mini(
                    sub, "JARAK ANTAR BARIS VIDEO (piksel):", "85",
                    width=7)
                tk.Label(sub, text="caption mengalir ke baris berikutnya: "
                                   "5 video = 5x, 20 video = 20x",
                         bg=C_CARD, fg=C_MUTED,
                         font=F_S, wraplength=360,
                         justify="left").pack(side="left")
            elif kunci == "pos_submit":
                # J: jumlah klik + submit otomatis
                sub = tk.Frame(c3, bg=C_CARD)
                sub.pack(fill="x", padx=(26, 0))
                self.ent_klik_submit = self._field_mini(
                    sub, "JUMLAH KLIK (1-10):", "1", width=7)
                self.kirim_var = tk.BooleanVar(value=True)
                self._check(sub, "Klik SUBMIT otomatis di akhir "
                                 "(matikan kalau mau cek dulu manual)",
                            self.kirim_var)
        self.lbl_ambil = tk.Label(c3, text="", bg=C_CARD, fg=C_YELLOW,
                                  font=F_S, anchor="w", wraplength=560,
                                  justify="left")
        self.lbl_ambil.pack(fill="x", pady=(6, 0))
        tk.Label(c3, text="Ambil posisi = klik AMBIL, lalu dalam 5 detik "
                          "arahkan mouse ke target di browser dan "
                          "diamkan. Urutan otomatis saat MULAI:\n"
                          "A jadwal → B negara → C pilih negara → "
                          "D tanggal (diketik otomatis) → E OKE → F tambah "
                          "video → G klik/scroll → H pilih video "
                          "(Shift+↓) → H2 Buka → I caption per baris → "
                          "J Submit.\n"
                          "Kondisi halaman saat mengambil posisi:\n"
                          "• A — halaman Rilis karya, tombol 'Jadwal "
                          "rilis' terlihat.\n"
                          "• B/C — dialog jadwal terbuka: B saat dropdown "
                          "negara TERTUTUP; C saat daftar negara TERBUKA "
                          "(kalau pakai pencarian gambar, C boleh titik "
                          "mana pun dekat daftar; gambar referensinya "
                          "potongan layar tulisan 'Indonesia').\n"
                          "• D & E — form/kalender tanggal terlihat.\n"
                          "• F, G, H — dialog pilih file Windows terbuka "
                          "(H = video pertama di daftar file).\n"
                          "• H2 — tombol 'Buka' pada dialog file.\n"
                          "• I1 — daftar video di situs, baris teratas "
                          "TERTUTUP; I2/I3 — baris teratas TERBUKA (klik "
                          "dulu Edit-nya manual). Kalau Konfirmasi "
                          "letaknya sama dengan Edit, biarkan I3 belum "
                          "diatur.\n"
                          "• J — scroll halaman sampai BAWAH (tombol "
                          "Submit terlihat).\n"
                          "PENTING: semua baris video harus terlihat di "
                          "layar saat fase caption — kecilkan zoom "
                          "browser (Ctrl + minus) bila 20 video tidak "
                          "muat. Jangan pindahkan/resize jendela browser "
                          "setelah posisi diambil. Posisi tersimpan per "
                          "browser.",
                 bg=C_CARD, fg=C_MUTED, font=F_S, wraplength=560,
                 justify="left").pack(fill="x", pady=(2, 0))

        # ============ 4. PENGATURAN WAKTU ============
        c4 = self._card("4. PENGATURAN WAKTU (detik)")
        row4a = tk.Frame(c4, bg=C_CARD)
        row4a.pack(fill="x")
        row4b = tk.Frame(c4, bg=C_CARD)
        row4b.pack(fill="x")
        f1 = tk.Frame(row4a, bg=C_CARD)
        f1.pack(side="left", fill="x", expand=True, padx=(0, 6))
        f2 = tk.Frame(row4a, bg=C_CARD)
        f2.pack(side="left", fill="x", expand=True, padx=(6, 0))
        f3 = tk.Frame(row4b, bg=C_CARD)
        f3.pack(side="left", fill="x", expand=True, padx=(0, 6), pady=(2, 0))
        f4 = tk.Frame(row4b, bg=C_CARD)
        f4.pack(side="left", fill="x", expand=True, padx=(6, 0), pady=(2, 0))
        self.ent_mundur = self._field(f1, "MUNDUR SEBELUM MULAI", "5")
        self.ent_dialog = self._field(f2, "JEDA BUKA DIALOG/EDITOR", "2")
        self.ent_langkah = self._field(f3, "JEDA ANTAR LANGKAH", "1")
        self.ent_tunggu = self._field(f4, "TUNGGU UPLOAD PER VIDEO (x "
                                          "jumlah video)", "60")
        tk.Label(c4, text="MUNDUR = persiapan sebelum mulai.\n"
                          "JEDA BUKA DIALOG/EDITOR = tunggu dialog pilih file "
                          "Windows / editor / dropdown terbuka.\n"
                          "JEDA ANTAR LANGKAH = jeda klik-ketik di dalam "
                          "situs.\nTUNGGU UPLOAD PER VIDEO = waktu menunggu "
                          "satu video selesai terupload; total menunggu = "
                          "nilai ini dikali jumlah video (naikkan bila video "
                          "berukuran besar / internet lambat).",
                 bg=C_CARD, fg=C_MUTED, font=F_S, wraplength=560,
                 justify="left").pack(fill="x", pady=(6, 0))

        # ============ 5. STATUS ============
        c6 = self._card("5. STATUS")
        self.lbl_status = tk.Label(
            c6, text="● Siap — buka situs (Versi lama → Rilis karya), "
                     "ambil posisi, lalu tekan F6",
            bg=C_CARD, fg=C_ACCENT, font=F_H, anchor="w",
            wraplength=560, justify="left")
        self.lbl_status.pack(fill="x")
        self.lbl_progress = tk.Label(c6, text="Progres: -",
                                     bg=C_CARD, fg=C_MUTED, font=F_N,
                                     anchor="w")
        self.lbl_progress.pack(fill="x", pady=(4, 0))

        # ================= TOMBOL =================
        btns = tk.Frame(self.body, bg=C_BG)
        btns.pack(fill="x", padx=14, pady=(14, 0))
        self.btn_start = tk.Button(btns, text="MULAI (F6)",
                                   command=self._start, bg=C_ACCENT,
                                   fg=C_BTN_TXT,
                                   font=("Segoe UI", 11, "bold"),
                                   relief="flat", bd=0, cursor="hand2",
                                   activebackground=C_ACCENT_D,
                                   activeforeground=C_BTN_TXT)
        self.btn_start.pack(side="left", expand=True, fill="x",
                            ipady=10, padx=(0, 6))
        self.btn_stop = tk.Button(btns, text="BERHENTI (F7)",
                                  command=self._stop, bg=C_RED, fg="white",
                                  font=("Segoe UI", 11, "bold"), relief="flat",
                                  bd=0, cursor="hand2",
                                  activebackground=C_RED_D,
                                  activeforeground="white",
                                  state="disabled",
                                  disabledforeground="#ffd0da")
        self.btn_stop.pack(side="left", expand=True, fill="x",
                           ipady=10, padx=(6, 0))

        # ----- Footer -----
        tk.Label(self.root,
                 text="F6 = Mulai   |   F7 / ESC = Berhenti   |   "
                      "Pengaturan tersimpan otomatis",
                 bg=C_BG, fg=C_MUTED, font=F_S).pack(side="bottom", pady=8)

    # ================== HOTKEY GLOBAL ==================
    def _on_key(self, key):
        try:
            if key == kb_mod.Key.f6:
                self.root.after(0, self._start)
            elif key in (kb_mod.Key.f7, kb_mod.Key.esc):
                self.root.after(0, self._stop)
        except Exception:
            pass

    # ================== BANTU UI (THREAD-SAFE) ==================
    def _set_status(self, msg, color):
        def do():
            self.lbl_status.config(text="● " + msg, fg=color)
        self.root.after(0, do)

    def _set_progress(self, msg):
        def do():
            self.lbl_progress.config(text=msg)
        self.root.after(0, do)

    def _sleep(self, seconds):
        """Tidur yang bisa dibatalkan kapan saja lewat tombol stop."""
        end = time.time() + seconds
        while not self.stop_event.is_set():
            remain = end - time.time()
            if remain <= 0:
                break
            time.sleep(min(0.05, remain))

    # ================== DATA BROWSER ==================
    def _browser_baru(self, nama=""):
        entri = {"nama": nama or "Browser {}".format(len(self.browsers) + 1),
                 "folder": ""}
        for kunci in POS_KUNCI:
            entri[kunci] = None
        return entri

    def _sync_folder_to_browser(self):
        """Simpan isi kotak folder ke entri browser aktif saat ini."""
        if 0 <= self.aktif < len(self.browsers):
            self.browsers[self.aktif]["folder"] = self.ent_folder.get().strip()

    def _refresh_browser_list(self, keep=0):
        self._loading = True
        self.lb_browser.delete(0, "end")
        for i, b in enumerate(self.browsers):
            folder = b["folder"] or "(folder belum dipilih)"
            n = len(daftar_video(b["folder"])) if b["folder"] else 0
            info = "{}. {}  |  {}  [{} video]".format(i + 1, b["nama"],
                                                      folder, n)
            self.lb_browser.insert("end", info)
        keep = min(max(0, keep), max(0, len(self.browsers) - 1))
        if self.browsers:
            self.lb_browser.selection_set(keep)
            self.lb_browser.see(keep)
        self.aktif = keep
        self._loading = False

    def _on_browser_select(self, _ev=None):
        if self._loading:
            return
        sel = self.lb_browser.curselection()
        if not sel:
            return
        idx = sel[0]
        if idx == self.aktif:
            return
        self._sync_folder_to_browser()
        self.aktif = idx
        self._load_browser_to_ui()

    def _load_browser_to_ui(self):
        if not (0 <= self.aktif < len(self.browsers)):
            return
        b = self.browsers[self.aktif]
        self.ent_folder.delete(0, "end")
        self.ent_folder.insert(0, b["folder"])
        for kunci in POS_KUNCI:
            self._tampilkan_posisi(kunci)
        self._update_count()
        self._update_preview()

    def _tambah_browser(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("Tambah Browser")
        dlg.configure(bg=C_BG)
        dlg.resizable(False, False)
        dlg.transient(self.root)
        dlg.grab_set()
        body = tk.Frame(dlg, bg=C_BG)
        body.pack(fill="both", expand=True, padx=18, pady=(12, 8))
        tk.Label(body, text="TAMBAH BROWSER BARU", bg=C_BG, fg=C_ACCENT,
                 font=F_H, anchor="w").pack(fill="x", pady=(0, 8))
        tk.Label(body, text="NAMA BROWSER (mis. Chrome Akun 1, Edge Akun 2)",
                 bg=C_BG, fg=C_MUTED, font=F_S,
                 anchor="w").pack(fill="x", pady=(0, 1))
        ent = tk.Entry(body, bg=C_ENTRY, fg=C_TEXT, insertbackground=C_TEXT,
                       relief="flat", font=F_N, highlightthickness=1,
                       highlightbackground=C_LINE, highlightcolor=C_ACCENT)
        ent.pack(fill="x", ipady=6)
        ent.insert(0, "Browser {}".format(len(self.browsers) + 1))
        ent.select_range(0, "end")

        def simpan(_ev=None):
            nama = ent.get().strip() or "Browser {}".format(
                len(self.browsers) + 1)
            self._sync_folder_to_browser()
            self.browsers.append(self._browser_baru(nama))
            self._refresh_browser_list(keep=len(self.browsers) - 1)
            self._load_browser_to_ui()
            self._save_settings()
            dlg.grab_release()
            dlg.destroy()
            self._set_status("Browser '{}' ditambahkan. Pilih foldernya "
                             "lalu atur posisi kliknya.".format(nama),
                             C_ACCENT)

        def batal():
            dlg.grab_release()
            dlg.destroy()

        btnrow = tk.Frame(body, bg=C_BG)
        btnrow.pack(fill="x", pady=(12, 4))
        tk.Button(btnrow, text="SIMPAN", command=simpan, bg=C_ACCENT,
                  fg=C_BTN_TXT, font=("Segoe UI", 10, "bold"),
                  relief="flat", bd=0, cursor="hand2",
                  activebackground=C_ACCENT_D,
                  activeforeground=C_BTN_TXT).pack(
                      side="left", expand=True, fill="x", ipady=8,
                      padx=(0, 6))
        tk.Button(btnrow, text="BATALKAN", command=batal, bg=C_ENTRY,
                  fg=C_TEXT, font=("Segoe UI", 10, "bold"),
                  relief="flat", bd=0, cursor="hand2",
                  activebackground=C_LINE,
                  activeforeground=C_TEXT).pack(
                      side="left", expand=True, fill="x", ipady=8,
                      padx=(6, 0))
        ent.bind("<Return>", simpan)
        ent.focus_set()

    def _hapus_browser(self):
        if not self.browsers:
            return
        if len(self.browsers) == 1:
            messagebox.showinfo(APP_NAME,
                                "Minimal harus ada satu browser.\n"
                                "Kalau mau mengganti, tinggal ubah nama & "
                                "foldernya saja.")
            return
        idx = self.aktif
        nama = self.browsers[idx]["nama"]
        if not messagebox.askyesno(APP_NAME,
                                   "Hapus browser '{}' beserta posisi "
                                   "kliknya?".format(nama)):
            return
        self._sync_folder_to_browser()
        del self.browsers[idx]
        self._refresh_browser_list(keep=max(0, idx - 1))
        self._load_browser_to_ui()
        self._save_settings()
        self._set_status("Browser '{}' dihapus.".format(nama), C_ACCENT)

    # ================== POSISI KLIK ==================
    def _tampilkan_posisi(self, kunci):
        pos = None
        if 0 <= self.aktif < len(self.browsers):
            pos = self.browsers[self.aktif].get(kunci)
        if pos:
            self.lbl_pos[kunci].config(
                text="({}, {}) OK".format(pos[0], pos[1]), fg=C_ACCENT)
        else:
            self.lbl_pos[kunci].config(text="belum diatur", fg=C_YELLOW)

    def _ambil_posisi(self, kunci):
        if not PYNPUT_OK:
            messagebox.showerror(
                APP_NAME, "Library pynput belum terpasang.\n\n"
                          "Buka CMD lalu jalankan:\n  pip install pynput")
            return
        if not self.browsers:
            messagebox.showinfo(APP_NAME,
                                "Daftarkan dulu minimal satu browser.")
            return
        judul = JUDUL_POSISI[kunci]
        for b in self.btn_pos.values():
            b.config(state="disabled")

        def kerja():
            try:
                for s in range(5, 0, -1):
                    self.root.after(0, lambda s=s: self.lbl_ambil.config(
                        text="Arahkan mouse ke {} dan diamkan... {}".format(
                            judul, s)))
                    time.sleep(1)
                px, py = self.mouse.position

                def isi():
                    self._sync_folder_to_browser()
                    self.browsers[self.aktif][kunci] = [int(px), int(py)]
                    self._tampilkan_posisi(kunci)
                    self.lbl_ambil.config(
                        text="{} tersimpan: X={}, Y={} (browser: {})".format(
                            judul, int(px), int(py),
                            self.browsers[self.aktif]["nama"]),
                        fg=C_ACCENT)
                    for b in self.btn_pos.values():
                        b.config(state="normal")
                    self._save_settings()

                self.root.after(0, isi)
            except Exception:
                self.root.after(0, lambda: [
                    b.config(state="normal") for b in self.btn_pos.values()])
                self.root.after(0, lambda: self.lbl_ambil.config(
                    text="Gagal mengambil posisi.", fg=C_RED))

        threading.Thread(target=kerja, daemon=True).start()

    def _lihat_posisi(self, kunci):
        if not PYNPUT_OK or not self.browsers:
            return
        pos = self.browsers[self.aktif].get(kunci)
        if not pos:
            messagebox.showinfo(APP_NAME,
                                "Posisi ini belum diatur. Klik dulu "
                                "AMBIL.")
            return
        try:
            self.mouse.position = (pos[0], pos[1])
        except Exception:
            pass

    # ================== GAMBAR REFERENSI NEGARA ==================
    def _pilih_gambar_ref(self):
        """Pilih potongan layar sebagai gambar referensi negara (C)."""
        f = filedialog.askopenfilename(
            title="Pilih gambar referensi (potongan layar tulisan "
                  "'Indonesia')",
            filetypes=[("Gambar", "*.png *.jpg *.jpeg *.bmp"),
                       ("Semua file", "*.*")])
        if f:
            self.gambar_ref = f
            self.lbl_gambar.config(
                text=os.path.basename(f) + "  (siap)", fg=C_ACCENT)
            self._save_settings()

    def _tes_cari(self):
        """Tes pencarian gambar negara tanpa menjalankan seluruh alur."""
        if not PYNPUT_OK:
            messagebox.showerror(APP_NAME, "Library pynput belum terpasang.")
            return
        if not self.browsers:
            messagebox.showinfo(APP_NAME,
                                "Daftarkan dulu minimal satu browser.")
            return
        if not CV_OK:
            messagebox.showwarning(
                APP_NAME,
                "opencv-python belum terpasang — pencarian gambar tidak "
                "bisa dipakai.\n\nBuka CMD lalu jalankan:\n"
                "  pip install opencv-python")
            return
        if not self.gambar_ref or not os.path.isfile(self.gambar_ref):
            messagebox.showinfo(APP_NAME,
                                "Pilih dulu gambar referensinya "
                                "(PILIH GAMBAR).")
            return
        pos = self.browsers[self.aktif].get("pos_pilih_neg")
        if not pos:
            messagebox.showinfo(APP_NAME,
                                "Atur dulu posisi C sebagai titik acuan "
                                "pencarian (klik AMBIL pada C).")
            return
        try:
            radius = max(50, min(2000, int(self.ent_radius.get().strip()
                                           or "300")))
        except ValueError:
            radius = 300
        try:
            mirip = float(str(self.ent_kemiripan.get()).replace(",", ".")
                          or "0.8")
            mirip = max(0.5, min(0.99, mirip))
        except ValueError:
            mirip = 0.8

        def kerja():
            hasil = cari_di_layar(self.gambar_ref, pos[0], pos[1],
                                  radius, mirip)

            def lapor():
                if hasil:
                    x, y, skor = hasil
                    try:
                        self.mouse.position = (x, y)
                    except Exception:
                        pass
                    self.lbl_ambil.config(
                        text="TES: gambar KETEMU di ({}, {}) — kemiripan "
                             "{:.0%}. Mouse dipindah ke sana "
                             "(tidak diklik).".format(x, y, skor),
                        fg=C_ACCENT)
                else:
                    self.lbl_ambil.config(
                        text="TES: gambar TIDAK ketemu. Coba: perbesar "
                             "RADIUS, turunkan KEMIRIPAN (mis. 0.70), atau "
                             "potong ulang gambar referensi persis "
                             "sesuai tampilan di layar.",
                        fg=C_RED)
            self.root.after(0, lapor)

        threading.Thread(target=kerja, daemon=True).start()

    # ================== FOLDER, JUMLAH, CAPTION ==================
    def _pilih_folder(self):
        folder = filedialog.askdirectory(title="Pilih folder video untuk "
                                                "browser ini")
        if folder:
            folder = os.path.normpath(folder)
            self.ent_folder.delete(0, "end")
            self.ent_folder.insert(0, folder)
            self._sync_folder_to_browser()
            self._update_count()
            self._update_preview()
            self._save_settings()
            self._refresh_browser_list(keep=self.aktif)

    def _kunci_riwayat(self):
        b = self.browsers[self.aktif] if self.browsers else \
            {"nama": "?", "folder": ""}
        return "{}||{}".format(b["nama"], b["folder"].lower())

    def _riwayat_browser(self):
        return set(self.riwayat.get(self._kunci_riwayat(), []))

    def _update_count(self, *_):
        folder = self.ent_folder.get().strip()
        semua = daftar_video(folder)
        if not folder:
            self.lbl_count.config(text="Folder belum dipilih.", fg=C_MUTED)
        elif not semua:
            self.lbl_count.config(
                text="Tidak ada file video di folder ini "
                     "(cari .mp4 .mov .avi dll).", fg=C_YELLOW)
        else:
            if self.skip_var.get():
                sisa = [f for f in semua
                        if f not in self._riwayat_browser()]
                self.lbl_count.config(
                    text="Ditemukan {} video (urut nama A-Z) — {} belum "
                         "pernah terupload.".format(len(semua), len(sisa)),
                    fg=C_BLUE)
            else:
                self.lbl_count.config(
                    text="Ditemukan {} video (urut nama A-Z).".format(
                        len(semua)), fg=C_BLUE)
        self._update_preview()

    def _update_preview(self, *_):
        folder = self.ent_folder.get().strip()
        semua = daftar_video(folder)
        if self.skip_var.get() and semua:
            sudah = self._riwayat_browser()
            belum = [f for f in semua if f not in sudah]
            contoh = belum[0] if belum else semua[0]
        else:
            contoh = semua[0] if semua else "melati"
        teks = compose_caption(self.ent_caption.get(), contoh)
        n = len(teks)
        self.lbl_preview.config(
            text="Pratinjau caption :  {}   ({}{}/{} kar)".format(
                teks, n, "!" if n > JUDUL_MAX else "", JUDUL_MAX),
            fg=C_RED if n > JUDUL_MAX else C_ACCENT)

    def _bersihkan_riwayat(self):
        kunci = self._kunci_riwayat()
        n = len(self.riwayat.get(kunci, []))
        if n == 0:
            messagebox.showinfo(APP_NAME,
                                "Riwayat browser ini masih kosong.")
            return
        if messagebox.askyesno(
                APP_NAME,
                "Hapus riwayat {} video yang sudah terupload?\n\n"
                "Setelah dihapus, video yang sama bisa diupload ulang "
                "dari awal.".format(n)):
            self.riwayat.pop(kunci, None)
            self._save_riwayat()
            self._update_count()
            self._set_status("Riwayat browser ini dibersihkan.", C_ACCENT)

    # ================== MULAI / BERHENTI ==================
    def _snapshot(self):
        return {
            "browser": dict(self.browsers[self.aktif]) if self.browsers
                       else None,
            "folder": self.ent_folder.get().strip(),
            "jumlah": self.ent_jumlah.get().strip(),
            "caption": self.ent_caption.get(),
            "mundur": self.ent_mundur.get().strip(),
            "jeda_dialog": self.ent_dialog.get().strip(),
            "jeda_langkah": self.ent_langkah.get().strip(),
            "tunggu": self.ent_tunggu.get().strip(),
            "skip": bool(self.skip_var.get()),
            "skip_jadwal": bool(self.var_skip_jadwal.get()),
            "pakai_gambar": bool(self.var_gambar.get()),
            "gambar": self.gambar_ref,
            "radius": self.ent_radius.get().strip(),
            "kemiripan": self.ent_kemiripan.get().strip(),
            "tanggal": self.ent_tanggal.get().strip(),
            "klik_bebas1": self.ent_klik_bebas1.get().strip(),
            "scroll_bebas1": self.ent_scroll_bebas1.get().strip(),
            "arah_scroll": self.arah_scroll.get(),
            "klik_bebas2": self.ent_klik_bebas2.get().strip(),
            "jarak_baris": self.ent_jarak.get().strip(),
            "klik_submit": self.ent_klik_submit.get().strip(),
            "auto_kirim": bool(self.kirim_var.get()),
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
        self._sync_folder_to_browser()
        snap = self._snapshot()
        if not snap["browser"]:
            messagebox.showwarning(APP_NAME,
                                   "Daftarkan dulu minimal satu browser di "
                                   "bagian 1.")
            return
        try:
            jumlah = int(snap["jumlah"])
            mundur = int(snap["mundur"])
            jeda_dialog = float(snap["jeda_dialog"].replace(",", "."))
            jeda_langkah = float(snap["jeda_langkah"].replace(",", "."))
            tunggu = float(snap["tunggu"].replace(",", "."))
        except ValueError:
            messagebox.showwarning(
                APP_NAME, "JUMLAH VIDEO dan PENGATURAN WAKTU harus diisi "
                          "dengan angka yang benar.")
            return
        if jumlah < 1:
            messagebox.showwarning(APP_NAME,
                                   "Jumlah video minimal 1.")
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
        caption_only = bool(snap.get("caption_only"))
        if not caption_only:
            if not folder or not os.path.isdir(folder):
                messagebox.showwarning(
                    APP_NAME,
                    "Folder video belum dipilih atau tidak ada:\n"
                    + (folder or "(kosong)"))
                return
            # ---- posisi wajib sesuai alur A-J ----
            lewati_jadwal = snap["skip_jadwal"]
            slot_jadwal = ("pos_jadwal", "pos_negara", "pos_pilih_neg",
                           "pos_tanggal", "pos_oke")
            for kunci, label, wajib, _ket in POSISI_DEF:
                if not wajib:
                    continue
                if lewati_jadwal and kunci in slot_jadwal:
                    continue
                if kunci == "pos_submit" and not snap["auto_kirim"]:
                    continue
                if not snap["browser"].get(kunci):
                    messagebox.showwarning(
                        APP_NAME,
                        "Posisi {} belum diatur.\n\n"
                        "Lihat petunjuk di bagian 3, lalu klik AMBIL."
                        .format(label))
                    return
            # ---- pencarian gambar negara (C) ----
            if snap["pakai_gambar"]:
                if not snap["gambar"] or not os.path.isfile(snap["gambar"]):
                    messagebox.showwarning(
                        APP_NAME,
                        "Pencarian gambar aktif tapi gambar referensi "
                        "belum dipilih.\n\nKlik 'PILIH GAMBAR' di bagian 3 "
                        "(potongan layar tulisan negaranya).")
                    return
                if not CV_OK:
                    if not messagebox.askyesno(
                            APP_NAME,
                            "opencv-python belum terpasang sehingga "
                            "pencarian gambar tidak bisa dipakai.\n\n"
                            "Lanjut dengan KLIK BIASA di titik C?"):
                        return
                    snap["pakai_gambar"] = False
            # ---- tanggal-jam rilis (D) ----
            tgl = parse_tanggal(snap["tanggal"])
            if tgl is None:
                messagebox.showwarning(
                    APP_NAME,
                    "Format TANGGAL & JAM UPLOAD salah.\n\nContoh yang "
                    "benar:\n  2026-09-10 02:05:01")
                return
            snap["tanggal"] = tgl
        else:
            # mode lanjut-caption: cukup posisi I1 & I2 (+ J bila otomatis)
            for kunci in ("pos_edit", "pos_judul"):
                if not snap["browser"].get(kunci):
                    messagebox.showwarning(
                        APP_NAME,
                        "Mode lanjut-caption butuh posisi I1 (Edit) dan "
                        "I2 (Kotak caption).\n\nAmbil dulu di bagian 3.")
                    return
            if snap["auto_kirim"] and not snap["browser"].get("pos_submit"):
                messagebox.showwarning(
                    APP_NAME,
                    "Klik SUBMIT otomatis aktif tapi posisi J belum "
                    "diatur.\n\nAmbil dulu posisinya, atau matikan "
                    "centang 'Klik SUBMIT otomatis'.")
                return
        # ---- angka pelengkap alur ----
        try:
            klik_b1 = int(snap["klik_bebas1"])
            scroll_b1 = int(snap["scroll_bebas1"])
            klik_b2 = int(snap["klik_bebas2"])
            jarak = int(snap["jarak_baris"])
            klik_sub = int(snap["klik_submit"])
        except ValueError:
            messagebox.showwarning(
                APP_NAME,
                "JUMLAH KLIK / SCROLL / JARAK ANTAR BARIS harus diisi "
                "dengan angka yang benar.")
            return
        if not 0 <= klik_b1 <= 500:
            messagebox.showwarning(APP_NAME,
                                   "Jumlah klik G harus 0-500.")
            return
        if not 0 <= scroll_b1 <= 50:
            messagebox.showwarning(APP_NAME,
                                   "Jumlah scroll G harus 0-50.")
            return
        if not 0 <= klik_b2 <= 20:
            messagebox.showwarning(APP_NAME,
                                   "Jumlah klik H2 harus 0-20.")
            return
        if not 10 <= jarak <= 2000:
            messagebox.showwarning(
                APP_NAME, "Jarak antar baris harus 10-2000 piksel.")
            return
        if not 1 <= klik_sub <= 10:
            messagebox.showwarning(APP_NAME,
                                   "Jumlah klik J harus 1-10.")
            return
        snap["klik_bebas1"] = klik_b1
        snap["scroll_bebas1"] = scroll_b1
        snap["klik_bebas2"] = klik_b2
        snap["jarak_baris"] = jarak
        snap["klik_submit"] = klik_sub
        if snap["pakai_gambar"]:
            try:
                radius = max(50, min(2000, int(snap["radius"] or "300")))
            except ValueError:
                radius = 300
            try:
                mirip = max(0.5, min(0.99, float(
                    str(snap["kemiripan"]).replace(",", ".") or "0.8")))
            except ValueError:
                mirip = 0.8
            snap["radius"] = radius
            snap["kemiripan"] = mirip
        if mundur < 0 or mundur > 60:
            messagebox.showwarning(APP_NAME,
                                   "MUNDUR SEBELUM MULAI harus 0-60 detik.")
            return
        if jeda_dialog < 0.5:
            messagebox.showwarning(
                APP_NAME, "JEDA BUKA DIALOG/EDITOR minimal 0.5 detik supaya "
                          "dialog/editor sempat terbuka.")
            return
        if tunggu < 0:
            tunggu = 0

        # ---- susun daftar video yang mau diupload ----
        antrian = []
        if not caption_only:
            semua = daftar_video(folder)
            if not semua:
                messagebox.showwarning(
                    APP_NAME, "Tidak ada file video (.mp4/.mov/dll) di "
                              "folder ini.")
                return
            if snap["skip"]:
                sudah = self._riwayat_browser()
                semua = [f for f in semua if f not in sudah]
            if not semua:
                riw = self.riwayat.get(self._kunci_riwayat(), [])
                if riw and not messagebox.askyesno(
                        APP_NAME,
                        "Tidak ada video baru untuk diupload (semua sudah "
                        "terupload / folder kosong setelah dilewati).\n\n"
                        "Mau lanjut LANGSUNG KE FASE CAPTION untuk {} "
                        "video terakhir? (jadwal & tambah video "
                        "dilewati)".format(min(jumlah, len(riw)))):
                    return
                if riw:
                    jumlah = min(jumlah, len(riw))
                    snap["caption_only"] = True
                    caption_only = True
                else:
                    messagebox.showinfo(
                        APP_NAME,
                        "Tidak ada video untuk diproses.\n\nKlik 'Bersihkan "
                        "riwayat browser ini' bila mau mengulang dari "
                        "awal.")
                    return
            else:
                antrian = semua[:jumlah]

        # ---- cek panjang caption ----
        if caption_only:
            riw = self.riwayat.get(self._kunci_riwayat(), [])
            cek_caption = list(riw[-jumlah:])
        else:
            cek_caption = antrian
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
                         args=(snap, antrian, jumlah, mundur, jeda_dialog,
                               jeda_langkah, tunggu),
                         daemon=True).start()

    # ================== BANTUAN SCROLL ==================
    def _scroll_top(self):
        """Gulir halaman browser ke paling atas (roda mouse ke atas)."""
        try:
            self.mouse.scroll(0, 40)
        except Exception:
            pass

    def _scroll_bottom(self):
        """Gulir halaman browser ke paling bawah (untuk tombol Kirim)."""
        try:
            self.mouse.scroll(0, -80)
        except Exception:
            pass

    def _klik(self, pos):
        self.mouse.position = (pos[0], pos[1])
        time.sleep(0.2)
        self.mouse.click(Button.left, 1)

    def _klik_off(self, pos, dy=0):
        """Klik pada posisi (x, y + dy) — untuk baris video ke-n."""
        self._klik((int(pos[0]), int(pos[1]) + int(dy)))

    # ================== MESIN OTOMATIS ==================
    def _worker(self, snap, antrian, jumlah, mundur, jeda_dialog,
                jeda_langkah, tunggu):
        try:
            bnama = snap["browser"]["nama"]
            pos = {k: tuple(snap["browser"][k]) for k in POS_KUNCI
                   if snap["browser"].get(k)}
            caption_dasar = snap["caption"]
            kunci = "{}||{}".format(bnama, snap["folder"].lower())
            caption_only = bool(snap.get("caption_only"))
            sukses = 0

            # ---- hitung mundur sebelum mulai ----
            if mundur > 0:
                for s in range(mundur, 0, -1):
                    if self.stop_event.is_set():
                        self._finish("Dibatalkan sebelum mulai.", warn=True)
                        return
                    if caption_only:
                        pesan = ("Lanjut CAPTION dalam {} detik — buka "
                                 "halaman Rilis karya di '{}' sekarang...")
                    else:
                        pesan = ("Mulai dalam {} detik — buka halaman Rilis "
                                 "karya CutMotions di '{}' sekarang...")
                    self._set_status(pesan.format(s, bnama), C_YELLOW)
                    self._sleep(1.0)

            # =================================================
            # FASE 1 — JADWAL RILIS (A → E)
            # =================================================
            if not caption_only:
                if snap["skip_jadwal"]:
                    self._set_status("Langkah JADWAL (A-E) dilewati sesuai "
                                     "pengaturan.", C_YELLOW)
                else:
                    self._set_status(
                        "FASE 1/3 JADWAL RILIS — klik tombol 'Jadwal "
                        "rilis'... (jangan sentuh mouse/keyboard!)",
                        C_ACCENT)
                    self._klik(pos["pos_jadwal"])
                    self._sleep(jeda_dialog)

                    if self.stop_event.is_set():
                        self._finish("Dihentikan saat fase jadwal.",
                                     warn=True)
                        return
                    self._set_status("Klik dropdown 'NEGARA'...", C_ACCENT)
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
                                "(percobaan {}/3)...".format(
                                    os.path.basename(snap["gambar"]),
                                    snap["radius"], percobaan), C_ACCENT)
                            hasil = cari_di_layar(
                                snap["gambar"],
                                pos["pos_pilih_neg"][0],
                                pos["pos_pilih_neg"][1],
                                snap["radius"], snap["kemiripan"])
                            if hasil:
                                break
                            self._sleep(jeda_dialog)
                        if hasil:
                            x, y, skor = hasil
                            self._set_status(
                                "Negara KETEMU di ({}, {}) — kemiripan "
                                "{:.0%} — diklik.".format(x, y, skor),
                                C_ACCENT)
                            self._klik((x, y))
                        else:
                            self._set_status(
                                "Gambar negara TIDAK ketemu 3x — pakai "
                                "klik biasa di titik C.", C_YELLOW)
                            self._klik(pos["pos_pilih_neg"])
                    else:
                        self._set_status("Klik pilihan negara...", C_ACCENT)
                        self._klik(pos["pos_pilih_neg"])
                    self._sleep(jeda_langkah)

                    # ---- D: kolom tanggal + ketik tanggal-jam ----
                    if self.stop_event.is_set():
                        self._finish("Dihentikan sebelum mengisi tanggal.",
                                     warn=True)
                        return
                    self._set_status(
                        "Ketik tanggal-jam rilis: {}...".format(
                            snap["tanggal"]), C_ACCENT)
                    self._klik(pos["pos_tanggal"])
                    time.sleep(0.3)
                    with self.kb.pressed(Key.ctrl):
                        self.kb.press("a")
                        self.kb.release("a")
                    time.sleep(0.15)
                    self.kb.type(snap["tanggal"])
                    self._sleep(jeda_langkah)

                    # ---- E: OKE ----
                    if self.stop_event.is_set():
                        self._finish("Dihentikan sebelum klik OKE.",
                                     warn=True)
                        return
                    self._set_status("Klik 'OKE'...", C_ACCENT)
                    self._klik(pos["pos_oke"])
                    self._sleep(jeda_langkah + 0.5)

            # =================================================
            # FASE 2 — TAMBAH & PILIH VIDEO (F → H2)
            # =================================================
            if not caption_only:
                if self.stop_event.is_set():
                    self._finish("Dihentikan.", warn=True)
                    return
                self._set_status(
                    "FASE 2/3 TAMBAH VIDEO — klik '+ Tambah video'...",
                    C_ACCENT)
                self._klik(pos["pos_tambah"])
                self._sleep(jeda_dialog)

                # ---- G: klik bebas 1 + scroll ----
                if self.stop_event.is_set():
                    self._finish(
                        "Dihentikan setelah 'Tambah video'. Video belum "
                        "masuk — aman diulang dari awal.", warn=True)
                    return
                n_klik1 = snap["klik_bebas1"]
                n_scroll = snap["scroll_bebas1"]
                if n_klik1 or n_scroll:
                    self._set_status(
                        "Klik bebas {}x + scroll {}x ({})...".format(
                            n_klik1, n_scroll, snap["arah_scroll"]),
                        C_ACCENT)
                    arah = -3 if snap["arah_scroll"] == "Naik" else 3
                    for _ in range(n_klik1):
                        if self.stop_event.is_set():
                            break
                        self._klik(pos["pos_bebas1"])
                        time.sleep(0.3)
                    for _ in range(n_scroll):
                        if self.stop_event.is_set():
                            break
                        try:
                            self.mouse.scroll(0, arah)
                        except Exception:
                            pass
                        time.sleep(0.3)
                    self._sleep(jeda_langkah)

                # ---- H: klik video pertama + Shift + panah bawah ----
                if self.stop_event.is_set():
                    self._finish("Dihentikan di dialog pilih file.",
                                 warn=True)
                    return
                self._set_status(
                    "Klik video pertama + tahan SHIFT + panah bawah {}x "
                    "(memilih {} video dari atas)...".format(
                        max(0, jumlah - 1), jumlah), C_ACCENT)
                self._klik(pos["pos_video"])
                time.sleep(0.3)
                if jumlah > 1:
                    with self.kb.pressed(Key.shift):
                        for _ in range(jumlah - 1):
                            self.kb.press(Key.down)
                            self.kb.release(Key.down)
                            time.sleep(0.15)
                self._sleep(jeda_langkah)

                # ---- H2: klik bebas 2 (tombol Buka) ----
                if self.stop_event.is_set():
                    self._finish("Dihentikan sebelum klik Buka.", warn=True)
                    return
                self._set_status(
                    "Klik bebas {}x (tombol 'Buka')...".format(
                        snap["klik_bebas2"]), C_ACCENT)
                for _ in range(snap["klik_bebas2"]):
                    if self.stop_event.is_set():
                        break
                    self._klik(pos["pos_bebas2"])
                    time.sleep(0.4)
                self._sleep(jeda_langkah)

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
                        "F6 lagi — aplikasi menawarkan lanjut ke fase "
                        "caption.", warn=True)
                    return

                # ---- catat riwayat (tersimpan instan) ----
                self.riwayat.setdefault(kunci, [])
                for nama_file in antrian:
                    if nama_file not in self.riwayat[kunci]:
                        self.riwayat[kunci].append(nama_file)
                self._save_riwayat()
                sukses = len(antrian)

            # =================================================
            # FASE 3 — CAPTION per baris (I) lalu SUBMIT (J)
            # =================================================
            self._set_status("FASE 3/3 CAPTION — menggulir ke atas...",
                             C_ACCENT)
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
                        i + 1, n_cap, i + 1), C_ACCENT)
                self._klik_off(pos["pos_edit"], geser)
                self._sleep(jeda_dialog)

                # klik kotak caption baris ke-i + ketik caption
                if self.stop_event.is_set():
                    break
                self._set_status(
                    "[{}/{}] Menulis caption: {}".format(
                        i + 1, n_cap, caption_final), C_ACCENT)
                self._klik_off(pos["pos_judul"], geser)
                time.sleep(0.3)
                with self.kb.pressed(Key.ctrl):
                    self.kb.press("a")
                    self.kb.release("a")
                time.sleep(0.15)
                self.kb.type(caption_final)
                self._sleep(jeda_langkah)

                # klik tombol Konfirmasi baris ke-i
                # (kalau I3 tidak diatur, klik lagi titik Edit —
                #  letaknya sama persis dengan tombol Konfirmasi)
                if self.stop_event.is_set():
                    break
                titik_ok = pos.get("pos_konfirmasi", pos["pos_edit"])
                self._set_status(
                    "[{}/{}] Klik Konfirmasi...".format(i + 1, n_cap),
                    C_ACCENT)
                self._klik_off(titik_ok, geser)
                self._sleep(jeda_langkah + 0.5)

            if self.stop_event.is_set():
                self._finish(
                    "Dihentikan saat FASE CAPTION ({}/{} caption selesai). "
                    "Jalankan F6 lagi dan pilih 'lanjut ke fase caption' "
                    "— caption diulang dari baris atas dan yang sudah "
                    "jadi otomatis ditimpa sama.".format(i + 1, n_cap),
                    warn=True)
                return

            # =================================================
            # J — SUBMIT
            # =================================================
            if snap["auto_kirim"] and "pos_submit" in pos:
                self._set_status(
                    "Klik SUBMIT {}x (halaman digulir ke bawah)...".format(
                        snap["klik_submit"]), C_ACCENT)
                self._scroll_bottom()
                self._sleep(jeda_langkah + 0.5)
                for _ in range(snap["klik_submit"]):
                    if self.stop_event.is_set():
                        break
                    self._klik(pos["pos_submit"])
                    time.sleep(0.4)
                self._finish(
                    "Selesai! {} video: jadwal diatur, video ditambahkan "
                    "(Shift+↓), caption ditulis per baris, dan SUBMIT "
                    "sudah diklik. Cek status rilis di situs.".format(n_cap))
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
            self.lbl_status.config(text="● " + msg,
                                   fg=C_RED if warn else C_ACCENT)
            self._update_count()
        self.root.after(0, do)

    def _stop(self):
        if self.running:
            self.stop_event.set()
            self._set_status("Menghentikan...", C_YELLOW)

    # ================== SIMPAN / MUAT ==================
    def _save_settings(self):
        self._sync_folder_to_browser()
        data = {
            "browsers": self.browsers,
            "aktif": self.aktif,
            "jumlah": self.ent_jumlah.get(),
            "caption": self.ent_caption.get(),
            "mundur": self.ent_mundur.get(),
            "jeda_dialog": self.ent_dialog.get(),
            "jeda_langkah": self.ent_langkah.get(),
            "tunggu_upload": self.ent_tunggu.get(),
            "skip_uploaded": bool(self.skip_var.get()),
            "skip_jadwal": bool(self.var_skip_jadwal.get()),
            "pakai_gambar": bool(self.var_gambar.get()),
            "gambar_ref": self.gambar_ref,
            "radius_cari": self.ent_radius.get(),
            "kemiripan_cari": self.ent_kemiripan.get(),
            "tanggal_jam": self.ent_tanggal.get(),
            "klik_bebas1": self.ent_klik_bebas1.get(),
            "scroll_bebas1": self.ent_scroll_bebas1.get(),
            "arah_scroll": self.arah_scroll.get(),
            "klik_bebas2": self.ent_klik_bebas2.get(),
            "jarak_baris": self.ent_jarak.get(),
            "klik_submit": self.ent_klik_submit.get(),
            "auto_kirim": bool(self.kirim_var.get()),
            "versi": APP_VERSION,
        }
        try:
            with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception:
            pass

    def _load_settings(self):
        if not os.path.exists(SETTINGS_FILE):
            self.browsers = [self._browser_baru("Browser 1")]
            return
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            self.browsers = [self._browser_baru("Browser 1")]
            return
        if not isinstance(data, dict):
            self.browsers = [self._browser_baru("Browser 1")]
            return
        # ---- muat daftar browser (dengan sanitasi) ----
        # Posisi hanya dimuat bila pengaturan berasal dari v3.0 —
        # makna slot di versi lama sudah berubah sama sekali.
        dari_v3 = str(data.get("versi", "")).startswith("3")
        bs = data.get("browsers")
        self.browsers = []
        if isinstance(bs, list):
            for b in bs:
                if not isinstance(b, dict):
                    continue
                entri = {
                    "nama": str(b.get("nama") or "Browser"),
                    "folder": str(b.get("folder") or ""),
                }
                for kunci in POS_KUNCI:
                    pos = b.get(kunci) if dari_v3 else None
                    try:
                        entri[kunci] = [int(pos[0]), int(pos[1])] \
                            if pos else None
                    except Exception:
                        entri[kunci] = None
                self.browsers.append(entri)
        if not self.browsers:
            self.browsers = [self._browser_baru("Browser 1")]
        try:
            self.aktif = min(max(0, int(data.get("aktif", 0))),
                             len(self.browsers) - 1)
        except Exception:
            self.aktif = 0
        # ---- muat isian angka & teks ----
        pasangan = [
            ("jumlah", self.ent_jumlah), ("caption", self.ent_caption),
            ("mundur", self.ent_mundur), ("jeda_dialog", self.ent_dialog),
            ("jeda_langkah", self.ent_langkah),
            ("tunggu_upload", self.ent_tunggu),
            ("tunggu", self.ent_tunggu),  # kompatibel pengaturan lama v1.0
            ("tanggal_jam", self.ent_tanggal),
            ("radius_cari", self.ent_radius),
            ("kemiripan_cari", self.ent_kemiripan),
            ("klik_bebas1", self.ent_klik_bebas1),
            ("scroll_bebas1", self.ent_scroll_bebas1),
            ("klik_bebas2", self.ent_klik_bebas2),
            ("jarak_baris", self.ent_jarak),
            ("klik_submit", self.ent_klik_submit),
        ]
        for key, ent in pasangan:
            val = data.get(key)
            if val is not None:
                ent.delete(0, "end")
                ent.insert(0, str(val))
        self.skip_var.set(bool(data.get("skip_uploaded", True)))
        self.var_skip_jadwal.set(bool(data.get("skip_jadwal", False)))
        self.var_gambar.set(bool(data.get("pakai_gambar", False)))
        self.gambar_ref = str(data.get("gambar_ref") or "")
        if self.gambar_ref and os.path.isfile(self.gambar_ref):
            self.lbl_gambar.config(
                text=os.path.basename(self.gambar_ref) + "  (siap)",
                fg=C_ACCENT)
        arah = str(data.get("arah_scroll") or "Turun")
        self.arah_scroll.set(arah if arah in ("Turun", "Naik") else "Turun")
        self.kirim_var.set(bool(data.get("auto_kirim", True)))
        # ---- isi UI sesuai browser aktif ----
        self._refresh_browser_list(keep=self.aktif)
        self._load_browser_to_ui()

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


def main():
    root = tk.Tk()
    app = CutUploaderApp(root)
    if "--selftest" in sys.argv:
        def _ok():
            print("SELFTEST_OK")
            root.destroy()
        root.after(1800, _ok)
    if "--selftest-dialog" in sys.argv:
        def _dlg():
            app._tambah_browser()
        root.after(1000, _dlg)

        def _ok2():
            print("SELFTEST_DIALOG_OK")
            root.destroy()
        root.after(4500, _ok2)
    root.mainloop()
    if ("--selftest" in sys.argv) or ("--selftest-dialog" in sys.argv):
        print("SELFTEST_DONE")


if __name__ == "__main__":
    main()
