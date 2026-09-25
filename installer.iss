; ============================================================
;  CutUploader Pro - Installer Windows (Inno Setup 6)
;  Hasil: dist\CutUploaderPro-Setup.exe
;  Bangun EXE dulu dengan build_exe.bat atau GitHub Actions,
;  lalu jalankan BANGUN-INSTALLER.bat (butuh Inno Setup 6).
;  Download Inno Setup gratis: https://jrsoftware.org/isdl.php
; ============================================================

[Setup]
AppName=CutUploader Pro
AppVersion=6.3
AppVerName=CutUploader Pro v6.3 (Macro Studio Edition)
AppPublisher=zacrie85
AppPublisherURL=https://github.com/zacrie85/CutUploaderPro
AppSupportURL=https://github.com/zacrie85/CutUploaderPro
DefaultDirName={autopf}\CutUploader Pro
DefaultGroupName=CutUploader Pro
OutputDir=dist
OutputBaseFilename=CutUploaderPro-Setup
Compression=lzma2/max
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\CutUploaderPro.exe
WizardStyle=modern
Uninstallable=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Buat shortcut di Desktop"; \
    GroupDescription: "Pintasan:"

[Files]
Source: "dist\CutUploaderPro.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "PANDUAN.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\CutUploader Pro"; Filename: "{app}\CutUploaderPro.exe"
Name: "{group}\Panduan CutUploader Pro"; Filename: "{app}\PANDUAN.txt"
Name: "{group}\Uninstall CutUploader Pro"; Filename: "{uninstallexe}"
Name: "{autodesktop}\CutUploader Pro"; Filename: "{app}\CutUploaderPro.exe"; \
    Tasks: desktopicon

[Run]
Filename: "{app}\CutUploaderPro.exe"; \
    Description: "Jalankan CutUploader Pro sekarang"; \
    Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
