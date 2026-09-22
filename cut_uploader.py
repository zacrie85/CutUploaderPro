# -*- coding: utf-8 -*-
"""
============================================================
  CUTUPLOADER PRO  v2.0
  Aplikasi desktop uploader video batch otomatis
  khusus untuk situs CutMotions (Kwai)
------------------------------------------------------------
  Alur situs yang diikuti aplikasi ini (sesuai halaman asli):
    1. Login manual (email / kata sandi)
    2. Pilih "Versi lama"  ->  "Rilis karya"
    3. Halaman "Video Bublikasikan":
       FASE 1  UPLOAD   : klik "+ Tambah video" per video,
                          ketik path file di dialog Windows
       FASE 2  JADWAL   : (opsional) klik radio "Jadwalkan
                          rilis" + Negara Indonesia, sisanya
                          zona waktu & waktu rilis diatur
                          saat jeda F8
       FASE 3  CAPTION  : per video -> tombol "Edit" ->
                          kotak "Judul video" -> ketik
                          caption -> "Konfirmasi"
                          (baris berikut naik ke posisi yang
                          sama, jadi 1 set posisi dipakai
                          untuk semua video)
       FASE 4  KIRIM    : scroll ke bawah -> klik "Kirim"

  Batas situs: maksimal 20 video / sekali jalan,
  judul video maksimal 250 karakter.

  Hotkey:
    F6         : Mulai
    F7 / ESC   : Berhenti
    F8         : Lanjut (dari jeda jadwal rilis)

  Dibuat dengan Python + tkinter + pynput.
  Fokus utama: Windows desktop.
============================================================
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import time
import json
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

APP_NAME = "CutUploader Pro"
APP_VERSION = "2.0"

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
# Definisi 9 slot posisi klik di situs CutMotions
#   (kunci, label pendek, wajib?, nama lengkap)
# ------------------------------------------------------------
POSISI_DEF = [
    ("pos_tambah",     "A · Tambah video",     True,
     "TOMBOL '+ TAMBAH VIDEO'"),
    ("pos_edit",       "B · Edit (baris atas)", True,
     "TOMBOL 'EDIT' PADA BARIS VIDEO TERATAS"),
    ("pos_judul",      "C · Kotak Judul video", True,
     "KOTAK 'JUDUL VIDEO' (saat editor terbuka)"),
    ("pos_konfirmasi", "D · Tombol Konfirmasi", True,
     "TOMBOL 'KONFIRMASI' (saat editor terbuka)"),
    ("pos_kirim",      "E · Tombol Kirim",      True,
     "TOMBOL 'KIRIM' (halaman sudah discroll ke bawah)"),
    ("pos_jadwal",     "F · Radio Jadwalkan",   False,
     "RADIO 'JADWALKAN RILIS'"),
    ("pos_negara",     "G · Dropdown Negara",   False,
     "DROPDOWN 'NEGARA'"),
    ("pos_indonesia",  "H · Item Indonesia",    False,
     "ITEM 'INDONESIA' DI DAFTAR DROPDOWN NEGARA"),
    ("pos_batal",      "I · Batal (opsional)",  False,
     "TOMBOL 'BATAL' (tutup editor video terakhir)"),
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


class CutUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("{} v{}".format(APP_NAME, APP_VERSION))
        self.root.configure(bg=C_BG)
        self.root.geometry("640x960")
        self.root.minsize(540, 640)

        self.stop_event = threading.Event()
        self.running = False
        self._f8 = False  # penanda lanjut dari jeda jadwal (F8)

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
                            "Tambah video → Jadwal → Caption (Edit) → Kirim",
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
        self.lbl_pos = {}
        self.btn_pos = {}
        for kunci, label, wajib, _ket in POSISI_DEF:
            row = tk.Frame(c3, bg=C_CARD)
            row.pack(fill="x", pady=(3, 0))
            tk.Label(row, text=label, bg=C_CARD,
                     fg=C_TEXT if wajib else C_MUTED,
                     font=("Segoe UI", 9), width=22,
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
        self.lbl_ambil = tk.Label(c3, text="", bg=C_CARD, fg=C_YELLOW,
                                  font=F_S, anchor="w", wraplength=560,
                                  justify="left")
        self.lbl_ambil.pack(fill="x", pady=(6, 0))
        tk.Label(c3, text="Ambil posisi = klik AMBIL, lalu dalam 5 detik "
                          "arahkan mouse ke target di browser dan diamkan. "
                          "Kondisi halaman saat mengambil:\n"
                          "• A — halaman Rilis karya seperti biasa.\n"
                          "• B — baris video TERATAS dalam keadaan TERTUTUP "
                          "(tombol Edit terlihat di kanan).\n"
                          "• C & D — baris teratas TERBUKA (klik dulu Edit-nya "
                          "secara manual): arahkan ke kotak 'Judul video' dan "
                          "tombol 'Konfirmasi'.\n"
                          "• E — scroll halaman sampai BAWAH (tombol Kirim "
                          "terlihat).\n"
                          "• F/G/H — hanya untuk jadwal OTOMATIS (H diambil "
                          "saat dropdown negara sedang terbuka).\n"
                          "• I — hanya kalau setelah tambah video editor-nya "
                          "terbuka sendiri; kalau tidak, kosongkan saja.\n"
                          "Trik: setelah Konfirmasi, baris video berikutnya "
                          "naik ke posisi yang sama — jadi satu set posisi "
                          "B/C/D dipakai berulang untuk semua video.\n"
                          "Penting: jangan pindahkan / resize jendela browser "
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
        self.ent_tunggu = self._field(f4, "TUNGGU UPLOAD PER VIDEO", "60")
        tk.Label(c4, text="MUNDUR = persiapan sebelum mulai.\n"
                          "JEDA BUKA DIALOG/EDITOR = tunggu dialog pilih file "
                          "Windows terbuka / editor video terbuka.\n"
                          "JEDA ANTAR LANGKAH = jeda klik-ketik di dalam "
                          "situs.\nTUNGGU UPLOAD PER VIDEO = waktu menunggu "
                          "satu video selesai terupload sebelum menambah "
                          "video berikutnya (naikkan bila video berukuran "
                          "besar / internet lambat).",
                 bg=C_CARD, fg=C_MUTED, font=F_S, wraplength=560,
                 justify="left").pack(fill="x", pady=(6, 0))

        # ============ 5. JADWAL RILIS & KIRIM ============
        c5 = self._card("5. JADWAL RILIS & KIRIM")
        self.mode_jadwal = tk.StringVar(value="manual")
        rb1 = tk.Radiobutton(
            c5, text="Jadwal saya atur sendiri (sebelum mulai, atau saat "
                     "jeda F8)", variable=self.mode_jadwal, value="manual",
            bg=C_CARD, fg=C_TEXT, activebackground=C_CARD,
            activeforeground=C_TEXT, selectcolor=C_ENTRY, font=F_S,
            bd=0, highlightthickness=0, cursor="hand2", anchor="w",
            justify="left", wraplength=540)
        rb1.pack(fill="x")
        rb2 = tk.Radiobutton(
            c5, text="Otomatis klik: radio 'Jadwalkan rilis' + Negara "
                     "Indonesia (butuh posisi F, G, H)",
            variable=self.mode_jadwal, value="otomatis",
            bg=C_CARD, fg=C_TEXT, activebackground=C_CARD,
            activeforeground=C_TEXT, selectcolor=C_ENTRY, font=F_S,
            bd=0, highlightthickness=0, cursor="hand2", anchor="w",
            justify="left", wraplength=540)
        rb2.pack(fill="x", pady=(2, 0))
        self.f8_var = tk.BooleanVar(value=True)
        self._check(c5, "Jeda F8 sebelum fase caption (atur Zona waktu & "
                        "Waktu rilis di browser, lalu tekan F8 untuk "
                        "lanjut)", self.f8_var)
        self.kirim_var = tk.BooleanVar(value=True)
        self._check(c5, "Klik tombol 'Kirim' otomatis di akhir "
                        "(matikan kalau mau cek dulu secara manual)",
                    self.kirim_var)
        tk.Label(c5, text="Isi halaman 'Bublikasikan aturan': pilih "
                          "'Jadwalkan rilis', Negara = Indonesia, lalu "
                          "Zona waktu & Waktu rilis (tanggal-jam). Zona & "
                          "tanggal paling aman diisi saat jeda F8 karena "
                          "kalendernya sulit diklik otomatis.",
                 bg=C_CARD, fg=C_MUTED, font=F_S, wraplength=560,
                 justify="left").pack(fill="x", pady=(6, 0))

        # ============ 6. STATUS ============
        c6 = self._card("6. STATUS")
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
                      "F8 = Lanjut dari jeda jadwal   |   Pengaturan "
                      "tersimpan otomatis",
                 bg=C_BG, fg=C_MUTED, font=F_S).pack(side="bottom", pady=8)

    # ================== HOTKEY GLOBAL ==================
    def _on_key(self, key):
        try:
            if key == kb_mod.Key.f6:
                self.root.after(0, self._start)
            elif key in (kb_mod.Key.f7, kb_mod.Key.esc):
                self.root.after(0, self._stop)
            elif key == kb_mod.Key.f8:
                self._f8 = True
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
            "mode_jadwal": self.mode_jadwal.get(),
            "jeda_f8": bool(self.f8_var.get()),
            "auto_kirim": bool(self.kirim_var.get()),
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
        if not folder or not os.path.isdir(folder):
            messagebox.showwarning(APP_NAME,
                                   "Folder video belum dipilih atau tidak "
                                   "ada:\n" + (folder or "(kosong)"))
            return
        # ---- posisi wajib ----
        for kunci, label, wajib, _ket in POSISI_DEF:
            if wajib and not snap["browser"].get(kunci):
                messagebox.showwarning(
                    APP_NAME,
                    "Posisi {} belum diatur.\n\n"
                    "Lihat petunjuk di bagian 3, lalu klik AMBIL.".format(
                        label))
                return
        # ---- posisi jadwal otomatis ----
        if snap["mode_jadwal"] == "otomatis":
            for kunci in ("pos_jadwal", "pos_negara", "pos_indonesia"):
                if not snap["browser"].get(kunci):
                    messagebox.showwarning(
                        APP_NAME,
                        "Mode jadwal OTOMATIS butuh posisi F (Radio "
                        "Jadwalkan), G (Dropdown Negara) dan H (Item "
                        "Indonesia).\n\nAmbil dulu posisinya, atau ganti "
                        "mode ke 'saya atur sendiri'.")
                    return
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
        semua = daftar_video(folder)
        if not semua:
            messagebox.showwarning(
                APP_NAME, "Tidak ada file video (.mp4/.mov/dll) di folder "
                          "ini.")
            return
        if snap["skip"]:
            sudah = self._riwayat_browser()
            semua = [f for f in semua if f not in sudah]
            if not semua:
                messagebox.showinfo(
                    APP_NAME,
                    "Semua video di folder ini sudah pernah terupload.\n\n"
                    "Klik 'Bersihkan riwayat browser ini' bila mau "
                    "mengulang dari awal.")
                return
        antrian = semua[:jumlah]

        # ---- cek panjang caption ----
        terpanjang = 0
        for f in antrian:
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

        if snap["mode_jadwal"] == "manual" and not snap["jeda_f8"]:
            if not messagebox.askyesno(
                    APP_NAME,
                    "Jadwal mode MANUAL tanpa jeda F8.\n"
                    "Pastikan 'Jadwalkan rilis' + Negara Indonesia + Zona "
                    "waktu + Waktu rilis SUDAH diatur di browser sebelum "
                    "klik MULAI.\n\nLanjut?"):
                return

        self._save_settings()
        self.stop_event.clear()
        self._f8 = False
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

    # ================== MESIN OTOMATIS ==================
    def _worker(self, snap, antrian, jumlah, mundur, jeda_dialog,
                jeda_langkah, tunggu):
        try:
            bnama = snap["browser"]["nama"]
            pos = {k: tuple(snap["browser"][k]) for k in POS_KUNCI
                   if snap["browser"].get(k)}
            caption_dasar = snap["caption"]
            mode_otomatis = snap["mode_jadwal"] == "otomatis"
            kunci = "{}||{}".format(bnama, snap["folder"].lower())

            # ---- hitung mundur sebelum mulai ----
            if mundur > 0:
                for s in range(mundur, 0, -1):
                    if self.stop_event.is_set():
                        self._finish("Dibatalkan sebelum mulai.", warn=True)
                        return
                    self._set_status(
                        "Mulai dalam {} detik — buka halaman Rilis karya "
                        "CutMotions di '{}' sekarang...".format(s, bnama),
                        C_YELLOW)
                    self._sleep(1.0)

            # =================================================
            # FASE 1 — UPLOAD semua video (tombol Tambah video)
            # =================================================
            total = len(antrian)
            sukses = 0
            self._set_status(
                "FASE 1/4 UPLOAD — menambahkan {} video ke '{}' "
                "(jangan sentuh mouse/keyboard!)".format(total, bnama),
                C_ACCENT)
            for i, nama_file in enumerate(antrian):
                if self.stop_event.is_set():
                    break
                path_lengkap = os.path.abspath(
                    os.path.join(snap["folder"], nama_file))
                self._set_progress(
                    "FASE 1 UPLOAD {}/{}   |   {}".format(
                        i + 1, total, nama_file))

                # klik tombol "+ Tambah video" di situs
                self._set_status(
                    "[{}/{}] Klik '+ Tambah video'...".format(
                        i + 1, total), C_ACCENT)
                self._klik(pos["pos_tambah"])
                self._sleep(jeda_dialog)

                # ketik path file di dialog Windows + Enter
                if self.stop_event.is_set():
                    break
                self._set_status(
                    "[{}/{}] Memilih file: {}".format(
                        i + 1, total, nama_file), C_ACCENT)
                self.kb.type(path_lengkap)
                time.sleep(0.15)
                self.kb.press(Key.enter)
                self.kb.release(Key.enter)
                self._sleep(jeda_langkah + 0.5)

                # tunggu proses upload video selesai
                if self.stop_event.is_set():
                    break
                end = time.time() + tunggu
                while not self.stop_event.is_set():
                    sisa = end - time.time()
                    if sisa <= 0:
                        break
                    self._set_progress(
                        "FASE 1 UPLOAD {}/{}   |   menunggu upload {}: "
                        "{:.0f} dtk".format(i + 1, total, nama_file, sisa))
                    time.sleep(min(0.5, sisa))
                if self.stop_event.is_set():
                    break

                # catat riwayat (tersimpan instan)
                self.riwayat.setdefault(kunci, [])
                if nama_file not in self.riwayat[kunci]:
                    self.riwayat[kunci].append(nama_file)
                self._save_riwayat()
                sukses += 1

            if self.stop_event.is_set():
                self._finish(
                    "Dihentikan saat FASE UPLOAD. Tercatat {} video "
                    "(riwayat otomatis). Jalankan F6 lagi untuk "
                    "melanjutkan.".format(sukses), warn=True)
                return

            # =================================================
            # FASE 1.5 — tutup editor video terakhir (opsional)
            # =================================================
            if "pos_batal" in pos:
                self._set_status(
                    "Menutup editor video terakhir (klik Batal)...",
                    C_ACCENT)
                self._klik(pos["pos_batal"])
                self._sleep(jeda_langkah + 0.5)

            # =================================================
            # FASE 2 — JADWAL RILIS (opsional + jeda F8)
            # =================================================
            self._set_status("FASE 2/4 JADWAL RILIS — menggulir ke atas...",
                             C_ACCENT)
            self._scroll_top()
            self._sleep(jeda_langkah)

            if mode_otomatis and "pos_jadwal" in pos and \
                    "pos_negara" in pos and "pos_indonesia" in pos:
                self._set_status(
                    "Klik radio 'Jadwalkan rilis' + Negara Indonesia...",
                    C_ACCENT)
                self._klik(pos["pos_jadwal"])
                self._sleep(jeda_langkah)
                self._klik(pos["pos_negara"])
                self._sleep(jeda_dialog)
                self._klik(pos["pos_indonesia"])
                self._sleep(jeda_langkah)

            if snap["jeda_f8"]:
                self._f8 = False
                self._set_status(
                    "JEDA F8 — atur di browser: 'Jadwalkan rilis', "
                    "Negara Indonesia, Zona waktu, dan Waktu rilis "
                    "(tanggal-jam). Lalu tekan F8 untuk lanjut.",
                    C_YELLOW)
                t0 = time.time()
                while not self.stop_event.is_set() and not self._f8:
                    self._set_progress(
                        "FASE 2 JADWAL   |   menunggu F8: {:.0f} dtk "
                        "(F7/ESC = berhenti)".format(time.time() - t0))
                    time.sleep(0.2)
                if self.stop_event.is_set():
                    self._finish(
                        "Dihentikan saat jeda jadwal. {} video sudah "
                        "terupload & tercatat di riwayat.".format(sukses),
                        warn=True)
                    return
            elif mode_otomatis:
                self._set_status(
                    "Jadwal: radio + negara sudah diklik. Zona waktu & "
                    "Waktu rilis dianggap sudah diatur sebelumnya.",
                    C_YELLOW)

            if self.stop_event.is_set():
                self._finish("Dihentikan.", warn=True)
                return

            # =================================================
            # FASE 3 — CAPTION per video (Edit → Judul → Konfirmasi)
            # =================================================
            self._set_status("FASE 3/4 CAPTION — menggulir ke atas...",
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
            i = 0

            for i, nama_file in enumerate(daftar_caption):
                if self.stop_event.is_set():
                    break
                caption_final = compose_caption(caption_dasar, nama_file)
                self._set_progress(
                    "FASE 3 CAPTION {}/{}   |   {}".format(
                        i + 1, n_cap, caption_final))

                # klik tombol Edit pada baris video teratas
                self._set_status(
                    "[{}/{}] Klik tombol Edit...".format(i + 1, n_cap),
                    C_ACCENT)
                self._klik(pos["pos_edit"])
                self._sleep(jeda_dialog)

                # klik kotak Judul video + ketik caption
                if self.stop_event.is_set():
                    break
                self._set_status(
                    "[{}/{}] Menulis judul: {}".format(
                        i + 1, n_cap, caption_final), C_ACCENT)
                self._klik(pos["pos_judul"])
                time.sleep(0.3)
                with self.kb.pressed(Key.ctrl):
                    self.kb.press("a")
                    self.kb.release("a")
                time.sleep(0.15)
                self.kb.type(caption_final)
                self._sleep(jeda_langkah)

                # klik tombol Konfirmasi
                if self.stop_event.is_set():
                    break
                self._set_status(
                    "[{}/{}] Klik Konfirmasi...".format(i + 1, n_cap),
                    C_ACCENT)
                self._klik(pos["pos_konfirmasi"])
                self._sleep(jeda_langkah + 0.5)

            if self.stop_event.is_set():
                self._finish(
                    "Dihentikan saat FASE CAPTION ({}/{} judul selesai). "
                    "Jalankan F6 lagi — caption diulang dari baris atas "
                    "dan yang sudah jadi otomatis ditimpa sama.".format(
                        i + 1, n_cap), warn=True)
                return

            # =================================================
            # FASE 4 — KIRIM
            # =================================================
            if snap["auto_kirim"] and "pos_kirim" in pos:
                self._set_status(
                    "FASE 4/4 KIRIM — menggulir ke bawah lalu klik "
                    "Kirim...", C_ACCENT)
                self._scroll_bottom()
                self._sleep(jeda_langkah + 0.5)
                self._klik(pos["pos_kirim"])
                self._finish(
                    "Selesai! {} video: terupload, diberi caption, dan "
                    "sudah diklik Kirim. Cek status rilis di situs.".format(
                        n_cap))
            else:
                self._finish(
                    "Caption {} video selesai! Cek dulu di browser, lalu "
                    "klik tombol 'Kirim' secara manual.".format(n_cap))
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
            "mode_jadwal": self.mode_jadwal.get(),
            "jeda_f8": bool(self.f8_var.get()),
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
                    pos = b.get(kunci)
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
        ]
        for key, ent in pasangan:
            val = data.get(key)
            if val is not None:
                ent.delete(0, "end")
                ent.insert(0, str(val))
        self.skip_var.set(bool(data.get("skip_uploaded", True)))
        self.mode_jadwal.set(
            "otomatis" if data.get("mode_jadwal") == "otomatis"
            else "manual")
        self.f8_var.set(bool(data.get("jeda_f8", True)))
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
