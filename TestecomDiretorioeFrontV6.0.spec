# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('app.exe', '.'),  # O executável pode ser incluído, mas geralmente não é necessário se for o próprio arquivo a ser executado
        ('tesk.ico', '.'),
        ('TouchEmulator_TestenoDiretorio.bat', '.'),
        ('touch.json', '.'),
        ('Keyboard_TestenoDiretorio.bat', '.'),
        ('keyboard.json', '.'),
        ('MainWindow.ui', '.'),
        ('MainWindow.py', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Rotina de Testes de Loop',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    icon='tesk.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,  # Isso indica que queremos um único arquivo executável
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='TestecomDiretorioeFrontV6.0',
)
